"""
Module where is implemented all functions created to communicate with Twitter API.

:author: Jose L. Jorro-Aragoneses
:version: 1.0
"""
import json
from StdSuites.Type_Names_Suite import null

import oauth2 as oauth

"""
Keys to access to Twitter API.
"""
CONSUMER_KEY = "o2KxMD0ubvwOGlhdPv2T7TxZ7"
CONSUMER_SECRET = "1rQ1C9FYKLBRz2zGgxv4zAmIjl2FIHl17pR4drkqQwteehbxDG"
ACCESS_TOKEN = "808788660032303106-CPfSQKgfvf7mCAgaeVGeNxzUR4sgZ9L"
ACCESS_TOKEN_SECRET = "CcdVnR8nE1Rn0tqz1qINyfHZfcUVKpKeKHR1qhLIQxUEj"


def getClient():
    """
    Function that create the client to execute the API calls for Twitter.
    :return: client object needed to execute all Twitter API functions.
    """

    auth = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    access_token = oauth.Token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    client = oauth.Client(auth, access_token)

    return client

def getRelationship(client, userId1, userId2):
    """
    Funtion that return the Twitter relationship between 2 users.
    :param client: Twitter client to execute the API function.
    :param userId1: Twitter identity of the first users.
    :param userId2: Twitter identity of the second users.
    :return: str where is Twitter identity of user 1, Twitter identity of user 2, boolean to check if user1 follow 
                user2 and a boolean to check if user2 follow user1. Example: 1234::4321::True::False. If one of these
                users doesn't exists in Twitter, the functions return null.
    """

    friends_request = "https://api.twitter.com/1.1/friendships/show.json?source_id=" + str(userId1) + "&target_id=" + str(userId2);
    response, data = client.request(friends_request)

    object = json.loads(data)

    if 'relationship' in object.keys():
        return str(userId1) + "::" + str(userId2) + "::" + str(object['relationship']['source']['following']) + "::" + str(object['relationship']['source']['followed_by'])
    else:
        raise Exception("Twitter doesn't return a relationship.")