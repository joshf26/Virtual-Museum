import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self):
        pass

        # TODO: Get topics and cache
        self.topics = {}
        self.images = {}
        self.exhibit_name = []

    def request(self, path):
        """ Returns a BeautifulSoup of the specified path. """

        return BeautifulSoup(requests.get('https://kids.kiddle.co/{}'.format(path)).text, 'html.parser')
    #elizabeth
    def get_topics(self):
        return self.topics
    
    def get_images_captions(self):
        #return a dictionary of image url : caption 
        #isolate each "gallery-box" then get image and "gallery-text"
        
        return self.images
    
    def get_exhibit_name(self, topic):
        for name in self.request(topic).find_all('span', class_='mw-headline'):
            if name.get_text() != 'Images for kids' and name.get_text() != "Related pages":
                self.exhibit_name.append(name.get_text())
            # if name.has_attr('img'):
            # children = name.findChildren('img', recursive=True)
            # for child in children:
            #     print(child)
        # exhibit_name = self.request(topic).find_all('span', class_='mw-headline').get_text()
        print(*self.exhibit_name)
        
    def get_text(self):
        pass

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
