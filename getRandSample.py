import random
import os
from shutil import copyfile
from shutil import move
import sys

random.seed(667)

def switchFiles(k, inc, out, a):
    """
    k   : k random samples
    inc : incoming image path, abs value (relative to current directory)
    out : outgoing image path, same as inc
    csv : name of csv file that has the image names
    a   : action to take, copy or move (insert string)
    """
    files = os.listdir(inc)
    if len(files) < k:
        print("Error: only", len(files), "images available in specified input directory",
                "while", k, "were requested.")
        print("Now exiting.")
        sys.exit()

    rand = random.sample(range(0, len(files)), k)

    n_not_found = 0

    for i in range(0, k):
        im = files[rand[i]]
        if im.endswith(".jpg") or im.endswith(".png"):
            try:
                if a == "copy":
                    copyfile(inc + "/" + im, out + "/" + im)
                elif a == "move":
                    move(inc + "/" + im, out + "/" + im)
            except FileNotFoundError:
                n_not_found += 1

    print("files not found (should be 0):", n_not_found)


if (len(sys.argv) != 5):
    print("Usage: \"python3 getRandSample.py <n_random_samples> <path_in> <path_out> <action>\"")
else:
    k = int(sys.argv[1])
    inc = sys.argv[2]
    out = sys.argv[3]
    a   = sys.argv[4]

    switchFiles(k, inc, out, a)
