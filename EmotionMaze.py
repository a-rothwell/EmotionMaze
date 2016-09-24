from tkinter import *
programOver = False

root = Tk()
root.wm_title("Emotion Maze")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# Resize tk window and sets its location
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, -9, 0))

# Frame is a widget container
frame = Frame(root, background="gray", width=screenWidth, height=50)
frame.pack(side=TOP)

# Canvas is used to draw things in tkinter
canvas = Canvas(root, width=screenWidth, height=screenHeight)
canvas.pack()

playerXLocation = 0
playerYLocation = 0
playerSize = 10

canvas.create_rectangle(playerXLocation, playerYLocation, playerXLocation+playerSize+1, playerYLocation+playerSize+1, fill="red")

def the_event(event)
    print(event)
while not programOver:
    canvas.bind(a, the_event)



root.mainloop()
