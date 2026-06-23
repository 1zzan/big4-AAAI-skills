#!/usr/bin/env python3
"""Expand the AAAI security/LLM-agent corpus from the OJS candidate pool.

The script downloads selected PDFs to a local-only folder, extracts coarse
full-text structure with pdftotext, and regenerates the public metadata files.
Raw PDFs and JSONL full text remain outside git by default.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any


CURATED_TITLE_HINTS = [
    "Beyond Content: A Comprehensive Speech Toxicity Dataset",
    "Modulation-Based Backdoors",
    "Transferable Backdoor Attacks for Code Models",
    "VFCionX: Bridging Large and Small Models",
    "T2Agent: A Tool-augmented Multimodal Misinformation Detection Agent",
    "SIDE: Surrogate Conditional Data Extraction",
    "Beyond Traditional Threats: A Persistent Backdoor Attack",
    "SentinelLMs: Encrypted Input Adaptation",
    "Efficient Toxic Content Detection",
    "OUTFOX: LLM-Generated Essay Detection",
    "Inspecting Prediction Confidence for Detecting Black-Box Backdoor Attacks",
    "SEER: Backdoor Detection for Vision-Language Models",
    "Backdoor Attacks via Machine Unlearning",
    "COMBAT: Alternated Training",
    "Chronic Poisoning",
    "DataElixir: Purifying Poisoned Dataset",
    "Task-Agnostic Privacy-Preserving Representation Learning",
    "Value at Adversarial Risk",
    "Spear and Shield: Adversarial Attacks and Defense",
    "Adversarial Attacks on Federated-Learned Adaptive Bitrate",
    "MI-CAPTCHA",
    "Medical MLLM Is Vulnerable",
    "Investigating the Security Threat Arising from",
    "Is Your Autonomous Vehicle Safe",
    "Privacy-Preserving Low-Rank Adaptation",
    "SafeInfer: Context Adaptive Decoding Time Safety Alignment",
    "RAT: Adversarial Attacks on Deep Reinforcement Agents",
    "Retention Score: Quantifying Jailbreak Risks",
    "SADBA: Self-Adaptive Distributed Backdoor Attack",
    "CP-Guard: Malicious Agent Detection",
    "Global Attribute-Association Pattern Aggregation for Graph Fraud Detection",
    "Unveiling the Threat of Fraud Gangs",
    "Meme Trojan",
    "Adversarial-Inspired Backdoor Defense",
    "Attack on Prompt",
    "Backdoor Token Unlearning",
    "CL-Attack: Textual Backdoor Attacks",
    "CLNX: Bridging Code and Natural Language",
    "DF-MIA: A Distribution-Free Membership Inference Attack",
    "Portcullis: A Scalable and Verifiable Privacy Gateway",
    "NLSR: Neuron-Level Safety Realignment",
    "Scaling Trends for Data Poisoning in LLMs",
    "Simulate and Eliminate",
    "First Line of Defense",
    "Grimm: A Plug-and-Play Perturbation Rectifier",
    "HoneypotNet",
    "IBAS:Imperceptible Backdoor Attacks",
    "Defending Against Sophisticated Poisoning Attacks",
    "Label-Free Backdoor Attacks",
    "An LLM-based Quantitative Framework for Evaluating High-Stealthy Backdoor Risks",
    "Towards Robust Text-Attributed Federated Graph Learning",
    "StyleBreak: Revealing Alignment Vulnerabilities",
    "Multi-Faceted Attack",
    "DoBlock: Blocking Malicious Association Propagation",
    "Good Gradients Poison Your Model",
    "Backdoor Attacks on Open Vocabulary Object Detectors",
    "FedSEA-LLaMA",
    "PAGPL: Privacy-Aware Graph Prompt Learning",
    "PRISM: Privacy-Aware Routing",
    "SGoT-R1",
    "Attention to Threat-Relevant Objects",
    "DIFT: Protecting Contrastive Learning",
    "CoSPED: Consistent Soft Prompt Targeted Data Extraction",
    "DAVSP: Safety Alignment",
    "Differentiated Directional Intervention",
    "EASE: Practical and Efficient Safety Alignment",
    "Joint-GCG",
    "Privacy Preserving In-Context-Learning",
    "GeoShield",
    "SDEval: Safety Dynamic Evaluation",
    "IS-Bench: Evaluating Interactive Safety",
    "When Safe Unimodal Inputs Collide",
    "Safety Alignment of Large Language Models via Contrasting",
    "Uncovering and Aligning Anomalous Attention Heads",
    "WALKSAFE",
    "Mental Model-based Generation of Lies for Insider Threat Modeling",
]


FALLBACK_PATTERNS = [
    re.compile(p, re.I)
    for p in [
        r"cyber|cve|vulnerab|malware|ransomware|phishing|botnet|intrusion|endpoint|provenance|audit log|threat|fraud",
        r"jailbreak|guardrail|safety alignment|harmful|toxic|red.?team",
        r"privacy|private|secure inference|membership inference|data leakage|federated",
        r"backdoor|poison|trojan|adversarial attack|black-box attack|evasion|defense|malicious|captcha",
        r"(agent|agents|multi-agent|tool|mcp).*(attack|security|privacy|risk|threat|poison|backdoor|malicious|defense|safety)",
        r"(attack|security|privacy|risk|threat|poison|backdoor|malicious|defense|safety).*(agent|agents|multi-agent|tool|mcp)",
    ]
]


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def norm(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).lower()


def aaai_year(value: str | None) -> str:
    text = str(value or "")
    match = re.search(r"20(\d{2})", text)
    return f"AAAI-{match.group(1)}" if match else text


def slug(title: str, year: str) -> str:
    prefix = aaai_year(year).replace("AAAI-", "AAAI")
    ascii_title = title.encode("ascii", "ignore").decode("ascii")
    ascii_title = re.sub(r"[^A-Za-z0-9]+", "_", ascii_title).strip("_")
    ascii_title = re.sub(r"_+", "_", ascii_title)[:112].strip("_")
    return f"{prefix}_{ascii_title}.pdf"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_existing_records(pdf_dir: Path) -> list[dict[str, Any]]:
    jsonl = pdf_dir / "AAAI_security_llm_agent_fulltext_structure.jsonl"
    records: list[dict[str, Any]] = []
    if not jsonl.exists():
        return records
    for line in jsonl.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def existing_keys(records: list[dict[str, Any]], expansion: list[dict[str, Any]]) -> set[str]:
    keys: set[str] = set()
    for item in records + expansion:
        for field in ("title", "pdf_url", "article_url", "local_pdf"):
            value = item.get(field)
            if value:
                keys.add(norm(str(value)))
    return keys


def choose_candidates(candidates: list[dict[str, Any]], keys: set[str], additional: int) -> list[dict[str, Any]]:
    chosen: list[dict[str, Any]] = []
    used_urls: set[str] = set()

    def is_new(item: dict[str, Any]) -> bool:
        values = [item.get("title"), item.get("pdf_url"), item.get("article_url")]
        return all(norm(str(v)) not in keys for v in values if v) and norm(item.get("pdf_url")) not in used_urls

    for hint in CURATED_TITLE_HINTS:
        for item in candidates:
            if hint.lower() in item["title"].lower() and is_new(item):
                chosen.append(item)
                used_urls.add(norm(item.get("pdf_url")))
                break
        if len(chosen) >= additional:
            return chosen

    scored: list[tuple[int, dict[str, Any]]] = []
    for item in candidates:
        if not is_new(item):
            continue
        title = item["title"]
        score = int(item.get("score", 0))
        hits = sum(1 for pattern in FALLBACK_PATTERNS if pattern.search(title))
        if hits == 0:
            continue
        if re.search(r"adaptation|adaptive|prompt tuning", title, re.I) and not re.search(
            r"attack|security|privacy|backdoor|poison|jailbreak|threat|malicious|vulnerab|secure|safe|toxic",
            title,
            re.I,
        ):
            continue
        scored.append((score + 4 * hits, item))
    scored.sort(key=lambda row: (-row[0], row[1].get("year", ""), row[1]["title"]))

    for _, item in scored:
        if is_new(item):
            chosen.append(item)
            used_urls.add(norm(item.get("pdf_url")))
        if len(chosen) >= additional:
            break
    return chosen


def download_pdf(item: dict[str, Any], pdf_dir: Path, pause: float) -> Path:
    local_pdf = item.get("local_pdf") or slug(item["title"], item["year"])
    item["local_pdf"] = local_pdf
    target = pdf_dir / local_pdf
    if target.exists() and target.stat().st_size > 20_000:
        item["status"] = "downloaded"
        return target
    request = urllib.request.Request(
        item["pdf_url"],
        headers={"User-Agent": "Codex AAAI corpus metadata updater"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    if not data.startswith(b"%PDF"):
        raise RuntimeError(f"Downloaded content is not a PDF: {item['pdf_url']}")
    target.write_bytes(data)
    item["status"] = "downloaded"
    if pause:
        time.sleep(pause)
    return target


def run_pdftotext(pdftotext: str, pdf_path: Path) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "out.txt"
        cmd = [pdftotext, "-enc", "UTF-8", str(pdf_path), str(out)]
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return out.read_text(encoding="utf-8", errors="replace")


def clean_line(line: str) -> str:
    line = re.sub(r"\s+", " ", line).strip()
    return line[:180]


def find_sections(text: str) -> list[str]:
    lines = [clean_line(line) for line in text.splitlines()]
    headings: list[str] = []
    patterns = [
        r"^(abstract|introduction|related work|background|preliminar|problem|threat model|method|approach|framework|dataset|experiment|evaluation|result|ablation|discussion|limitation|ethic|conclusion|acknowledg|references)\b",
        r"^\d+(\.\d+)?\s+(introduction|related|background|problem|threat|method|approach|dataset|experiment|evaluation|result|ablation|discussion|limitation|conclusion)\b",
    ]
    for line in lines:
        if not line or len(line) > 180:
            continue
        if any(re.search(pattern, line, re.I) for pattern in patterns):
            headings.append(line)
        if len(headings) >= 12:
            break
    return headings


def has_signal(text: str, pattern: str) -> bool:
    return re.search(pattern, text, re.I) is not None


def labels_for(title: str, text: str) -> list[str]:
    title_probe = title.lower()
    head_probe = text[:2500].lower()
    probe = f"{title_probe}\n{head_probe}"
    labels: list[str] = []
    if has_signal(
        title_probe,
        r"cyber|malware|ransomware|vulnerab|cve|botnet|fraud|threat|intrusion|endpoint|provenance|audit log|traffic|phishing|misinformation",
    ) or has_signal(
        head_probe,
        r"cyber|malware|ransomware|vulnerab|cve|botnet|fraud|intrusion|endpoint|provenance|audit log|phishing|misinformation",
    ):
        labels.append("SOC/threat-analysis")
    if has_signal(
        probe,
        r"jailbreak|guardrail|safety|harmful|toxic|red.?team|misuse|safety alignment|large language model|vision-language model|\bllm\b|\bvlm\b|\bmllm\b",
    ) and has_signal(
        probe,
        r"attack|defen[sc]e|risk|threat|privacy|secure|safe|poison|backdoor|vulnerab|harmful|toxic|jailbreak|guardrail|alignment",
    ):
        labels.append("LLM-safety-attack-defense")
    if has_signal(
        probe,
        r"\bagents?\b|multi-agent|\btools?\b|\bmcp\b|code completion|software development|mobile|smartphone|fact-check",
    ) and has_signal(
        probe,
        r"attack|security|privacy|risk|threat|poison|backdoor|malicious|defen[sc]e|safety|secure|misinformation",
    ):
        labels.append("agent/tool-security")
    if has_signal(probe, r"backdoor|poison|trojan|data extraction"):
        labels.append("backdoor/poisoning")
    if has_signal(probe, r"privacy|private|secure inference|membership inference|leakage|federated|unlearning"):
        labels.append("privacy/security-alignment")
    if not labels:
        labels.append("security-adjacent")
    return labels


def snippets(text: str, pattern: str, limit: int = 4) -> list[str]:
    paras = [clean_line(p) for p in re.split(r"\n\s*\n", text)]
    found: list[str] = []
    for para in paras:
        if len(para) < 80:
            continue
        if re.search(pattern, para, re.I):
            found.append(para[:320])
        if len(found) >= limit:
            break
    return found


def structure_record(item: dict[str, Any], pdf_path: Path, text: str) -> dict[str, Any]:
    title = item["title"]
    lower = text.lower()
    return {
        "local_pdf": pdf_path.name,
        "year": aaai_year(item.get("year")),
        "title": title,
        "source": "expansion_2026_06",
        "pdf_url": item.get("pdf_url"),
        "article_url": item.get("article_url"),
        "pages": max(1, text.count("\f")),
        "labels": labels_for(title, text),
        "section_headings": find_sections(text),
        "has_threat_model_signal": has_signal(lower, r"threat model|attacker|attack|malicious|adversar|risk"),
        "has_dataset_signal": has_signal(lower, r"dataset|benchmark|corpus|data set|samples|tasks"),
        "has_metric_signal": has_signal(lower, r"metric|accuracy|precision|recall|f1|auc|attack success|asr|false positive|rate"),
        "has_baseline_signal": has_signal(lower, r"baseline|state-of-the-art|sota|compare|compared|outperform"),
        "has_ablation_signal": has_signal(lower, r"ablation|component|sensitivity|variant|without"),
        "has_limitation_signal": has_signal(lower, r"limitation|discussion|ethic|responsible|future work|drawback"),
        "has_artifact_signal": has_signal(lower, r"github|code|release|available|reproducib|artifact|dataset|benchmark"),
        "problem_snippets": snippets(text, r"challenge|problem|difficult|threat|risk|vulnerab|malicious|privacy|safety"),
        "contribution_snippets": snippets(text, r"we propose|we introduce|we present|contribution|framework|benchmark|dataset"),
        "evaluation_snippets": snippets(text, r"experiment|evaluation|result|baseline|metric|accuracy|attack success|ablation"),
        "risk_snippets": snippets(text, r"attacker|threat model|malicious|jailbreak|backdoor|poison|privacy|harmful"),
    }


def merge_records(old_records: list[dict[str, Any]], new_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for record in old_records + new_records:
        key = norm(record.get("pdf_url")) or norm(record.get("local_pdf")) or norm(record.get("title"))
        merged[key] = record
    return sorted(merged.values(), key=lambda r: (r.get("year", ""), r.get("title", "")))


def md_escape(value: Any) -> str:
    text = str(value if value is not None else "")
    text = re.sub(r"\s+", " ", text).strip()
    return text.replace("|", "\\|")


def signal_names(record: dict[str, Any]) -> str:
    names = []
    for key, label in [
        ("has_threat_model_signal", "threat_model"),
        ("has_dataset_signal", "dataset"),
        ("has_metric_signal", "metric"),
        ("has_baseline_signal", "baseline"),
        ("has_ablation_signal", "ablation"),
        ("has_limitation_signal", "limitation"),
        ("has_artifact_signal", "artifact"),
    ]:
        if record.get(key):
            names.append(label)
    return ", ".join(names)


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def make_report(records: list[dict[str, Any]]) -> str:
    year_counts = Counter(record["year"] for record in records)
    label_counts: Counter[str] = Counter()
    for record in records:
        label_counts.update(record.get("labels", []))
    signal_counts = Counter()
    for record in records:
        for key in [
            "has_threat_model_signal",
            "has_dataset_signal",
            "has_metric_signal",
            "has_baseline_signal",
            "has_ablation_signal",
            "has_limitation_signal",
            "has_artifact_signal",
        ]:
            if record.get(key):
                signal_counts[key] += 1

    lines = [
        "# AAAI Security/LLM-Agent Full-Text Structure Report",
        "",
        f"Corpus size: {len(records)} PDFs. Generated from full-text `pdftotext` extraction.",
        "",
        "## Counts",
        "",
        "| Bucket | Count |",
        "|---|---:|",
    ]
    for year, count in sorted(year_counts.items()):
        lines.append(f"| {md_escape(year)} | {count} |")
    lines.extend(["", "## Topic Labels", "", "| Label | Count |", "|---|---:|"])
    for label, count in label_counts.most_common():
        lines.append(f"| {md_escape(label)} | {count} |")
    lines.extend(["", "## Structural Signals", "", "| Signal | Papers |", "|---|---:|"])
    for key in [
        "has_threat_model_signal",
        "has_dataset_signal",
        "has_metric_signal",
        "has_baseline_signal",
        "has_ablation_signal",
        "has_limitation_signal",
        "has_artifact_signal",
    ]:
        lines.append(f"| {key} | {signal_counts[key]} |")
    lines.extend(
        [
            "",
            "## Paper-Level Structure Index",
            "",
            "| Year | Title | Labels | Key sections | Signals | Local PDF |",
            "|---|---|---|---|---|---|",
        ]
    )
    for record in records:
        sections = ", ".join(record.get("section_headings", [])[:8])
        labels = ", ".join(record.get("labels", []))
        lines.append(
            f"| {md_escape(record.get('year'))} | {md_escape(record.get('title'))} | "
            f"{md_escape(labels)} | {md_escape(sections)} | {md_escape(signal_names(record))} | "
            f"`{md_escape(record.get('local_pdf'))}` |"
        )
    lines.append("")
    return "\n".join(lines)


def update_count_references(repo_root: Path, total: int, expansion_count: int, label_counts: Counter[str]) -> None:
    replacements = [
        (repo_root / "resources/aaai-security-corpus/AAAI_security_llm_agent_corpus_index.md", [
            (r"expanded from the initial 18-paper seed set to \d+ PDFs", f"expanded from the initial 18-paper seed set to {total} PDFs"),
            (r"`AAAI_security_llm_agent_expansion_manifest\.json`: \d+ additional downloaded", f"`AAAI_security_llm_agent_expansion_manifest.json`: {expansion_count} additional downloaded"),
        ]),
        (repo_root / "skills/aaai-conference-on-artificial-intelligence/references/security-llm-agent-aaai-patterns.md", [
            (r"Corpus size after expansion: \d+ PDFs", f"Corpus size after expansion: {total} PDFs"),
        ]),
        (repo_root / "skills/aaai-security-paper-review/SKILL.md", [
            (r"Use the \d+-paper full-text structure report", f"Use the {total}-paper full-text structure report"),
        ]),
        (repo_root / "skills/aaai-writing-style/SKILL.md", [
            (r"the \d+-paper AAAI security/LLM-agent corpus", f"the {total}-paper AAAI security/LLM-agent corpus"),
        ]),
        (repo_root / "skills/aaai-writing-style/references/security-llm-agent.md", [
            (r": \d+ AAAI-24/25/26 papers", f": {total} AAAI-24/25/26 papers"),
        ]),
    ]
    for path, patterns in replacements:
        text = path.read_text(encoding="utf-8")
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)
        if path.name == "AAAI_security_llm_agent_corpus_index.md":
            text = replace_label_table(text, label_counts)
        path.write_text(text, encoding="utf-8")


def replace_label_table(text: str, label_counts: Counter[str]) -> str:
    table = ["Current full-text label counts:", "", "| Label | Count |", "|---|---:|"]
    for label, count in label_counts.most_common():
        table.append(f"| {label} | {count} |")
    table.append("")
    pattern = r"Current full-text label counts:\n\n\| Label \| Count \|\n\|---\|---:\|\n(?:\|.*\|\n)+"
    return re.sub(pattern, "\n".join(table), text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=repo_root_from_script())
    parser.add_argument("--pdf-dir", type=Path, required=True)
    parser.add_argument("--additional", type=int, default=48)
    parser.add_argument("--pdftotext", default=shutil.which("pdftotext") or "pdftotext")
    parser.add_argument("--pause", type=float, default=0.1)
    parser.add_argument("--rebuild-all", action="store_true", help="Re-extract every local PDF already in the JSONL.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    pdf_dir = args.pdf_dir.resolve()
    pdf_dir.mkdir(parents=True, exist_ok=True)
    corpus_dir = repo_root / "resources" / "aaai-security-corpus"

    candidate_pool = read_json(corpus_dir / "AAAI_security_llm_agent_candidate_pool.json")["candidates"]
    expansion = read_json(corpus_dir / "AAAI_security_llm_agent_expansion_manifest.json")
    existing_records = load_existing_records(pdf_dir)
    keys = existing_keys(existing_records, expansion)
    selected = choose_candidates(candidate_pool, keys, args.additional)

    print(f"existing records: {len(existing_records)}")
    print(f"selected additions: {len(selected)}")
    for item in selected:
        print(f"- {item['year']} {item['title']}")
    if args.dry_run:
        return 0

    new_records: list[dict[str, Any]] = []
    for item in selected:
        pdf_path = download_pdf(item, pdf_dir, args.pause)
        text = run_pdftotext(args.pdftotext, pdf_path)
        record = structure_record(item, pdf_path, text)
        new_records.append(record)
        print(f"extracted: {pdf_path.name}")

    if args.rebuild_all:
        rebuild_items: list[dict[str, Any]] = []
        seen_local: set[str] = set()
        for record in existing_records + new_records:
            local_pdf = record.get("local_pdf")
            if not local_pdf or local_pdf in seen_local:
                continue
            seen_local.add(local_pdf)
            rebuild_items.append(record)
        rebuilt: list[dict[str, Any]] = []
        for item in rebuild_items:
            pdf_path = pdf_dir / item["local_pdf"]
            if not pdf_path.exists():
                print(f"missing local PDF, keeping old record: {item['local_pdf']}", file=sys.stderr)
                rebuilt.append(item)
                continue
            text = run_pdftotext(args.pdftotext, pdf_path)
            rebuilt.append(structure_record(item, pdf_path, text))
        merged_records = merge_records([], rebuilt)
    else:
        merged_records = merge_records(existing_records, new_records)
    write_jsonl(pdf_dir / "AAAI_security_llm_agent_fulltext_structure.jsonl", merged_records)
    (pdf_dir / "AAAI_security_llm_agent_fulltext_structure_report.md").write_text(
        make_report(merged_records), encoding="utf-8"
    )

    # Public repo stores metadata/report only, not raw PDFs or JSONL snippets.
    new_expansion = expansion + [
        {
            "year": str(item.get("year")),
            "issue": item.get("issue"),
            "title": item.get("title"),
            "article_url": item.get("article_url"),
            "pdf_url": item.get("pdf_url"),
            "score": item.get("score"),
            "hits": item.get("hits", []),
            "local_pdf": item.get("local_pdf"),
            "status": item.get("status", "downloaded"),
        }
        for item in selected
    ]
    seen_pdf_urls: set[str] = set()
    dedup_expansion: list[dict[str, Any]] = []
    for item in new_expansion:
        key = norm(item.get("pdf_url")) or norm(item.get("title"))
        if key not in seen_pdf_urls:
            seen_pdf_urls.add(key)
            dedup_expansion.append(item)
    write_json(corpus_dir / "AAAI_security_llm_agent_expansion_manifest.json", dedup_expansion)
    (corpus_dir / "AAAI_security_llm_agent_fulltext_structure_report.md").write_text(
        make_report(merged_records), encoding="utf-8"
    )
    shutil.copy2(corpus_dir / "AAAI_security_llm_agent_corpus_index.md", pdf_dir / "AAAI_security_llm_agent_corpus_index.md")
    shutil.copy2(corpus_dir / "AAAI_security_llm_agent_candidate_pool.json", pdf_dir / "AAAI_security_llm_agent_candidate_pool.json")
    write_json(pdf_dir / "AAAI_security_llm_agent_expansion_manifest.json", dedup_expansion)

    label_counts: Counter[str] = Counter()
    for record in merged_records:
        label_counts.update(record.get("labels", []))
    update_count_references(repo_root, len(merged_records), len(dedup_expansion), label_counts)
    shutil.copy2(corpus_dir / "AAAI_security_llm_agent_corpus_index.md", pdf_dir / "AAAI_security_llm_agent_corpus_index.md")

    print(f"corpus size: {len(merged_records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
