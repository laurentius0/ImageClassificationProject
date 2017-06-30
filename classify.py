import sys, os, time, json
sys.path.insert(0, 'util/')
from removeBrokenImages import *
from convertPNG2JPG import *
from labelImages import *

with open("config.json") as config_file:
    cfg = json.load(config_file)

im_dir = cfg["classifying"]["classify_dir"]
threshold = cfg["classifying"]["threshold"]
model_path = cfg["classifying"]["model_path"]
tags_file = cfg["classifying"]["tags_file"]
output_csv_path = cfg["classifying"]["output_csv_path"]
output_csv_name = cfg["classifying"]["output_csv_name"]

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
    print("Starting to classify...")
    labelImages(im_dir, paths, threshold, model_path, tags_file, output_csv_path, output_csv_name)
    print("Done classifying...")
