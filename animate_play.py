"""
HW5 - Part 2 (40 pts)
Animate play 2735 from game 2022100210 (PIT @ NYJ, Week 4, 2022 season) and save as a .gif.

Run on hpc-student.charlotte.edu, from a working folder in the user's own home directory,
reading from the class's shared BigDataBowl_2024 data folder:
  /projects/class/spoa4001_u01/SportsTrackingTransformer/data/BigDataBowl_2024

Input file used: play_2735_tracking.csv - a small extract of tracking_week_4.csv containing
only the 943 rows (41 frames x 23 players/ball) for this specific game+play, produced with:
  (head -1 tracking_week_4.csv; grep "^2022100210,2735," tracking_week_4.csv) > play_2735_tracking.csv
(full extraction commands in part2_extraction_commands.txt)

Citation / approach:
  Hand-written matplotlib FuncAnimation script (field drawn with patches/lines, one scatter
  marker per player per frame, saved via the Pillow writer). The general FuncAnimation-for-
  player-tracking-data technique follows the approach described in Miranda Auhl's PyCon US
  2022 talk, "Animating NFL play-by-play data using matplotlib's FuncAnimation()":
  https://pycon-archive.python.org/2022/schedule/presentation/25/index.html
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe

tracking = pd.read_csv("play_2735_tracking.csv")
colors = {"PIT": "#ffb612", "NYJ": "#125740", "football": "#6b4423"}
team_labels = {"PIT": "Steelers (PIT)", "NYJ": "Jets (NYJ)"}
frames = sorted(tracking["frameId"].unique())

# yard-line numbers as they'd read on a real broadcast field
yard_numbers = {20: "10", 30: "20", 40: "30", 50: "40", 60: "50",
                70: "40", 80: "30", 90: "20", 100: "10"}

outline = [pe.withStroke(linewidth=2, foreground="black")]

fig, ax = plt.subplots(figsize=(12, 7.3))
fig.subplots_adjust(top=0.80)


def draw_field():
    ax.clear()
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 53.3)
    ax.set_facecolor("#1f7a3d")
    ax.axvspan(0, 10, color="#145c34")
    ax.axvspan(110, 120, color="#145c34")
    for yard in range(10, 111, 5):
        ax.axvline(yard, color="white", lw=0.5, alpha=0.3)
    ax.axvline(10, color="white", lw=2)
    ax.axvline(110, color="white", lw=2)
    for x, label in yard_numbers.items():
        ax.text(x, 4, label, color="white", fontsize=9, fontweight="bold",
                 ha="center", path_effects=outline)
        ax.text(x, 49.3, label, color="white", fontsize=9, fontweight="bold",
                 ha="center", path_effects=outline)
    ax.set_xticks([])
    ax.set_yticks([])

    legend_handles = [mpatches.Patch(color=colors[t], label=team_labels[t]) for t in ["PIT", "NYJ"]]
    legend_handles.append(mpatches.Patch(color=colors["football"], label="Football"))
    ax.legend(handles=legend_handles, loc="upper center", ncol=3, fontsize=8,
              framealpha=0.85, bbox_to_anchor=(0.5, 1.28))


def update(frame_id):
    draw_field()
    snap = tracking[tracking["frameId"] == frame_id]
    for _, row in snap.iterrows():
        is_ball = row["club"] == "football"
        ax.scatter(row["x"], row["y"], s=60 if is_ball else 150,
                   color=colors[row["club"]], edgecolors="black", zorder=3)
        if not is_ball:
            ax.text(row["x"], row["y"], str(int(row["jerseyNumber"])),
                    ha="center", va="center", fontsize=7, color="white", zorder=4)
            last_name = str(row["displayName"]).split()[-1]
            ax.text(row["x"], row["y"] + 1.6, last_name, ha="center", va="center",
                     fontsize=6, color="white", zorder=4, path_effects=outline)
    fig.suptitle(f"Game 2022100210 | Play 2735 | Frame {frame_id}", fontsize=12, y=0.96)


anim = animation.FuncAnimation(fig, update, frames=frames, interval=100)
anim.save("play_2735_game_2022100210.gif", writer="pillow", fps=10)
print("Saved play_2735_game_2022100210.gif")
