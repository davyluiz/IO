from tkinter import *


root = Tk()
root.iconbitmap('../assets/cube.ico')
root.title("SECAD")
root.configure(background="#F7F7F7")
root.minsize(500, 500)  # width, height
root.maxsize(500, 500)
root.geometry("500x500+420+120")  # width x height + x + y

# Create Label in our window
text = Label(root, text="F label.", bd=0)
text.pack()
text2 = Label(root, text="Snd label", bd=0)
text2.pack()
root.mainloop()

root.mainloop()
