import youtube_dl
import platform
def download_clip(url, name,data):
    '''
    path viene de fichero de configuracion
    '''
    print (data[name])
    sistema =platform.system()
    print (sistema)

    if sistema == 'Linux':
        directorio = data['configuration']['download_dir_linux']
    else:
        directorio = data['configuration']['download_dir_win32']
    ydl_opts = {
            'format': data[name]['format'],
            'outtmpl': directorio +'/'+'%(title)s-%(id)s.%(ext)s',
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