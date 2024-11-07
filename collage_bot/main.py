from tkinter import *

import webbrowser


root=Tk()
root.config(bg="purple")

def openurl():
    path="file:///C:/Users/WELCOME/Desktop/collage_bot/collage_bot/index.html"
    webbrowser.open(path)


root.geometry("300x300")

b1=Button(root,text="CHATBOT",command=openurl,font=("Broadway",20),pady=50,padx=30,activebackground="green",activeforeground="yellow")
b1.pack()

root.mainloop()

