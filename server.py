import giphy_client
import flask
from json import loads
from os import getenv

app = flask.Flask(__name__)
api_instance = giphy_client.DefaultApi()
api_key = getenv('GIPHY_TOKEN')


limit = 100
lang = 'en' 

@app.route('/', methods=['GET'])
def home():
    return(flask.render_template('index.html'))

@app.route('/search/<query>', methods=['GET'])
def search_results(query):
    res = api_instance.gifs_search_get(api_key, query, limit=limit, lang=lang).to_dict()['data']
    body = '<style>' + open('static/style.css').read() + '</style>'
    for gif in res:
        print('hi')
        url = gif['images']['downsized']['url']
        body = body + '<a href="' + url + '"><img src="' + url + '"></a>'
        print(body)
    return(body)
