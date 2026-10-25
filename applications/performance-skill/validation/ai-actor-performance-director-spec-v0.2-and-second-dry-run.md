# AI Actor Performance Director: Specification v0.2 and Second Dry Run

> Status: spec validation stage, Skill not yet created  
> Second test type: no dialogue, restrained grief  
> Knowledge base status: "emotion" directory not found, using the independent-generation fallback

# Part 1: Specification v0.2

## 1. v0.2 Core Structure

The Skill keeps the three-layer architecture:

1. Scene and character continuity lock
2. Shot timeline
3. Performance beats within each shot

On top of the original eight performance dimensions, four execution fields are added:

- speaker: the current speaker; null when there is no dialogue
- camera_subject: who the camera is watching
- trigger_event: the event that causes a change in the performance
- evidence_source: whether an action comes from the user, a reference video, the emotion knowledge base, or independent generation

These four are not "performance content"; they are system metadata that make sure the prompt executes correctly and can be traced.

## 2. Mandatory Pre-Checks

Before generating performance beats, complete these in order:

### 2.1 Character and Objective

Answer:

- Who the character is
- Their relationship to the others in the scene
- What is happening right now
- What the character wants to achieve
- What the character wants to hide

### 2.2 Timing Feasibility

With dialogue, calculate:

Spoken line duration + breaths + pauses + post-line reaction + cut buffer

Without dialogue, calculate:

Time to register the trigger + physiological delay + development of the action + emotional peak + fall-off or stillness

When there is not enough time, you must:

- Increase the length
- Cut lines
- Reduce the number of actions
- Merge non-essential shots

Do not simply speed up delivery or cram every action into the same second.

### 2.3 Optional Emotion Knowledge Base

Search order:

1. Understand the character and the conflict
2. Build a structured query
3. Look for the "emotion" directory
4. Return candidate actions
5. Judge whether they fit the current character
6. If nothing is found or nothing fits, generate independently

The knowledge base is not a requirement and must not block the task.

## 3. v0.2 Performance Beat Fields

### System Fields

- Shot number
- Start and end time
- speaker
- camera_subject
- trigger_event
- evidence_source

### Eight Performance Dimensions

1. Time and shot
2. Character objective
3. Emotional starting point -> trigger -> end point
4. Lines and trigger words; when there are no lines, record the non-verbal trigger
5. Visible facial action
6. Eyeline, body and weight
7. Voice, breath, pauses and silence
8. End state and prohibited early reactions

## 4. Non-Dialogue Trigger Rules

A trigger_event can be:

- A phone vibrating
- A door opening
- The other person stopping what they are doing
- A doctor shaking their head
- Seeing a particular object
- Hearing a distant sound
- Noticing an empty seat
- Reading a message
- The other person not answering
- Ambient sound suddenly stopping

A non-dialogue trigger must have three stages:

1. The event actually happens
2. The character perceives and understands the event
3. The change in performance begins

The character must not react before the event happens, and must not hit the emotional peak on the same frame the event happens.

## 5. Silence Rules

Silence is not "no sound". It needs to state:

- Whether ambient sound continues
- Whether the character is breathing
- Whether clothing or objects make sound
- Whether there is swallowing, a nasal breath or an unfinished inhale
- How long the silence lasts
- What changed before and after the silence

A scene without dialogue should not use continuous background music in place of the whole performance. If there is background music, it must not mask breathing or key ambient sounds.

## 6. Stages of Physiological Reaction

### Tears

Break into:

1. A wet sheen on the surface of the eye
2. Water pooling on the lower lid
3. Blinking fails to clear the pooling
4. A tear spills over the lid
5. The tear runs down the cheek
6. Whether the tear is wiped away

### Breath

Break into:

- Normal breathing
- Breathing becomes shallow
- An inhale is cut off
- Breath-holding
- Exhale release
- Breathing recovers

### Swallowing and Jaw

Use to show an attempt to regain control:

- A slight swallow in the throat
- Jaw clenches
- Jaw releases
- Lips try to close

Physiological reactions must serve the character's objective, not be piled on just for a "cinematic" feel.

## 7. Reaction Time After Lines and Events

After an important line or trigger event, real reaction time must be allowed.

The suggested minimum is not a fixed number; it depends on the action:

- A single blink or eye movement: about 0.2-0.6 seconds
- A brief pause after taking in information: about 0.5-1.5 seconds
- Inhaling, swallowing and regaining control: about 1-2 seconds
- Tears forming slowly: usually takes several beats and should not happen instantly

These values are only for timing feasibility checks, not a universal performance speed for every character.

## 8. v0.2 Fixed Output

1. Input understanding and assumptions
2. Timing feasibility report
3. Emotion knowledge base usage
4. Scene and character continuity lock
5. Shot timeline
6. Performance beat table
7. Complete Master Prompt
8. Model-adapted version; only when a model is specified
9. Negative constraints
10. Post-generation acceptance checklist
11. Single-variable fix order
12. Uncertainties and source notes

---

# Part 2: Second Dry Run

## 1. Test Scene

### Agent-Generated Test Input

A woman of about 40 sits alone at the table in a kitchen at night. There are two cups on the table, and one of them has not been used. Her phone vibrates, and the screen shows a message with bad news that has already been confirmed. The picture does not show the actual text, and there is no dialogue.

Character objective:

> She wants to keep herself together and not fall apart right away.

Performance goal:

> Move from ordinary waiting to grasping the facts, then into restrained grief; no heavy crying, no tears at the first moment.

Length: 15 seconds.

### Why This Test

It can verify:

- Whether a trigger chain can still be built without lines
- Whether silence can be described concretely
- Whether the emotion relies on observable evidence
- Whether the first tear can be staged in phases
- Whether the Skill relies too heavily on arguments and dialogue

## 2. Input Understanding and Assumptions

Stated facts:

- One person
- Kitchen at night
- The phone message is the trigger event
- No dialogue
- The character is trying to hold back

Agent assumptions:

- The message content is not shown, to avoid inventing a specific death, illness or relationship event.
- The second cup only hints that she was waiting for someone else; it does not define who that person is.
- No background music, to keep the ambience and the breathing.
- In the end no tear falls; "water pooled but still held on the lid" is used to test a restrained performance.

## 3. Timing Feasibility

15-second breakdown:

- 0.0-2.5 seconds: ordinary waiting state
- 2.5-3.0 seconds: phone vibrates
- 3.0-5.0 seconds: looks at and reads the message
- 5.0-7.0 seconds: delay in understanding
- 7.0-10.5 seconds: physiological reaction gradually builds
- 10.5-13.5 seconds: tries to regain control
- 13.5-15.0 seconds: stillness, not fully recovered

There is enough time; no extra shots or actions are needed.

## 4. Emotion Knowledge Base

- emotion_library_used: false
- fallback_reason: knowledge base path not found
- Source of actions: generated independently by the agent from the character's objective and visible evidence

## 5. Scene and Character Continuity Lock

- The same kitchen at night.
- The woman sits in the same place at the table; she does not stand up or leave.
- The two cups, the phone and the chair do not move.
- The warm kitchen light is steady, with no dramatic flicker.
- The camera stays on a medium close-up and does not cut to a close-up of the message.
- The actual message text is not shown.
- No second person and no off-screen dialogue are added.
- Keep the low hum of the fridge, distant traffic, the phone vibration and the character's breathing.

## 6. Shot Timeline

| Shot | Time | Camera subject | Shot size | Camera | Task |
|---|---:|---|---|---|---|
| 1 | 0.0-15.0 sec | The woman | Medium close-up from the chest up, with part of the table and both cups visible | Locked-off, with only a very slight breathing feel | Observe the trigger, understanding, restraint and stillness continuously |

This scene does not cut. Reasons:

- Cutting to a close-up of the phone would shift attention from the performance to the message content.
- A single medium close-up tests whether the Skill can carry the story on performance evidence alone.

## 7. Performance Beat Table

| Time | speaker | camera_subject | trigger_event | Objective | Emotional change | Performance evidence | End state | Prohibitions |
|---|---|---|---|---|---|---|---|---|
| 0.0-2.5 | null | The woman | None | Keep up a normal state while waiting | Calm but tired | Right hand lightly holding a cup handle, eyes resting near the other cup; breathing steady | Holds her seated position | Do not pre-play grief |
| 2.5-3.0 | null | The woman | Phone vibrates once on the table | Locate the sound | Calm -> attention interrupted | Eyes move first, head follows about 0.2 sec later; hand still holding the cup handle | Looks at the phone | Do not frown or cry immediately |
| 3.0-5.0 | null | The woman | Reads the screen | Understand the message | Attention -> beginning to understand | Fingers leave the cup handle, hover above the table for about 0.3 sec, then drop; eyes keep reading, no blinking | Body briefly freezes | Do not collapse instantly |
| 5.0-7.0 | null | The woman | Message finished | Refuse to accept it right away | Understanding -> slight loss of focus | Eyes still toward the phone but no longer reading; lips part naturally by about 2 mm; an inhale stops halfway | Holds her breath about 0.5 sec | Do not drop her head or cover her face |
| 7.0-9.0 | null | The woman | Breath-hold ends | Keep control | Defence starts to loosen | Inner brows lift very slightly, lower lids gradually tighten; jaw clenches; no large shoulder movement | Slow exhale | Do not let a tear form |
| 9.0-10.5 | null | The woman | Slow exhale | Push the emotion back down | Restraint -> eyes welling | A wet sheen appears on the eyes; nostrils flare slightly once; a swallow in the throat | Eyes leave the phone | Tears must not spill over the lid |
| 10.5-12.0 | null | The woman | Sees the other cup on the table | Keep pretending everything is normal | Welling -> stronger restraint | Eyes move to the empty cup; right hand reaches toward it but stops a few centimetres from the handle | Hand hovers | Do not grab the cup, no heavy crying |
| 12.0-13.5 | null | The woman | Hand cannot complete the action | Regain control of her body | Restraint near its limit -> pulling back | Hand slowly withdraws to her own side; lips try once to close but do not fully succeed; water pools on the lower lids | Breathing partly recovers | Do not wipe her eyes, no sound |
| 13.5-15.0 | null | The woman | No new event | Keep her composure | Unresolved stillness | She sits up a little, but her shoulders stay lower than at the start; eyes rest between the empty cup and the tabletop; only one unsteady exhale is heard | Picture ends in an unresolved state | No falling tear, no smile, no swelling music |

## 8. Complete Master Prompt

Generate a 15-second, realistic, cinematic short with no dialogue, showing a performance of restrained grief.

A kitchen at night. A woman of about 40 sits alone at the table. There are two cups on the table, and one of them has not been used. A phone lies on the table. Use a medium close-up from the chest up, with part of the table, the phone and both cups visible. The camera is locked off, with only a very slight breathing feel. The whole piece is one shot with no cuts; do not show the actual text of the phone message, and do not add a second person or off-screen dialogue.

0.0-2.5 seconds: she keeps up an ordinary waiting state. Her right hand lightly holds a cup handle, her eyes resting near the other cup. Her breathing is steady, and her face shows only slight tiredness, with no early sign of grief.

At 2.5 seconds the phone vibrates once on the table. Her eyes turn to the phone first, and her head follows about 0.2 seconds later. Her hand still holds the cup handle. Do not frown, hold her breath or cry on the same frame as the vibration.

3.0-5.0 seconds: she reads the screen. The fingers of her right hand leave the cup handle and hover above the table for about 0.3 seconds, then, having lost their purpose, slowly drop back to the table. She keeps reading and does not blink. The phone text is not visible.

5.0-7.0 seconds: she has finished reading the message but does not accept it right away. Her eyes are still toward the phone but no longer reading. Her lips part naturally by about 2 millimetres. She draws in a breath, but the inhale stops halfway, and she holds her breath for about 0.5 seconds. Her body briefly freezes. Do not drop her head, do not cover her face, do not suddenly cry.

7.0-9.0 seconds: she tries to keep control. Her inner brows lift only very slightly, her lower lids gradually tighten, and her jaw clenches. Her shoulders do not drop in an exaggerated way. When the breath-hold ends she exhales slowly.

9.0-10.5 seconds: a wet sheen begins to appear on her eyes, but the tears must not spill over the lids. Her nostrils flare slightly once, and she makes one controlled swallow. She moves her eyes away from the phone.

10.5-12.0 seconds: she sees the other cup on the table. Her right hand instinctively reaches toward that cup but stops a few centimetres from the handle. This unfinished action shows her trying to carry on waiting as before, though she can no longer do it. Do not grab the cup, do not suddenly add crying sounds.

12.0-13.5 seconds: she slowly draws her hand back to her own side. Her lips try once to close but do not fully succeed. Water pools on her lower lids, but no tear may fall. She does not wipe her eyes and makes no sound.

13.5-15.0 seconds: she tries to sit up a little, but her shoulders stay lower than at the start. Her eyes rest between the empty cup and the tabletop. She lets out just one unsteady, very quiet exhale. The picture ends in an unresolved stillness.

There is no background music in the sound. Keep only the low hum of the fridge, very distant traffic, the phone vibration, faint rustles of clothing, swallowing and the character's breathing. All sound stays close and restrained, with no musical climax.

## 9. Negative Constraints

- Do not show the actual message content.
- Do not add a second person, off-screen dialogue or flashback images.
- Do not pre-play grief before the phone vibrates.
- Do not reach the emotional peak on the same frame she reads the message.
- Do not drop her head and cover her face, and no sudden sobbing.
- Tears may only show as a wet sheen and water pooled on the lower lids; they must not fall.
- Do not add a sentimental score.
- Do not cut to a close-up of the phone.
- Do not grab the empty cup or throw a cup.
- Do not change the positions of the cups, the phone or the character.
- Do not use exaggerated brow movement or plastic-looking tear glints.

## 10. Post-Generation Acceptance

### Trigger

- [ ] The phone vibrates first and the character reacts after
- [ ] The eyes move first and the head follows slightly later
- [ ] There is a delay in understanding after reading the message

### Performance

- [ ] No grief is pre-played at the start
- [ ] The inhale stops halfway
- [ ] The eyes well up gradually
- [ ] The hand reaches toward the empty cup but does not complete the action
- [ ] At the end she tries to sit up but does not truly recover

### Tears

- [ ] Only a wet sheen and water pooled on the lower lids
- [ ] No tear spills over the lid
- [ ] The character does not wipe away tears

### Sound

- [ ] No background music
- [ ] The phone vibration is clear but not too loud
- [ ] Breathing, swallowing and ambient sound are audible
- [ ] The silence is not filled with unrelated sound effects

## 11. Findings from the Second Dry Run

### Finding 1: The Skill should not make "line trigger words" mandatory for every scene

A scene without lines still has a complete trigger chain.

Formal revision:

> The fourth dimension changes from "Lines and trigger words" to "Trigger event and carrier of expression". The carrier of expression can be a line, an environmental event, the other person's action, an object or silence.

### Finding 2: Silence must be part of the seventh dimension

Beyond voice, breath and pauses, the "soundscape of the silence" also needs to be stated.

Formal revision:

> The seventh dimension becomes "Voice, breath, pauses and silence", and must state the ambient sound, the character's physiological sounds and whether there is music.

### Finding 3: The character's objective needs to include "what they want to hide"

A character does not only want to complete an external action; they may also want to stop some emotion from showing.

Formal revision:

The character field is split into:

- External objective
- Internal suppression goal

In this example:

- External objective: carry on waiting as normal
- Internal suppression goal: not fall apart right away

### Finding 4: Unfinished actions are important performance evidence

A hand reaching for the cup without grabbing it is more actionable than "she is very sad".

Formal revision:

> Add a "completion state" to the body action field: completed, stopped, failed, interrupted, deliberately withdrawn.

### Finding 5: A single shot does not mean there is no time structure

Even when the whole piece does not cut, it still needs to be broken into trigger, understanding, physiological delay, the action forming, suppression and post-line stillness.

Formal revision:

> The Layer 2 shot timeline and the Layer 3 performance beats must stay separate; one shot can contain several beats.

### Finding 6: The knowledge base is still not a blocker

With no emotion directory, the Skill can still complete the task using the character's objective and observable evidence.

## 12. Conclusions from the Second Dry Run

The second test shows that this method does not only work for argument dialogue; it can also handle a wordless, single-character, restrained grief scene.

The core structure still holds, but the eight dimensions need a final adjustment to:

1. Time and shot
2. External objective and internal suppression goal
3. Emotional starting point -> trigger -> end point
4. Trigger event and carrier of expression
5. Visible facial action
6. Eyeline, body, weight and action completion state
7. Voice, breath, pauses and silence
8. End state and prohibited early reactions

This version is more complete than the eight dimensions in the original video, because it covers all of:

- Scenes with dialogue
- Scenes without dialogue
- Multi-character scenes
- Solo silent performance
- Physiological reactions
- Unfinished actions
- Trigger delay
- Soundscape and silence

The next step should be the third and final spec stress test: overlapping multi-character dialogue, the camera watching the listener, and the speaker off-screen. Once that passes, form Specification v1.0 and decide whether to create the Skill formally.
