import argparse
import logging
import typing

parser = argparse.ArgumentParser(
    description="""program description"""
)

parser.add_argument(
    "-l",
    "--length",
    help="Concert Premiere intended Length",
)

args = parser.parse_args()

if __name__ != "__main__":
    exit()

tracks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 200, 0, 23, 345, 65, 44557, 23, 6, 879, 1]
