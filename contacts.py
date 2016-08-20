import csv

Flag = True

while Flag:
    contact = input("Introduceti Numele si numarul de telefon: ")
    dicktionary = dict(x.split() for x in contact.splitlines())
    maiDoriti = input("Mai doriti sa introduceti numere? (y/n)")
    with open('contacts.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in dicktionary.items():
                writer.writerow([key, value])

    if maiDoriti == 'y':
        Flag = True
    else:
        Flag = False

