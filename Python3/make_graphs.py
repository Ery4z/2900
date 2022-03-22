import matplotlib.pyplot as plt

import numpy as np 

import os
root = os.getcwd()
from pathlib import Path

plt.rc('xtick', labelsize=16) 
plt.rc('ytick', labelsize=16) 
plt.rcParams.update({'font.size': 16}) 
colors2 = ['steelblue', 'crimson']
colors = ['gold','greenyellow','mediumaquamarine','steelblue','midnightblue', 'crimson']


"""--------------------------------------------------------------------------------------------------
PLOT (MULTIPLE) signals depending on the time and the corresponding continuous FT 
INPUTS: 
    - signals : a matrix of [(n+1)xm] dimensions where n (nb of channels) << m 
                    first row must be the time vector! 
    - fft : a matrix of [(n+1)xm] dimensions where n (nb of channels) << m 
                    first row must be the frequency vector!
    - legend : list of singal's name
    - show_fig : True if the plot must be displayed on screen, False otherwise
    - (file_path) : path where the graph must be saved (if needed)
--------------------------------------------------------------------------------------------------"""
def plot_cft(signals, fft, legend, show_fig, file_path=None): 
    # One big figure to frame the whole
    fig = plt.figure(figsize=(12,3))
    ax1 = fig.add_subplot(121) 

    # Plot each time channel
    for idx, color in zip(range(1, signals.shape[0]), colors2):
        ax1.plot(signals[0], signals[idx], linewidth=2, color = color, alpha=.7)
        ax1.set_xlabel('Time (sec)')
        
    # Plot each frequency channel
    ax2 = fig.add_subplot(122) 
    for idx, color, label in zip(range(1, fft.shape[0]), colors2, legend):
        ax2.plot(fft[0], fft[idx], label= label, linewidth=2, color = color, alpha=.7)
        ax2.set_xlabel('Frequency (Hz)')
        ax2.legend(bbox_to_anchor=(1.04,1), loc="upper left") 
        
    # Save file
    if file_path:
        if not os.path.exists(Path(file_path).parent):
            os.makedirs(Path(file_path).parent)
        plt.savefig(file_path)

    # Display graph on screen
    if show_fig:
        plt.show()
    #plt.close()


"""--------------------------------------------------------------------------------------------------
PLOT (MULTIPLE) signals depending on the time and the corresponding discrete FT 
INPUTS: 
    - signals : a matrix of [(n+1)xm] dimensions where n (nb of channels) << m 
                    first row must be the time vector! 
    - fft : a matrix of [(n+1)xm] dimensions where n (nb of channels) << m 
                    first row must be the frequency vector!
    - legend : list of singal's name
    - show_fig : True if the plot must be displayed on screen, False otherwise
    - (file_path) : path where the graph must be saved (if needed)
--------------------------------------------------------------------------------------------------"""
def plot_1dft(signal, fft, legend, show_fig, file_path=None): 
    # One big figure to frame the whole
    fig = plt.figure(figsize=(12,3))
    ax1 = fig.add_subplot(121) 
    ax1.stem(signal[0], signal[1])
    ax1.set_xlabel('Time (sec)')
        
    ax2 = fig.add_subplot(122) 
    ax2.stem(fft[0], fft[1], label=legend)
    ax2.set_xlabel('Frequency (Hz)')
    ax2.legend(bbox_to_anchor=(1.04,1), loc="upper left") 
        
    # Save file
    if file_path:
        if not os.path.exists(Path(file_path).parent):
            os.makedirs(Path(file_path).parent)
        plt.savefig(file_path)

    # Display graph on screen
    if show_fig:
        plt.show()
    #plt.close()

"""--------------------------------------------------------------------------------------------------
PLOT (MULTIPLE) signals depending on the time and the corresponding discrete FT 
INPUTS: 
    - signals : a matrix of [(n+1)xm] dimensions where n (nb of channels) << m 
                    first row must be the time vector! 
    - fft : a matrix of [(n+1)xm] dimensions where n (nb of channels) << m 
                    first row must be the frequency vector!
    - legend : list of singal's name
    - show_fig : True if the plot must be displayed on screen, False otherwise
    - (file_path) : path where the graph must be saved (if needed)
--------------------------------------------------------------------------------------------------"""
def plot_dft(signals, fft, legend, show_fig, file_path=None): 
    # One big figure to frame the whole
    fig = plt.figure(figsize=(12,3))
    ax1 = fig.add_subplot(121) 

    # Plot each time channel
    for idx, color in zip(range(1, signals.shape[0]), colors2):
        ax1.plot(signals[0], signals[idx], color = color, alpha=.7, marker= '.')
        ax1.set_xlabel('Time (sec)')
        
    # Plot each frequency channel
    ax2 = fig.add_subplot(122) 
    for idx, color, label in zip(range(1, fft.shape[0]), colors2, legend):
        ax2.plot(fft[0], fft[idx], label= label, color = color, alpha=.7, marker =  '.')
        ax2.set_xlabel('Frequency (Hz)')
        ax2.legend(bbox_to_anchor=(1.04,1), loc="upper left") 
        
    # Save file
    if file_path:
        if not os.path.exists(Path(file_path).parent):
            os.makedirs(Path(file_path).parent)
        plt.savefig(file_path)

    # Display graph on screen
    if show_fig:
        plt.show()
    #plt.close()


"""--------------------------------------------------------------------------------------------------
PLOT (MULTIPLE) signals depending on the time and the corresponding continuous FT 
INPUTS: 
    - signals : a matrix of [(n+1)xm] dimensions where n (nb of channels) << m 
                    first row must be the time vector! 
    - fft : a matrix of [(n+1)xm] dimensions where n (nb of channels) << m 
                    first row must be the frequency vector!
    - legend : list of singal's name
    - show_fig : True if the plot must be displayed on screen, False otherwise
    - (file_path) : path where the graph must be saved (if needed)
--------------------------------------------------------------------------------------------------"""
def plot_window(win, fft, legend, show_fig, file_path=None): 
    # One big figure to frame the whole
    fig = plt.figure(figsize=(12,4))
    ax1 = fig.add_subplot(121) 

    # Plot each time channel
    ax1.plot(win[0], win[1], linewidth=2)
    ax1.set_xlabel('Time (sec)')
        
    # Plot each frequency channel
    ax2 = fig.add_subplot(122) 
    ax2.plot(fft[0], fft[1], label= legend, linewidth=2)
    ax2.set_xlabel('$\Omega$')
    ax2.set_ylabel('$| W(e^{j \Omega}) |$ in dB')
    ax2.legend(bbox_to_anchor=(1.04,1), loc="upper left") 
        
    # Save file
    if file_path:
        if not os.path.exists(Path(file_path).parent):
            os.makedirs(Path(file_path).parent)
        plt.savefig(file_path)

    # Display graph on screen
    if show_fig:
        plt.show()
    #plt.close()
