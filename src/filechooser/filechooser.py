from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\jayCg\\OneDrive\\Escritorio\\Repython\\proyecto",
                                          title="Archivos de entrada",
                                          filetypes=(("text file","*.txt"),("All files","*.*")))
    if filepath: 
        with open(filepath, 'r') as file:
            print(file.read())
    
Window = Tk()
Window.geometry("100x50")
button = Button(text="Abrir", command=openFile)
button.pack()
Window.mainloop()    