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

    def __getitem__(self, item):
        return self.x
        return self.y

tall = 10
wide = 10
maze = [[Square(x,y) for y in range(0,wide)] for x in range(0,tall)]

solution = list()
#for i in range(0,wide):
    #for j in range(0,tall):
        #print("X is in square" + str(maze[i][j].x))
        #print("Y is in square" + str(maze[i][j].y))
visited = 0
global startX
startX = 0
global startY
startY = 0
print("The X startPoint is: " + str(startX))
print("The Y startPoint is: " + str(startY))
# print(" ")

def mazeCreate():
    global visited
    global startX
    global startY
    for num in range(0,100):
        print("---------New Thread --------" + str(num))
        addpath(startX, startY, findneighbor(startX,startY))


def findneighbor(startX,startY):
    neighborWall = random.randint(0, 3)
    if neighborWall == 0 and startX != 0 and not maze[startX - 1][startY].beenTo:
        return 0
    elif neighborWall == 1 and startY != 0 and not maze[startX][startY - 1].beenTo:
        return 1
    elif neighborWall == 2 and startX != 9  and not maze[startX + 1][startY].beenTo:
        return 2
    elif neighborWall == 3 and startY != 9 and not maze[startX][startY - 1].beenTo:
        return 3
    else:
        neighborWall = 0
        if neighborWall == 0 and startX != 0 and not maze[startX - 1][startY].beenTo:
            num = 0
            return num

        neighborWall = neighborWall + 1
        if neighborWall == 0 and startX != 0 and not maze[startX - 1][startY].beenTo:
            num = 0
            return num

        neighborWall = neighborWall + 1
        if neighborWall == 2 and startX != 9 and not maze[startX + 1][startY].beenTo:
            num = 2
            return num
        neighborWall = neighborWall + 1
        if neighborWall == 3 and startY != 9 and not maze[startX][startY - 1].beenTo:
            num = 3
            return num
        else:
            return -1


def addpath(startX, startY, int):
    global visited
    current = maze[startX][startY]
    if int == -1:
        print("DeadEnd")
        if len(solution) != 0:
            print(solution)
            recenter(solution[len(solution)-1])
            solution.pop()
        return visited
    if int == 0:
        path = maze[startX-1][startY]
        path.before = current
        solution.append(current)
        current.left = False
        path.right = False
        path.beenTo = True
    if int == 1:
        path = maze[startX][startY-1]
        path.before = current
        solution.append(current)
        current.top = False
        path.bottom = False
        path.beenTo = True
    if int == 2:
        path = maze[startX+1][startY]
        path.before = current
        solution.append(current)
        current.right = False
        path.left = False
        path.beenTo = True
    if int == 3:
        path = maze[startX][startY+1]
        path.before = current
        solution.append(current)
        current.bottom = False
        path.top = False
        path.beenTo = True
    path.beenTo = True
    current.beenTo = True
    visited = visited + 1
    recenter(path)
    #type(current)
    return visited

def allTried(visited):
    if tall * wide == visited:
        return True
    else:
        return False


def recenter(square):
    global startX
    global startY
    startX = square.x
    startY = square.y
    print(startX)
    print(startY)

def recentercase(x,y):
    global startX
    global startY
    startX = x
    startY = y
    print(startX)
    print(startY)

mazeCreate()
for i in range(0,wide):
    for j in range(0,tall):
        print("X is in square" + str(maze[i][j].beenTo))
        print("Y is in square" + str(maze[i][j].beenTo))

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
x = 0
y = 0
# Draw Horizontal Maze Lines
while int(yPoint) <= 10 + boxWidth * numBoxes:
    while int(xPoint) <= int(screenWidth/2+numBoxes/2*boxWidth):
        if maze[x][y].top:  # THis will be changed to if the square has a top or is bottom of the maze
            graphMaze.append(canvas.create_line(xPoint, yPoint, xPoint + boxWidth, yPoint))
        else:
            pass
        xPoint += boxWidth
        if x < wide - 1 :
            x += 1
    xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
    x = 0
    if y < tall - 2:
        y += 1
    yPoint += boxWidth
# Draw Vertical Maze Lines
x = 0
y = 0
xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
yPoint = 10
while int(yPoint) <= boxWidth * numBoxes:
    while int(xPoint) <= int(screenWidth/2+numBoxes/2*boxWidth)+boxWidth:
        if maze[x][y].left:
            graphMaze.append(canvas.create_line(xPoint, yPoint, xPoint, yPoint + boxWidth))
        else:
            pass
        xPoint += boxWidth
        if x < wide - 1 :
            x += 1
    xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
    x=0
    if y < tall - 2:
        y += 1
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

