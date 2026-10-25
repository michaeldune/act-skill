---
name: direct-ai-actor-performance
description: Rewrite a script, dialogue, character conflict, rough AI video prompt or reference performance into a precise video-generation prompt in which emotion and the actor's performance dominate. Use when the user mentions the Performance Skill, AI actors, emotional build, micro-expressions, crying scenes, arguments, goodbyes, pauses in dialogue, breathing, cutting in, off-screen voices, camera placement that serves emotion, or performance prompts for Kling, Seedance 2.0 or MiniMax H3.
---

# Performance Skill

## Goal and priorities

Translate "what the character is doing" into "why the character does it, how the emotion unfolds over time, and what evidence the audience can see". The final prompt must be led by the actor's performance. Camera, continuity and technical settings only support the performance.

Default information budget:

- Emotion and the actor's performance: 60%-70%
- Dialogue, sound, breathing and pauses: 10%-15%
- Camera position, framing and movement: 10%-15%
- Character, environment, prop and lighting continuity: 5%-8%
- Model parameters and image-quality words: 3%-5%

If the user asks for a different split, follow the user. Never let camera jargon, quality adjectives, background detail or knowledge-base material take over.

## Workflow

1. **Lock the input facts**: extract the characters, relationships, place, time, dialogue, order of events, any existing camera setups, what must not change, and what is uncertain. Do not add story facts.
2. **Find the dramatic core**: in one sentence, state the external goal, the suppressed internal goal, the obstacle and the turn. If there is no conflict, do not invent big emotion; play it through small intentions and behaviour.
3. **Build the emotional curve**: starting state -> trigger -> suppression or escalation -> turn -> what remains at the end. Every emotion needs a cause, a time and a visible carrier.
4. **Search the emotion knowledge base when useful**: understand the characters and the scene first, then search `knowledge-base/emotion` at the repository root with `scripts/search_emotion_library.py`. The script reads the `ACT_SKILL_KB` environment variable first, then finds the knowledge base inside the repository. Take only the pieces that fit; when nothing matches or a piece conflicts, generate your own instead of forcing a template.
5. **Allocate time**: write start and end times per shot or performance beat. Leave time for the trigger and the reaction first, then place dialogue and action. When needed, check overlaps, gaps and dialogue length with `scripts/validate_timeline.py`.
6. **Design the performance**: every key beat covers at least "intention, trigger, visible reaction, sound or silence, end state". Use the eight-dimension performance framework for important passages.
7. **Design the camera intent**: decide still or moving first, then write the camera position, what starts the move, its path, speed, duration and stopping point. The camera only serves emotion and the reveal of information.
8. **Compress continuity**: write only what is most likely to drift in this shot: identity, wardrobe, spatial relationships, prop state, light direction and the continuity of the soundscape.
9. **Adapt to the model**: read `references/model-adapters.md` and output a Kling, Seedance 2.0 or MiniMax H3 version. When the version is unknown, write conservatively and generically, and never invent features.
10. **Check backwards and repair**: fix emotional cause and effect and the beats first, then dialogue ownership and reaction timing, then the camera, and continuity and parameters last.

## The eight-dimension performance framework

For each key beat, decide in order:

1. **Time and shot**: which second, which shot, how long it lasts.
2. **Dual goals**: the external action the character wants to complete; the internal state the character wants to hide, hold down or keep the other person from noticing.
3. **Emotional path**: start, trigger, direction of change and end point, not just the name of the emotion.
4. **Trigger and carrier**: which line, sound, look, object or action triggers it; whether the reaction lands in the eyes, face, breath, posture, hands or action.
5. **Facial action**: use movements a viewer can actually see, such as the eyelids tightening, the corners of the mouth losing support, the jaw tightening briefly; avoid writing only "sad face". Consult `references/facs-action-units.md` when needed, but write natural language in the prompt.
6. **Body and action**: where the eyes land, head and neck direction, chest and shoulders, weight, steps, the task in the hands, and whether the action is completed, interrupted, held or fails.
7. **Sound and silence**: speaker, volume, timbre, pace, breath, pauses, swallowing, broken phrasing, cutting in, off-screen voices and necessary silence.
8. **Ending and forbidden reactions**: where the emotion is left at the end of the shot; explicitly forbid reactions that would break the beat, such as tears too early, turning the head too early, looking at the trigger too early, or large movements without a reason.

## Dialogue and trigger rules

- Mark the `speaker` of every line; mark the `camera_subject` when needed. They can differ.
- For an off-screen voice, a phone call, a broadcast or a voice behind a door, state where the sound comes from and who in frame reacts.
- For cutting in and interruptions, write who interrupts whom, after which word or action, and what unfinished reaction the interrupted person is left with.
- When there is no dialogue, give a trigger: an ambient sound, a look, a photo, a door, a phone vibrating, an object changing state, or someone else's silent action.
- A reaction usually comes after its trigger; unless the story requires it, do not let a character know the next event in advance.

## Camera intent rules

For every shot, add one internal judgement: `What does the audience need to feel at this moment, so why is the camera here, and why does it move or not move?`

- **Still**: for pressure, awkwardness, waiting, nowhere to escape, or letting micro-expressions happen on their own; always write the emotional reason for staying still.
- **Moving**: only a trigger, a change in the relationship, a reveal of information or a physical action may drive it. Write the start condition, direction or path, speed, duration and stopping point.
- **Position**: distance, eye height, side angle, obstruction and the spatial relationship between characters should reflect closeness, distance, control, vulnerability or unequal information.
- No mechanical formulas such as "sadness always pushes in, anger is always handheld". The same emotion may call for opposite camera choices depending on the character's goal.
- Camera movement must not steal the actor's small reactions; when unsure, prefer stable, readable and minimal movement.

For complex dialogue, off-screen voices and camera patterns, see `references/dialogue-camera.md`.

## Minimal continuity lock

Add one line only when there is a risk of drift:

`Continuity lock: key identity and wardrobe features; spatial axis and character positions; the hand, direction and state of key props; key light direction and time of day; the action and emotional residue from the previous shot.`

Keep only the 1-2 most recognisable anchors in each category. Unless the user asks, do not write long set descriptions, camera specifications or wardrobe lists.

## Output format

By default, deliver a copy-ready prompt organised in this order:

1. **Model and total duration**
2. **Scene and continuity lock** (1-3 lines)
3. **Dramatic core and overall performance direction**
4. **Shot timeline**: for each shot, the time, subject, trigger, performance, dialogue or sound, camera intent and end state
5. **Global forbidden reactions**
6. **Model adaptation notes where needed** (keep them short)

If the user wants only one model, output only that version. If no model is given, give a generic master first, then the minimal differences for Kling, Seedance 2.0 and MiniMax H3, without copying the full text three times. For MiniMax H3 the prompt itself must be written in H3's own format; see the H3 section of `references/model-adapters.md`.

## Quality checklist

Before delivering, check each item:

- Is every change of emotion triggered by a clear event rather than switching out of nowhere?
- Do the external action and the suppressed internal goal both hold at the same time?
- Does every abstract emotion have at least one piece of evidence that can be seen or heard?
- Do expression, breath, body and voice happen in sequence instead of all at once?
- Are dialogue ownership, off-screen voices, interruptions and the target of each reaction clear?
- Does the time hold the dialogue, pauses and action? Is the action density too high?
- Does the camera explain why it moves or stays still, and does it start at the right trigger?
- Are camera and continuity short and subordinate, not overpowering the performance?
- Are the user's original story, order, lines and constraints kept? Is everything added purely executional?
- Are model capabilities stated conservatively, with no unconfirmed features promised?

## Repair order

When the output is unstable, change one variable at a time:

1. Remove conflicting emotions and actions.
2. Reduce the number of actions per shot and lengthen the key pauses.
3. Make the order of trigger and reaction, and the speaker and the subject on camera, explicit.
4. Simplify or remove unmotivated camera moves.
5. Add the single most necessary continuity anchor.
6. Only then adjust image quality, camera language or model parameters.
