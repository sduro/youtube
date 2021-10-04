# Installation
Download all repository into a folder with all dependencies.
```
1. pip install spotipy
2. pip install youtubeDL
```

# Run application
```bash
python youtube.py
```
## Configuration
You can edit the youtube.json directly
```json
{
    "configuration": {
        "Win32": "c:\\",
        "Linux": "/home/$USER/Música",
        "bitrate": "192"
    },
    "mp3": {
        "format": "bestaudio/best",
        "noplaylist": "True",
        "continue_dl": "True",
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192"
    },
    "mp4": {
        "format": "bestvideo+bestaudio/best",
        "noplaylist": "True",
        "continue_dl": "True",
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp4",
        "preferredquality": "192"
    }
}
```
## Features
- [x] Download mp3/mp4 from Youtube
- [x] Download mp3 from Spotify with API
- [x] Configuration page
- [ ] Checking page with all software needed
- [ ] Check when download is done