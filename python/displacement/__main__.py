import sys


if len(sys.argv) < 3:
    print("missing values")
    exit(1)


def displacement(velocity, time):
    return velocity * time


v = int(sys.argv[1])
t = int(sys.argv[2])
print(displacement(v, t*2))
