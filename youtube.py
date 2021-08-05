import youtube_dl
import json
from bottle import run, get, post, request, template, route # or route

with open("youtube.json", "r") as jsonfile:
    data = json.load(jsonfile) # Reading the file
    jsonfile.close()

@get('/login') # or @route('/login')
def login():
    return '''
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
    #download_clip("https://www.youtube.com/watch?v="+username,downloadoption)
    download_clip(URL,downloadoption)
    yield "Done"
    return '''<form action="/login" method="post">
                 <input value="Back" type="submit" />
        </form>
        '''

def download_clip(url, name):
    '''
    Cambiar path para raspberry /home/pi/Documents/youtube
    '''
    if name == "mp4":
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': data['download_dir']+'%(title)s-%(id)s.%(ext)s',#+name, #Cambiar path para raspberry
            'noplaylist': True,
            'continue_dl': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': '%(ext)s',
                'preferredquality': data['bitrate'], }]
        }
    else:
        ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': data['download_dir']+'%(title)s.mp3',#+name,
        'noplaylist': True,
        'continue_dl': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': data['bitrate'], }]
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            info_dict = ydl.extract_info(url, download=True)
            ydl.prepare_filename(info_dict)
            ydl.download([url])
            return True
    except Exception:
        return False 

#download_clip("https://www.youtube.com/watch?v=uGhKqb2Ow3E",True)
run(host='localhost', port=8088, debug=True)