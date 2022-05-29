from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

iris = datasets.load_iris()
classifier = RandomForestClassifier()
classifier.fit(iris.data, iris.target)

joblib.dump(classifier, 'model.joblib')