'''
Pagina web para descargar mp3
config.json ->fichero de configuracion
'''
import json
import os
import platform
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
from bottle import run, get, post, request, template, route,static_file,redirect, view # or route
from download import download_clip
from download import search_and_dowload

with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile) # Reading the JSON file
    jsonfile.close()

def config():
    with open("config.json", "w") as jsonfile:
        json.dump(data,jsonfile,ensure_ascii=False) # writing the JSON file with new configuration
        jsonfile.close()



@route("/static/css/<filename>")
def server_static(filename):
	return static_file(filename,root="./static/css") #command to access at CSS files

@get('/youtube') # or @route('/login')
def login():
    actual_path = os.getcwd()
    directorio = data['configuration'][platform.system()] #get the actual SO
    return template('static/youtube.html',path=actual_path,download_path=directorio)

@route("/static/css/<filename>")
def server_static(filename):
	return static_file(filename,root="./static/css")

@post('/youtube') # or @route('/login', method='POST')
def do_login():
    #yield "Downloading..."
    URL = request.forms.get('URL')
    downloadoption = request.forms.get('downloadoption')
    download_clip(URL,downloadoption,data)
    #yield "Done"
    return template('static/main.html',path="done")

####################
# Spotify function #
####################

@route('/spotify')
def spotify():
    actual_path = os.getcwd()
    directorio = data['configuration'][platform.system()]
    return template('static/spotify.html',path=actual_path,download_path=directorio)
    

@post('/spotify') # or @route('/login', method='POST')
def spotify_do():
    #https://open.spotify.com/track/2WyNqDHLRJLzJuidCsO1Ey?si=452e58a9890c4bf0
    #To access authorised Spotify data
    client_id = '6bbbe4ed36e74435bb87f04904cb0d31'
    client_secret = 'cfdc80fa279f4d8cbf2a24b161293910'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
    downloadoption = request.forms.get('URL')
    # spotify object to access API
    #result =sp.track("https://open.spotify.com/track/2WyNqDHLRJLzJuidCsO1Ey?si=73c4738c9c2647f1")
    result = sp.track(downloadoption)
    print (result['artists'][0]['name'], result['name'])
    string_to_search=result['artists'][0]['name']+' '+ result['name']
    
    #downloadoption = request.forms.get('downloadoption')
    search_and_dowload(string_to_search,data) #url=url,dowloadoption=

    directorio = data['configuration'][platform.system()]
    #return template('static/index.html',path=os.getcwd(),download_path=directorio)
    return template('static/main.html',path="done")

####################
# Config  function #
####################

@route('/config')
def configuration():
    directorio = data['configuration'][platform.system()]
    return template('static/configuration.html',path=directorio)

@post('/config')
def configuration_save():
    '''Guardar el path de la pagina 
    configuracion a la variable de json'''

    new_path = request.forms.get('new_path')
    data['configuration'][platform.system()]= new_path
    return template('static/configuration.html',path=new_path)

@route('/')
def menu():
    return template('static/main.html',path="main")

run(host='localhost', port=8088, debug=True)