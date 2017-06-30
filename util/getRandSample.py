# NextPax - AI_student_group
# JUNE 2017

import random
import os
from shutil import copyfile
from shutil import move
import sys


def get_rand_sample(k, image_path):
    """
    generate k random files from image_path

    Input:
    - k          : k random samples
    - image_path : image path, abs value (relative to current directory)

    Output:
    - rand_imgs : a list of k random images
    """
    files = os.listdir(image_path)
    if len(files) < k:
        print("Error getting random sample: only", len(files), "images available in specified",
            "input directory, while", k, "were requested.")
        print("Now exiting.")
        sys.exit()

    rand = random.sample(range(0, len(files)), k)
    rand_imgs = []

    for i in range(0, k):
        im = files[rand[i]]
        if im.endswith(".jpg") or im.endswith(".png"):
            rand_imgs.append(im)

    return rand_imgs
