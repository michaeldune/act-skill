# Emotion Knowledge Base Maintenance Guide

## What you can submit

- Descriptions of emotions and acting methods
- Gaze, face, breath, pauses and vocal states
- Body actions, weight and unfinished actions
- Observations of film or actors' performances
- Prompts verified by real generations
- Failure cases and the fixes that worked

## Suggested submission format

```text
Content type: quotation / personal observation / real test
Source:
Emotion:
Characters and scenes it applies to:
Keep the original wording?:
May it be merged and de-duplicated?:
Text:
```

## Bar for inclusion

An entry should answer at least:

1. What event triggers the emotion?
2. What external action does the character want to complete?
3. What is the character hiding or holding back?
4. How does the emotion change in stages?
5. What can the audience see?
6. What can the audience hear?
7. Is the action completed, held or does it fail in the end?
8. Which reactions must not happen too early?

Material with only abstract emotion labels and no executable behaviour must be translated into behaviour before it can be included.

## Versioning

- Small additions: bump the minor version, for example `v1.1`.
- Structural changes: bump the major version, for example `v2.0`.
- Mark verified content separately from experience still to be verified.
- Do not force contradictory experience into one entry; note the conditions each applies under.
- The Markdown version is the source for Git comparison, collaboration and search; the Word version is generated from it for reading. Keep them in sync.
