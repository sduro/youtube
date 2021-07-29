import youtube_dl
from bottle import run, get, post, request # or route

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            URL: <input name="username" type="text" />
            Title: <input name="songname" type="text" />
            <input value="Download" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    songname = request.forms.get('songname')
    download_clip("https://www.youtube.com/watch?v="+username,songname+".mp3")
    return "<p>Download</p>"

def download_clip(url, name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/home/sduro/Documentos/'+name,
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
run(host='localhost', port=8080, debug=True)