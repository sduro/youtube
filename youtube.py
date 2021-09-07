'''
Pagina web para descargar mp3
youtube.json ->fichero de configuracion
'''
import json
import os
from bottle import run, get, post, request, template, route,static_file, view # or route
from download import download_clip

with open("youtube.json", "r") as jsonfile:
    data = json.load(jsonfile) # Reading the file
    jsonfile.close()

def config():
    with open("youtube.json", "w") as jsonfile:
        json.dump(data,jsonfile,ensure_ascii=False) # writing the file
        jsonfile.close()

@route("/static/css/<filename>")
def server_static(filename):
	return static_file(filename,root="./static/css")

@get('/login') # or @route('/login')
def login():
    actual_path = os.getcwd()
    return template('static/index.html',path=actual_path,download_path=data['configuration']['download_dir'])
    
@post('/login') # or @route('/login', method='POST')
def do_login():
    yield "Downloading..."
    URL = request.forms.get('URL')
    downloadoption = request.forms.get('downloadoption')
    download_clip(URL,downloadoption,data)
    yield "Done"
    return template('/static/index.html')

@route('/config')
def configuration():
    return template('static/configuration.html')

@post('/config')
def configuration_save():
    new_path = request.forms.get('new_path')
    print (new_path)
    data['configuration']['download_dir'] = new_path
    return template('static/configuration.html')

run(host='localhost', port=8088, debug=True)