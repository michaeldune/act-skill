# AI Actor Performance Director Skill Spec Draft

Status: specification stage, Skill not yet created  
Folder name: direct-ai-actor-performance  
Display name: AI Actor Performance Director

## 1. Core Positioning

Turn a script, dialogue, character conflict, rough video idea or existing prompt into AI actor performance directions organised by shot and by time.

Core controls:

1. The character's objective
2. The emotional starting point, turn and end point
3. Lines and trigger words
4. Visible facial action
5. Eyeline, body and weight
6. Voice, breath and pauses
7. The state after the line is spoken
8. Reactions that must not happen early
9. Picture and sound sync for multi-character dialogue

Core principle:

> First understand the characters, the relationship and the conflict, then design the emotional arc; first write visible and audible actions in natural language, then use AU/FACS for extra calibration only when needed.

## 2. Scope

Use it for:

- Generating performance-driven AI video prompts from dialogue
- Making crying, anger, farewells, confessions, arguments and similar performances feel more natural
- Designing pauses, breaths, voice breaks and micro-expressions for lines
- Turning a rough prompt into actionable actor directions
- Designing emotional build so a character does not cry or explode too early
- Breaking down two-hander and multi-character scenes
- Diagnosing mechanical performances and proposing single-variable fixes
- Extracting performance rhythm from a reference video

Not responsible for:

- Every module of full video reverse engineering
- General cinematography, colour grading and editing instruction
- Subtitle recognition and long-form video transcription
- Platform memberships, credits and interface ads
- Guaranteeing success on the first generation
- Replacing natural-language actions with AU numbers
- Imitating a real actor's identity, face or voice

## 3. Input Contract

Minimum required information:

1. Who is in the scene
2. The relationship between the characters
3. The current event or conflict
4. What the character wants to achieve
5. The lines or main action
6. Target video length

Optional information:

- Target model
- Existing storyboard
- Reference video
- Character appearance, wardrobe and voice
- Setting and period
- Aspect ratio
- Language and accent
- Content that must not appear
- Emotion knowledge base path

When information is missing:

- No model specified: output a model-agnostic Master Prompt.
- No aspect ratio specified: do not set a specific ratio on your own.
- No length specified: estimate it from the length of the lines and say so.
- No full lines given: design only action beats, do not invent key dialogue.
- No character history given: do not add marriages, relatives or past experiences.
- Ask only when the answer would significantly change the character's action.

## 4. Overall Workflow

1. Read the script, dialogue, reference video or rough prompt.
2. Establish the characters, relationships, event and objectives.
3. Optionally search the "emotion" knowledge base.
4. Filter for visible and audible evidence that fits the current character.
5. Build scene and character continuity locks.
6. Divide the shot timeline.
7. Break each shot into emotional beats.
8. Bind each change to a trigger word in the lines.
9. Generate facial, eyeline, body and weight actions.
10. Add voice, breath, pauses and post-line state.
11. Add reactions that are forbidden from happening early.
12. Add AU/FACS calibration as needed.
13. Check timing closure, multi-character sync and continuity.
14. Output the complete prompt, an acceptance checklist and a failure-fix order.

## 5. Optional "Emotion" Knowledge Base

### 5.1 Positioning

The "emotion" folder is an optional enhancement layer. It is not the core of the Skill, and it does not decide the story.

Correct order:

1. First understand the characters, relationships, event and objectives.
2. Decide which emotional process is needed.
3. Then search the knowledge base for actions, voice, breath and suppression reactions.
4. Select only content that fits the current character and stage.
5. If nothing is found or quality is insufficient, generate independently.

The knowledge base must serve the character; the character must never be forced to fit the knowledge base.

### 5.2 Path Priority

1. A path given explicitly in the user's current request
2. The emotion_library_path saved in the Skill configuration
3. A directory named "emotion" in the current workspace
4. If none is found, skip the search

The following locations have been checked so far, and no directory named "emotion" has been found:

- <workspace>
- <media-library>

This does not block finalising the spec; just supply the real path before creating the Skill.

### 5.3 Search Cannot Match "Sad" Alone

A query should include at least:

- Emotion family: sadness, anger, fear, shame, etc.
- Character objective: hold on to someone, interrogate, conceal, refuse, etc.
- Social situation: public, private, facing family or strangers
- Mode of expression: restrained, explosive, numb, delayed
- Intensity and direction of change
- Current stage: defence, crack, loss of control, recovery
- Line state: before speaking, trigger word, pause, after the line
- Prohibitions: no tears yet, do not look away yet, etc.

Even within "sad", distinguish between:

- Restrained sadness
- Sadness within shame
- Sadness behind an angry defence
- Suddenly receiving bad news
- Breakdown after long suppression
- A farewell where the character does not want the other person to notice
- A delayed reaction after numbness
- Sadness triggered by guilt

### 5.4 Filtering Search Results

Each candidate must be checked for whether it:

- Fits the character's objective
- Fits the character's personality
- Fits the current emotional stage
- Can be expressed in picture or sound
- Is compatible with the timing of the lines
- Conflicts with other actions
- Would make a reaction happen early
- Exceeds what the target model can execute reliably

Keep, in priority order:

1. Observable action
2. Direction of action
3. Speed and intensity
4. Breath and voice
5. Trigger conditions
6. Prohibited early reactions
7. The end state of the action

Discard:

- Purely literary description
- Abstract psychological explanation
- Value judgements like "ultimate, explosive, award-winning performance"
- Piles of actions with no timing relationship
- One-size-fits-all templates unrelated to the character

### 5.5 Fallback

Generate independently in these cases:

- No matching results
- Results contain only abstract emotion words
- Results conflict with the character's objective
- Results require the character to cry or explode early
- Several results contradict each other
- Content clearly belongs to a different, specific character
- Level of detail exceeds what the target model can handle

Finding nothing is not an error and must not block the task.

### 5.6 Source Labels

During analysis, distinguish between:

- Provided directly by the user
- Emotion knowledge base
- Observed in a reference video
- Generated independently by the agent
- Inferred by the agent from context

The final prompt should not show source labels often, but added content must never be passed off as something the user set.

## 6. Three-Layer Prompt Architecture

### Layer 1: Scene and Continuity Lock

Includes:

- Total length
- Setting and period
- Character identities
- Appearance, age, wardrobe and hair
- Spatial relationships between characters
- Voice and language
- Identity continuity
- Necessary visual tone
- Key lighting that affects the performance
- What must not change

Goal: keep the actors, the set and the spatial relationships from drifting.

### Layer 2: Shot Timeline

Each shot includes:

- Shot number
- Start and end time and duration
- Camera subject
- Shot size
- Camera position and angle
- Camera movement
- Transition
- Performance beats within the shot

Goal: first decide who the camera is looking at, then describe who is performing.

### Layer 3: Performance Beats

Each beat includes:

- Time range
- Current speaker
- Current camera subject
- Character objective
- Emotional starting point and end point
- Lines and trigger words
- Facial action
- Eyeline
- Body and weight
- Voice, breath and pauses
- Post-line state
- Prohibited early reactions

## 7. The Eight Dimensions as Finalised

### 1. Time and Shot

Timecodes must belong to a specific shot and state the current camera subject.

### 2. Character Objective

Use playable verbs: hold on to, interrogate, conceal, persuade, probe, protect, refuse, force an admission.

Avoid writing only "pain, anger, conflicted".

### 3. Emotional Starting Point and End Point

Write the change, for example:

- Hard-line questioning -> a crack appears in the defence
- Numbness -> beginning to grasp the facts
- Suppressed anger -> brief loss of control -> regaining control
- Trying to comfort -> realising a line has been crossed

### 4. Lines and Trigger Words

State clearly:

- The full line
- The word that triggers the change
- Stressed words
- The word where intensity begins to drop
- Whether the line is interrupted
- Whether the sentence is left unfinished

### 5. Visible Facial Action

Describe the feature, direction, speed, intensity, onset, peak and fade. AU is not required.

### 6. Eyeline, Body and Weight

Describe the eyeline target, looking away and back, head angle, leaning in or pulling back, shoulders, chest, weight, finger tension and the weight of movement.

### 7. Voice, Breath and Pauses

As needed, describe volume, pitch, pace, timbre, amount of breath, sentence-end contour, consonant force, voice breaks, throat sounds, swallowing, inhaling, exhaling, breath-holding and pause length.

### 8. End State and Prohibited Early Reactions

End state examples:

- Closes mouth immediately after speaking
- Lips stay slightly parted
- Keeps looking at the other person
- Eyes drop
- Body stops leaning in
- Breathing settles
- Holds a brief stillness

Prohibition examples:

- No early tears
- Not at peak from the first frame
- Do not look away early
- Do not mouth the wrong lines while the other person is speaking
- Do not hold the same expression throughout
- Do not return to calm before the sentence ends

## 8. Emotional Beat Rules

### 8.1 Every Change Needs a Cause

A trigger can be:

- A line or a word
- The other person's action
- New information arriving
- A silence
- The character realising they said the wrong thing

Jumping from anger to sadness with no trigger is not allowed.

### 8.2 Keep the Suppression Process Wherever Possible

For example:

- Wants to cry but no tears yet
- Wants to speak but does not make a sound right away
- Wants to move closer but stops
- Wants to look away but forces their eyes back
- Wants to explode but first lowers their voice

### 8.3 Actions Must Rise and Fall

Use Onset -> Apex -> Offset:

- The action begins
- It reaches its peak
- It gradually fades

Avoid maximum intensity on the first frame, and avoid an action that appears and then holds forever.

## 9. Multi-Character Dialogue Rules

### 9.1 Separate the Speaker from the Camera Subject

Each time range must state clearly:

- Who is speaking
- Who the camera is watching
- How the listener reacts

When the camera is on the listener, the speaker can be off-screen, but the listener must not lip-sync the speaker's words.

### 9.2 Overlapping Dialogue

Must state:

- Who speaks first
- Who cuts in, and on which word before it is finished
- Which mouth shape the interrupted character freezes on
- Whether the interrupted character blinks, inhales or goes still
- When the camera cuts

### 9.3 Unfinished Sentences

State exactly where the sentence is cut off, along with the trailing sound, mouth shape and post-line reaction.

### 9.4 Reactions Must Not Come Early

The listener reacts only after the trigger word or information arrives. Do not let them cry, turn their head or freeze their mouth before the key content has been said.

## 10. Timing Rules

Total length is made up of:

Spoken line duration + breaths + pauses + reactions + shot transition buffer = total length

Basic checks:

- Shot times are continuous or the gaps are explicit
- No unintended overlaps
- The last timestamp does not exceed the total length
- Each line's time range can hold the actual word count
- Key pauses take up real time
- Emotional changes are not all crammed into the same second

The finished Skill should include a timing validation script that checks for overlaps, gaps, total length, beat durations and line ranges that are too short.

## 11. AU/FACS Rules

Priority:

Natural-language action > direction, speed, intensity > timing and trigger relationships > AU numbers

Use AU only when:

- The user explicitly asks for it
- The target model is known to parse it
- A facial action needs further disambiguation
- Natural-language test results are unstable

Never output AU numbers alone. A full AU table will go in a separate reference file later, not in the core SKILL.md.

## 12. Fixed Output Structure

### 1. Scene and Character Lock

Characters, relationships, setting, voice, continuity and items that must not change.

### 2. Shot Timeline

Fields: shot, time, camera subject, shot size, camera position, movement, transition.

### 3. Performance Beat Table

Fields: time, speaker/camera subject, objective, emotional change, trigger word, face, body/eyeline, voice/breath, end state, prohibitions.

### 4. Complete Master Prompt

Model-agnostic and ready to use.

### 5. Model-Adapted Prompt

Output only when the user specifies a model.

### 6. Optional AU Calibration

Not required by default.

### 7. Negative Constraints

Cover at least: early emotion, one fixed expression, mechanical lip movement, mouthing the wrong lines, mismatched eyelines, identity drift, wardrobe changes, weightless movement and untriggered outbursts.

### 8. Post-Generation Acceptance

Output a QA list that can be checked off item by item.

### 9. Failure-Fix Order

Timecodes -> speaker and camera subject -> line triggers -> natural-language actions -> voice and breath -> prohibitions -> AU calibration.

Change only one variable at a time.

## 13. Acceptance Criteria

### Characters

- Face, age, hair and wardrobe stay stable
- Relationships and spatial positions do not drift
- Eyelines connect accurately

### Shots

- Timing closes
- The camera subject is clear
- The axis and over-the-shoulder relationships are consistent
- Cuts do not interrupt the wrong character

### Performance

- Emotion has a starting point, trigger, turn and end point
- Actions do not peak on the first frame
- Key changes are visible or audible
- Suppression reactions are preserved
- The post-line state is clear

### Dialogue and Sound

- Speakers match mouth movement
- Overlap timing is correct
- Off-screen voices do not drive the wrong character's mouth
- Breaths and pauses take up real time
- Voice changes are bound to specific words

### Prohibitions

- Tears do not come early
- Outbursts do not come early
- Listener reactions do not come before the information arrives
- No single expression is held throughout

## 14. Future Skill File Structure

Suggested contents:

- SKILL.md: core workflow, three-layer architecture, eight dimensions, output and acceptance rules
- agents/openai.yaml: interface name and default prompt
- scripts/validate_timeline.py: timing validation
- scripts/search_emotion_library.py: candidate search in the emotion knowledge base
- references/emotion-retrieval.md: emotion search and filtering rules
- references/facs-action-units.md: optional AU reference
- references/dialogue-and-lip-sync.md: multi-character dialogue, overlaps and lip sync
- references/model-adapters.md: adaptation rules for different video models

The emotion search script only "finds candidates"; the agent decides whether they suit the current character. The script must never assemble the final prompt directly.

## 15. Current Conclusions

Largely settled:

- Skill name and boundaries
- Three-layer architecture
- Eight dimensions
- Emotional beat and line-trigger principles
- Natural language first, AU as support
- Separating speaker and camera subject in multi-character scenes
- The correct place for the optional emotion knowledge base
- Fixed output structure
- QA and single-variable fix principles

Still to confirm before creation:

1. The real path of the "emotion" folder
2. File types, hierarchy and naming inside the folder
3. Which video models to adapt for first
4. Rules for estimating line duration
5. Whether to output only the Master Prompt by default, or a specific model version first

None of these change the subject of the Skill; they only affect how knowledge base search, the timing script and model adaptation are implemented.
