from bottle import route, run


@route('/topics')
def topics():
    return {
        'topic 1': 'image url for topic 1',
        'topic 2': 'image url for topic 1',
        'topic 3': 'image url for topic 1',
    }


@route('/museum/<topic>')
def museum(topic):
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


if __name__ == '__main__':
    run(host='localhost', port=8080)
