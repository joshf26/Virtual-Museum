from bottle import route, run
from bs4 import BeautifulSoup

from scraper import Scraper


@route('/topics')
def topics():
    return scraper.get_topics()


@route('/museum/<topic>')
def museum(topic):
    return scraper.get_museum(topic)


if __name__ == '__main__':
    scraper = Scraper()

    x = scraper.request('').select_one('#mw-content-text').select('a')
    print(*[y.text for y in x])

    # run(host='localhost', port=8080)
