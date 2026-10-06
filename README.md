# HW5 - Sports Modeling Class

## Part 1 (30 pts) - Original vs. modified score

Using `games.csv` and `games2.csv` on hpc-student.charlotte.edu, inside
`/projects/class/spoa4001_u01/SportsTrackingTransformer/data/BigDataBowl_2024/`:

- **Original score (games.csv):** Chargers (LAC) 19, Broncos (DEN) 16
- **Modified score (games2.csv):** Chargers (LAC) 21, Broncos (DEN) 17

(Week 6, gameId 2022101700.) Commands run and their output are in
[`part1_evidence.txt`](./part1_evidence.txt).

## Part 2 (40 pts) - Play animation

Animation of play 2735 from game 2022100210 (PIT @ NYJ, Week 4, 2022 season -
Breece Hall rush up the middle for 5 yards, Q3 1st down).

- [`part2_extraction_commands.txt`](./part2_extraction_commands.txt) - commands used to
  locate the game/play and extract its tracking rows
- [`animate_play.py`](./animate_play.py) - script that builds the animation
- [`play_2735_game_2022100210.gif`](./play_2735_game_2022100210.gif) - the output

**Citation:** the matplotlib `FuncAnimation` approach follows the technique described in
Miranda Auhl's PyCon US 2022 talk, "Animating NFL play-by-play data using matplotlib's
FuncAnimation()":
https://pycon-archive.python.org/2022/schedule/presentation/25/index.html
