import argparse
import logging
from typing import Union

from find_sum import IllegalArgumentError, find_sum

if __name__ != "__main__":
    exit()

parser = argparse.ArgumentParser(
    description="""This script determines wether a set of 3 tracks from the track_list argument can be used as a
    preshow with intended premiere_length length."""
)

parser.add_argument(
    "-l",
    "--premiere_length",
    help="Concert Premiere intended Length in int.",
)

parser.add_argument(
    "-t",
    "--track_list",
    help="The track list to evaluate. Pass in a list of coma separated ints.",
)

args = parser.parse_args()

tracks = [int(track) for track in args.track_list.split(',')]
premiere_length = int(args.premiere_length)

if len(tracks) < 3:
    logging.error("Argument track_list must contain at least 3 elements.")

if premiere_length <= 0:
    logging.error("Argument premiere length must be greater or equal to 1.")

try:
    return_value: Union[list[int], None] = find_sum(premiere_length, tracks)
    print(return_value)
    if return_value is None:
        exit(0)
    else:
        exit(1)
except Exception as e:
    print(e)
    logging.error(e)
