# TIMER.py
#   by Anonymous
#
# Created:
#   6/10/2020, 2:13:40 PM
# Last edited:
#   6/10/2020, 10:52:23 PM
# Auto updated?
#   Yes
#
# Description:
#   This file implements a neat little timer. Will support multiple stules
#   in the future, hopefully even a cool clock or something, but for now it
#   just counts down like a digital clock. Tries to minimize CPU usage by
#   avoiding explicit waits 'n' stuff.
#

import argparse
import select
import sys
import time


def main(total_secs):
    print("\n*** TIMER v1.0.0 ***\n")

    print("Time to go:")
    while total_secs > 0:
        try:
            # Extract the hours, minutes & seconds
            hours = total_secs // 3600
            tmp = total_secs % 3600
            minutes = tmp // 60
            seconds = tmp % 60

            # Print
            print(f"\r\033[K{hours:02d}:{minutes:02d}:{seconds:02d}", end="")

            # Wait a bit to make a timer and not a counter
            time.sleep(1)

            # Update the time
            total_secs -= 1
        except KeyboardInterrupt:
            print("\n\nTimer paused. Press enter to resume, or hit Ctrl+C again to stop.")
            try:
                input()
            except KeyboardInterrupt:
                print("\n\nTIMER STOPPED.\n\a")
                return 0

    # Print all-zeroes + done
    print(f"\r\033[K{0:02d}:{0:02d}:{0:02d}\n\nTIMER PASSED.\n\a")

    return 0


if __name__ == "__main__":
    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", default="15:00", type=str, help="The time for the timer to run. Can be given as seconds 'ss', minutes and seconds 'mm:ss' or hours, minutes and seconds: 'HH:mm:ss'.")
    
    args = parser.parse_args()

    # Try to parse the time
    colon_count = args.time.count(":")
    if colon_count > 2:
        print("ERROR: Time has invalid format: must either be 'ss' (seconds), 'mm:ss' (minutes & seconds) or 'HH:mm:ss' (hours, minutes & seconds)", file=sys.stderr)
        exit(-1)
    
    # First, parse the hours
    total_secs = 0
    if colon_count == 2:
        hours_str = args.time[0:args.time.find(":")]
        args.time = args.time[args.time.find(":") + 1:]
        if len(hours_str) == 0: hours_str = "0"

        # Try to convert to int
        try:
            hours = int(hours_str)
            if hours < 0: raise ValueError()
            total_secs += hours * 3600
        except ValueError:
            print("ERROR: Time has invalid format: number of hours is not an integer >= 0", file=sys.stderr)
            exit(-1)

    if colon_count == 1 or colon_count == 2:
        minutes_str = args.time[0:args.time.find(":")]
        args.time = args.time[args.time.find(":") + 1:]
        if len(minutes_str) == 0: minutes_str = "0"

        # Try to convert to int
        try:
            minutes = int(minutes_str)
            if minutes < 0: raise ValueError()
            total_secs += minutes * 60
        except ValueError:
            print("ERROR: Time has invalid format: number of minutes is not an integer >= 0", file=sys.stderr)
            exit(-1)
    
    # We always run the number of seconds
    seconds_str = args.time
    if len(seconds_str) == 0: seconds_str = "0"
    # Try to convert to int
    try:
        seconds = int(seconds_str)
        if seconds < 0: raise ValueError()
        total_secs += seconds
    except ValueError:
        print("ERROR: Time has invalid format: number of seconds is not an integer >= 0", file=sys.stderr)
        exit(-1)

    exit(main(total_secs))