# AI Actor Performance Director: First Dry Run

> Test goal: check whether the Skill specification can turn a two-person argument scene into an actionable 30-second performance prompt.  
> Test status: specification test only; no Skill is created and no video is generated.  
> Test scene: the "husband and wife argue, the woman moves from counterattack to vulnerability" example from the video tutorial.

## 1. Test Input

### Scene

Mid-20th century, the back porch of an ordinary American working-class home. An old wooden door, faded walls and desaturated green plants. The husband and wife stand facing each other.

### Characters

- Man: about 50, trying to keep up his toughness and pride, unwilling to admit that his life has stalled for years.
- Woman: about 45-50, feels that everything she gave has been erased; she first hits back with anger, then exposes long-suppressed hurt.

### Relationship

A married couple who have lived together for a long time. This is not a fight between strangers but a reckoning of the relationship after years of build-up.

### Dialogue

Man:

"It's not easy for me to admit that I've been standing in the same place for eighteen years."

Woman:

"Well, I've been standing with you! I've been right here with you, Troy! I got a life, too. I gave eighteen years of my life to stand in the same spot as you. What about my life? What about me?"

### Targets

- Total duration: 30 seconds
- Landscape
- Native English dialogue
- Performance focus: suppression, counterattack, self-justification, defenses cracking, voice breaking, a brief stillness
- The first tear must not appear early

## 2. Input Check

### 2.1 Dialogue Duration Check

The dialogue is about 55 English words.

At an average rate of 145 words per minute, the dialogue alone needs about 22.8 seconds. Then add:

- The man's suppressed state before speaking: about 0.5 seconds
- The hard cut between the man and the woman: about 0.2 seconds
- The woman's two noticeable pauses: about 1.5-2.0 seconds
- The woman's short inhale: about 0.3 seconds
- The man's post-line reaction: about 2.5 seconds
- The closing two-person stillness: about 1 second

Total requirement is about 28-30 seconds. It fits in 30 seconds, but there is no room for more dialogue.

### 2.2 Timecode Problem in the Original Tutorial

The original tutorial example sets the man's shot at 0-3.7 seconds. The man's line is about 17 English words; finishing it in 3.7 seconds means a rate close to 276 words per minute, which does not meet the "suppressed but clear" performance requirement.

So this dry run cannot simply reuse 0-3.7 seconds and must redistribute:

- Shot 1: 0.0-6.0 seconds
- Shot 2: 6.0-26.5 seconds
- Shot 3: 26.5-29.0 seconds
- Shot 4: 29.0-30.0 seconds

This is the first important problem the dry run found:

> The Skill must first check the actual duration of the dialogue before accepting or changing the timecodes the user gives.

### 2.3 Emotion Knowledge Base

No actual "emotion" folder was found, so:

- emotion_library_used: false
- fallback: designed independently from the character objectives, the dialogue and the visible actions in the video tutorial

This fallback did not block the task, which shows the optional knowledge base is positioned correctly.

## 3. Scene and Character Continuity Lock

### Global Lock

- A 30-second realistic, cinematic domestic argument short.
- Both characters always keep the same face, age, hairstyle and wardrobe.
- The man is on the left of the space, the woman on the right.
- Observe the 180-degree axis; eyelines match exactly.
- The setting is always the same back porch, with no modern objects added.
- The camera stays restrained: no orbit, no fast crane up or down, no sudden zoom.
- The scene is driven mainly by faces, breath, eyes, voice and small body movements.

### Man Lock

- Solid but tired body.
- Low, slightly rough voice.
- His anger is not continuous shouting; he lowers his voice, then briefly raises it.
- Right after the line he regains control and adds no further exaggerated action.

### Woman Lock

- Mature, slightly husky voice.
- At first she uses anger to hold her defenses.
- Once her defenses crack, her volume drops and her breath becomes unsteady.
- Her eyes can gradually well up, but the first tear may only cross the lower lid after her last question ends.

## 4. Shot Timeline

| Shot | Time | Subject | Shot size and position | Camera | Dramatic task |
|---|---:|---|---|---|---|
| 1 | 0.0-6.0 s | Man | Close-up from the chest up, three-quarter profile | Nearly locked off, very slight handheld breathing | Holds down his resentment, then a short burst at the end |
| 2 | 6.0-26.5 s | Woman | Over-the-shoulder close-up, the man's shoulder as a soft foreground on the left | Basically locked off, very slow push-in in the later part | Counterattack -> self-justification -> crack -> vulnerable question |
| 3 | 26.5-29.0 s | Man | Over-the-shoulder close-up past the woman | Locked off | Takes in her words but cannot answer right away |
| 4 | 29.0-30.0 s | Both | Restrained two-shot, medium | Locked off | Keeps the relationship at a stalemate, no easy reconciliation |

## 5. Performance Beat Table

| Time | Speaker/Subject | Objective | Emotional change | Line trigger | Visible and audible action | End state | Prohibited |
|---|---|---|---|---|---|---|---|
| 0.0-0.5 | Man/Man | Keep his pride | Hard restraint | Before speaking | Lips pressed shut, jaw clenched, brows pulled inward; short, shallow inhale | Ready to speak | Do not raise the volume |
| 0.5-4.4 | Man/Man | Admit it without showing weakness | Restraint -> rising resentment | "admit" | First half of the line low, consonants heavy; eyes stay fixed on the woman | Neck starts to tense | No shouting, no looking away |
| 4.4-5.7 | Man/Man | Force her to understand him | Resentment -> short burst | "eighteen years" | Nostrils flare, body leans forward a few centimeters, volume rises briefly, jaw opens | Last word lands | No sustained loud volume |
| 5.7-6.0 | Man/Man | Regain control | Burst -> pulled back | End of line | Shuts his mouth at once, stops leaning, keeps staring | Hard cut | No added action |
| 6.0-9.3 | Woman/Woman | Hit back immediately | Defensive anger | "standing with you" | Chin pushed out, brows lowered, body leaning forward; fast pace, voice sharp but clear | Still looking straight at the man | No tears |
| 9.3-12.2 | Woman/Woman | Prove she has always been there | Anger held -> starts to justify herself | "right here with you" | Right hand points briefly into the space between them, no big waving; stresses "right here" | Hand returns close to the body | No sudden sadness |
| 12.2-14.5 | Woman/Woman | Fight for her existence to be acknowledged | Self-justification strengthens | "I got a life, too" | Stresses "life"; jaw briefly unclenches, eyes still aggressive | Short inhale | Tears must not fall |
| 14.5-19.8 | Woman/Woman | Make him acknowledge her sacrifice | Self-justification -> defenses crack | "eighteen years of my life" | Volume rises on "my life"; on "same spot as you" her head gives one short nod toward the man | Force drops at the end of the line | No sustained pointing |
| 19.8-20.3 | Woman/Woman | Hold back losing control | The crack widens | Between lines | Short inhale, eyes drop away for about 0.4 seconds; lips tremble slightly | Forces herself to look up | No tears falling |
| 20.3-23.3 | Woman/Woman | Demand whether he sees her | Hurt enters the voice | "What about my life?" | First question still fairly high and fast; looks back at the man; eyes moist | Slight voice crack at the end of the line | No sobbing |
| 23.3-24.0 | Woman/Woman | Decides to expose the most vulnerable question | Aggression disappears | Pause | An inhale does not fully go in; shoulders drop slightly; lips stay slightly parted | Ready for the second question | Do not move the body away |
| 24.0-26.0 | Woman/Woman | Ask him to acknowledge her as a person | Vulnerable confession | "What about me?" | Second question softer and slower; "me" falls at the end, the voice clearly loses its support for the first time | Lips still slightly parted | Does not wipe tears right away |
| 26.0-26.5 | None/Woman | Wait for an answer | Vulnerability -> stillness | End of line | Only now may the first tear cross the right lower lid; does not lower her head | Hard cut to the man | No added crying sounds |
| 26.5-29.0 | None/Man | Takes in the question but cannot answer | Toughness fails -> silence | After hearing "me" | Eyes briefly lose focus, jaw loosens; inhales but makes no sound; shoulders slowly drop | Still looking at the woman | No early reaction, no lines |
| 29.0-30.0 | None/Both | Keep the relationship unresolved | Stalemate | None | Both hold their positions; only breath and ambient sound remain | Picture ends | No hug, no reconciliation, no smile fading in |

## 6. Full Master Prompt

Generate a 30-second, realistic, cinematic domestic argument short with native synchronized English dialogue. The story takes place on the back porch of an ordinary mid-20th-century American working-class home. An old wooden door, faded walls and desaturated green plants. Both characters always keep the same face, age, wardrobe and hairstyle. The man is on the left of the space, the woman on the right; observe the 180-degree axis and match eyelines exactly. The camera is restrained and the scene is driven mainly by the actors' faces, breath, eyes, voices and small body movements; no orbit, fast crane up or down, or sudden zoom.

Shot 1, 0.0-6.0 seconds. Close-up of the man from the chest up, three-quarter profile facing frame right. The camera is nearly locked off, with only a very slight handheld breathing feel.

0.0-0.5 seconds, the man holds his toughness. Lips pressed shut, jaw clenched, brows pulled inward. A short, shallow inhale; he does not raise his volume.

0.5-4.4 seconds, he says in a low, restrained voice: "It's not easy for me to admit that I've been standing in the same place for eighteen years." The first half of the line is low, with heavy consonants. On "admit" his brows tighten further, but he still does not look away.

4.4-5.7 seconds, on "eighteen years" his nostrils flare, his neck muscles tighten, his body leans a few centimeters toward the woman and his volume rises briefly. Not continuous shouting, just a short burst from someone pushed to the edge.

5.7-6.0 seconds, as the last word lands he shuts his mouth at once, stops leaning and regains control of his body. Hard cut, no fades.

Shot 2, 6.0-26.5 seconds. Over-the-shoulder close-up of the woman, the man's shoulder and the back of his head as a soft foreground on the left of frame. The woman is center-right, framed from the chest up. The camera is basically locked off; after 20 seconds it makes an almost imperceptible slow push-in.

6.0-9.3 seconds, the woman meets the man's anger head-on. She leans forward, chin pushed out, brows lowered. She says quickly, sharply but clearly: "Well, I've been standing with you!" She is still using anger to protect herself and must not cry.

9.3-12.2 seconds, she goes on: "I've been right here with you, Troy!" Stress "right here." Her right hand points only once, briefly, into the space between them, with no exaggerated waving. She keeps looking straight at the man, her aggression held.

12.2-14.5 seconds, she says: "I got a life, too." Stress "life." Her jaw briefly unclenches and her eyes shift from pure attack to asserting her own existence. After the line comes one short inhale; her eyes may catch a moist reflection, but tears must not fall.

14.5-19.8 seconds, she continues: "I gave eighteen years of my life to stand in the same spot as you." On "my life" her volume rises again; on "same spot as you" her head gives one short nod toward the man. The force starts to drop at the end of the line. Do not keep pointing, and do not suddenly go into crying.

19.8-20.3 seconds, she takes a short inhale and her eyes drop away for about 0.4 seconds. Her lips tremble slightly, then she forces herself to look up again. Her defenses begin to crack, but tears still must not fall.

20.3-23.3 seconds, she looks back at the man and asks in a voice still fairly high but now unsteady: "What about my life?" The first question still carries accusation, with a slight voice crack at the end of the line. Her eyes are pooling, but no sobbing.

23.3-24.0 seconds, she pauses for about 0.7 seconds. An inhale does not fully go in, her shoulders drop slightly, her lips stay slightly parted. Her aggression disappears in the pause.

24.0-26.0 seconds, she asks more softly and more slowly: "What about me?" The end of "me" falls, and her voice clearly loses its support for the first time. After the line her lips stay slightly parted; she does not wipe her tears right away and does not lower her head.

26.0-26.5 seconds, hold on her still reaction. The first tear may only cross the right lower lid after the second question has fully ended. She is still looking at the man, with no exaggerated crying sounds added.

Shot 3, 26.5-29.0 seconds. Cut to an over-the-shoulder close-up of the man, the woman as a soft foreground on the left of frame. The man must react only after hearing "me," never earlier. His eyes briefly lose focus, his jaw loosens, he inhales but makes no sound, his shoulders slowly drop. He is still looking at the woman but cannot answer.

Shot 4, 29.0-30.0 seconds. Cut to a restrained medium two-shot. Both keep their original positions in space; only breath, faint fabric sounds and the quiet ambience of the yard remain. The relationship is still unresolved. No hug, no reconciliation, no smile, no sentimental fade-out.

## 7. Negative Constraints

- Do not start crying or shouting from the first frame.
- The first tear must not come before 26.0 seconds.
- The woman must not hold one and the same angry or sad expression throughout.
- The man's reaction must not come before the woman finishes "me."
- When the camera is on the listener, the listener must not wrongly lip-sync the speaker.
- Do not add a hug, touch, exit or reconciliation.
- Do not change the characters' age, face, hairstyle, wardrobe or positions in space.
- Do not use exaggerated stage-play gestures.
- Do not use a continuous push-in, orbit or unmotivated shake.
- Do not turn AU numbers or facial actions into mechanically synchronized animation.

## 8. Post-Generation Acceptance Checklist

### Timing

- [ ] Total duration is 30 seconds
- [ ] The man's line was not forced into 3.7 seconds
- [ ] The two noticeable pauses take real time
- [ ] The first tear comes no earlier than 26.0 seconds

### Dialogue

- [ ] The man's and the woman's lip sync match their own lines
- [ ] The man reacts only after the woman's last question ends
- [ ] No wrong overlapping of lines
- [ ] Line endings, inhales and pauses are in sync with the picture

### Performance

- [ ] The man goes through restraint -> short burst -> regaining control
- [ ] The woman goes through counterattack -> self-justification -> crack -> vulnerable question
- [ ] The second question is clearly softer and slower than the first
- [ ] After speaking, the woman keeps slightly parted lips and stillness
- [ ] The man's silent reaction is clear but not overdone

### Continuity

- [ ] Faces, age, hairstyles and wardrobe are stable
- [ ] The man is always on the left of the space, the woman on the right
- [ ] Over-the-shoulder relationships and eyelines are consistent
- [ ] No modern objects added to the setting

## 9. Single-Variable Fix Order After a Failure

1. Lines cannot be finished: first lengthen the shot or cut lines; do not first push the delivery to an unnatural speed.
2. Reaction comes early: strengthen the timing constraints on the trigger word and "no early reaction."
3. Emotion jumps suddenly: add the crack stage and suppression actions.
4. Pauses feel meaningless: give the pauses an inhale, eye direction and post-line state.
5. Tears come early: split "eyes welling up" and "tear crossing the lid" into two stages.
6. Facial direction is wrong: first strengthen the natural-language direction, then consider AUs.
7. Multi-person lip sync is wrong: separate the speaker, the subject on camera and off-screen voices again.

Change one item at a time, then regenerate and compare against the checklist.

## 10. Specification Problems Found in the First Dry Run

### Problem 1: No Mandatory Dialogue Duration Check

The original specification had timing rules, but they should become a mandatory step before the performance beats are generated.

Revision:

> Before accepting shot timecodes, first calculate the word count, a reasonable speaking rate, and the pause and breath budget. When time is short, the timing must be adjusted or a cut to the lines suggested.

### Problem 2: The "Eight Dimensions" Alone Cannot Handle Multi-Person Dialogue

Writing only the eight dimensions can still confuse who is speaking and whom the camera is watching.

Revision:

> Add two system fields outside the eight dimensions: speaker and camera_subject. They are execution metadata and do not count as performance dimensions.

### Problem 3: Emotional Start and End Are Not Enough

The trigger condition must also be recorded, or the emotion jumps without cause.

Revision:

> Expand "emotional start and end" into "emotional start -> trigger event -> emotional end."

### Problem 4: Tears Need Their Own Stages

Writing only "must not cry early" is not precise enough.

Revision:

> Split tears into four stages: moist reflection on the eye, water pooling on the lower lid, tear crossing the lid, and moving down the cheek, and allow each to be timed separately.

### Problem 5: The Post-Line State Is Core and Should Not Be Compressed

The most valuable performance in this test happens after the lines end: the woman keeps her lips slightly parted, the man inhales but cannot answer.

Revision:

> Every important line must reserve post-line reaction time; a beat without a post-line state counts as incomplete.

### Problem 6: The Knowledge Base Fallback Passed the Test

The task was still completed with no emotion directory, which shows that keeping the knowledge base optional is correct.

Revision:

> No change. Keep "if retrieval finds nothing, generate independently without blocking the task."

## 11. Specification v0.2 Revision List

The next version of the specification should formally add:

1. A mandatory dialogue duration budget stage
2. The two system fields speaker and camera_subject
3. An emotion trigger event field
4. Staged rules for tears and other continuous physiological effects
5. A minimum reaction time after important lines
6. A pre-generation timing feasibility report
7. Post-generation checks by timestamp, not only an overall assessment

## 12. Dry Run Conclusion

The three-layer architecture, the eight performance dimensions, line triggers, suppression actions, post-line states and forbidden early reactions all work in practice.

But the first dry run proved that the formal Skill cannot be just a "writing template"; it must also include execution checks:

- Can the lines be finished in time
- Who is speaking
- Whom the camera is watching
- Does the reaction come after the trigger
- Do tears happen in stages
- Is real time left for post-line reactions

So the current specification can move to v0.2, but creating the final Skill right away is still not recommended. The next step is to merge these revisions into the formal specification, then run a second dry run with a "restrained grief without dialogue" scene to check that the Skill works for more than dialogue arguments.
