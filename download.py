import youtube_dl
def download_clip(url, name,data):
    '''
    path viene de fichero de configuracion
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