#-------------------------------------------------------------------------
# AUTHOR: Jasmit Mahajan
# FILENAME: naive_bayes.py
# SPECIFICATION: This program will calculate using the naive-bayes algorithm
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

from sklearn.naive_bayes import GaussianNB
import csv

db = []
dbTest = []
X = []
Y = []

# reading the training data
# --> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

dict_obj = {
    "Sunny": 0,
    "Overcast": 1,
    "Rain": 2,
    "Hot": 0,
    "Mild": 1,
    "Cool": 2,
    "High": 0,
    "Normal": 1,
    "Weak": 0,
    "Strong": 1,
    "No": 0,
    "Yes": 1
}

# transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
# X =
for i in range(len(db)):
    tempArr = []
    for j in range(1, len(db[i]) - 1):
        tempArr.append(dict_obj[db[i][j]])
    X.append(tempArr)

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
# Y =
for i in range(len(db)):
    Y.append(dict_obj[db[i][len(db[i]) - 1]])

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the data in a csv file
# --> add your Python code here
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)

# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

# use your test samples to make probabilistic predictions.
# --> add your Python code here
# -->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for d in dbTest:
    tempArr.clear()
    for i in range(1, len(d) - 1):
        tempArr.append(dict_obj[d[i]])
    predict = clf.predict_proba([tempArr])[0]

    if predict[0] > 0.75:
        for i in range(len(d) - 1):
            print(d[i].ljust(15), end='')
        print("No".ljust(15) + str(predict[0]))

    if predict[1] > 0.75:
        for i in range(len(d) - 1):
            print(d[i].ljust(15), end='')
        print("Yes".ljust(15) + str(predict[1]))