# AAAI Security Corpus Metadata

This directory stores non-PDF metadata for the AAAI security, SOC, threat-analysis, and LLM-agent corpus used by the skills.

Included files:

- `AAAI_security_llm_agent_corpus_index.md`: seed corpus and extracted venue patterns.
- `AAAI_security_llm_agent_expansion_manifest.json`: expanded paper manifest with official AAAI OJS URLs.
- `AAAI_security_llm_agent_candidate_pool.json`: broad title-level candidate pool from AAAI-24, AAAI-25, and AAAI-26 OJS issue pages.
- `AAAI_security_llm_agent_fulltext_structure_report.md`: readable structure report with paper labels, section signals, and evidence flags.

Not included:

- PDF files.
- Full extracted paper text.
- Generated JSONL snippets from full PDFs.

Use the official OJS URLs in the manifest to download papers when local full-text inspection is needed.

