"""
Module: comp110_lab03

Module with functions to manipulate audio using the sound module and its
classes / functions.
"""

import sound

def print_samples(snd, start_index, end_index):
    """
    Prints the samples from start_index up to and including
    end_index in sound object snd.
    """

    for i in range(start_index, end_index + 1):
        # Get sample at index i, and print it out
        smpl = snd.get_sample(i)
        print(smpl)


def print_left_channel(snd):
    """
    Prints all the samples in the sound object snd.
    """

    for sample in snd:
        left_value = sample.get_left()
        print(left_value)


def scale_volume(snd, factor):
    """
    Decreases the volume of a sound object by a specified factor.

    Paramters:
    snd (Sound): The sound object whose volume is to be decreased.
    factor (float): The factor by which the volume is to be decreased.

    Returns:
    A new sound object that is a copy of snd, but with volumes scaled by
    factor.
    """

    new_snd = snd.copy()

    for smpl in new_snd:
        # Scale left channel of smpl
        current_left = smpl.get_left()
        scaled_left = round(current_left * factor)
        smpl.set_left(scaled_left)

        # Scale right channel of smpl
        current_right = smpl.get_right()
        scaled_right = round(current_right * factor)
        smpl.set_right(scaled_right)

    return new_snd


""" Write your lab 3 functions below this point. """
