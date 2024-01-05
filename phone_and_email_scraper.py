# phone_and_email_scraper.py

#! /usr/bin/python3

import re
import pyperclip


# Create a phone number regex
phone_num_regex = re.compile(r'''
# Formats: 415-550-0000, 550-0000, (415) 550-0000, 555-0000 ext 12345, ext. 12345, x12345
(                            
((\d\d\d)|(\(\d\d\d\)))?       # area code (optional)
(\s|-)                         # first seperator (space or -)
\d\d\d                         # next three digits
(\s|-)                         # second seperator (space or -)
(\d\d\d\d)                     # last four digits
(((ext(\.)?\s) |x)             # extension signifier (optional)
(\d{2,5}))?                    # extension number (optional)
)
''', re.VERBOSE)


# Create an email address regex
email_address_regex = re.compile(r'''
(
# Format: some12_.+thing@some12_.+domain.ending
                                 
[a-z0-9_.+]+                   # username
@                              # @ symbol
[a-z0-9_.+]+                   # domain name
)
''', re.VERBOSE | re.IGNORECASE)


# Get the text off the clipboard
text = pyperclip.paste()


# Extract email and phone number information
phone_number_groups = phone_num_regex.findall(text)
email_address_groups = email_address_regex.findall(text)

full_phone_numbers = []
full_email_addresses = []

print('Extracted Phone Numbers: ')
for number in phone_number_groups:
    print('[+] ' + str(number[0]))
    full_phone_numbers.append(number[0])
print()
print()
print('Extracted Email Addresses: ')
for address in email_address_groups:
    print('[+] ' + str(address))
    full_email_addresses.append(address)

results = open('results.txt', 'w')
results.write('Phone Numbers\n')
for number in full_phone_numbers:
    results.write(str(number) + '\n')
results.write('\n')
results.write('Email Addresses\n')
for address in full_email_addresses:
    results.write(str(address) + '\n')
results.close()

print()
print('The results of the program have been written to the \
file titled results.txt in the current directory')