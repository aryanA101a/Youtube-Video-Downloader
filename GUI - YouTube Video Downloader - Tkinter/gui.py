from tkinter import filedialog,messagebox
from tkinter import *
from downloadLogic import downloadLogic
from tkinter.ttk import *
bluegrey='#192734'


window = Tk()

window.title("Youtube Video Downloader")

window.geometry('500x200')
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

variable = StringVar(window)

file_size_value = OptionMenu(window, variable, "----Select----", "1080p", "720p", "480p", "360p", "240p")
file_size_value.pack()
file_size_value.place(relx =.3,rely=.5, anchor = N)

# lbl3 = Label(window, text="Status: ",background=bluegrey,foreground='White')

# lbl3.place(relx =.38,rely=.5, anchor = N) 



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

def fileSizeValue():
    fileSize = variable.get()
    return fileSize

def clicked():
    
    url = txt.get()
    path=pathHolder()
    fileSize = fileSizeValue()
    FileSize=downloadLogic(url,path, fileSize)
    lbl2.configure(text='FileSize: '+FileSize)
    messagebox.showinfo('Downloaded!', 'Video has been saved to '+path)
    


btn = Button(window, text="Download",style='W.TButton',command=clicked,width=20)

btn.place(relx =.5,rely=.8, anchor = CENTER) 

btn1 = Button(window, text="Browse",style='W.TButton', command=pathAssignment)

btn1.place(relx =.95,rely=.3, anchor = NE) 

window.resizable(0,0)
window.mainloop()
