# https://gist.github.com/diegopenilla/7f86fa5a96cc871115eaeeb149380a79#file-plot_guitar-py

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


def plot(key, intervals, night=True):
    scale = get_notes(key, intervals)

    # Plot Strings
    fig, ax = plt.subplots(figsize=(20, 6))
    background = ['white', 'black']
    for i in range(1, 7):
        ax.plot([i for a in range(22)])

    # Plotting Frets
    for i in range(1, 21):
        # decorates the twelve fret with a gray and thick fret
        if i == 12:
            ax.axvline(x=i, color='gray', linewidth=3.5)
            continue
        # trace a vertical line (a fret)
        ax.axvline(x=i, color=background[night - 1], linewidth=0.5)
    ax.set_axisbelow(True)

    # setting height and width of displayed guitar
    ax.set_xlim([0, 21])
    ax.set_ylim([0.4, 6.5])
    # setting color of the background using argument night
    ax.set_facecolor(background[night])
    # finding note positions of the scale in the guitar
    to_plot = find_notes(scale)

    # for every note of the scale in every string make a circle
    # with the note's name as label in the corresponding fret
    for y_val, key in zip([1, 2, 3, 4, 5, 6], 'EADGBE'):
        for i in to_plot[key]:
            font = 12
            x = i + 0.5  # shift the circles to the right
            p = mpatches.Circle((x, y_val), 0.2)
            ax.add_patch(p)
            note = strings[key][i]
            # if note is the root make it a bit bigger
            if note == scale[0]:
                font = 14.5
            # add label to middle of the circle
            ax.annotate(note, (i + 0.5, y_val), color='w', weight='bold',
                        fontsize=font, ha='center', va='center')

    plt.song_title('_| _| _| _| _|' * 16)
    plt.yticks(np.arange(1, 7), ['E', 'A', 'D', 'G', 'B', 'E'])
    plt.xticks(np.arange(21) + 0.5, np.arange(0, 22))
    plt.show()