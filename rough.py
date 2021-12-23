from tkinter import *
import webbrowser

root = Tk()

url = "https://ndma.gov.in/Natural-Hazards/Floods"

def openweb():
    webbrowser.open(url,new=1) #new=1 opens in new window new=2 opens new tab

Btn = Button(root, text = "Flood Info",command=openweb)
Btn.pack()

root.mainloop()