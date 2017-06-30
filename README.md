# Image Classification at NextPax
This is the image classification model, divided into three sections: train, test and classify. The parameters of the model can be configured in the __config.json__ file. First we will list the dependencies after which we will guide you through the possible parameter that you can tweak per section. The backlog of this product can be found under the projects tab on GitHub. Each item is clickable, and will supply an explanation for being added to the backlog.

## Dependencies
* Tensorflow 1.1.0 (GPU version recommended)
* Python 2 or 3 tested with the following package versions:
    * Pandas 0.19
    * Matplotlib.pyplot 1.5.1
    * Pickle 72223
    * Seaborn 0.7.1
    * Numpy 1.11.2
    * Sklearn 0.18.1



## Training
Training is done with the __train.py__ file. You can tweak the following parameters:

| parameter        | description           | example setting (default) |
| ------------- |:-------------:| -----:|
| im_dir      | directory containing image folders  | fotos/ |
| remove_dups | on/off, for training it is advised to keep this on, to negate overfitting      |    on |
| output_graph | name of the trained model, should end in .pb | retrained_graph.pb |
| output_labels | txt file containing the labels (same as image folder names) | retrained_labels.txt |

Training can take a while, depending on the amount of images. After the training is done the following files are created:
* output_graph : the trained model, used for further classification
* output_labels : txt file containing the different labels
* inception : folder containing the inception model from Google
* bottlenecks : folder containing folders with bottlenecks created by retraining the inception model
* training_summaries : folder containing information to visualize the trained model in Tensorboard

## Testing
Testing is done with the __test.py__ file. You can tweak the following parameters:

| parameter        | description           | example setting (default) |
| ------------- |:-------------:| -----:|
|    im_dir   | directory containing the test image folders  | test/ |
| thresholds | the thresholds on which the model will test | [0, 0.8] |
| model_path | path to the output_graph from __train.py__ | retrained_graph.pb |
| tags_file | path to the output_labels from __train.py__ | retrained_labels.txt|


After the testing is done the following file is created:
* conf_matrix.png : file showing which errors have been made


## Classifying
Classifying is done with the __classify.py__ file. You can tweak the following parameters:

| parameter        | description           | example setting (default) |
| ------------- |:-------------:| -----:|
|    im_dir   | directory containing the image folders to be labeled | ./tolabel |
| threshold | the threshold on which the model will test | [0.8] |
| model_path | path to the output_graph from __train.py__ | retrained_graph.pb |
| tags_file | path to the output_labels from __train.py__ | retrained_labels.txt |
| output_csv_path | directory for the output csv file | ./ |
| output_csv_name | name of the output csv containing labeled images | output.csv |

After classifying is done the following file is created:
* output.csv : a csv file containing the filenames and predicted classes

## Get random sample from data
To take a random sample of the data the getRandSample.py file can be used. The files are moved or copied to another folder. usage: 
| parameter        | description           | example setting (default) |
| ------------- |:-------------:| -----:|
|    n   | amount of samples that should be taken | 100 |
|path_in| the location of the entire dataset |fullset/|
|path_out| the location of the samples taken from the entire dataset |testset/|
|action | action to apply to the images, move or copy to their new location | "copy" or "move"|
