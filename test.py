import sys, os, time, json

sys.path.insert(0, 'util/')
from removeBrokenImages import *
from convertPNG2JPG import *
from testImages import *
from createConfusionMatrix import *

with open("config.json") as config_file:
    cfg = json.load(config_file)

im_dir = cfg["testing"]["test_dir"]
thresholds = cfg["testing"]["thresholds"]
model_path = cfg["testing"]["model_path"]
tags_file = cfg["testing"]["tags_file"]

if __name__ == "__main__":
    paths = os.listdir(im_dir)

    # remove all faulty images from all specified image folders
    print("Removing faulty images...")
    removeBrokenImages(im_dir, paths)
    print("Done removing faulty images...")

    # convert all png images to jpg images
    print("Converting png to jpg...")
    convertPNG2JPG(im_dir, paths)
    print("Done converting png to jpg...")

    # classify
    print("Starting to test...")
    all_predicts = testImages(im_dir, paths, tags_file, thresholds, model_path)
    print("Done testing...")
    
    # create confusion matrix
    print("Starting to create confusion matrices...")
    createConfusionMatrix(all_predicts, thresholds)
    print("Created confusion matrices...")
