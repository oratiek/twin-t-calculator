import os
import sys
import math
import numpy as np
sys.path.append("../")
from core.utils import *

PI = math.pi

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

stock = PartsStock()
registers = stock.registers()
capacitors = stock.capacitors()

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
