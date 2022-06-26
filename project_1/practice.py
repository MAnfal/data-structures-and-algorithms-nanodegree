import re

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def is_bangalore_area_code(phone_number):
    # we wanna make sure that this substring is in the start and not anywhere else.
    return phone_number[:5] == '(080)'


def is_telemarketer_number(phone_number):
    return '(' not in phone_number and \
           ')' not in phone_number and \
           ' ' not in phone_number and \
           phone_number[:3] == '140'


def is_fixed_line_number(phone_number):
    # We need to check whether the number starts with a bracket followed by a 0.
    return phone_number[:2] == '(0'


def extract_fixed_line_area_code(phone_number):
    search_results = re.search('^\((.*)\)', phone_number)

    return search_results.group(1)


def is_mobile_number(phone_number):
    return '(' not in phone_number and \
           ')' not in phone_number and \
           ' ' in phone_number and \
           phone_number[0] in ['7', '8', '9']


# Area code list.
area_code_list = []
calls_made_to_fixed_lines_in_bangalore = 0

for call_record in calls:
    calling_number = call_record[0]
    called_to_number = call_record[1]

    if is_bangalore_area_code(calling_number):
        if is_bangalore_area_code(called_to_number):
            calls_made_to_fixed_lines_in_bangalore += 1

        if is_fixed_line_number(called_to_number):
            area_code_list.append(extract_fixed_line_area_code(called_to_number))
        elif is_mobile_number(called_to_number):
            area_code_list.append(called_to_number[:4])
        elif is_telemarketer_number(called_to_number):
            area_code_list.append('140')

print('The numbers called by people in Bangalore have codes:')

# In order to try to avoid introducing a new variable to hold values of set because we will then need
# an un-altered list for calculating percentage, I am doing both sorted and set inline now.
for area_code in sorted(set(area_code_list)):
    print(area_code)

print(
    '\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'
    .format((calls_made_to_fixed_lines_in_bangalore / len(area_code_list) * 100))
)
