# Changelog

This project manages changes to the skill, the knowledge base and the model adapters with semantic versioning.

## [1.1.0] - 2026-10-24

### Added

- A MiniMax H3 adapter in `references/model-adapters.md`: mode selection by attached media (three-field brief, first-frame alignment line, six-section reference brief), the performance timeline in H3's `[Shot N]` and timestamp grammar, `<d>` dialogue tags with speaker IDs, lips closing as an event after every line, voice references attached in speaking order and as WAV, and the fal Realism People LoRA as a tested fix for oily skin in hard light.

### Changed

- The whole repository is translated into English: the skill, references, knowledge base, validation records, documentation, examples and issue template. Chinese file and folder names are renamed to English (`knowledge-base/emotion`, `applications/performance-skill`, `asset-index.md` and so on).
- `search_emotion_library.py` accepts longer English headings (up to 80 characters), still recognises Chinese headings, ignores English words shorter than three letters in a query, and looks for the knowledge base in `knowledge-base/emotion`.
- Script messages are in English.
- The Word version of the knowledge base is regenerated from the English Markdown.

## [1.0.0] - 2026-08-03

### Added

- The complete Codex skill structure for the `Performance Skill`.
- The output priority in which emotion and the actor's performance take 60%-70% of the prompt.
- The eight-dimension performance framework, dual goals, emotional triggers, residue at the end and forbidden reactions.
- Rules for dialogue ownership, off-screen voices, cutting in, interruptions and triggers without dialogue.
- Camera Intent, with rules for when the camera stays still or moves, its path and its stopping point.
- Conservative model adaptation for Kling and Seedance 2.0.
- A searchable starting emotion knowledge base, in both Markdown and Word.
- The knowledge-base search script and the timeline validation script.
- Records of three dry runs, a stress test and the final acceptance check.

### Design decisions

- The emotion knowledge base only offers candidate actions; it never replaces judgement about the character and the story.
- Camera, continuity, background and technical parameters must not overpower the actor's performance.
- When the version is unknown, unconfirmed model abilities are never promised.
