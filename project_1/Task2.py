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

longest_call_record = None

for call_record in calls:
    call_record[3] = int(call_record[3])

    if longest_call_record is None or longest_call_record[3] < call_record[3]:
        longest_call_record = call_record

print("{} spent the longest time, {} seconds, on the phone during {}".format(longest_call_record[1], longest_call_record[3], longest_call_record[2]))
