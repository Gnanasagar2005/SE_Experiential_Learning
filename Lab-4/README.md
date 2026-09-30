# Lab 4 - Vibe Coding

Assigned repo: [SETAPESU26/43_reaction-time-tester](https://github.com/SETAPESU26/43_reaction-time-tester),
a Pygame reaction time tester. The broken code was fixed and the four README tasks were added
by prompting an AI assistant (Claude), one prompt per task.

## Contents

| File | What it is |
|---|---|
| [reaction-time-tester/](reaction-time-tester/) | The updated game code |
| [videos/before-changes.mp4](videos/before-changes.mp4) | Gameplay before any change, showing the timing bug |
| [videos/after-changes.mp4](videos/after-changes.mp4) | Gameplay after the fixes, with false start, results screen, replay and sound |
| [chat-history.pdf](chat-history.pdf) | The prompts and responses, task by task |

## What was changed

| Task | Change |
|---|---|
| 1. Input timing | Reaction time is measured from when the screen turns green. A click during the grey wait is a false start: a red screen, a buzz, and the round is replayed |
| 2. Game over | A results screen lists every round's time, the average and the false-start count |
| 3. Replay | On the results screen, 1 / 2 / 3 start a new session on Easy (3 rounds), Medium (5) or Hard (7). Esc exits |
| 4. Sound | Generated tones for the go cue, a false start and the end of the session, with no audio files needed |

## Running it

```bash
cd reaction-time-tester
pip install -r requirements.txt
python main.py
```
