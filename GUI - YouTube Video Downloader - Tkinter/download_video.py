from pytube import *
vid=''

def download_video(url,path,progress):
    def progress_function(stream, chunk, bytes_remaining):
        size = video.filesize
        progress_value = 100-bytes_remaining/size*100
        progress.set(progress_value)
# Inputs the URL
    video_url = url
# Passing the url in the pytube function, that is YouTube
    yt = YouTube(video_url, on_progress_callback=progress_function)

# Here you have to choose any one format of the stream (format contains mime_type, resolution, fps, vcodec, acodec). Also, you can change it if you want but I've chosen the first format.
    video = yt.streams.first()
    
    

# Downloads the .mp4 file into the current directory. You can change it if you want.
    video.download(path)
    fs=str(round(video.filesize/(1024*1024))) + 'MB'
    return fs
    
