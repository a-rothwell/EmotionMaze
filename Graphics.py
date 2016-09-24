from tkinter import *
programOver = False

root = Tk()
root.wm_title("Emotion Maze")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# Resize tk window and sets its location
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, -9, 0))
root.resizable(FALSE, FALSE)

# Frame is a widget container
frame = Frame(root, background="gray", width=screenWidth, height=50)
frame.pack(side=TOP)

# Canvas is used to draw things in tkinter
canvas = Canvas(root, width=screenWidth, height=screenHeight-20)
canvas.pack()
numBoxes = 50
boxWidth = int((screenHeight-100) / numBoxes)
# topBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, 50, screenWidth/2+numBoxes/2*boxWidth, 50)
# bottomBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, boxWidth*numBoxes, screenWidth/2+numBoxes/2*boxWidth, boxWidth*numBoxes)
# leftBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, 50, screenWidth/2-numBoxes/2*boxWidth, boxWidth * numBoxes)
# rightBorderLine = canvas.create_line(screenWidth/2+numBoxes/2*boxWidth, 50, screenWidth/2+numBoxes/2*boxWidth, boxWidth * numBoxes)

xPoint = screenWidth/2-numBoxes/2*boxWidth
yPoint = 10
maze = list()
n = 0
# Draw Horizontal Maze Lines
while int(yPoint) <= 10 + boxWidth * numBoxes:
    while int(xPoint) <= int(screenWidth/2+numBoxes/2*boxWidth):
        if:  # THis will be changed to if the square has a top or is bottom of the maze
            maze.append(canvas.create_line(xPoint, yPoint, xPoint + boxWidth, yPoint))
        else:
            continue
        xPoint += boxWidth
        #print(xPoint)
    xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
    yPoint += boxWidth
    #print(yPoint)
# Draw Vertical Maze Lines
xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
yPoint = 10
while int(yPoint) <= boxWidth * numBoxes:
    while int(xPoint) <= int(screenWidth/2+numBoxes/2*boxWidth)+boxWidth:
        if True:
            # THis will be changed to if the square has a Left
            # or is far right of the maze(watch out for start and end of maze
            maze.append(canvas.create_line(xPoint, yPoint, xPoint, yPoint + boxWidth))
        else:
            continue
        xPoint += boxWidth
    xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
    yPoint += boxWidth


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
        count = 0
        while(count < self.speed) :
            if self.playerCanMoveLeft :
                self.xLocation -= 1
                count+=1
            else:
                break
    def movePlayerRight(self, event):
        count = 0
        while count < self.speed :
            if self.playerCanMoveRight :
                self.xLocation += 1
                count += 1
            else :
                break
    def movePlayerUp(self, event):
        count = 0
        while count < self.speed :
            if self.playerCanMoveUp :
                self.yLocation -= 1
                count += 1
            else :
                break
    def movePlayerDown(self, event):
        count = 0
        while count < self.speed :
            if self.playerCanMoveDown:
                self.yLocation += 1
                count += 1
            else :
                break


player = Player(20, 20, boxWidth/2)
playerPiece = canvas.create_rectangle(player.xLocation, player.yLocation, player.xLocation+player.size+1, player.yLocation+player.size+1, fill="red")
# canvas.delete("all")
root.grid()
root.bind('<Left>', player.movePlayerLeft)
root.bind('<Right>', player.movePlayerRight)
root.bind('<Up>', player.movePlayerUp)
root.bind('<Down>', player.movePlayerDown)
#Updates Window
def updateWindow():
    root.after(10, updateWindow)
    global playerPiece
    canvas.delete(playerPiece)
    playerPiece = canvas.create_rectangle(player.xLocation, player.yLocation, player.xLocation + player.size + 1,
                            player.yLocation + player.size + 1, fill="red")

root.after(10, updateWindow)

root.mainloop()

