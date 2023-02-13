'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file
data = open('employee_data.csv', 'r')


# create an empty dictionary
dict = {}

# use a loop to iterate through the csv file
# check if the employee fits the search criteria

with open('employee_data.csv', 'rt') as data1:
    data2 = csv.DictReader(data1, delimiter=',', quotechar='"')
    for employee in data2:
        employee["Salary"] = float(
            employee["Salary"]) * 1.1 * float((employee["Title"] == "CSR"))
    for employee in data2:
        print("Manager Name:" + employee["First Name"] +
              employee["Last Name"] + "Current Salary:" + employee["Salary"])


print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout
