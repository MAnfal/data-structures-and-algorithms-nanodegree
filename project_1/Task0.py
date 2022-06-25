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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# This is text record information.
first_record_sending_number, first_record_receiving_number, first_record_timestamp = texts[0]

# This is call record information.
last_record_calling_number, last_record_answering_number, last_record_call_timestamp, last_record_total_call_duration = calls[len(calls) - 1]

print(
    "First record of texts, {} texts {} at time {}".format(
        first_record_sending_number,
        first_record_receiving_number,
        first_record_timestamp
    )
)

print(
    "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
        last_record_calling_number,
        last_record_answering_number,
        last_record_call_timestamp,
        last_record_total_call_duration
    )
)