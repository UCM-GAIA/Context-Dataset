import json
import oauth2 as oauth


CONSUMER_KEY = "o2KxMD0ubvwOGlhdPv2T7TxZ7"
CONSUMER_SECRET = "1rQ1C9FYKLBRz2zGgxv4zAmIjl2FIHl17pR4drkqQwteehbxDG"
ACCESS_TOKEN = "808788660032303106-CPfSQKgfvf7mCAgaeVGeNxzUR4sgZ9L"
ACCESS_TOKEN_SECRET = "CcdVnR8nE1Rn0tqz1qINyfHZfcUVKpKeKHR1qhLIQxUEj"


def getClient():
    auth = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    access_token = oauth.Token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    client = oauth.Client(auth, access_token)
    return client

def areFollowed(client, userId1, userId2):
    friends_request = "https://api.twitter.com/1.1/friendships/show.json?source_id=" + str(userId1) + "&target_id=" + str(userId2);
    response, data = client.request(friends_request)

    object = json.loads(data)

    if 'relationship' in object.keys():
        print(str(userId1) + "::" + str(userId2) + "::" + str(object['relationship']['source']['followed_by']) + "::" + str(object['relationship']['source']['following']))
