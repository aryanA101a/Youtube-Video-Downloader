from pytube import *
vid=''

def download_audio(url,path,progress):
    def progress_function(stream, chunk, bytes_remaining):
        size = audio[0].filesize
        progress_value = 100-bytes_remaining/size*100
        progress.set(progress_value)
    #Create a Youtube URL with our URL
    yt = YouTube(url, on_progress_callback=progress_function)
    #We only want the audio
    audio=yt.streams.filter(only_audio=True).all()
    #Download and save to path
    audio[0].download(path)