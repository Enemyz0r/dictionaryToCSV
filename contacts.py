# -*- coding: utf-8 -*-
# python 3.x
# Create a csv file from dictionary
# File format: name, phone number
# Usage: dicttocsv.py
# eg.(in bash): python3 dicttocsv.py
######################################

import csv

Flag = True # flag for program loop

while Flag:
    contact = input("Please enter name and phone number (eg. John 555-789134): ")
    dictionary = dict(x.split() for x in contact.splitlines())
    choice = input("Would you like to further add numbers?  (y/n)")
    with open('dicttocsv.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in dictionary.items():
                writer.writerow([key, value])

    if choice == 'y':
        Flag = True
    else:
        Flag = False
