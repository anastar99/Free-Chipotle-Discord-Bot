chipotle_url = 'https://twitter.com/ChipotleTweets'
import requests


class Shovel:

    def __init__(self):
        pass

    def newPost(self):
        pass
    def monitor(self):
        pass

    def checkPost(self):
        pass

    def go(self):

        r = requests.get(chipotle_url)
        print(r.text)
        return # embed


if __name__ == "__main__":
    Shovel().go()