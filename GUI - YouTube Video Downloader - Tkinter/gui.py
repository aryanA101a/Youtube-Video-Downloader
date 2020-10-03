from tkinter import filedialog, messagebox
from tkinter import *
from downloadLogic import downloadLogic, downloadAudioLogic
from tkinter.ttk import *

bluegrey = '#192734'

window = Tk()

window.title("Youtube Video Downloader")

window.geometry('500x200')
window.configure(bg=bluegrey)

# Create style object
sto = Style()

# configure style
sto.configure('W.TButton', font=('Roboto', 10, 'bold'),
              foreground='White', background='#FF304E')

lbl = Label(window, text="Youtube Video URL", background=bluegrey, foreground='White')

lbl.place(relx=.03, rely=.1, anchor=NW)

txt = Entry(window, width=25)

txt.place(relx=.5, rely=.1, anchor=N)

lbl1 = Label(window, text="Download Location", background=bluegrey, foreground='White')

lbl1.place(relx=.03, rely=.3, anchor=NW)

txt1 = Entry(window, width=25)

txt1.place(relx=.5, rely=.3, anchor=N)

lbl2 = Label(window, text="FileSize:", background=bluegrey, foreground='White')

lbl2.place(relx=.03, rely=.5, anchor=NW)


# lbl3 = Label(window, text="Status: ",background=bluegrey,foreground='White')

# lbl3.place(relx =.38,rely=.5, anchor = N)


def pathAssignment():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    txt1.delete(0, END)
    txt1.insert(0, folder_selected)
    root.destroy()
    return


def pathHolder():
    path = txt1.get()
    return path


def clicked():
    url = txt.get()
    path = pathHolder()
    FileSize = downloadLogic(url, path)
    lbl2.configure(text='FileSize: ' + FileSize)
    messagebox.showinfo('Downloaded!', 'Video has been saved to ' + path)


def AudioClicked():
    url = txt.get()
    path = pathHolder()
    FileSize = downloadAudioLogic(url, path)
    lbl2.configure(text='FileSize: ' + FileSize)
    messagebox.showinfo('Downloaded!', 'Audio has been saved to ' + path)


btn = Button(window, text="Download", style='W.TButton', command=clicked, width=10)
btn.place(relx=.5, rely=.8, anchor=NE)

btn2 = Button(window, text="Download Audio", style='W.TButton', command=AudioClicked, width=15)

btn2.place(relx=.5, rely=.8, anchor=NW)

btn1 = Button(window, text="Browse", style='W.TButton', command=pathAssignment)

btn1.place(relx=.95, rely=.3, anchor=NE)

window.resizable(0, 0)
window.mainloop()
