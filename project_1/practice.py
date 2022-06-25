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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Assumptions
# 1. Number is a telemarketer number so it'll start with 140, have no () and no spaces.
# 2. It won't send/receive texts so we only have to look in the calls CSV.
# 3. If in the calls CSV we found out that a certain number had a call made to but was telemarketer, remove that from our results.


telemarketer_dictionary = {}


def is_telemarketer_number(phone_number):
    return '(' not in phone_number and \
           ')' not in phone_number and \
           ' ' not in phone_number and \
           phone_number[:3] == '140'


for call_record in calls:
    calling_number = call_record[0]

    if is_telemarketer_number(calling_number) and calling_number not in telemarketer_dictionary:
        telemarketer_dictionary[calling_number] = 1

for call_record in calls:
    called_to_number = call_record[1]

    if is_telemarketer_number(called_to_number) and called_to_number in telemarketer_dictionary:
        del telemarketer_dictionary[called_to_number]

print('These numbers could be telemarketers: ')

for number in sorted(telemarketer_dictionary.keys()):
    print(number)
