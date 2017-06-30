import matplotlib.pyplot as plt
import pandas as pd
import pickle
import seaborn as sb
import numpy as np

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

sb.set_style("whitegrid")

def createConfusionMatrix(all_predicts, thresholds):
    """
    Creates a confusion matrix

    Input:
    - data: list of tuples containing the true label and the predicted label

    Output:
    - conf_matrix.png
    """
    for data, threshold in zip(all_predicts, thresholds):
        y_test = [elem[0] for elem in data]
        y_pred = [elem[1] for elem in data]

        class_names = sorted(set(y_test))

        # Compute confusion matrix
        cnf_matrix = confusion_matrix(y_test, y_pred)

        # Convert values to float
        cnf_matrix = cnf_matrix.astype(float)

        # Convert values to percentage of row
        for i, vec in enumerate(cnf_matrix):
            cnf_matrix[i] = vec / sum(vec)

        # Turn it into a dataframe
        df_cm = pd.DataFrame(cnf_matrix, index= class_names)
        df_cm.columns = class_names
        plt.figure(figsize=(10, 7))
        sb.heatmap(df_cm, annot=True, fmt='.4f', linewidth=1, cbar=False, cmap='Blues')
        plt.title('Inception v3 \nAccuracy: {0:.3f}\n'.format(accuracy_score(y_test, y_pred)))
        plt.ylabel('True label')
        plt.xlabel('Predicted label');
        plt.savefig("conf_matrix_{0}.png".format(threshold), dpi=100, format="png")

