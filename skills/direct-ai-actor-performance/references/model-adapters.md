# Adapting to Kling, Seedance 2.0 and MiniMax H3

## The shared master

First write a platform-independent performance master: total duration, scene lock, character goals, emotional curve, second-by-second beats, dialogue and sound, camera intent, end state and forbidden reactions. Model adaptation only changes how this is organised, never the logic of the performance.

## Seedance 2.0

Official material describes Seedance 2.0 as accepting multimodal input (text, images, audio and video), with automatic shot planning, multi-shot audio-visual generation and high-quality output up to about 15 seconds. When adapting:

- Within 15 seconds, a clear multi-shot timeline is fine; the number of shots follows the completeness of the performance, never cut up just to show the feature off.
- When the user provides character images, motion videos or audio, state what each one is for: identity and look, motion or camera reference, voice or rhythm reference.
- Make dialogue, ambient sound and key silences explicit; avoid filling the track with music, dialogue and ambience all at once.
- For fine-detail stability, hyper-realistic texture or strong motion, still use conservative wording, and protect the result with the fewest continuity anchors.

Official sources:

- https://seed.bytedance.com/blog/seedance-2-0-official-launch
- https://seed.bytedance.com/en/seedance2_0

## Kling

Kling's features change between versions and interfaces. The official Kling VIDEO 3.0 guide covers native audio and video, multi-shot and custom multi-shot, and element references, but these abilities must not be assumed for every older version. When adapting:

- Once the interface is confirmed to support "custom multi-shot", split the shots in time order and give each one its duration.
- Once element or character references are confirmed, use the references to lock identity, look or voice; the text only adds the states most likely to drift, without repeating long character descriptions.
- When the version is unknown or there is only a plain text box, output one connected prompt and express the beats with "first... the trigger... finally...", using fewer platform-specific fields.
- Keep dialogue, timbre and ambience notes only when native audio is available; otherwise treat sound notes as a rhythm reference for the performance and never promise usable sound.

Official source:

- https://app.klingai.com/cn/quickstart/klingai-video-3-model-user-guide

## MiniMax H3

H3 was trained on a structured brief, not on free prose, so the performance master has to be poured into H3's own fields. Everything below the "Format" heading is fixed syntax; everything in the performance timeline is still the master's acting, written in English. Notes marked "tested" were measured on MiniMax H3 through SimpliGen cards in October 2026; the rest is the documented H3 format.

### Format: pick the mode from the media actually attached

- **No images (T2VA):** three fields, in this order.

  ```text
  integrated_multimodal_description: [Shot 1] ...
  overall_soundscape: ...
  non_diegetic_music: ...
  ```

  Write `None.` in `non_diegetic_music` when there is no score.
- **One image that is the first frame (I2VA):** the first line is exactly
  `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.`
  then one blank line, then the three fields. Describe how the existing image comes to life; do not invent what the image does not show.
- **Character, place or voice references (Ref2VA):** six sections in this order: `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, `non_diegetic_music`. Bind each person to their picture inside the subject line (`<Subject 1> is the woman in <Picture 1>, with ...`), give every subject a retention line (`fully_preserved` for people, `partially_preserved` for a setting), and number pictures in the order they are attached.

The performance timeline goes in `integrated_multimodal_description` (T2VA, I2VA) or `detailed_description` (Ref2VA). The 60%-70% performance budget applies to that timeline, not to the fixed section headers.

### The performance timeline in H3 terms

- `[Shot 1]` has no timestamp. Later shots start `[Shot N] At MM:SS.mmm, the camera cuts to ...` with times that increase and stay inside the clip. Inside a shot, put each beat on the clock: `At 00:03.500, ...`. The master's trigger-then-reaction order maps directly onto these timestamps; give the reaction its own, later timestamp.
- **Every shot states its camera.** Unstated, H3 drifts and reframes. For a still camera write `The frame never moves: no pan, no push-in, no zoom, no reframing.` For a move, name one move, its amplitude and speed, and what visibly changes because of it.
- **Two characters reacting to each other** need, in each beat, an eye line ("her eyes on him", restated where it matters), a facing or distance end state, and a separate timestamp for the reaction. Without them H3 renders both actions but not the relationship.
- **Movement toward a target needs a stop:** a timestamp for the halt, a distance ("two paces in front of him") and the overshoot ruled out ("she does not walk past him").
- **Give each beat one primary change and an observable end state**, about four seconds for anything that handles an object, and keep the most important beat out of the last second.

### Dialogue

- Give every speaker a stable ID, `(S1)`, `(S2)`, and describe the voice once outside the tag: pitch, timbre, pace, accent.
- Put the spoken words, verbatim, inside `<d>[English] the exact words</d>` in the beat where they are spoken. Never translate or paraphrase inside `<d>`.
- **After every line, write three things** (tested: this removed invented words on a seed that had garbled twice):
  1. the closure as an event: `The instant the line ends, her lips close completely and all speaking motion stops.`
  2. an observable silent end state for the leftover time: `For the rest of the shot she stays silent, lips closed, eyes on the door.`
  3. the failure named as a prohibition: `She speaks only once, does not repeat any part of the line, and no further words occur.`
  This is the opposite of the Seedance advice to avoid mouth mechanics: for H3 the closure sentence is required.
- Budget about 2.5 to 3.5 words per second of speech (tested range 2 to 4, depending on the delivery), so roughly 40 words per 15 seconds, and leave time after the last line.
- H3 generates a soundtrack for the whole clip. When nobody speaks, say so (`No one speaks; their lips stay closed throughout.`) and describe what is heard instead. `overall_soundscape: None.` does not produce silence.
- Directions aimed at the generator ("keep it short", "do not add anything") have no effect; describe what happens in the scene instead.

### Voice references (one `<Audio N>` per speaker)

- **Attach the voices in the order the characters first speak.** Tested with two women whose references differed only in pitch: in speaking order each got her own voice; attached in reverse order, with every label still bound correctly, the voices swapped on both seeds. H3 gives the first-attached voice to the first speaker whatever the labels say. A man and a woman hide the problem, because the gender in the prompt wins.
- **Use uncompressed WAV from the source, never MP3.** Tested: a 32 kbps MP3 reference left the generated voice with almost no energy above 6 kHz (0.01-0.02% against 0.71-0.89% for the same voice as WAV). Converting an MP3 to WAV does not restore it. A good reference is one isolated voice with no music, noise or room echo, at a steady level.

### Faces and realism

- In hard light H3 tends to give skin an oily, waxy shine. The fal **MiniMax H3 Realism People LoRA** (`h3-realism-people-t2v-i2v-r2v`, trigger `r34l1sm` at the start of the prompt) removed that shine at strength 0.7 on both test seeds (shine pixels on the face from about 1-2% down to under 0.1%); 1.0 added little except lower contrast. It also regenerates the shot, so framing and the person change with it. Two other realism LoRAs tested in the same scene (Digicam Realism Improve, Facial Realism CloseUp) did not reduce the shine.
- Large, sudden facial muscle movements can break facial anatomy, especially from a noisy reference or one with heavy freckles, acne or scars. Prefer clean, evenly lit references and keep the biggest expressions brief.

### What stays the same

The eight-dimension framework, the dual goals, trigger before reaction, the camera intent and the forbidden reactions all carry over unchanged. Only the container changes.

## Adaptation rules for every model

- Do not make the model name, resolution, "cinematic" or camera model the body of the prompt.
- Do not promise input counts, durations or audio abilities the platform has not confirmed.
- Do not add unnecessary cuts just because multi-shot is supported.
- Do not output three nearly identical long prompts; use the master plus the differences.
