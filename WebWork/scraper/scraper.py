import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self):
        pass

        # TODO: Get topics and cache
        self.topics = {}

    def request(self, path):
        """ Returns a BeautifulSoup of the specified path. """

        return BeautifulSoup(requests.get('https://kids.kiddle.co/{}'.format(path)).text, 'html.parser')

    def get_topics(self):
        return self.topics

    def get_museum(self, topic):
        return {
            'exhibit 1': [
                {
                    'imageUrl': 'image url for exhibit 1 display 1',
                    'imageCaption': 'image caption for exhibit 1 display 1',
                    'text': 'text for exhibit 1 display 1',
                },
                {
                    'imageUrl': 'image url for exhibit 1 display 2',
                    'imageCaption': 'image caption for exhibit 1 display 2',
                    'text': 'text for exhibit 1 display 2',
                },
            ],
            'exhibit 2': [
                {
                    'imageUrl': 'image url for exhibit 1',
                    'imageCaption': 'image caption for exhibit 1',
                    'text': 'text for exhibit 1',
                },
            ],
        }
