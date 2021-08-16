import youtube_dl

def download_clip(url, name,data):
    '''
    path viene de fichero de configuracion
    '''
    print (data[name])
    ydl_opts = {
            'format': data[name]['format'],
            'outtmpl': data['configuration']['download_dir']+'%(title)s-%(id)s.%(ext)s',
            'noplaylist': True,
            'continue_dl': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': data[name]['preferredcodec'],
                'preferredquality': data[name]['preferredquality'], }]
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