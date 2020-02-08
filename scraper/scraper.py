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
            elif topic['href'] == '/Organism': imageURL = '/images/thumb/1/14/Animal_diversity.png/300px-Animal_diversity.png'
            elif topic['href'] == '/Anatomy': imageURL = '/images/thumb/d/d5/Lateral_head_anatomy_detail.jpg/300px-Lateral_head_anatomy_detail.jpg'
            elif topic['href'] == '/Medicine': imageURL = '/images/thumb/0/08/Surgeons_at_Work.jpg/300px-Surgeons_at_Work.jpg'
            elif topic['href'] == '/Chemistry': imageURL = '/images/thumb/d/d8/Atom_diagram.png/300px-Atom_diagram.png'
            elif topic['href'] == '/Avalanche': imageURL = 'images/thumb/7/7e/Fourpeaked-fumaroles-cyrus-read1.JPG/300px-Fourpeaked-fumaroles-cyrus-read1.JPG'
            elif topic['href'] == '/Physics': imageURL = '/images/thumb/9/9a/CollageFisica.jpg/300px-CollageFisica.jpg'
            elif topic['href'] == '/Measurement': imageURL = '/images/thumb/8/82/Measuring_Tape_Inch%2BCM.jpg/300px-Measuring_Tape_Inch%2BCM.jpg'
            elif topic['href'] == '/Calendar': imageURL = '/images/thumb/7/7b/Petaluma_and_Santa_Rosa_Railroad_Co._Calendar.jpg/321px-Petaluma_and_Santa_Rosa_Railroad_Co._Calendar.jpg'
            elif topic['href'] == '/Food': imageURL = '/images/thumb/c/c5/Foods.jpg/200px-Foods.jpg'
            elif topic['href'] == '/Beer': imageURL = '/images/thumb/d/d7/Lager_beer_in_glass.jpg/300px-Lager_beer_in_glass.jpg'
            elif topic['href'] == '/Mathematics': imageURL = '/images/thumb/2/21/Euclid.jpg/300px-Euclid.jpg'
            elif topic['href'] == '/Technology': imageURL = '/images/thumb/4/45/Leonardo-Robot3.jpg/300px-Leonardo-Robot3.jpg'
            elif topic['href'] == '/Communication': imageURL = '/images/b/b1/Rudy_Giuliani_speaking.jpg'
            elif topic['href'] == '/Electronics': imageURL = '/images/thumb/d/d7/Desktop_computer_clipart_-_Yellow_theme.svg/300px-Desktop_computer_clipart_-_Yellow_theme.svg.png'
            elif topic['href'] == '/Renewable_energy': imageURL = '/images/thumb/b/bb/Alternative_Energies.jpg/250px-Alternative_Energies.jpg'
            elif topic['href'] == '/Glass': imageURL = '/images/thumb/a/a4/Glass-Ball.jpg/300px-Glass-Ball.jpg'
            elif topic['href'] == '/Transport': imageURL = '/images/thumb/7/76/Incheon_International_Airport.jpg/600px-Incheon_International_Airport.jpg'
            elif topic['href'] == '/Culture': imageURL = '/images/thumb/a/ab/Chemin_montant_dans_les_hautes_herbes_-_Pierre_Auguste_Renoir.jpg/300px-Chemin_montant_dans_les_hautes_herbes_-_Pierre_Auguste_Renoir.jpg'
            elif topic['href'] == '/Architecture': imageURL = 'src="/images/thumb/1/15/Petersdom_von_Engelsburg_gesehen.jpg/300px-Petersdom_von_Engelsburg_gesehen.jpg"'
            elif topic['href'] == '/Film': imageURL = '/images/c/c4/Fox_movietone_2.jpg'
            elif topic['href'] == '/Music': imageURL = '/images/thumb/5/5d/Elvis_Presley_first_national_television_appearance_1956.jpg/300px-Elvis_Presley_first_national_television_appearance_1956.jpg'
            elif topic['href'] == '/Game': imageURL = '/images/thumb/2/2a/UEFA-Women%27s_Cup_Final_2005_at_Potsdam_1.jpg/300px-UEFA-Women%27s_Cup_Final_2005_at_Potsdam_1.jpg'
            elif topic['href'] == '/History': imageURL = '/images/thumb/4/4e/History-Dielman-Highsmith.jpeg/971px-History-Dielman-Highsmith.jpeg'
            elif topic['href'] == '/Prehistory': imageURL = 'https://kids.kiddle.co/images/9/99/Great_Sphinx_of_Giza_2.jpg'
            elif topic['href'] == '/': imageURL =
            elif topic['href'] == '/': imageURL =
            elif topic['href'] == '/': imageURL =
            elif topic['href'] == '/': imageURL =
            elif topic['href'] == '/': imageURL =
            elif topic['href'] == '/': imageURL =
            elif topic['href'] == '/': imageURL =

            self.topics.update({topic['href'] : imageURL})
            # print (topic['href'])
            # print (self.topics[topic['href']])
        #print (self.topics)
        return self.topics

    def get_exhibit_name(self, topic):
        for name in self.request(topic).select('h2 mw-headline'):#self.request(topic).find_all('span', class_='mw-headline', tag = 'h2'):
            if name.get_text() != 'Images for kids' and name.get_text() != "Related pages":
                #if name.find("img") == None:
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
        self.get_exhibit_name(topic)
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
