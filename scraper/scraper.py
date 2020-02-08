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

    def get_topics(self):
        # topics format    topic url : image url
        names = self.request('').select_one('#mw-content-text').select('ol a')
        # science to astronomy
        imageURL = '/images/thumb/3/3c/Size_planets_comparison.jpg/380px-Size_planets_comparison.jpg'
        for topic in names:
            if topic['href'] == '/Biology': imageURL = '/images/thumb/3/32/EscherichiaColi_NIAID.jpg/535px-EscherichiaColi_NIAID.jpg'
            if topic['href'] == '/Organism': imageURL = '/images/thumb/1/14/Animal_diversity.png/300px-Animal_diversity.png'
            if topic['href'] == '/Anatomy': imageURL = '/images/thumb/d/d5/Lateral_head_anatomy_detail.jpg/300px-Lateral_head_anatomy_detail.jpg'
            if topic['href'] == '/Medicine': imageURL = '/images/thumb/0/08/Surgeons_at_Work.jpg/300px-Surgeons_at_Work.jpg'
            if topic['href'] == '/Chemistry': imageURL = '/images/thumb/d/d8/Atom_diagram.png/300px-Atom_diagram.png'
            if topic['href'] == '/Avalanche': imageURL = 'images/thumb/7/7e/Fourpeaked-fumaroles-cyrus-read1.JPG/300px-Fourpeaked-fumaroles-cyrus-read1.JPG'
            if topic['href'] == '/Physics': imageURL = '/images/thumb/9/9a/CollageFisica.jpg/300px-CollageFisica.jpg'
            if topic['href'] == '/Measurement': imageURL = '/images/thumb/8/82/Measuring_Tape_Inch%2BCM.jpg/300px-Measuring_Tape_Inch%2BCM.jpg'
            if topic['href'] == '/Calendar': imageURL = '/images/thumb/7/7b/Petaluma_and_Santa_Rosa_Railroad_Co._Calendar.jpg/321px-Petaluma_and_Santa_Rosa_Railroad_Co._Calendar.jpg'
            if topic['href'] == '/Food': imageURL = '/images/thumb/c/c5/Foods.jpg/200px-Foods.jpg'
            if topic['href'] == '/Beer': imageURL = '/images/thumb/d/d7/Lager_beer_in_glass.jpg/300px-Lager_beer_in_glass.jpg'
            if topic['href'] == '/Mathematics': imageURL = '/images/thumb/2/21/Euclid.jpg/300px-Euclid.jpg'
            if topic['href'] == '/Technology': imageURL = '/images/thumb/4/45/Leonardo-Robot3.jpg/300px-Leonardo-Robot3.jpg'
            if topic['href'] == '/Communication': imageURL = '/images/b/b1/Rudy_Giuliani_speaking.jpg'
            if topic['href'] == '/': imageURL =
            if topic['href'] == '/': imageURL =
            if topic['href'] == '/': imageURL =

            self.topics.update({topic['href'] : imageURL})
            # print (topic['href'])
            # print (self.topics[topic['href']])
        #print (self.topics)
        return self.topics

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
    
    def get_images_captions(self):
        #return a dictionary of image url : caption 
        #isolate each "gallery-box" then get image and "gallery-text"
        
        return self.images

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
