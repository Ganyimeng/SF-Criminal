# coding: utf-8
import numpy as np
import scipy as sp
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from pandas import read_csv

data = read_csv(u'..\\train.csv')
print data['Dates'][:100]

# data = []
# labels = []


# y[labels == 'fat'] = 1

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# clf = tree.DecisionTreeClassifier(criterion='entropy')
# print(clf)
# clf.fit(x_train, y_train)

# with open("tree.dot", 'w') as f:
#     f = tree.export_graphviz(clf, out_file=f)

# print(clf.feature_importances_)

# answer = clf.predict(x_train)
# print(x_train)
# print(answer)
# print(y_train)
# print(np.mean(answer == y_train))

# precision, recall, thresholds = precision_recall_curve(
#     y_train, clf.predict(x_train))
# answer = clf.predict_proba(x)[:, 1]
# print(classification_report(y, answer, target_names=['thin', 'fat']))
