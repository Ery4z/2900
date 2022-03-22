import matplotlib.pyplot as plt

import numpy as np

import os

root = os.getcwd()
from pathlib import Path


plt.rc("font", size=20)
plt.rc("xtick", labelsize=16)
plt.rc("ytick", labelsize=16)
plt.rc("axes", titlesize=16)


"""--------------------------------------------------------------------------------------------------
PLOT FREQUENCY RESPONSE OF A DIGITAL FILTER
INPUTS: 
    - fs : sampling frequency 
    - w : The frequencies at which h was computed, in the same units as fs (see freqz)
    - h : The frequency response, as complex numbers (see freqz)
    - (zoom) : True to display zoom around transition band
--------------------------------------------------------------------------------------------------"""


def plot_response(fs, w, h, zoom=False):
    fig, ax1 = plt.subplots()
    ax1.set_title("Digital filter frequency response")
    ax1.plot(0.5 * fs * w / np.pi, 20 * np.log10(np.abs(h)))
    ax1.set_ylabel("Amplitude [dB]", color="steelblue")
    ax1.set_xlabel("Frequency [Hz]", color="steelblue")
    ax2 = ax1.twinx()
    angles = np.unwrap(np.angle(h))
    ax2.plot(0.5 * fs * w / np.pi, angles, "crimson")
    ax2.set_ylabel("Angle (radians)", color="crimson")
    ax2.grid()
    ax2.axis("tight")
    if zoom:
        ax3 = plt.axes([1.2, 0.6, 0.45, 0.25])
        x = 0.5 * fs * w / np.pi
        signal = 20 * np.log10(np.abs(h))
        ax3.plot(x, signal)
        ax3lim = [1500, 2000]
        ax3.set_xlim(ax3lim[0], ax3lim[1])
        ax3.set_ylim(
            np.min(signal[(x > ax3lim[0]) & (x < ax3lim[1])]),
            np.max(signal[(x > ax3lim[0]) & (x < ax3lim[1])]),
        )
        ax3.grid(True)

        ax4 = plt.axes([1.2, 0.25, 0.45, 0.25])
        x = 0.5 * fs * w / np.pi
        signal = 20 * np.log10(np.abs(h))
        ax4.plot(x, signal)
        ax4lim = [2500, 3000]
        ax4.set_xlim(ax4lim[0], ax4lim[1])
        ax4.set_ylim(
            np.min(signal[(x > ax4lim[0]) & (x < ax4lim[1])]),
            np.max(signal[(x > ax4lim[0]) & (x < ax4lim[1])]),
        )
        ax4.grid(True)

    plt.show()


def plotSignalAndDft(
    x1, y1, x2, y2, x_label=["", ""], y_label=["", ""], title="", discrete=[True, True]
):
    fig = plt.figure(figsize=(12, 5))
    # Subfigure 1 -  time plot
    ax1 = fig.add_subplot(121)
    if discrete[0]:
        ax1.stem(x1, y1, basefmt=" ")
    else:
        ax1.plot(x1, y1)
    ax1.set_xlabel(x_label[0])
    ax1.set_ylabel(y_label[0])
    # Subfigure 2 - frequency plot
    ax2 = fig.add_subplot(122)
    if discrete[1]:
        ax2.stem(x2, y2, basefmt=" ")
    else:
        ax2.plot(np.split(x2, 2)[0], np.split(y2, 2)[0])
    ax2.set_xlabel(x_label[1])
    ax2.set_ylabel(y_label[1])
    plt.title(title)
    plt.show()
