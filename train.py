import sys, os, time, json

sys.path.insert(0, 'util/')
from duplicatesCheck import *
from removeBrokenImages import *
from convertPNG2JPG import *
from retrain import *

with open("config.json") as config_file:
    cfg = json.load(config_file)

im_dir = cfg["training"]["train_dir"]
# paths = cfg["training"]["paths"]
remove = cfg["training"]["remove_dups"]

output_graph = cfg["training"]["output_graph"]
output_labels = cfg["training"]["output_labels"]

if __name__ == "__main__":
    paths = os.listdir(im_dir)

    # remove all faulty images from all specified image folders
    print("Removing faulty images...")
    removeBrokenImages(im_dir, paths)
    print("Done removing faulty images...")

    # check for duplicates in the data
    print("Removing duplicate images...")
    dupCheck(im_dir, paths, remove)
    print("Done removing duplicates...")

    # convert all png images to jpg images
    print("Converting png to jpg...")
    convertPNG2JPG(im_dir, paths)
    print("Done converting png to jpg...")

    # default options for the retraining of the neural network
    sumdir_def = "training_summaries/basic"
    bottleneckdir_def = "bottlenecks"
    ntrstep_def = 4000
    learnrate_def = 0.01
    testperc_def = 10
    valperc_def = 10
    evalstep_def = 10
    trbatchsize_def = 100
    testbatch_def = -1

    # train
    print("Starting to train...")
    retrain(im_dir, output_graph, output_labels, sumdir_def, bottleneckdir_def,
                    ntrstep_def, learnrate_def, testperc_def, valperc_def,
                    evalstep_def, trbatchsize_def, testbatch_def)
    print("Done training...")
