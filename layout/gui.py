from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.iconbitmap('../assets/ico/cube.ico')
root.title("SECAD")
root.configure(background="#F6F6F6")
root.minsize(500, 500)  # width, height
root.maxsize(500, 500)
root.geometry("500x500+420+120")  # width x height + x + y

# Create Label in our window
text = Label(root, text="INICIALIZANDO INTERFACE", bd=0)
text.pack()

# text2 = Label(root, text="Snd label", bd=0)
# text2.pack()
root.mainloop()


