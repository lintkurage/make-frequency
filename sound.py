#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
正弦波、矩形波、三角波、のこぎり波のwavファイルを出力する.
"""

__author__='lintkurage'
__version__='0.0.1'
__date__='2024/06/14'

import struct
import wave
import numpy as np

def main():
    """
    main program

    parameters
    f0:fundamental frequency(initial value:440Hz)
    higher_harmonics_number:higher harmonics number(initial value:7)
    sampling_frequency:sampling frequency(initial value:48000Hz)
    seconds:seconds(initial value:3sec)
    amplitude:amplitude(initial value:1)
    """
    f0=440.0
    higher_harmonics_number=7
    sampling_frequency=48000
    secounds=3
    amplitude=1

    #sin wave
    sine_fname='sine.wav'


def create_sine(f0,amplitude,sampling_frequency,seconds):
    """
    create sin wave
    """
    frame=np.arange(0,sampling_frequency*seconds)
    return amplitude*np.sin(2*np.pi*frame*f0/sampling_frequency)

def sine(f0,amplitude,sampling_frequency,seconds,sine_fname):
    """
    sin wave file
    """
    sine_wave=create_sine(f0,amplitude,sampling_frequency,seconds)

def minmax_normalized(waves):
    """
    wave normalized for -1 to 1
    """
    min_value=np.min(waves)
    max_value=np.max(waves)
    normalized_wave=2*((waves-min_value)/(max_value-min_value))-1
    return normalized_wave

if __name__=='__main__':

    import sys

    sys.exit(main())