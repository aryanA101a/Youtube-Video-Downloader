from pytube import *
vid=''

def downloadLogic(url,path, fileSize):
# Inputs the URL
    video_url = url

# Passing the url in the pytube function, that is YouTube
    yt = YouTube(video_url)

# Here you have to choose any one format of the stream (format contains mime_type, resolution, fps, vcodec, acodec). Also, you can change it if you want but I've chosen the first format.
    video = yt.streams.filter(subtype='mp4', resolution=fileSize).first()

# Downloads the .mp4 file into the current directory. You can change it if you want.
    video.download(path)
    fs=str(round(video.filesize/(1024*1024))) + 'MB'
    return fs
    
