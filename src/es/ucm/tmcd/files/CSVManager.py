'''
Script where is defined all functions to manager the MovieTweetings files (CSV) and create new CSV files.
:author: Jose L. Jorro-Aragoneses
:version: 1.0
'''
import csv;


def read_users(path):
    """
    Function that read all users used in MovieTweetings dataset.
    :param path: location where is saved users dataset in the system.
    :type path: str
    :return: dict where the key is the user identity in the dataset and value is the Twitter identity of this user.
    """
    result = {}

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            usr = row[0].split('::')
            result[usr[0]] = usr[1]

    return result
