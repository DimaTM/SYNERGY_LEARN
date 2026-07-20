import random

def randbool(r, mxr):
    t = random.randint(1, mxr)
    if (t <= r):
        return True
    return False