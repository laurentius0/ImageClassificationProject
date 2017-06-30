# NextPax - AI_student_group
# JUN 2017

from PIL import Image
from PIL import ImageFile
import os
import sys
import pandas as pd



def removeBrokenImages(path_prefix, paths):
    """
    Remove corrupt Images.

    Input:
    - path_prefix : "root" folder of other paths
    - paths       : list of paths to folders with images

    Output:
    - text file containing names of removed images
    """
    ImageFile.LOAD_TRUNCATED_IMAGES = False
    count = 0
    corruptImages = []
    for path in paths:
        imagenames = os.listdir(path_prefix + "/" + path)
        naam = os.path.basename(os.path.normpath(path_prefix + "/" + path))
        for imagename in imagenames:
            if imagename.endswith('.jpg') or imagename.endswith('.png'):
                try:
                    im = Image.open(path_prefix + "/" + path + "/" + imagename)
                    im.rotate(45)
                except:
                    os.remove(path_prefix + "/" + path + "/" + imagename)
                    corruptImages.append([imagename, path_prefix + "/" + path])
                    count = count + 1
    if os.path.isfile("corrupt_images.csv"):
        outdf = pd.read_csv(open("corrupt_images.csv", "rb"))
        outmatrix = outdf.as_matrix()
        outmatrix = outmatrix.tolist()
        corruptImages.extend(outmatrix)

    outdf = pd.DataFrame(corruptImages)
    outdf.to_csv("corrupt_images.csv", index=False)
    print("Removed", count, "faulty images...")

