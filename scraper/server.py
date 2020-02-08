from bottle import route, run
from json import dumps

from scraper import Scraper


@route('/topics')
def topics():
    return dumps(scraper.get_topics())


@route('/museum/<topic>')
def museum(topic):
    return dumps(scraper.get_museum(topic))


if __name__ == '__main__':
    scraper = Scraper()
    #topics()
    # museum("test")
    
    #scraper.get_exhibit('Dinosaur')
    #x = scraper.request('').select_one('#mw-content-text').select('a')
    #print(*[y.text for y in x])``

    run(host='localhost', port=8080)
