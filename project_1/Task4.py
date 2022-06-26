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


telemarketer_dictionary = {}

# First of all, we will format the entire list into a dictionary to prep for the next step.
for call_record in calls:
    calling_number = call_record[0]

    if calling_number not in telemarketer_dictionary:
        telemarketer_dictionary[calling_number] = None

# Now, we will exclude the numbers from this dictionary that were on the receiving end of call. They are not supposed
# to receive calls.
for call_record in calls:
    called_to_number = call_record[1]

    if called_to_number in telemarketer_dictionary:
        del telemarketer_dictionary[called_to_number]

for text_record in texts:
    text_sending_number = text_record[0]
    text_receiving_number = text_record[1]

    if text_sending_number in telemarketer_dictionary:
        del telemarketer_dictionary[text_sending_number]

    if text_receiving_number in telemarketer_dictionary:
        del telemarketer_dictionary[text_receiving_number]


print('These numbers could be telemarketers: ')

for number in sorted(telemarketer_dictionary.keys()):
    print(number)
