from pytube import *
vid=''

def download_audio(url,path):
    #Create a Youtube URL with our URL
    yt = YouTube(url)
    #We only want the audio
    audio=yt.streams.filter(only_audio=True).all()
    #Download and save to path
    audio[0].download(path)