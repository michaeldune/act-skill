# Searching and Using the Emotion Knowledge Base

## Search order

1. First derive from the user's input: the relationship between characters, the external goal, what is being held back, the trigger event, the emotional stage, the intensity and the end state.
2. Build the query from "emotion + stage + behavioural tendency + scene constraint", for example: `sadness restrained delayed does not want to be seen`.
3. Run:

```powershell
python scripts/search_emotion_library.py --query "sadness restrained delayed" --top-k 5 --json
```

4. Treat candidate entries only as a vocabulary of actions, never as a source of story facts.
5. Filter out actions that conflict with the character's identity, physical state, relationships, scene, timing or the user's lines.
6. When there are no strong matches, generate your own with the eight-dimension framework; never force a fit just to "use the knowledge base".

If the knowledge base lives in a custom folder, pass `--library <path>` or set the `ACT_SKILL_KB` environment variable.

## How much to take

- Each performance beat usually takes 1 primary carrier + 1 supporting carrier.
- Do not stack eyes, brows, mouth, tears, hands, shoulders, steps and breath all in the same second.
- Knowledge-base material should end up as only a few precise actions in the prompt, never a copied paragraph of explanation.

## Selection criteria

Keep, in priority:

- Actions with a causal link to the trigger event.
- Actions the camera can capture clearly.
- Actions that create tension with what the character "wants to hide".
- Actions that can be completed naturally within the given time.
- Actions that connect smoothly with the previous shot's action, breath and prop state.

Discard:

- Actions with the right emotion label but the wrong character motive.
- Actions that are over-dramatic, happen all at once, or do not fit in the time available.
- Reactions that require the character to know the next event in advance.
- Descriptions that only show off terminology and cannot become a visible performance.
