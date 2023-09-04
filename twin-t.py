import os
import sys
import math
import numpy as np

PI = math.pi

def test():
    vals = ["10k", "10M", "10G", "0.1u", "1u", "47n", "100p"]

    for val in vals:
        print(unit2num(val))

def unit2num(val):
    convert_table = {
            "k":math.pow(10, 3),
            "M":math.pow(10, 6),
            "G":math.pow(10, 9),
            "m":math.pow(10, -3),
            "u":math.pow(10, -6),
            "n":math.pow(10, -9),
            "p":math.pow(10, -12),
            }

    # check whcih unit val have
    for key in convert_table.keys():
        if key in val:
            num = float(val.split(key)[0])
            return num * convert_table[key]

    return int(val)

def calc(R, C):
    R = unit2num(R)
    C = unit2num(C)
    freq = 1 / (2*PI * R * C)
    return freq

def load_parts(path):
    parts = []
    if os.path.exists(path):
        with open(path, "r") as f:
            for row in f.readlines():
                row = row.strip("\n")
                for val in row.split(","):
                    parts.append(val)
    else:
        return False
    return parts

registers = load_parts("src/registers.txt")
capacitors = load_parts("src/capacitors.txt")

freqs = {}
for R in registers:
    for C in capacitors:
        freq = (calc(R, C))
        freqs["{}:{}".format(R,C)] = freq

try:
    target_freq = sys.argv[1]
except IndexError:
    print("You need to specify target frequency")
    sys.exit(0)
print("target_freq:", target_freq)
# ゆるす差分を決める (500Hzまで)
print("{:^20} {:^15} {:^10}".format("freq", "R", "C"))
for key in freqs.keys():
    freq = freqs[key]
    diff = abs(unit2num(target_freq) - freq)
    if diff < 500: # if diff is less than 1kHz
        R,C = key.split(":")
        print("{:^20} {:^15} {:^10}".format(freq, R, C))
