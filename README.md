# news-image-20261120-patoary

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/sami30357/news-image-20261120-patoary/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/sami30357/news-image-20261120-patoary/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page newspaper front page summing up Friday 20 November 2026: Kyiv's
bridges hit, Cyclone Akvan ashore, Asia's AI sell-off, BepiColombo reaching
Mercury — 36 stories across the world, drawn from scratch with Python PIL.
Four hero stories with drawn panels, a five-moment timeline, a stat strip,
ten mid stories, a schematic world map with numbered pins, and a date check
that keeps Thursday's news out.

## What is on the page

- A masthead naming Friday 20 November 2026 and the three biggest stories.
- "Friday in five moments": the day's arc from the overnight Kyiv barrage
  to the late COP31 overtime in Antalya.
- A six-box stat strip (drones, missiles, evacuations, markets, visas, quake).
- Four heroes: Kyiv's bridges, Cyclone Akvan, the AI sell-off, BepiColombo.
- "The day's ten" plus 22 more briefs — 36 stories in all, every one sourced.
- A date check naming the Thursday 19 November news that was left out.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

To redraw the poster from scratch, run `python3 render.py` (needs Pillow);
it writes `entry.png` (1024×1024, deterministic — same bytes every run).

---

<sub>Entered on [make.fun](https://make.fun/?ref=7b8zsyv7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
