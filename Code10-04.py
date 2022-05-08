from tkinter import*
window = Tk()

photo = PhotoImage(file = "gif/dog.gif")
label1 = Lable(window, image = photo)

label1.pack()

window.mainloop()
