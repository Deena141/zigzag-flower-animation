import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Settings
N = 14
P = 300
AMP = 0.7
SIZE = 4

x = np.linspace(-6, 6, P)
theta = np.linspace(-np.pi/4, np.pi/4, P)

# Flower shape
r = SIZE * np.cos(2 * theta)
fx = r * np.cos(theta)
fy = r * np.sin(theta)

# Figure
fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_aspect("equal")
ax.axis("off")

# Red, pink, orange colours
colors = ["red", "deeppink", "hotpink", "orange",
          "orangered", "pink"] * 3

lines = [
    ax.plot([], [], color=colors[i], lw=2.5)[0]
    for i in range(N)
]

center = ax.scatter([], [], color="orange", s=0)


def update(frame):

    w = 0

    if 150 <= frame < 240:
        w = (frame - 150) / 90
        w = w * w * (3 - 2 * w)

    elif 240 <= frame < 390:
        w = 1

    elif frame >= 390:
        w = 1 - min((frame - 390) / 90, 1)

    for i, line in enumerate(lines):

        # Zigzag
        y0 = (i - 6.5) * 0.6
        y = y0 + AMP * np.sin(1.6*x + i*0.35 - frame*0.7)

        # Flower
        a = 2*np.pi*i/N + frame*0.01
        X = fx*np.cos(a) - fy*np.sin(a)
        Y = fx*np.sin(a) + fy*np.cos(a)

        # Morph
        line.set_data(
            (1-w)*x + w*X,
            (1-w)*y + w*Y
        )

    center.set_offsets([[0, 0]])
    center.set_sizes([w * 300])

    return lines + [center]


anim = FuncAnimation(
    fig,
    update,
    frames=480,
    interval=30,
    repeat=True
)

plt.show()
