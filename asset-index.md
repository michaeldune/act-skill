# Act Skill Asset Index

This repository is the single source of truth for the `Performance Skill` source code, knowledge base and validation records.

## Folder conventions

- `skills/`: executable Codex skills.
- `knowledge-base/`: domain knowledge the skill can search, one folder per topic.
- `applications/`: real cases, tests, templates and reviews.
- `registry/`: machine-readable skill registration.
- `docs/`: architecture, knowledge-base maintenance and usage notes.
- `examples/`: input and output examples you can copy.

## Current assets

- Display name: `Performance Skill`
- Internal skill name: `direct-ai-actor-performance`
- Skill: `skills/direct-ai-actor-performance`
- Emotion knowledge base: `knowledge-base/emotion`
- Application records: `applications/performance-skill`

A local central folder can be configured with `ACT_SKILL_KB`; it is not a hard dependency for running the repository.

## Rules for new assets

1. A new skill goes in `skills/<internal-name>/`, with its display name in `agents/openai.yaml`.
2. Reusable knowledge goes in `knowledge-base/<topic>/` and must not be buried in the skill's main instructions.
3. Real cases and validation reports go in `applications/<display-name>/`.
4. Register the path, version, model adapters and knowledge-base dependencies in `registry/skills.json`.
5. Keep only one editable source; other install locations use a directory junction or a symbolic link.
