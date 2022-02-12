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
    logging.error("not enough tracks")
    exit(0)
if premiere_length <= 0:
    logging.error("show duration must be > 0")
    exit(0)

try:
    return_value: Union[list[int], None] = find_sum(premiere_length, tracks)
    if return_value is None:
        logging.error("No match found for this concert")
        exit(0)
    else:
        print(f"""
        We have a match for the show!
        Track numbers {return_value} are fit with a length of: 
        {tracks[return_value[0]]} + {tracks[return_value[1]]} + {tracks[return_value[2]]} = {premiere_length}
        """)
        exit(1)
except Exception as e:
    logging.error(e)
    exit(0)
