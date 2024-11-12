from flask import Flask, render_template, url_for
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from sklearn.datasets import load_iris, load_wine, load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import time

import matplotlib
matplotlib.use('Agg')  

app = Flask(__name__)

def plot_to_base64(fig):

    img_stream = BytesIO()
    fig.savefig(img_stream, format='png')
    img_stream.seek(0)

    img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8')
    return img_base64

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bai1')
def bai1():

    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100
    report = classification_report(y_test, y_pred)

    return render_template('bai1.html', accuracy=accuracy, report=report)

@app.route('/bai2')
def bai2():

    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)


    fig, ax = plt.subplots()
    ax.matshow(cm, cmap='Blues', alpha=0.7)
    for (i, j), val in np.ndenumerate(cm):
        ax.text(j, i, f'{val}', ha='center', va='center', color='red')
    plt.title('Ma trận nhầm lẫn Naive Bayes')
    plt.xlabel('Dự đoán')
    plt.ylabel('Thực tế')

    img_base64 = plot_to_base64(fig)
    plt.close()

    return render_template('bai2.html', plot_image=img_base64)

@app.route('/bai3')
def bai3():

    wine = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.2, random_state=42)
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100
    recall = classification_report(y_test, y_pred, output_dict=True)['macro avg']['recall']
    precision = classification_report(y_test, y_pred, output_dict=True)['macro avg']['precision']

    return render_template('bai3.html', accuracy=accuracy, recall=recall, precision=precision)
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

@app.route('/bai4')
def bai4():

    wine = load_wine()
    X, y = wine.data, wine.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    k_values = [1, 3, 5, 7, 9]
    accuracies = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)


    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(k_values, accuracies, marker='o', linestyle='-', color='b')
    ax.set_title('Mối quan hệ giữa k và độ chính xác của mô hình KNN')
    ax.set_xlabel('Giá trị của k')
    ax.set_ylabel('Độ chính xác')
    ax.set_xticks(k_values)
    ax.grid(True)


    img_base64 = plot_to_base64(fig)
    plt.close()


    accuracies_str = [f"k={k}: {acc:.2f}" for k, acc in zip(k_values, accuracies)]
    return render_template('bai4.html', plot_image=img_base64, accuracies=accuracies_str)


@app.route('/bai5')
def bai5():

    from sklearn.datasets import load_breast_cancer

    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100

    fig, ax = plt.subplots(figsize=(20, 10))
    plot_tree(model, feature_names=cancer.feature_names, class_names=cancer.target_names, filled=True, ax=ax)
    plt.title('Cây quyết định trên Breast Cancer')

    img_base64 = plot_to_base64(fig)
    plt.close()

    return render_template('bai5.html', accuracy=accuracy, plot_image=img_base64)

@app.route('/bai6')
def bai6():

    digits = load_digits()
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100

    return render_template('bai6.html', accuracy=accuracy)

@app.route('/bai7')
def bai7():

    digits = load_digits()
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
    kernels = ['linear', 'poly', 'rbf']
    results = {}

    for kernel in kernels:
        model = SVC(kernel=kernel)
        start_time = time.time()  
        model.fit(X_train, y_train)
        end_time = time.time()  
        training_time = end_time - start_time  

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred) * 100

        results[kernel] = {'accuracy': accuracy, 'training_time': training_time}
    return render_template('bai7.html', results=results)

@app.route('/bai8')
def bai8():
    try:

        from sklearn.datasets import fetch_openml
        from sklearn.neural_network import MLPClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score


        mnist = fetch_openml('mnist_784', version=1)
        X_train, X_test, y_train, y_test = train_test_split(mnist.data, mnist.target, test_size=0.2, random_state=42)


        model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=20, random_state=42)

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred) * 100

        return render_template('bai8.html', accuracy=accuracy)
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
