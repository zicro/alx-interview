#!/usr/bin/python3
""" Module for storing the function that reads stdin line by line and computes
    metrics
"""
from sys import stdin


def print_stats(status_codes, file_size):
    """ Function that prints the statistics """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    counter = 0
    try:
        for line in stdin:
            counter += 1
            data = line.split()
            try:
                file_size += int(data[-1])
                status_codes[data[-2]] += 1
            except Exception:
                pass
            if counter % 10 == 0:
                print_stats(status_codes, file_size)
        print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
