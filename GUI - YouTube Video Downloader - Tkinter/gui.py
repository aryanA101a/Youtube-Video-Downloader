from tkinter import filedialog,messagebox
from tkinter import *
from download_video import download_video
from download_audio import download_audio
from tkinter.ttk import *
from threading import Thread
bluegrey='#192734'


window = Tk()

window.title("Youtube Video Downloader")

window.geometry('500x250')
window.configure(bg=bluegrey)

#Create style object
sto = Style()

#configure style
sto.configure('W.TButton', font= ('Roboto', 10, 'bold'),
foreground='White',background='#FF304E')





lbl = Label(window, text="Youtube Video URL",background=bluegrey,foreground='White')

lbl.place(relx =.03,rely=.1, anchor = NW) 

txt = Entry(window,width=25)

txt.place(relx =.5,rely=.1, anchor = N) 


lbl1 = Label(window, text="Download Location",background=bluegrey,foreground='White')

lbl1.place(relx =.03,rely=.3, anchor = NW) 

txt1 = Entry(window,width=25)

txt1.place(relx =.5,rely=.3, anchor = N) 

lbl2 = Label(window, text="FileSize:",background=bluegrey,foreground='White')

lbl2.place(relx =.03,rely=.5, anchor = NW) 

lbl3 = Label(window, text="Status: ",background=bluegrey,foreground='White')

lbl3.place(relx =.38,rely=.5, anchor = N) 

progress = IntVar()
progress_bar = Progressbar(maximum=100, variable=progress)

progress_bar.place(relx =.45,rely=.5, anchor = NW, width=250) 

def pathAssignment():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    txt1.delete(0,END)
    txt1.insert(0,folder_selected)
    root.destroy()
    return

def pathHolder():

    path = txt1.get()
    return path

def download_video_button_clicked():
    Thread(target=dl_video_click).start()

def dl_video_click():
    url = txt.get()
    path=pathHolder()
    FileSize=download_video(url,path,progress)
    lbl2.configure(text='FileSize: '+FileSize)
    messagebox.showinfo('Downloaded!', 'Video has been saved to '+path)

def download_audio_button_clicked():
    Thread(target=dl_audio_click).start()

def dl_audio_click():
    url = txt.get()
    path=pathHolder()
    FileSize=download_audio(url,path,progress)
    messagebox.showinfo('Downloaded!', 'Audio has been saved to '+path)
    


btn_download_video = Button(window, text="Download Video",style='W.TButton',command=download_video_button_clicked,width=20)
btn_download_video.place(relx =.5,rely=.7, anchor = CENTER) 

btn_download_audio = Button(window, text="Download Audio",style='W.TButton',command=download_audio_button_clicked,width=20)
btn_download_audio.place(relx =.5,rely=.9, anchor = CENTER) 

btn_set_directory = Button(window, text="Browse",style='W.TButton', command=pathAssignment)
btn_set_directory.place(relx =.95,rely=.3, anchor = NE) 

window.resizable(0,0)
window.mainloop()
