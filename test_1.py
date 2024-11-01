from evaluation import accuracy, confusion_score, get_dir, train_test_split
from decision_tree import DecisionTree
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

###### OUR MODEL ######
def get_predictions_dt_ours(X_train, y_train, X_test, y_test):
    model = DecisionTree(min_samples_split=2, max_depth=2, metric='gini')
    model.fit(X_train, y_train)
    model.print_tree(columns = columns)
    predictions = model.predict(X_test)
    print("--- Our Model (DT) ---")
    print(f"Model's Accuracy: {accuracy(y_test, predictions)}")
    precision, recall, f1_score = confusion_score(y_test, predictions, "macro")
    print(f"Model's F1 (Macro): {f1_score}")
    print(f"Model's Precision (Macro): {precision}")
    print(f"Model's Recall (Macro): {recall}")
    precision, recall, f1_score = confusion_score(y_test, predictions, "micro")
    print(f"Model's F1 (Micro): {f1_score}")
    print(f"Model's Precision (Micro): {precision}")
    print(f"Model's Recall (Micro): {recall}")


###### SKLEARN MODEL ######
def get_predictions_dt_sklearn(X_train, y_train, X_test, y_test):
    decision_tree_classifier = DecisionTreeClassifier()
    decision_tree_classifier.fit(X_train, y_train)
    predictions = decision_tree_classifier.predict(X_test)

    # Calculate evaluating metrics
    print("--- Sklearn's Model (DT) ---")
    print(f"Model's Accuracy: {accuracy(y_test, predictions)}")
    precision, recall, f1_score = confusion_score(y_test, predictions, "macro")
    print(f"Model's F1 (Macro): {f1_score}")
    print(f"Model's Precision (Macro): {precision}")
    print(f"Model's Recall (Macro): {recall}")
    precision, recall, f1_score = confusion_score(y_test, predictions, "micro")
    print(f"Model's F1 (Micro): {f1_score}")
    print(f"Model's Precision (Micro): {precision}")
    print(f"Model's Recall (Micro): {recall}")

def scale(X):
    """
    Standardizes the data in the array X.

    Parameters:
        X (numpy.ndarray): Features array of shape (n_samples, n_features).

    Returns:
        numpy.ndarray: The standardized features array.
    """
    # Calculate the mean and standard deviation of each feature
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)

    # Standardize the data
    X = (X - mean) / std

    return X

if __name__ == "__main__":
    path = get_dir("breast-cancer.csv")
    df = pd.read_csv(path)
    names = ['radius_mean',
    'texture_mean',
    'perimeter_mean',
    'area_mean',
    'smoothness_mean',
    'compactness_mean',
    'concavity_mean',
    'concave points_mean',
    'symmetry_mean',
    'radius_se',
    'perimeter_se',
    'area_se',
    'compactness_se',
    'concavity_se',
    'concave points_se',
    'radius_worst',
    'texture_worst',
    'perimeter_worst',
    'area_worst',
    'smoothness_worst',
    'compactness_worst',
    'concavity_worst',
    'concave points_worst',
    'symmetry_worst',
    'fractal_dimension_worst']

    X = df[names].values
    y = df['diagnosis'].values.reshape(-1,1)
    columns = df[names].columns.values

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    get_predictions_dt_ours(X_train, y_train, X_test, y_test)
    get_predictions_dt_sklearn(X_train, y_train, X_test, y_test)
