from tkinter import *
programOver = False

root = Tk()
root.wm_title("Emotion Maze")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# Resize tk window and sets its location
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, -9, 0))
root.resizable(FALSE,FALSE)

# Frame is a widget container
frame = Frame(root, background="gray", width=screenWidth, height=50)
frame.pack(side=TOP)

# Canvas is used to draw things in tkinter
canvas = Canvas(root, width=screenWidth, height=screenHeight)
canvas.pack()

class Player:
    """Represents a Player Object"""
    def __init__(self, x, y, size):
        self.xLocation = x
        self.yLocation = y
        self.size = size
        self.speed = 5
    def playerCanMoveRight(self):
        return True
    def playerCanMoveLeft(self):
        return True
    def playerCanMoveUp(self):
        return True
    def playerCanMoveDown(self):
        return True
    def movePlayerLeft(self, event) :
        if self.playerCanMoveLeft :
            self.xLocation -= self.speed
        print("PLayer moving Left")
    def movePlayerRight(self, event):
        if self.playerCanMoveRight :
            self.xLocation += self.speed
    def movePlayerUp(self, event):
        if self.playerCanMoveUp :
            self.yLocation -= self.speed
    def movePlayerDown(self, event):
        if self.playerCanMoveDown:
            self.yLocation += self.speed


player = Player(20, 20, 10)
playerPiece = canvas.create_rectangle(player.xLocation, player.yLocation, player.xLocation+player.size+1, player.yLocation+player.size+1, fill="red")
# canvas.delete("all")
root.grid()
root.bind('<Left>', player.movePlayerLeft)
root.bind('<Right>', player.movePlayerRight)
root.bind('<Up>', player.movePlayerUp)
root.bind('<Down>', player.movePlayerDown)

def updateWindow():
    root.after(10, updateWindow)
    global playerPiece
    canvas.delete(playerPiece)
    playerPiece = canvas.create_rectangle(player.xLocation, player.yLocation, player.xLocation + player.size + 1,
                            player.yLocation + player.size + 1, fill="red")

root.after(10, updateWindow)

root.mainloop()

