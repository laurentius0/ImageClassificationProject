import os, sys
import pickle

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# change this as you see fit
#image_folder = sys.argv[1]

# path to images
# path_prefix = "./test/"
# path1 = "a_test"
# path2 = "c_test"
# path3 = "f_test"
# path4 = "j_test"
# path5 = "k_test"
# path6 = "l_test"


# paths = [path1, path2, path3, path4, path5, path6]

# # the correct tags of the images in the folder
# # NOTE: underscores (_) in the folder names will be seen as a space!
# # can be found in "./retrained_labels.txt"
# tag1 = "a train"
# tag2 = "c train"
# tag3 = "f train"
# tag4 = "j train"
# tag5 = "k train"
# tag6 = "l train"

# correct_tags = [tag1, tag2, tag3, tag4, tag5, tag6]

def testImages(path_prefix, paths, tags_file, thresholds, modelpath):
    # # open the file that contains all the tags
    # with open(tags_file) as f:
    #     correct_tags = readlines()

    # # strip new lines from the tags
    # correct_tags = [tag.strip() for tag in correct_tags]


    # threshold for right classification
    # thresholds = [.1, .2, .3, .4, .5, .6, .7, .8, .9]

    # path to model (*.pb)
    # modelpath = "retrained_graph.pb"


    # print('Paths are correct...')

    all_predicts = []

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile(tags_file)]

    # Unpersists graph from file
    with tf.gfile.FastGFile(modelpath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        for threshold in thresholds:
            predicts = []
            good = 0
            wrong = 0
            underThresh = 0
            total = 0
            for i in range(len(paths)):
                path = path_prefix + "/" + sorted(set(paths))[i]
                correct_tag = sorted(set(label_lines))[i]

                dirs = os.listdir( path )
                total += len(dirs)

                for item in dirs:

                    # Read in the image_data
                    image_data = tf.gfile.FastGFile(path+"/"+item, 'rb').read()

                    # Feed the image_data as input to the graph and get first prediction
                    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

                    predictions = sess.run(softmax_tensor, \
                         {'DecodeJpeg/contents:0': image_data})

                    # Sort to show labels of first prediction in order of confidence
                    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]


                    if (max(predictions[0]) < threshold):
                        underThresh += 1
                    elif (label_lines[top_k[0]] == correct_tag):
                        predicts.append((correct_tag, label_lines[top_k[0]]))
                        good = good +1
                    else:
                        predicts.append((correct_tag, label_lines[top_k[0]]))
                        wrong = wrong + 1
            all_predicts.append(predicts)
            print('With threshold: %.2f' % (threshold))
            print('accuracy: %.2f%% (good: %.5f)' % (good*100./(total-underThresh), good))
            print('below threshold: %.2f%% (under threshold: %.5f)' % (underThresh*100./total, underThresh))
            print('wrong %%: %.2f (number: %.2f)' % (wrong*100./(total-underThresh), wrong))
            print('\n')

    return all_predicts
