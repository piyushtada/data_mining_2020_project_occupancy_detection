import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



# def getting_data_ready():

#     # for loading all the data
#     df = pd.read_csv('https://raw.githubusercontent.com/piyushtada/data_mining_2020_project_occupancy_detection/master/jupyter_notebooks/data/scaled_datatrainingcopy.csv')
#     # df_test1 = pd.read_csv('/Users/piyush2017/Code/2020_Data_Mining_Project_02/data_mining_2020_project_occupancy_detection/jupyter_notebooks/data/scaled_datatestcopy.csv')
#     # df_test2 = pd.read_csv('/Users/piyush2017/Code/2020_Data_Mining_Project_02/data_mining_2020_project_occupancy_detection/jupyter_notebooks/data/scaled_datatest2copy.csv')

#     # class_name = "Occupancy"

#     attributes = [col for col in df.columns if col != class_name]
#     X = df[attributes].values
#     y = df[class_name]

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100, stratify=y)

#     # attributes = [col for col in df.columns if col != class_name]
#     # X_test1 = df_test1[attributes].values
#     # y_test1 = df_test1[class_name]


#     # attributes = [col for col in df.columns if col != class_name]
#     # X_test2 = df_test2[attributes].values
#     # y_test2 = df_test2[class_name]
    
    
#     return X_train, X_test, y_train, y_test #, X_test1, y_test1, X_test2, y_test2


def show_report(tests= tests,clf= clf):
    for test, results, name in tests:

        y_pred = clf.predict(test)
        print('\n ===============Results for {}================== \n'.format(name))
        print('Accuracy %s' % accuracy_score(results, y_pred))
        print('F1-score %s' % f1_score(results, y_pred, average=None))
        print(classification_report(results, y_pred))
        y_score = clf.predict_proba(test)
        plot_roc(results, y_score)
        plot_lift_curve(results, y_score)
        plt.show()