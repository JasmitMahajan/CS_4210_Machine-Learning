#-------------------------------------------------------------------------
# AUTHOR: Jasmit Mahajan
# FILENAME: find_s.py
# SPECIFICATION: This program will use the contact_lens.csv file to output the hypothesis of the Find-S Algorithm
# FOR: CS 4200- Assignment #1
# TIME SPENT: 1 hr 30 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
for row in db:
    if row[4] == "Yes":
        for num in range(0, len(hypothesis)):
            hypothesis[num] = row[num]
        break

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")

##--> add your Python code here
for row in db:
    if row[4] == "Yes":
        for num in range(0, len(hypothesis)):
            if hypothesis[num] != "?" and hypothesis[num] != row[num]:
                hypothesis[num] = "?"

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)