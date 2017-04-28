"""
Script where is defined the main method to complete the information for MovieTweetings.

:author: Jose L. Jorro-Aragoneses
:version: 1.0
"""

import src.es.ucm.tmcd.files.CSVManager as csv
import TwitterAPI as tw

"""
Definition of all constants used in the script.
"""
USERS_FILE = '../../../../data/users.dat'


def obtain_relationships(api, users):
    """
    Function to create a new CSV where is defined the type of relationship between each couple of users.
    :param api: client used to call all API functions in Twitter.
    :type api: object
    :param users: dictionary of users where the key is the user identity and value is the user identity in Twitter.
    :type users: dict
    :return: nothing
    """
    for x in range(len(users.keys())):
        for y in range(x + 1, len(users.keys())):
            user1 = users[x]
            user2 = users[y]
            tw.getRelationship(api, user1, user2)


def main():

    # Read all users from CSV file
    users = csv.read_users(USERS_FILE)

    # Obtain client from Twitter to call all functions
    api = tw.getClient()

    # Obtain groups of friends for all users in dataset
    # createFriendsCSV(api, users)

if __name__ == '__main__':
    main()