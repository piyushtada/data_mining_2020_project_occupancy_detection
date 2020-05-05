# Occupancy-detection-data

This is a repository for data for the data mining project we did for class:

Accurate occupancy detection of an office room from light, temperature, humidity and CO2 measurements using statistical learning models. Luis M. Candanedo, Véronique Feldheim. Energy and Buildings. Volume 112, 15 January 2016, Pages 28-39.
  
## Project Task 1 - Basic Classifiers and Evaluation

1. Prepare the dataset in order to build several basic classifiers able to predict room occupancy from the available variables. You are welcome in creating new variables.

2. Solve the classification task with k-NN (testing values of k), Naive Bayes, Logistic Regression, Decision Tree using cross-validation and/or random/grid search for parameter estimation.

3. Evaluate each classifier using Accuracy, Precision, Recall, F1, ROC, AUC and Lift Chart.

4. Try to reduce the dimensionality of the dataset using the methods studied (or new ones). Test PCA and try to solve the classification task in two dimensions. Plot the dataset in the two new dimensions and observe the decision boundary and the one of the trained algorithms.

5. Analyze the value distribution of the class to predict and turn the dataset into an imbalanced version reaching a strong majority-minority distribution (e.g. 96%-4%). Then solve again the classification task adopting the various techniques studied (or new ones).

6. Select two continuous attributes, define a regression problem and try to solve it using different techniques reporting various evaluation measures. Plot the two-dimensional dataset. Then generalize to multiple linear regression and observe how the performance varies.

7. Draw your conclusions about the basic classifiers and techniques adopted in this analysis.

## Project Task 2 - Advanced Classifiers and Evaluation

1. Using the dataset for classification prepared for Task 1 build several advanced classifiers able to predict room occupancy from the available variables. In particular, you are required to use SVM (linear and non-linear), NN (Single and Multilayer Perceptron), DNN (design at least two different architectures), Ensemble Classifier (RandomForest, AdaBoost and a Bagging technique in which you can select a base classifier of your choice with a justification).

2. Evaluate each classifier using Accuracy, Precision, Recall, F1, ROC, etc; Draw your conclusion about the classifiers.

3. Highlight in the report different aspects typical of each classifier. For instance for SVM: is a linear model the best way to shape the decision boundary? Or for NN: what are the parameter sets or the convergence criteria suggesting you are avoiding overfitting? How many iterations/base classifiers are needed to allow a good estimation using an ensemble method? Which is the feature importance for the Random Forest?

4. You are NOT required to experiment also in the imbalanced case but if you do it is not considered a mistake.

## Project Task 3 - Time Series Analysis and Forecasting/Classification

1. Exploit the temporal information of the dataset preparing it for a univariate framework of analysis, i.e. select a feature and use it as your time series. You are welcome in using more than one reliable temporal split to have more time series of the same feature. You are welcome in creating more than a dataset using more than a feature and report the result on the feature you prefer or more than one. Analyze such datasets for finding motifs and/or anomalies and shaplets. Visualize and discuss them and their relationship with the class of the time series.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/piyushtada/data_mining_2020_project_occupancy_detection.git/master?filepath=https%3A%2F%2Fgithub.com%2Fpiyushtada%2Fdata_mining_2020_project_occupancy_detection%2Fblob%2Fmaster%2Fjupyter_notebooks%2F10_TimeSeriesgc_shapelet%2520discovery-2020-05-01.ipynb)

2. On the dataset(s) created, compute clustering based on Euclidean/Manhattan and DTW distances and compare the results. To perform the clustering you can choose among different similarity methods, i.e., shape-based, feature-based, approximation-based, compression-based, etc.. Finally, analyze the clusters and the clustering and highlight similarities and differences.

3. Apply forecasting methods on the dataset(s) created. Make sure to preprocess adequately the time series according to the method used (e.g., an exponential smoothing or an autoregression), indeed checking stationarity and reducing trends and seasonality or with the help of a statistically significant test;

4. Solve the classification task on the univariate dataset created using different approaches, i.e., traditional classification, shapelet-based, feature-based, etc.

5. Solve the classification task considering the whole dataset as a multivariate dataset. Develop the classification process you prefer (e.g. exploiting shapelets, traditional classifiers, CNN, or RNN) to maximize accuracy and F1-score.
