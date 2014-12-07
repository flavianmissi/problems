import sys

if len(sys.argv) < 3:
    print("missing input")
    exit(1)

_, soldiers1, soldiers2 = sys.argv
soldiers1, soldiers2 = int(soldiers1), int(soldiers2)

print(soldiers2 - soldiers1)
