from tkinter import *
import random


class Square:
    left = True
    right = True
    top = True
    bottom = True
    beenTo = False
    before = None
    def __init__(self, x, y):
        self.x = x
        self.y = y


tall = 10
wide = 10
maze = [[Square(x,y) for x in range(0,wide)] for y in range(0,tall)]

#for i in range(0,wide):
    #for j in range(0,tall):
        #print("X is in square" + str(maze[i][j].x))
        #print("Y is in square" + str(maze[i][j].y))
visited = 0
global startX
startX = 0
global startY
#startY = random.randint(0, tall - 1)
startY = 0
# print("The X startPoint is: " + str(startX))
# print("The Y startPoint is: " + str(startY))
# print(" ")

def mazeCreate():
    global visited
    while(tall * wide != visited):
        addpath(startX, startY, findneighbor(startX,startY))

    #implement graphics here
    print("Exit")


def findneighbor(startX,startY):
    neighborWall = random.randint(0, 3)
    if neighborWall == 0 and startX != 0 and not maze[startX - 1][startY].beenTo:
        print("returned 0")
        return 0
    elif neighborWall == 1 and startY != 0 and not maze[startX][startY - 1].beenTo:
        print("returned 1")
        return 1
    elif neighborWall == 2 and startX != 9  and not maze[startX + 1][startY].beenTo:
        print("returned 2")
        return 2
    elif neighborWall == 3 and startY != 9 and not maze[startX][startY - 1].beenTo:
        print("returned 3")
        return 3
    else:
        neighborWall = 0
        if neighborWall == 0 and startX != 0 and not maze[startX - 1][startY].beenTo:
            print("returned 0")
            num = 0
            return num

        neighborWall = neighborWall + 1
        if neighborWall == 0 and startX != 0 and not maze[startX - 1][startY].beenTo:
            print("returned 0")
            num = 0
            return num

        neighborWall = neighborWall + 1
        if neighborWall == 2 and startX != 9 and not maze[startX + 1][startY].beenTo:
            print("returned 2")
            num = 2
            return num
        neighborWall = neighborWall + 1
        if neighborWall == 3 and startY != 9 and not maze[startX][startY - 1].beenTo:
            print("returned 3")
            num = 3
            return num
        else:
            return -1


def addpath(startX, startY, int):
    global visited
    current = maze[startX][startY]
    print("Add Path in this direction..." + str(int))
    if int == 0:
        path = maze[startX-1][startY]
        current.left = False
        path.right = False
    if int == 1:
        path = maze[startX][startY-1]
        current.up = False
        path.down = False
    if int == 2:
        path = maze[startX+1][startY]
        current.right = False
        path.left = False
    if int == 3:
        path = maze[startX][startY+1]
        current.down = False
        path.up = False
    if int == -1:
        path = current.before
        visited -= 1
    current.beenTo = True
    visited = visited + 1
    path.before = current

    recenter(path)
    #type(current)
    return visited

def allTried(visited):
    print("All Tried")
    print(tall * wide)
    print(visited)
    if tall * wide == visited:
        return True
    else:
        return False

def recenter(square):
    print("recenter")
    global startX
    global startY
    startX = square.x
    startY = square.y
    print(startX)
    print(startY)

mazeCreate()

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
numBoxes = tall
boxWidth = int((screenHeight-100) / numBoxes)
# topBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, 50, screenWidth/2+numBoxes/2*boxWidth, 50)
# bottomBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, boxWidth*numBoxes, screenWidth/2+numBoxes/2*boxWidth, boxWidth*numBoxes)
# leftBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, 50, screenWidth/2-numBoxes/2*boxWidth, boxWidth * numBoxes)
# rightBorderLine = canvas.create_line(screenWidth/2+numBoxes/2*boxWidth, 50, screenWidth/2+numBoxes/2*boxWidth, boxWidth * numBoxes)

xPoint = screenWidth/2-numBoxes/2*boxWidth
yPoint = 10
endPosition = canvas.create_rectangle(int(screenWidth/2+numBoxes/2*boxWidth), int(boxWidth * numBoxes-boxWidth+10),
                                      int(screenWidth/2+numBoxes/2*boxWidth+boxWidth), int(boxWidth * numBoxes+10), fill = "green")

graphMaze = list()
n = 0
x = 0
y = 0
# Draw Horizontal Maze Lines
while int(yPoint) <= 10 + boxWidth * numBoxes:
    while int(xPoint) <= int(screenWidth/2+numBoxes/2*boxWidth):
        if maze[x][y].top == True:  # THis will be changed to if the square has a top or is bottom of the maze
            graphMaze.append(canvas.create_line(xPoint, yPoint, xPoint + boxWidth, yPoint))
        else:
            continue
        xPoint += boxWidth
        if x < wide - 1 :
            x += 1
        # print(xPoint)
    xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
    x = 0
    if y< tall - 1:
        y += 1
    yPoint += boxWidth
    # print(yPoint)
# Draw Vertical Maze Lines
xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
yPoint = 10
while int(yPoint) <= boxWidth * numBoxes:
    while int(xPoint) <= int(screenWidth/2+numBoxes/2*boxWidth)+boxWidth:
        if True:
            # THis will be changed to if the square has a Left
            # or is far right of the maze(watch out for start and end of maze
            graphMaze.append(canvas.create_line(xPoint, yPoint, xPoint, yPoint + boxWidth))
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


player = Player(screenWidth/2-numBoxes/2*boxWidth, 11, boxWidth/2)
playerPiece = canvas.create_rectangle(player.xLocation, player.yLocation, player.xLocation+player.size+1,
                                      player.yLocation+player.size+1, fill="red")
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

