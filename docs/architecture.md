# Architecture

## The three-layer prompt structure

1. **Scene and continuity lock**: keeps only the identity, space, props, light and previous-shot state most likely to drift.
2. **Shot timeline and Camera Intent**: sets the triggers, the timing of reactions, the camera position, and why it moves or stays still.
3. **The actor's eight-dimension performance**: completes the performance through intention, emotional path, face, body, voice, end state and forbidden reactions.

The three layers are not equal. The actor's performance is the core; the first two layers only make the performance readable, continuous and possible to generate.

## Execution data

A complex beat can record five fields:

- `speaker`: the person actually speaking.
- `camera_subject`: the main subject the camera is watching.
- `trigger_event`: the word, sound, look, object or action that triggers a change in the performance.
- `evidence_source`: where the audience sees or hears the change.
- `information_priority`: what the audience must understand first at this moment.

## Repair order when generation fails

1. Remove conflicting emotions and actions.
2. Reduce the action density per shot and lengthen the key pauses.
3. Fix the order of trigger and reaction, and the speaker and the subject on camera.
4. Simplify unmotivated camera moves.
5. Add the single most necessary continuity anchor.
6. Only then adjust image quality and model parameters.

Change one variable at a time, so you can tell what actually fixed it.
