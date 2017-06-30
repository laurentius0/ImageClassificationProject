import os, sys, json
import pandas as pd

import tensorflow as tf

import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# with open("config.json") as config_file:
#     cfg = json.load(config_file)

# path_prefix = cfg["classifying"]["path_prefix"]
# paths = cfg["classifying"]["paths"]
# threshold = cfg["classifying"]["threshold"]
# modelpath = cfg["classifying"]["model_path"]
# output_csv_path = cfg["classifying"]["output_csv_path"]
# output_csv_name = cfg["classifying"]["output_csv_name"]


def labelImages(path_prefix, paths, threshold, modelpath, tags_file, output_csv_path, output_csv_name):
    pred_list = []
    unclassified_list = []

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile(tags_file)]

    # Unpersists graph from file
    with tf.gfile.FastGFile(modelpath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        for path in paths:
            dirs = os.listdir( path_prefix + "/" + path )

            for item in dirs:
                # Read in the image_data
                image_data = tf.gfile.FastGFile(path_prefix + "/" + path+"/"+item, 'rb').read()

                # Feed the image_data as input to the graph and get first prediction
                softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

                predictions = sess.run(softmax_tensor, \
                     {'DecodeJpeg/contents:0': image_data})

                # Sort to show labels of first prediction in order of confidence
                top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                if (max(predictions[0]) < threshold):
                    unclassified_list.append([item, '0'])
                    unclassified_list[-1].extend(predictions[0])
                else:
                    pred_list.append([item, label_lines[top_k[0]]])
                    pred_list[-1].extend(predictions[0])

    labels = ['conf '+lbl for lbl in label_lines]
    cols = ['file_name', 'predicted_label']
    cols.extend(labels)
    pred_list.extend(unclassified_list)
    df = pd.DataFrame(pred_list, columns=cols)
    df = df.round(5)

    df.to_csv(output_csv_path + "/" + output_csv_name, index=False)
