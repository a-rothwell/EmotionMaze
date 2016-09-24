from tkinter import *
from tkinter import ttk

root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# Resize tk window and sets its location
root.geometry('%dx%d+%d+%d' % (screenWidth / 2, screenHeight, screenWidth / 2, 0))
root.resizable(FALSE, FALSE)


# l =ttk.Label(root, text="Starting...")
# l.grid()
# l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
# l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
# l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
# l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
# l.bind('<Key>', lambda e: l.configure(text='a button pressed'))

def moveLeft(event):
    global x
    # print("Old X : " + str(x))
    x -= 1
    # print("New X : " + str(x))


def moveRight(event):
    global x
    x += 1
    # print("New X: " + str(x))

root.grid()
root.bind('<Left>', moveLeft)
root.bind('<Right>', moveRight)

root.mainloop()
