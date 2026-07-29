import math

def mapValue(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def clamp(value, min, max):
    if value < min:
        value = min
    if value > max:
        value = max
    return value


