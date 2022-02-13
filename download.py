import youtube_dl
import platform

def download_clip(url, name,data):
    '''
    path viene de fichero de configuracion
    '''
    print (data[name])
    directorio = data['configuration'][platform.system()]
    
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

def search_and_dowload(url, data):
    '''
    path viene de fichero de configuracion
    '''
    directorio = data['configuration'][platform.system()]
    
    ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': directorio +'/'+'%(title)s-%(id)s.%(ext)s',
            'noplaylist': True,
            'continue_dl': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', }]
    }
    try:
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info("ytsearch: "+url)
            #print (info)
            return True
    except Exception:
        return False 