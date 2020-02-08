import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self):
        pass

        # TODO: Get topics and cache
        self.topics = {}
        self.images = {}
        self.exhibit = []

    def request(self, path):
        """ Returns a BeautifulSoup of the specified path. """

        return BeautifulSoup(requests.get('https://kids.kiddle.co/{}'.format(path)).text, 'html.parser')

    def get_topics(self):
        # topics format    topic url : image url
        names = self.request('').select_one('#mw-content-text').select('ol a')
        # science to astronomy
        image_url = '/images/thumb/3/3c/Size_planets_comparison.jpg/380px-Size_planets_comparison.jpg'
        for topic in names:
            if topic['href'] == '/Biology': image_url = '/images/thumb/3/32/EscherichiaColi_NIAID.jpg/535px-EscherichiaColi_NIAID.jpg'
            elif topic['href'] == '/Organism': image_url = '/images/thumb/1/14/Animal_diversity.png/300px-Animal_diversity.png'
            elif topic['href'] == '/Anatomy': image_url = '/images/thumb/d/d5/Lateral_head_anatomy_detail.jpg/300px-Lateral_head_anatomy_detail.jpg'
            elif topic['href'] == '/Medicine': image_url = '/images/thumb/0/08/Surgeons_at_Work.jpg/300px-Surgeons_at_Work.jpg'
            elif topic['href'] == '/Chemistry': image_url = '/images/thumb/d/d8/Atom_diagram.png/300px-Atom_diagram.png'
            elif topic['href'] == '/Avalanche': image_url = 'images/thumb/7/7e/Fourpeaked-fumaroles-cyrus-read1.JPG/300px-Fourpeaked-fumaroles-cyrus-read1.JPG'
            elif topic['href'] == '/Physics': image_url = '/images/thumb/9/9a/CollageFisica.jpg/300px-CollageFisica.jpg'
            elif topic['href'] == '/Measurement': image_url = '/images/thumb/8/82/Measuring_Tape_Inch%2BCM.jpg/300px-Measuring_Tape_Inch%2BCM.jpg'
            elif topic['href'] == '/Calendar': image_url = '/images/thumb/7/7b/Petaluma_and_Santa_Rosa_Railroad_Co._Calendar.jpg/321px-Petaluma_and_Santa_Rosa_Railroad_Co._Calendar.jpg'
            elif topic['href'] == '/Food': image_url = '/images/thumb/c/c5/Foods.jpg/200px-Foods.jpg'
            elif topic['href'] == '/Beer': image_url = '/images/thumb/d/d7/Lager_beer_in_glass.jpg/300px-Lager_beer_in_glass.jpg'
            elif topic['href'] == '/Mathematics': image_url = '/images/thumb/2/21/Euclid.jpg/300px-Euclid.jpg'
            elif topic['href'] == '/Technology': image_url = '/images/thumb/4/45/Leonardo-Robot3.jpg/300px-Leonardo-Robot3.jpg'
            elif topic['href'] == '/Communication': image_url = '/images/b/b1/Rudy_Giuliani_speaking.jpg'
            elif topic['href'] == '/Electronics': image_url = '/images/thumb/d/d7/Desktop_computer_clipart_-_Yellow_theme.svg/300px-Desktop_computer_clipart_-_Yellow_theme.svg.png'
            elif topic['href'] == '/Renewable_energy': image_url = '/images/thumb/b/bb/Alternative_Energies.jpg/250px-Alternative_Energies.jpg'
            elif topic['href'] == '/Glass': image_url = '/images/thumb/a/a4/Glass-Ball.jpg/300px-Glass-Ball.jpg'
            elif topic['href'] == '/Transport': image_url = '/images/thumb/7/76/Incheon_International_Airport.jpg/600px-Incheon_International_Airport.jpg'
            elif topic['href'] == '/Culture': image_url = '/images/thumb/a/ab/Chemin_montant_dans_les_hautes_herbes_-_Pierre_Auguste_Renoir.jpg/300px-Chemin_montant_dans_les_hautes_herbes_-_Pierre_Auguste_Renoir.jpg'
            elif topic['href'] == '/Architecture': image_url = 'src="/images/thumb/1/15/Petersdom_von_Engelsburg_gesehen.jpg/300px-Petersdom_von_Engelsburg_gesehen.jpg"'
            elif topic['href'] == '/Film': image_url = '/images/c/c4/Fox_movietone_2.jpg'
            elif topic['href'] == '/Music': image_url = '/images/thumb/5/5d/Elvis_Presley_first_national_television_appearance_1956.jpg/300px-Elvis_Presley_first_national_television_appearance_1956.jpg'
            elif topic['href'] == '/Game': image_url = '/images/thumb/2/2a/UEFA-Women%27s_Cup_Final_2005_at_Potsdam_1.jpg/300px-UEFA-Women%27s_Cup_Final_2005_at_Potsdam_1.jpg'
            elif topic['href'] == '/History': image_url = '/images/thumb/4/4e/History-Dielman-Highsmith.jpeg/971px-History-Dielman-Highsmith.jpeg'
            elif topic['href'] == '/Prehistory': image_url = '/images/9/99/Great_Sphinx_of_Giza_2.jpg'
            elif topic['href'] == '/Geography': image_url = '/images/thumb/1/12/World_map_2004_CIA_large_1.7m_whitespace_removed.jpg/800px-World_map_2004_CIA_large_1.7m_whitespace_removed.jpg'
            elif topic['href'] == '/Africa': image_url = '/images/thumb/0/0f/LocationAfrica.png/300px-LocationAfrica.png'
            elif topic['href'] == '/Afghanistan': image_url = '/images/thumb/1/19/Afghanistan_%28orthographic_projection%29.svg/350px-Afghanistan_%28orthographic_projection%29.svg.png'
            elif topic['href'] == '/Amsterdam': image_url = '/images/thumb/6/6d/Flag_of_Amsterdam.svg/180px-Flag_of_Amsterdam.svg.png 1.5x, /images/thumb/6/6d/Flag_of_Amsterdam.svg/240px-Flag_of_Amsterdam.svg.png 2x'
            elif topic['href'] == '/Amazon_River': image_url = '/images/thumb/6/6f/Mouths_of_amazon_geocover_1990.png/300px-Mouths_of_amazon_geocover_1990.png'
            elif topic['href'] == '/Alps': image_url = '/images/thumb/0/0d/L%C3%BCnersee_vom_Saulakopf_1.JPG/200px-L%C3%BCnersee_vom_Saulakopf_1.JPG'
            elif topic['href'] == '/Sarah_Bernhardt': image_url = '/images/thumb/a/a8/Sarah_Bernhardt_-_Project_Gutenberg_eText_19955.jpg/200px-Sarah_Bernhardt_-_Project_Gutenberg_eText_19955.jpg'
            elif topic['href'] == '/Louis_Armstrong': image_url = '/images/thumb/6/6f/Beethoven.jpg/300px-Beethoven.jpg'
            elif topic['href'] == '/Roald_Amundsen': image_url = '/images/thumb/0/06/CristobalColon.jpg/300px-CristobalColon.jpg'
            elif topic['href'] == '/Archimedes': image_url = '/images/thumb/2/2b/Archimedes_%28Idealportrait%29.jpg/541px-Archimedes_%28Idealportrait%29.jpg'
            elif topic['href'] == '/Aristotle': image_url = '/images/thumb/a/a4/Socrates_Louvre.jpg/300px-Socrates_Louvre.jpg'
            elif topic['href'] == '/Behavior': image_url = '/images/thumb/b/b4/Sixteen_faces_expressing_the_human_passions._Wellcome_L0068375_%28cropped%29.jpg/180px-Sixteen_faces_expressing_the_human_passions._Wellcome_L0068375_%28cropped%29.jpg'
            elif topic['href'] == '/God': image_url = '/images/thumb/5/50/Brahma_Halebid.jpg/334px-Brahma_Halebid.jpg'
            elif topic['href'] == '/Society': image_url = '/images/thumb/f/f8/Detail_of_Les_tres_riches_heures_-_March.jpg/699px-Detail_of_Les_tres_riches_heures_-_March.jpg'
            elif topic['href'] == '/Family': image_url = '/images/thumb/e/e5/Paus_family_portrait_NFB-18645.jpg/300px-Paus_family_portrait_NFB-18645.jpg'
            elif topic['href'] == '/Language': image_url = '/images/thumb/5/53/Novi_Sad_mayor_office.jpg/300px-Novi_Sad_mayor_office.jpg'

            self.topics.update({topic['href'][1:] : 'https://kids.kiddle.co' + image_url})
        
        # for key in self.topics: print (key, ': \n', self.topics[key])
        
        return self.topics

    def get_exhibit(self, topic):
        exhibit_dict = {}
        prev_exhibit = ''
        img_list = []
        cpt_list = []
        text_list = []
        image = ''
        imgcpt_indx = 0
        # tags for images and headlines
        for html in self.request(topic).select_one('#mw-content-text').find_all(['div','h2','h3']):
            # if there's a headline, will always find the first headline as true
            if html.find(class_ = 'mw-headline'):
                # store exhibit if first exhibit or prior exhibit had no images
                if len(img_list) == 0:
                    prev_exhibit = html.find(class_ = 'mw-headline').text
                    body = html.find(class_ = 'mw-headline').parent.find_next_sibling('p')
                    if body is not None:
                        print(html.find(class_ = 'mw-headline').parent.find_next_sibling('p').text)

                else:
                    exhibit_dict["exhibit_name"] = prev_exhibit
                    exhibit_dict["imageUrl"] = img_list
                    exhibit_dict["caption"] = cpt_list
                    self.exhibit.append(exhibit_dict)

                    exhibit_dict = {}
                    img_list = []
                    cpt_list = []
                    text_list = []
                    #  store exhibit after adding previous
                    prev_exhibit = html.find(class_ = 'mw-headline').text
            # check if there's a heading to be stored, therefore images at the intro are not added
            # can be changed later, maybe the exhibit name can be the article title or smthng
            if html.find('img') and prev_exhibit != '': 
                image = html.find('img')['src']
                # idk images are repeated, didn't figure out why
                image = 'https://kids.kiddle.co' + image
                if image not in img_list:
                    img_list.append(image)

                    if prev_exhibit == 'Images for kids':
                        caption = html.find('img').parent.parent.parent.find_next_sibling('div')
                        if caption is not None:
                            cpt_list.append(caption.find('p').text.strip())
                        else:
                            cpt_list.append("")
                    
                    # Not in the `Images for kids` exhibit
                    else:
                        caption = html.find('img').parent.find_next_sibling('div', 'thumbcaption')
                        if caption is not None:
                            cpt_list.append(caption.text.strip())
                        else:
                            cpt_list.append("")


        if len(img_list) > 0:
            # add the last exhibit if there are images....this also includes Images for Kids
            exhibit_dict["exhibit_name"] = prev_exhibit
            exhibit_dict["imageUrl"] = img_list
            exhibit_dict["caption"] = cpt_list
            self.exhibit.append(exhibit_dict)
            exhibit_dict = {}

        # for i in self.exhibit:
        #     for key in i:
        #         print(key, ' : \n',i[key], '\n')
        return self.exhibit
    
    def get_images_captions(self):
        #return a dictionary of image url : caption 
        #isolate each "gallery-box" then get image and "gallery-text"
        
        return self.images

    def get_text(self):
        pass

    def get_museum(self, topic):
        self.get_exhibit(topic)
