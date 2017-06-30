# NextPax - AI_student_group
# JUN 2017

import os
from PIL import Image
from PIL import ImageFile


def convertPNG2JPG(path_prefix, paths):
    """
    Convert all PNG images in the image_path to JPG, deleting the original

    Input:
    - path_prefix : "root" folder of other paths
    - paths       : list of folders with PNG images

    Output:
    - No return value
    """
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    count = 0

    for image_path in paths:
        images = os.listdir(path_prefix + "/" + image_path)
        for image in images:
            removed = 0
            if image[-4:] != ".png":
                continue
            try:
                im = Image.open(path_prefix + "/" + image_path + "/" + image)
                rgb_im = im.convert('RGB')
                rgb_im.save(path_prefix + "/" + image_path + "/" + image[:-4] + ".jpg")
                os.remove(path_prefix + "/" + image_path + "/" + image)
                count = count + 1
            except:
                pass

    print("Converted", count, "images from png to jpg...")

