# Performance Skill Final Acceptance

- Acceptance date: 2026-08-03
- Display name: Performance Skill (originally the Chinese name "表演skill")
- Internal name: direct-ai-actor-performance
- Skill structure check: passed `quick_validate.py`
- Python script compilation: passed
- Search of the Word emotion knowledge base: passed; the query "sadness restrained delayed does not want to be seen" returned the sadness entry first
- 12-second performance timeline: passed; no overlaps, out-of-range beats or dialogue overruns
- Visual check of the Word file: 11 pages in total; checked page by page, with no cropping, overflow, garbled text or broken tables
- Model adaptation: includes conservative Kling adaptation and Seedance 2.0 multimodal and multi-shot adaptation
- Installation: one central source folder plus a junction into the Codex skills folder, to avoid two drifting copies of the source

## English translation re-check (2026-10-24)

- The search script was rerun against the English Markdown knowledge base: the same sadness query returns "1. Sadness: Restraint, Delayed Reaction and the Edge of Breaking" first (score 115). See `smoke-search-result.json`.
- The 12-second timeline was rerun with the English dialogue. The English trigger line ("Let's end it here.") is estimated at 1.79 s against the original Chinese line's 1.45 s, so that beat's reserved action time was reduced from 1.5 s to 1.2 s; the timeline now passes with no issues. See `smoke-timeline-result.json`.
- The Word file was regenerated from the English Markdown and has not had the original page-by-page visual check.
- A MiniMax H3 adapter was added to `references/model-adapters.md`.

## Core boundaries

By default, emotion and the actor's performance take 60%-70% of the prompt; sound 10%-15%; camera 10%-15%; continuity 5%-8%; technical words 3%-5%. Camera, background, identity continuity and model parameters must never overpower the performance.

## Reviewable results

- `smoke-search-result.json`: the top knowledge-base hit and its text.
- `smoke-timeline.json`: the 12-second test input.
- `smoke-timeline-result.json`: the timeline validation result.
- `validation/`: the specification draft, the three dry runs and the camera stress test.
