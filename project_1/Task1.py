"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Assumption here is that we want to know total number of unique telephone numbers in both text and calls.
# The assumption will also include all the numbers in both sending and receiving ends.

telephone_number_dict = {}


def populate_dict(data_list):
    for row in data_list:
        if row[0] not in telephone_number_dict:
            telephone_number_dict[row[0]] = 1

        if row[1] not in telephone_number_dict:
            telephone_number_dict[row[1]] = 1


populate_dict(texts)
populate_dict(calls)

print("There are {} different telephone numbers in the records.".format(len(telephone_number_dict)))
