import youtube_dl
import os
from bottle import run, get, post, request, template # or route

@get('/login') # or @route('/login')
def login():

    return '''
        <form action="/login" method="post">
            Youtube URL: <input name="URL" type="text" />
            Video ID: <input name="username" type="text" />
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
    URL = request.forms.get('URL')
    username = request.forms.get('username')
    downloadoption = request.forms.get('downloadoption')
    print (downloadoption)
    #download_clip("https://www.youtube.com/watch?v="+username,downloadoption)
    download_clip(URL,downloadoption)
    return '''<form action="/login" method="post">
                 <input value="Back" type="submit" />
        </form>
        '''

def download_clip(url, name):
    '''download video equal to MP4, only audio MP3'''
    if name == "mp4":
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '/home/sduro/Documentos/%(title)s-%(id)s.%(ext)s',#+name,
            'noplaylist': True,
            'continue_dl': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': '%(ext)s',
                'preferredquality': '192', }]
        }
    else:
        ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/home/sduro/Documentos/%(title)s.mp3',#+name,
        'noplaylist': True,
        'continue_dl': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', }]
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
run(host='0.0.0.0', port=8080, debug=True)