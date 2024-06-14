#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
正弦波、矩形波、三角波、のこぎり波のwavファイルを出力する.
"""

__author__='lintkurage'
__version__='0.1.0'
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
    seconds=3
    amplitude=1

    frame=np.arange(0,sampling_frequency*seconds)

    #sin wave
    sine_fname='sine.wav'
    sine(f0,amplitude,sampling_frequency,frame,sine_fname)


def create_sine(f0,amplitude,sampling_frequency,frame):
    """
    create sin wave
    """
    return amplitude*np.sin(2*np.pi*frame*f0/sampling_frequency)

def sine(f0,amplitude,sampling_frequency,frame,sine_fname):
    """
    sin wave file
    """
    sin_wave=create_sine(f0,amplitude,sampling_frequency,frame)
    sin_wave=minmax_normalized(sin_wave)
    wave_pack(sin_wave,frame,sampling_frequency,sine_fname)

def minmax_normalized(waves):
    """
    wave normalized for -1 to 1
    """
    min_value=np.min(waves)
    max_value=np.max(waves)
    normalized_wave=2*((waves-min_value)/(max_value-min_value))-1
    return normalized_wave

def wave_pack(waves,frame,sampling_frequency,sine_fname):
    """
    quantization wav file create function
    """
    waves=np.array(waves*(2**15-1)).astype(np.int16)

    binary_wave=struct.pack("h"*len(frame),*waves)  #バイナリデータとしてパック
    wave_write=wave.Wave_write(sine_fname)
    parameters=(1,2,sampling_frequency,len(frame),'NONE','not compressed')
    wave_write.setparams(parameters)
    wave_write.writeframes(binary_wave)
    wave_write.close()

if __name__=='__main__':

    import sys

    sys.exit(main())