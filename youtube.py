'''
Pagina web para descargar mp3
youtube.json ->fichero de configuracion
'''
import youtube_dl
import json
from bottle import run, get, post, request, template, route # or route
from download import download_clip

with open("youtube.json", "r") as jsonfile:
    data = json.load(jsonfile) # Reading the file
    jsonfile.close()

@get('/login') # or @route('/login')
def login():
    return '''
            <form action="/login" method="post">
            Youtube URL: <input name="URL" type="text" />
            <label for="downloadoption">Option</label>
                <select name="downloadoption" id="downloadoption">
                <option value="mp3">Solo Audio</option>
                <option value="mp4">Audio+Video</option>
            </select> 
            <input value="Download" type="submit" />
        </form>
    '''
@post('/login') # or @route('/login', method='POST')
def do_login():
    yield "Downloading..."
    URL = request.forms.get('URL')
    downloadoption = request.forms.get('downloadoption')
    download_clip(URL,downloadoption,data)
    yield "Done"
    return '''<form action="/login" method="post">
                 <input value="Back" type="submit" />
        </form>
        '''
run(host='localhost', port=8088, debug=True)