"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Assumptions.
# 1. The call we will process here will be in September 2016. Everything else will be auto-ignored.
# 2. We will look at both calling and called to numbers, build a hashmap using dicitonary and process it find out max time.


number_to_time_spent_map = {}
longest_call_record = {
    'number': None,
    'seconds': None
}


def is_call_in_sep_2016(date_time_string):
    return '9-2016' in date_time_string


def add_record_in_dict(number, time):
    if number in number_to_time_spent_map:
        number_to_time_spent_map[number] += time
    else:
        number_to_time_spent_map[number] = time


for call_record in calls:
    calling_number = call_record[0]
    called_to_number = call_record[1]
    date_time = call_record[2]

    if is_call_in_sep_2016(date_time):
        # we are going to perform a str -> int conversion so we should better be sure we need it.
        # that's why calling it inside the if condition.
        time_spent = int(call_record[3])

        add_record_in_dict(calling_number, time_spent)
        add_record_in_dict(called_to_number, time_spent)

for number, time_in_seconds in number_to_time_spent_map.items():
    if longest_call_record['seconds'] is None or longest_call_record['seconds'] < time_in_seconds:
        longest_call_record['number'] = number
        longest_call_record['seconds'] = time_in_seconds


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_call_record['number'], longest_call_record['seconds']))
