import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self):
        pass

        # TODO: Get topics and cache
        self.topics = {}
        self.images = {}

    def request(self, path):
        """ Returns a BeautifulSoup of the specified path. """

        return BeautifulSoup(requests.get('https://kids.kiddle.co/{}'.format(path)).text, 'html.parser')
    #elizabeth
    def get_topics(self):
        return self.topics
    
    #tiffany
    def get_images_captions(self):
        #return a dictionary of image url : caption 
        #isolate each "gallery-box" then get image and "gallery-text"
        return self.images
    
    def get_exhibit_name(self):
    
    def get_text(self):
    

    def get_museum(self, topic):
        #fill images
        self.get_images_captions()
        #loop through self.images, divide by 4 for now -> 0-3 images as base cases
        #if 0-1 images -> 1 exhibit
        return {
            # GET mw-headline //maybe later if you we want exhibition titles 
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
