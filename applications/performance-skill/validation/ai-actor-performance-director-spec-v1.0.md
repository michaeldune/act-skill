# AI Actor Performance Director Specification v1.0

> Skill directory name: direct-ai-actor-performance  
> Display name: AI Actor Performance Director  
> Status: final specification, Skill not yet created

## 1. Core Goal

Take the script, dialogue, character conflict, rough video concept, reference-video observations or existing prompt that the user provides, and rewrite it into a more precise, actionable AI actor performance prompt.

Absolute core:

- What the character wants to do
- What the character wants to hide
- How the emotion develops
- What event triggers the change
- How the lines drive the performance
- How the face, eyes and body change
- How the voice, breath, pauses and silence change
- What state the character holds once the line or event is over
- Which reactions must not happen early

Highest principle:

> Emotion, performance and line triggers always make up the body of the prompt. Camera, character consistency, background consistency, lighting, props and physical rules are only short guardrails that serve the performance, unless they directly carry an emotional or narrative function.

## 2. Information Budget

Suggested share of the final prompt:

| Module | Share |
|---|---:|
| Character objective, emotion and performance beats | 60%-70% |
| Lines, voice, breath, pauses and silence | 10%-15% |
| Camera that serves the performance | 10%-15% |
| Character, background, prop and lighting consistency | 5%-8% |
| Other necessary technical constraints | 3%-5% |

Everything can be checked in full internally, but the final output must be compressed.

Cut test:

> If deleting a description would not change the character's performance, the emotional cause and effect, a key camera move or necessary continuity, it does not go into the main prompt.

## 3. Scope

Use it for:

- Writing performance-led video prompts from dialogue
- Designing emotional arcs such as crying, anger, farewell, confession, argument and reconciliation
- Designing trigger words, stresses, pauses, breaths and post-line states for dialogue
- Turning rough descriptions like "she is sad" into visible and audible actions
- Designing restrained performances without dialogue
- Handling two- or multi-person overlapping dialogue, off-screen voices and listener reactions
- Rebuilding performance rhythm from a reference video
- Diagnosing mechanical performances and giving single-variable fixes

Not responsible for:

- Every module of full video reverse-engineering
- A general encyclopedia of cinematography, lighting, grading and editing
- Subtitle recognition
- Platform ads and button tutorials
- Guaranteeing success on the first generation
- Replacing natural-language actions with AU numbers
- Imitating a real person's identity, face or voice

## 4. Input Handling

### Minimum Required Information

1. Who is in the scene
2. The characters' relationship
3. The current event or conflict
4. The character's external objective
5. The character's internal suppression goal
6. The lines or main action
7. Target duration

### Optional Information

- Target model
- Storyboard
- Reference video
- Appearance, wardrobe and voice
- Setting and period
- Aspect ratio
- Language and accent
- Prohibited content
- Emotion knowledge base path

### Constraint Ledger

Internally, first separate:

- Must not change
- Can be improved without changing the meaning
- Missing but must be added
- Cannot be confirmed
- Optional enhancement

Never pass off something the Agent added as a user setting.

## 5. Main Workflow

1. Extract the user's non-negotiable requirements.
2. Establish the characters, relationships, event and objectives.
3. Determine what each character wants to hide or prevent.
4. Check whether the lines fit the total duration.
5. Optionally search the "emotion" knowledge base.
6. Build a short scene and character continuity lock.
7. Divide the shot timeline.
8. Define a Camera Intent for each shot.
9. Break each shot into performance beats.
10. Bind every change to a line or a non-verbal trigger event.
11. Generate facial, eye, body, voice and breath evidence.
12. Add post-line states and forbidden early reactions.
13. Add short consistency guardrails according to risk.
14. Add AU/FACS support where needed.
15. Compress low-value detail.
16. Output the Master Prompt, QA and fix order.

## 6. Optional Emotion Knowledge Base

The emotion knowledge base only supplies candidate evidence; it does not decide the character's story.

Correct order:

1. First understand the characters and the conflict
2. Generate a structured emotion query
3. Find the matching directory
4. Retrieve candidate actions
5. Judge whether they suit the current character
6. If nothing is found or nothing fits, generate independently

A query must not use only "sad"; it should also include:

- Character objective
- Internal suppression goal
- Emotional stage
- Mode of expression
- Intensity
- Dialogue state
- Physical state
- Prohibitions

The same emotion must be split into distinct forms such as restrained, ashamed, defensive, delayed, numb and explosive.

From retrieval results, keep first:

- Observable actions
- Direction, speed and intensity of the action
- Breath and voice
- Trigger conditions
- Suppression actions
- End states

Discard purely literary adjectives, marketing language, piles of actions with no timing relationship, and one-size-fits-all templates unrelated to the character.

When the knowledge base finds nothing, is of poor quality or conflicts with the character, generate independently without blocking the task.

## 7. Three-Layer Architecture

### Layer 1: Short Scene and Continuity Lock

Keep only what is necessary:

- Character identity and relationship
- Setting
- Characters' positions in space
- Necessary voice traits
- Key background anchors
- What must not change

Default compressed wording:

> Characters keep the same face, age, build, hairstyle, wardrobe and voice across all shots; character blocking, the main background anchors and key prop positions stay consistent.

Expand an item only when it directly takes part in the performance.

### Layer 2: Shot Timeline and Camera Intent

Each shot includes:

- Start and end time
- What the camera is watching
- Whom the audience is aligned with for now
- Whether it prioritizes the speaker, the reaction or the relationship
- Shot size, position, height, angle and distance
- Static or moving
- Why it does not move
- What event triggers a move
- Move path, speed, duration and stopping position

Camera does not mechanically equal the character's emotion. The character's state, the camera's attitude and the audience's position must be kept separate:

- actor_state
- camera_attitude
- viewer_alignment

### Layer 3: The Actor's Eight Performance Dimensions

1. Time and shot
2. External objective and internal suppression goal
3. Emotional start -> trigger -> end
4. Trigger event and channel of expression
5. Visible facial action
6. Eyes, body, center of gravity and action completion state
7. Voice, breath, pauses and silence
8. End state and forbidden early reactions

## 8. Execution Metadata

The following fields prevent multi-character and sound-picture errors and do not count toward the eight dimensions' length:

- speaker: who is currently speaking
- camera_subject: what the camera is watching
- trigger_event: the event that triggers the change
- evidence_source: user, knowledge base, reference video or independently generated
- information_priority: what the current shot shows first

## 9. Performance Rules

### Character Objective

Prefer action verbs:

- Hold on to
- Interrogate
- Conceal
- Persuade
- Refuse
- Probe
- Protect
- Force an admission

Also record what the character is trying to hold down:

- Not letting themselves cry
- Not letting the other person see their fear
- Not admitting the truth
- Not letting their voice break

### Emotional Change

Do not write only "sad" or "angry"; write:

> Start -> trigger event -> process of change -> end

Every change must be triggered by a line, an action, new information, a silence or an environmental event.

### Suppression

Keep first:

- Wanting to cry but not yet letting the tears fall
- Wanting to speak but not making a sound yet
- Wanting to move closer but stopping
- Wanting to look away but looking back again
- Wanting to explode but first lowering the voice

### Action Phases

Important actions include:

- Onset: the start
- Apex: the peak
- Offset: the fade

Do not reach maximum intensity on the first frame, and do not hold an action forever.

### Action Completion State

An action can be:

- Completed
- Halted
- Failed
- Interrupted
- Deliberately withdrawn

An unfinished action often has more performance value than a direct emotion label.

## 10. Dialogue, No Dialogue and Multi-Person Dialogue

### Dialogue Scenes

Break down:

- State before speaking
- Trigger word
- Stressed words
- Voice change
- Eyes and body
- Breaths and pauses
- End of line
- Post-line reaction

### Scenes Without Dialogue

The trigger chain must include:

1. The event happens
2. The character perceives it
3. The character understands it
4. Physiological delay
5. Change in performance

Silence needs ambient sound, breath, fabric, swallowing and duration specified.

### Multi-Person Dialogue

Always separate:

- Who is speaking
- Whom the camera is watching
- Who is only listening
- Who is off screen
- Who is interrupted

A listener reacts only after the information arrives. When the camera is on the listener, the listener must not lip-sync the off-screen speaker.

For overlapping dialogue, specify:

- Where the interruption lands
- The mouth shape the interrupted person holds
- The interrupted person's inhale, blink or stillness
- When the camera cuts

## 11. Camera Rules

### Static

A locked-off camera suits protecting a micro-performance, delaying information, sustaining a stalemate or avoiding cueing the emotion early.

Static does not mean rigid; a very slight handheld breathing can stay, but it must not upstage the performance.

### Moving

Every move must state:

1. Why it starts
2. When it starts
3. Where it moves
4. Speed
5. Duration
6. Stopping position
7. Why it stops

Untriggered descriptions like "slow push-in for a more cinematic feel" are forbidden.

### No Mechanical Mapping

- Sadness does not always mean a push-in
- Dominance does not always mean a low angle
- Vulnerability does not always mean a high angle
- A raised voice does not always mean a move
- Do not cut on every line
- Do not use a continuous orbit in place of performance

## 12. Timing Feasibility

With dialogue:

> Speaking time + breaths + pauses + post-line reaction + cut buffer = total duration

Without dialogue:

> Event + perception + understanding + physiological delay + action development + stillness = total duration

When time is short, adjust the duration, cut lines, reduce actions or merge shots; do not simply push the delivery to an unnatural speed.

Reaction time must be reserved after every important line and trigger event.

## 13. Physiological Reactions

Use as needed; do not pile them on by default.

Tears can be broken into:

1. Moist reflection on the eye
2. Water pooling on the lower lid
3. Blinking fails to clear it
4. A tear crosses the lid
5. It moves down the cheek
6. Whether the tear is wiped

Breath can be broken into:

- Shallowing
- Interruption
- Holding the breath
- Release on the exhale
- Recovery

These reactions must serve the character's objective.

## 14. Consistency Added by Risk

Add only when the corresponding risk is present:

| Risk | Short guardrail |
|---|---|
| Character drift across shots | Identity, wardrobe, hairstyle and voice lock |
| Complex reverse-shot space | Blocking, axis and background anchors |
| Prop takes part in the performance | Hands, contact, position and end state |
| Tears take part in the emotion | Tear stages and lighting consistency |
| Overlapping dialogue or off-screen voice | speaker, camera_subject and lip-sync lock |
| Multi-shot stitching | Start state and end state of each shot |
| No relevant risk | Do not write it |

Support rules take one to three sentences and must not share equal length with the eight performance dimensions.

## 15. Action Density

Suggested for each key beat:

- 1 main change that must happen
- 1-2 supporting pieces of evidence
- 1 voice or breath change
- At most 1 camera move

Sort actions into:

- must
- should
- optional

When the model is overloaded, delete optional first, then should; never delete the main performance change.

## 16. AU/FACS

Priority:

> Natural-language action > direction, speed, intensity > timing and trigger > AU number

Add AUs only when the user explicitly asks, the model can parse them, or an action needs disambiguating.

Never output AU numbers alone.

## 17. Fixed Output

1. Input understanding and necessary assumptions
2. Timing feasibility report
3. Emotion knowledge base usage
4. Short scene and continuity lock
5. Shot timeline and Camera Intent
6. Performance beat table
7. Full Master Prompt
8. Version adapted to the target model
9. Lean negative constraints
10. Post-generation acceptance checklist
11. Single-variable fix order
12. Uncertainties and source notes

## 18. QA

### Emotion and Performance

- The emotion has a start, trigger, process and end
- No reaction comes before the information arrives
- Actions do not peak on the first frame
- Suppression and unfinished actions are kept
- The post-line state is clear

### Dialogue and Voice

- Speaker, listener and lip sync are correct
- Overlapping dialogue and off-screen voices are timed correctly
- Breaths, pauses and silences take real time
- Voice changes are bound to specific words or events

### Camera

- What the camera is watching is clear
- Moving or not moving both have a reason
- Moves have a trigger, path, speed and stop
- The camera does not replace the actor's performance

### Short Consistency

- Character identity does not drift
- Blocking and key background do not flip
- Key props do not move on their own
- Continuous effects such as tears do not reset across shots

## 19. Single-Variable Fix Order

1. Timecodes
2. speaker and camera_subject
3. Trigger events
4. The character's main action
5. Voice, breath and pauses
6. Camera trigger and movement
7. Forbidden early reactions
8. Short consistency lock
9. AU fine-tuning

Change one item at a time, then regenerate and check.

## 20. Skill File Plan

Suggested layout when it is formally created:

- SKILL.md: core workflow, three-layer structure, eight dimensions, output and QA
- scripts/validate_timeline.py: timeline closure and dialogue budget
- scripts/search_emotion_library.py: optional emotion candidate retrieval
- references/emotion-retrieval.md: emotion retrieval and filtering
- references/dialogue-camera.md: overlapping dialogue, off-screen voices and camera
- references/facs-action-units.md: optional AU reference
- references/model-adapters.md: model adaptation

Scripts handle deterministic checks; the Agent handles character understanding and performance judgment.

## 21. Final Sign-Off

The three rounds of testing have covered:

- A two-person argument with emotional escalation
- Restrained grief from a single character without dialogue
- Multi-person overlapping dialogue, off-screen voices, listener reactions and camera psychology

Specification v1.0 meets the conditions for creating the Skill.

Before formal creation, only confirm:

1. The actual path and internal structure of the "emotion" knowledge base
2. The first video models to prioritize for adaptation
3. The Skill install location

None of these change the core method; they only affect optional retrieval and model adaptation.
