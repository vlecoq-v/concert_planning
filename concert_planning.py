import argparse
import logging
import typing

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

track_list: list[int] = list(map(int, args.track_list.split(',')))

print(track_list)
print(args.premiere_length)
