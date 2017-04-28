'''

Manager to read and write CSV files

'''

import csv;

def readUsersCSV(path):

    result = {}

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            usr = row[0].split('::')
            result[usr[0]] = usr[1]

    return result