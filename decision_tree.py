#-------------------------------------------------------------------------
# AUTHOR: Jasmit Mahajan
# FILENAME: decision_tree.py
# SPECIFICATION: This program will read the contact_lens.csv file and return the decision tree using the ID3 algorithm.
# FOR: CS 4200- Assignment #1
# TIME SPENT: 10 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# For the first column of entries: Young = 1, Presbyopic = 2, and Prepresbyopic = 3
# For the second column of entries: Myope = 1, Hypermetrope = 2
# For the third column of entries: No = 1, Yes = 2
# For the fourth column of entries: Reduced = 1, Normal = 2

#--> add your Python code here
X = [
	[1,1,1,1],
	[2,1,1,2],
	[3,1,1,1],
	[3,1,1,2],
	[2,1,2,2],
	[1,1,2,2],
	[1,2,1,1],
	[3,1,2,1],
	[2,2,1,1],
	[1,1,2,1]
]

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# For the fifth column: No = 1, Yes = 2
#--> add your Python code here
Y = [1,1,1,2,2,2,1,1,1,2]

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
