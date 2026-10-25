# AI Actor Performance Director: Third Stress Test and Camera System

> Test type: two-person overlapping dialogue, off-screen voice, camera holding on the listener, the psychological role of camera placement  
> Status: final specification stress test; the Skill has not been created yet  
> Emotion knowledge base: directory not found; continuing with the self-generated fallback

# Part One: Camera System Revision

## 1. A precise definition of "the camera represents the character's mood"

Camera placement does not automatically equal the character's mood.

More precisely:

> The camera's position, distance, height, angle, obstruction, stability and movement determine the relationship between the audience and the character, and when the audience gets to see the character's emotion.

For example:

- A frontal close-up can pull the audience straight into the character's emotion, or it can make the character look scrutinised.
- A side-on wide shot can express distance, or it can simply establish the space.
- A slow push-in can increase psychological closeness, or it can create pressure.
- A locked-off camera can express restraint, deadlock, helplessness or cool observation.
- Handheld shake can express instability, or it can simply give a documentary feel.

So the Skill cannot use a dictionary of "this emotion always maps to this camera setup". It must answer:

1. Whose side the audience should be on at this moment
2. Whether the audience should be watching the speaker or the listener at this moment
3. How much psychological distance the audience should keep from the character
4. Whether emotional information should be shown immediately or held back
5. Whether camera movement would destroy the actor's micro-performance

## 2. New: camera intent fields

Add the following fields to every shot:

- viewer_alignment: whom the audience is temporarily aligned with
- information_priority: whether to prioritise the line, the reaction or the spatial relationship
- camera_subject: what the camera is watching
- camera_position: where the camera is placed
- camera_height: camera height
- camera_angle: frontal, profile, over-the-shoulder, from behind, etc.
- subject_distance: distance from the character
- framing: shot size and the character's position in frame
- negative_space: direction and purpose of the negative space
- camera_state: static, handheld breathing, moving
- movement_trigger: what event triggers the move
- movement_path: push in, pull out, lateral track, follow, etc.
- movement_speed: speed
- movement_easing: whether the move starts and stops smoothly
- movement_end_state: when it stops and where it lands
- movement_motivation: the dramatic reason for moving or not moving

## 3. "Not moving" also needs a reason

A locked-off camera is appropriate when:

- The character is suppressing something, and small physical actions matter more than a camera change
- The two characters reach a deadlock
- The audience needs to wait for the character's reaction
- The camera should not hint at the emotion in advance
- A sudden move would weaken the sense of reality
- The spatial relationship must stay stable

Static does not mean completely rigid. You can keep:

- Very slight handheld breathing
- Slight focus breathing
- Framing shifts caused by the character's breathing

None of these may be large enough to upstage the performance.

## 4. "Moving" needs a trigger and an end

Wrong:

"The camera slowly pushes in to add a cinematic feel."

Right:

"Only after the character hears the key fact and stops arguing does the camera begin an extremely slow push-in; the push lasts 2.5 seconds, tightening from a chest-up close shot to a shoulder-up close-up, and stops before the character speaks again."

Every move must state:

1. Why it starts
2. At what moment it starts
3. Where it moves to
4. How fast it moves
5. How long it lasts
6. Where it stops
7. Why it holds still after stopping

## 5. Common camera behaviours and when to use them

### Static camera

Suits:

- Restraint
- Waiting
- Deadlock
- Making the audience actively search for micro-expressions

Risk:

- If the actor does too little, the frame goes dead

### Extremely slow push-in

Suits:

- Information gradually sinking into the character
- Defences beginning to fail
- The audience needing to move closer step by step

Risk:

- Pushing in on every moment of sadness becomes a cliche
- Pushing in too early gives away the emotion ahead of time

### Slow pull-out

Suits:

- A relationship that cannot be saved
- The character being swallowed by the environment
- Revealing isolation after the emotion has played out

Risk:

- Easily becomes overly sentimental
- Weakens facial detail

### Lateral move

Suits:

- Revealing another character
- Shifting the power balance between two people
- Turning from one person's point of view to the two-person relationship

Risk:

- An unmotivated lateral move looks like showing off technique

### Handheld

Suits:

- Realism
- Physical closeness
- An unstable relationship

Risk:

- Shake cannot replace the actor's own instability
- In micro-performance scenes the movement must be very small

### Hard cut

Suits:

- A trigger word that brings a clear turn
- Having to switch who the camera is watching
- Needing to make a line collide with a reaction

Risk:

- Cutting to the listener too early gives away the reaction
- Cutting too late may miss a key micro-action

## 6. The camera must not mechanically mirror the emotion

Forbidden:

- Pushing in every time the character raises their voice
- Always shooting from above when the character is sad
- Always shooting from below when the character is dominant
- Cutting on every line
- Slow motion on every pause
- Every cry going from medium shot to close-up via a push-in
- Constant orbiting for a "cinematic feel"

The camera and the actor can be in contrast:

- The character collapses inside while the camera stays calm and locked off
- The character looks calm on the surface while the camera slowly closes in to reveal something wrong
- The character speaks while the camera stays on the listener
- After the character erupts, the camera pulls out instead of pushing in

# Part Two: Third Stress Test

## 1. Test scene

### Scene

A hospital corridor waiting area at night. The sister stands by the window; the brother sits on a bench. They have just learned that their father's condition has worsened. The sister tries to organise what happens next; the brother refuses to keep listening.

### Original dialogue

Sister:

"I called the family. They'll be here before morning. We need to decide--"

Brother, cutting in:

"Don't."

Sister:

"We don't have time."

Brother:

"I said don't."

### Performance goals

- The sister holds down her fear by taking action and organising.
- The brother uses refusal to keep the fact from getting in.
- The first "Don't" cuts in from off-screen.
- The camera is still watching the sister at that moment and does not cut to the brother right away.
- Only after the sister's reaction has played out does it cut to the brother.
- The second refusal is quieter but more resolute.

### Duration

20 seconds.

## 2. Timing feasibility

The dialogue is about 25 English words; at a normal, restrained pace it needs about 10-12 seconds.

The remaining 8-10 seconds or so can be used for:

- The opening state
- The sister's reaction after the first interruption
- The cut to the brother
- The sister continuing off-screen
- The two-person deadlock after the second refusal

20 seconds is feasible.

## 3. Scene and continuity locks

- The sister always stands by the window; the brother always sits on the bench.
- They are about 2.5 metres apart.
- The sister is on the left of the space; the brother is on the right.
- The hospital corridor fluorescent lighting is steady and does not flicker.
- Ambient sound includes a distant cart, the ventilation system and occasional footsteps.
- No background music.
- The sister's voice is slightly fast but controlled; the brother's voice is low and short of breath.
- No doctors, nurses or other speakers are added.

## 4. Shot and camera design

### Shot one: 0.0-9.0 seconds

Camera subject: the sister.  
Framing: chest-up profile close shot.  
Camera position: front right of the sister, close to eye level; the brother is out of frame.  
Audience relationship: temporarily aligned with the sister, understanding that she keeps control by organising things.  
State: static, keeping only very slight handheld breathing.  
Why it does not move: the sister is using words to keep order, and a camera move would hint too early that she is about to lose control.  
Key rule: when the brother first cuts in, do not cut; keep watching the sister take in the line.

### Shot two: 9.0-16.5 seconds

Camera subject: the brother.  
Framing: medium close-up over the sister's shoulder, with her shoulder as a blurred foreground on the left.  
Camera position: about 5 cm below eye level, with no obvious low angle.  
Audience relationship: shifts from the sister's logic of action to the brother's refusal.  
State: static from 9.0-11.0 seconds; from 11.0 seconds an extremely slow push-in begins.  
Movement trigger: the brother does not look at the sister but stares at the floor; after the sister says "time" off-screen, his breath stops for a beat.  
Path: straight push-in of about 15 cm.  
Speed: very slow, lasting about 2 seconds.  
Stop: stops before the brother speaks a second time.  
Why it moves: not because he is sad, but because the audience is finally allowed to get close to his refusal mechanism.

### Shot three: 16.5-20.0 seconds

Camera subject: the relationship between the two.  
Framing: static two-person medium shot.  
Camera position: side-on to the corridor, preserving the empty space and distance between them.  
Audience relationship: steps back from individual emotion into a relationship space that cannot be crossed.  
State: completely static.  
Why it does not move: neither of them has resolved anything, and any further push-in would create a false emotional conclusion.

## 5. Performance beat table

| Time | speaker | camera_subject | trigger_event | Character objective | Emotional change | Performance and camera | End state | Forbidden |
|---|---|---|---|---|---|---|---|---|
| 0.0-1.5 | null | Sister | None | Keep control through action | Tense but functioning | Sister looks out of the window, phone in her right hand; camera static | Ready to speak | No early trembling |
| 1.5-6.4 | Sister | Sister | She starts organising things herself | Get the brother to accept the next step | Control -> speaking faster | She says the first two sentences without looking at the brother; her thumb rubs the edge of the phone once; camera does not move | Keeps talking | No crying, no looking into the lens |
| 6.4-7.2 | Sister | Sister | Reaching "decide--" | Force herself to keep going | Pressure appears under the control | She finally starts turning her head toward the brother; the sentence is unfinished | Lips held in an unfinished mouth shape | Does not stop the sentence on her own |
| 7.2-7.6 | Brother off-screen | Sister | Brother cuts in with "Don't" | Keep the fact from getting in | The sister's action is cut off | Male voice enters from behind frame right; camera stays on the sister | Sister stops turning her head | Do not cut to the brother |
| 7.6-9.0 | null | Sister | The interruption has happened | Hide that it hit her | Control -> brief blankness | Sister blinks once, an incomplete inhale; her grip on the phone tightens; camera stays static | She closes her mouth again | Does not answer right away |
| 9.0-11.0 | null | Brother | Hard cut to the brother | Refuse to acknowledge the fact | Defensive numbness | Brother looks down, hands clasped; camera static | Does not look at the sister | Do not show the sister's mouth |
| 11.0-13.6 | Sister off-screen | Brother | Sister says "We don't have time" | Force the brother to face reality | Brother numb -> defences tighten | Sister's voice comes from front left; brother holds his breath for a beat after "time"; only then does the camera begin an extremely slow push-in | Jaw tightens | Do not push in early |
| 13.6-14.8 | null | Brother | Sister finishes | Hold the refusal | Defences close to breaking | Push-in stops; brother swallows, still does not look up | Ready to speak | No tears |
| 14.8-16.2 | Brother | Brother | He decides to refuse again | End the sister's topic | Refusal quieter, more resolute | He says "I said don't." more quietly than the first time; the end of "don't" does not drop into a plea | Closes his mouth immediately | No shouting |
| 16.2-16.5 | null | Brother | The line ends | Hold the boundary | Brief loss of strength | After his lips close, his jaw trembles once | Hard cut to two-shot | No extra lines |
| 16.5-20.0 | null | Both | No new event | Each holds their defences | Deadlock | Two-person medium shot; sister still standing, brother still sitting; a large empty space kept between them; camera completely still | Ends unresolved | No moving closer, no hug, no score |

## 6. Full Master Prompt

Generate a 20-second, realistic, cinematic two-person performance short in a hospital corridor with natively synced English dialogue. Night-time waiting area: the sister stands by the window on the left of the space, the brother sits on a bench on the right of the space, about 2.5 metres apart. The fluorescent lighting is steady. No background music; keep only the ventilation system, a distant cart, occasional footsteps, clothing rustle and the characters' breathing. Both characters keep the same faces, ages, clothing and positions in space throughout.

Shot one, 0.0-9.0 seconds. The camera is front right of the sister, close to eye level, in a chest-up profile close shot. The brother is out of frame. The camera is static, keeping only very slight handheld breathing. It does not move here because the sister is keeping control through words and practical arrangements, and the camera should not hint in advance that she is about to be hit.

0.0-1.5 seconds: the sister looks out of the window, holding her phone in her right hand. She is tense but still functioning, with no early trembling or tears.

1.5-7.2 seconds: speaking slightly fast but clearly, she says: "I called the family. They'll be here before morning. We need to decide--" She does not look at the brother right away. While speaking, her thumb rubs the edge of the phone only once. On "decide--" she finally begins to turn her head, the sentence still unfinished.

At 7.2 seconds, the brother cuts in from behind frame right with a low but sudden: "Don't." The camera must not cut to the brother; it stays on the sister's face. Her head turn stops midway, she blinks once, her inhale does not finish, and the fingers holding the phone briefly tighten. She does not answer right away. The camera stays static the whole time, letting the audience see her take in the interruption in full.

At 9.0 seconds, hard cut to shot two. Medium close-up over the sister's shoulder, with her shoulder as a blurred foreground on the left and the brother sitting on the right of frame. The camera is close to eye level but about 5 cm below the brother's eyes, with no obvious low angle.

9.0-11.0 seconds: the brother looks down at the floor, hands clasped. He refuses to acknowledge the fact, but does not cry. The camera stays static.

11.0-13.6 seconds: off-screen, front left, the sister says: "We don't have time." Her voice is controlled and does not rise into an argument. The brother must hold his breath for a beat only after hearing "time". The camera must also begin its extremely slow straight push-in only after "time", lasting about 2 seconds over a total distance of about 15 cm. The push-in is not because of "sadness"; it is because the audience is only now allowed to get close to his refusal. The push-in stops before he speaks again.

13.6-14.8 seconds: the camera has already stopped. The brother swallows once, his jaw tightens, he still does not look up, and he does not cry.

14.8-16.2 seconds: he says: "I said don't." It is quieter than the first time but more resolute. The end of "don't" must not turn into a plea. He closes his mouth immediately after, his jaw trembles once, he adds no further lines and does not shout.

At 16.5 seconds, hard cut to shot three. A static two-person medium shot from the side of the corridor. The sister still stands on the left, the brother still sits on the right, with a clear empty space between them. The camera is completely static, with no further push-in or pull-out. They do not move closer, do not hug and do not resolve anything. Keep only breathing, the ventilation system and the distant cart. The shot ends in an unresolved deadlock between them.

## 7. Negative constraints

- The first "Don't" must be an off-screen voice.
- Do not cut to the brother on the first interruption.
- The sister must stop turning her head only after hearing the interruption.
- The camera must not start pushing in before "time".
- The push-in must stop before the brother speaks a second time.
- Do not cut on every line.
- No constant orbiting, fast zooms or emotional shake.
- Do not use a high angle to automatically show vulnerability, or a low angle to automatically show dominance.
- The brother must not lip-sync the sister's off-screen lines.
- While the sister speaks off-screen, the shoulder in frame may show slight breathing, but no wrong mouth movement may appear.
- Neither cries, hugs or reconciles.
- The final shot is completely static; do not use a pull-out to milk the emotion.

## 8. Post-generation acceptance

### Interruption and lip sync

- [ ] The sister's "decide--" is an unfinished sentence
- [ ] The brother's first "Don't" comes from off-screen, behind frame right
- [ ] The camera is still watching the sister at that moment
- [ ] The sister hears it first, then stops turning her head
- [ ] The brother does not lip-sync the sister's off-screen lines

### Camera

- [ ] Shot one is static, with no early push-in
- [ ] The camera stays on the sister after the first interruption
- [ ] Shot two is static first, then pushes in after "time"
- [ ] The push-in is extremely slow, about 15 cm
- [ ] The camera has stopped before the brother speaks
- [ ] The closing two-person medium shot is completely static

### Performance

- [ ] The sister holds down her fear by organising things
- [ ] The first interruption leaves her briefly blank
- [ ] The brother's first refusal is sudden; the second is quieter and more resolute
- [ ] The emotion is not carried by crying
- [ ] The ending keeps the unresolved space

# Part Three: Findings from the Third Test

## Finding 1: Camera placement needs to be independent of the eight performance dimensions

Camera placement does not belong only to "time and shot"; it also carries the audience relationship, the distribution of information and the delay of emotion.

Formal revision:

> Add Camera Intent to the three-layer architecture as a required sub-module of Layer 2, rather than stuffing it into the actor's eight dimensions.

## Finding 2: "Character emotion" and "camera attitude" must be kept separate

A character can collapse while the camera stays calm; a character can be calm while the camera gradually closes in.

Formal revision:

- actor_state: what the character is going through
- camera_attitude: how the camera treats the character
- viewer_alignment: whom the audience is temporarily aligned with

The three must not be assumed to be the same by default.

## Finding 3: Camera moves must have a trigger

In this example, the camera only starts closing in on the brother after the sister says "time" off-screen.

Formal revision:

> Every camera move must provide movement_trigger, movement_path, movement_speed, movement_duration and movement_end_state.

## Finding 4: A static camera must also be designed

Staying on the sister after the first interruption shows "the line hitting the listener" better than cutting straight to the brother.

Formal revision:

> When camera_state is static, also state why_static and which micro-performance the stillness is protecting.

## Finding 5: Cutting is a matter of information ethics

Whoever you cut to decides whose reaction the audience learns first.

Formal revision:

> information_priority must state whether the shot prioritises speaking, receiving, a hidden reaction or the spatial relationship.

## Finding 6: Camera movement cannot replace performance

If the actor has no breathing, swallowing, eyeline or jaw changes, a push-in on its own will not automatically produce emotion.

Formal revision:

> Camera action must complement the actor's action; camera movement must not be used to rescue a hollow performance.

# Part Four: Final Specification Maturity

The three rounds of testing now cover:

1. A two-person argument with emotional escalation
2. Restrained, wordless grief from a single actor
3. Off-screen voice, interruption, listener reaction and the psychological role of camera placement

After the third test, the formal Skill should use:

## Layer 1: Scene and character continuity locks

Lock characters, relationships, space, voice, wardrobe, identity and environment.

## Layer 2: Shot timeline and Camera Intent

Besides each shot's start and end times, it must also state:

- Whom the audience is aligned with
- What information is being prioritised right now
- Whom the camera is watching
- Camera position, height, angle and distance
- Composition and negative space
- Static or moving
- Why it does not move
- What triggers a move
- Movement path, speed, duration and stopping point

## Layer 3: The actor's eight performance dimensions

1. Time and shot
2. External action objective and internal suppression goal
3. Emotional start -> trigger -> end
4. Trigger event and expressive channel
5. Visible facial action
6. Eyeline, body, weight and completion state of actions
7. Voice, breath, pauses and silence
8. End state and forbidden early reactions

## Execution metadata

- speaker
- camera_subject
- trigger_event
- evidence_source
- actor_state
- camera_attitude
- viewer_alignment
- information_priority

## Current conclusion

The specification is now ready to move to Specification v1.0.

The next step no longer needs more concepts. Instead:

1. Merge the results of the three tests
2. Remove duplicate rules
3. Fix the final inputs, workflow, fields and output template
4. Produce a lean Specification v1.0
5. Then have the user confirm whether to formally create the Skill
