'''
Pagina web para descargar mp3
youtube.json ->fichero de configuracion
'''
import json
import os
import platform
from bottle import run, get, post, request, template, route,static_file,redirect, view # or route
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
    sistema =platform.system()
    if sistema == 'Linux':
        directorio = data['configuration']['download_dir_linux']
    else:
        directorio = data['configuration']['download_dir_win32']
    return template('static/index.html',path=actual_path,download_path=directorio)

@route("/static/css/<filename>")
def server_static(filename):
	return static_file(filename,root="./static/css")

@post('/login') # or @route('/login', method='POST')
def do_login():
    yield "Downloading..."
    URL = request.forms.get('URL')
    downloadoption = request.forms.get('downloadoption')
    download_clip(URL,downloadoption,data)
    yield "Done"
    actual_path = os.getcwd()
    sistema =platform.system()
    if sistema == 'Linux':
        directorio = data['configuration']['download_dir_linux']
    else:
        directorio = data['configuration']['download_dir_win32']
    return "Hello World!"
    #return template('static/index.html',path=actual_path,download_path=directorio)
    
@route('/config')
def configuration():
    return template('static/configuration.html')

@post('/config')
def configuration_save():
    '''Guardar el path de la pagina 
    configuracion a la variable de json'''

    new_path = request.forms.get('new_path')
    sistema =platform.system()
    if sistema == 'Linux':
        data['configuration']['download_dir_linux'] = new_path
    else:
        data['configuration']['download_dir_win32'] = new_path
    return template('static/configuration.html')

run(host='localhost', port=8088, debug=True)