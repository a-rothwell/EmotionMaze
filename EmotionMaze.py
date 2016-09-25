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

tall = 25
wide = tall
maze = [[Square(x,y) for y in range(0,wide)] for x in range(0,tall)]

solution = list()
solution.append(maze[0][0])
#for i in range(0,wide):
    #for j in range(0,tall):
        #print("X is in square" + str(maze[i][j].x))
        #print("Y is in square" + str(maze[i][j].y))
visited = 0
startX = 0
startY = 0

def mazeCreate():
    global visited
    global startX
    global startY
    for num in range(0 , (tall * 2) ** 2):
        addpath(findneighbor())


def findneighbor():
    global startX
    global startY
    neighborWall = random.randint(0, 3)
    if neighborWall == 0 and startX != 0 and not maze[startX - 1][startY].beenTo:
        return 0
    elif neighborWall == 1 and startY != 0 and not maze[startX][startY - 1].beenTo:
        return 1
    elif neighborWall == 2 and startX != tall - 1  and not maze[startX + 1][startY].beenTo:
        return 2
    elif neighborWall == 3 and startY != tall - 1 and not maze[startX][startY + 1].beenTo:
        return 3
    else:
        neighborWall = 0
        if neighborWall == 0 and startX != 0 and not maze[startX - 1][startY].beenTo:
            num = 0
            return num

        neighborWall = neighborWall + 1
        if neighborWall == 1 and startY != 0 and not maze[startX ][startY - 1].beenTo:
            num = 1
            return num

        neighborWall = neighborWall + 1
        if neighborWall == 2 and startX != tall - 1 and not maze[startX + 1][startY].beenTo:
            num = 2
            return num
        neighborWall = neighborWall + 1
        if neighborWall == 3 and startY != tall - 1 and not maze[startX][startY + 1].beenTo:
            num = 3
            return num
        else:
            return -1


def addpath(int):
    global visited
    global startX
    global startY
    current = maze[startX][startY]
    if int == -1:
        if len(solution) != 0:
            recenter(solution[len(solution)-1])
            solution.pop()
        return visited
    if int == 0:
        path = maze[startX-1][startY]
        path.before = current
        solution.append(path)
        current.left = False
        path.right = False
        path.beenTo = True
    if int == 1:
        path = maze[startX][startY - 1]
        path.before = current
        solution.append(path)
        current.top = False
        path.bottom = False
        path.beenTo = True
    if int == 2:
        path = maze[startX + 1][startY]
        path.before = current
        solution.append(path)
        current.right = False
        path.left = False
        path.beenTo = True
    if int == 3:
        path = maze[startX][startY + 1]
        path.before = current
        solution.append(path)
        current.bottom = False
        path.top = False
        path.beenTo = True
    path.beenTo = True
    current.beenTo = True
    visited = visited + 1
    recenter(path)
    return visited



def recenter(square):
    global startX
    global startY
    startX = square.x
    startY = square.y
    if startX == tall - 1 and startY == tall - 1:
        pntSol = list()
        pntSol = solution.copy()
        pntSol.reverse()
        for points in pntSol:
            print(pntSol[-1:])
            pntSol.pop()

mazeCreate()

root = Tk()
root.wm_title("Emotion Maze")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# Resize tk window and sets its location
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, -9, 0))
# root.resizable(FALSE, FALSE)

# Frame is a widget container
frame = Frame(root, background="gray", width=screenWidth, height=50)
frame.pack(side=TOP)

# Canvas is used to draw things in tkinter
canvas = Canvas(root, width=screenWidth, height=screenHeight-20)
canvas.pack()
numBoxes = tall
boxWidth = int((screenHeight-100) / numBoxes)
topBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, 10, screenWidth/2+numBoxes/2*boxWidth, 10)
bottomBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, 10+boxWidth*numBoxes, screenWidth/2+numBoxes/2*boxWidth, 10+boxWidth*numBoxes)
leftBorderLine = canvas.create_line(screenWidth/2-numBoxes/2*boxWidth, 10, screenWidth/2-numBoxes/2*boxWidth, 10+boxWidth * numBoxes)
rightBorderLine = canvas.create_line(screenWidth/2+numBoxes/2*boxWidth , 10, screenWidth/2+numBoxes/2*boxWidth,
                                     10+boxWidth * numBoxes)

xPoint = screenWidth/2-numBoxes/2*boxWidth
yPoint = 10
#endPosition = canvas.create_rectangle(int(screenWidth/2+numBoxes/2*boxWidth)-boxWidth, int(boxWidth * numBoxes-boxWidth+10),
#                                     int(screenWidth/2+numBoxes/2*boxWidth+boxWidth)-boxWidth,
#                                      int(boxWidth * numBoxes+10), fill = "light green", outline=None)

class Hitbox():
    def __init__(self, minX , maxX , minY, maxY):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY

graphMaze = list()
borderHitboxes = list()
x = 0
y = 0
while y < tall:
    while x < wide:
        if maze[x][y].top:
            graphMaze.append(canvas.create_line(xPoint, yPoint, xPoint + boxWidth, yPoint))
            borderHitboxes.append(Hitbox(xPoint,xPoint + boxWidth , yPoint, yPoint))
        else:
            pass
        xPoint += boxWidth
        x += 1
    xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
    x = 0
    y += 1
    yPoint += boxWidth
# Draw Vertical Maze Lines
x = 0
y = 0
xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
yPoint = 10
while y < tall:
    while x < wide:
        if maze[x][y].left:
            graphMaze.append(canvas.create_line(xPoint, yPoint, xPoint, yPoint + boxWidth))
            borderHitboxes.append(Hitbox(xPoint, xPoint, yPoint, yPoint + boxWidth))
        else:
            pass
        xPoint += boxWidth
        x += 1
    xPoint = int(screenWidth/2-numBoxes/2*boxWidth)
    x = 0
    y += 1
    yPoint += boxWidth
#print(len(borderHitboxes))


class Player:
    """Represents a Player Object"""

    def __init__(self, x, y, size):
        self.xLocation = x
        self.yLocation = y
        self.size = size
        self.speed = 5
        self.updateHitbox()
    def updateHitbox(self):
        self.hitbox = Hitbox(self.xLocation, self.xLocation + self.size, self.yLocation, self.yLocation + self.size)
    def checkForCollision(self, newHitbox):
        xCollision = False
        yCollision = False
        for boxes in borderHitboxes:
            if newHitbox.minX >= boxes.minX and newHitbox.minX <= boxes.maxX or newHitbox.maxX >= boxes.minX and newHitbox.maxX <= boxes.maxX :
                xCollision = True
            if newHitbox.minY >= boxes.minY and newHitbox.minY <= boxes.maxY or newHitbox.maxY >= boxes.minY and newHitbox.maxY <= boxes.maxY :
                yCollision = True
            if xCollision and yCollision:
                return False
            else:
                return True

    def playerCanMoveRight(self):
        print("Hitbox xMin: " + str(self.hitbox.minX) + " Hitbox xMax: " + str(self.hitbox.maxX) + "\n Hitbox yMin: "
              + str(self.hitbox.minY) + "Hitbox yMax: " + str(self.hitbox.maxY))
        return self.checkForCollision(Hitbox(self.hitbox.minX + 1, self.hitbox.maxX + 1,self.hitbox.minY , self.hitbox.maxY))
    def playerCanMoveLeft(self):
        print("Hitbox xMin: " + str(self.hitbox.minX) + " Hitbox xMax: " + str(self.hitbox.maxX) + "\n Hitbox yMin: "
              + str(self.hitbox.minY) + "Hitbox yMax: " + str(self.hitbox.maxY))
        return self.checkForCollision(Hitbox(self.hitbox.minX - 1, self.hitbox.maxX - 1, self.hitbox.minY, self.hitbox.maxY))
    def playerCanMoveUp(self):
        print("Hitbox xMin: " + str(self.hitbox.minX) + " Hitbox xMax: " + str(self.hitbox.maxX) + "\n Hitbox yMin: "
              + str(self.hitbox.minY) + "Hitbox yMax: " + str(self.hitbox.maxY))
        return self.checkForCollision(Hitbox(self.hitbox.minX , self.hitbox.maxX,self.hitbox.minY -1 , self.hitbox.maxY - 1))
    def playerCanMoveDown(self):
        print("Hitbox xMin: " + str(self.hitbox.minX) + " Hitbox xMax: " + str(self.hitbox.maxX) + "\n Hitbox yMin: "
              + str(self.hitbox.minY) + "Hitbox yMax: " + str(self.hitbox.maxY))
        return self.checkForCollision(Hitbox(self.hitbox.minX , self.hitbox.maxX,self.hitbox.minY + 1 , self.hitbox.maxY + 1))
    def movePlayerLeft(self, event) :
        count = 0
        while(count < self.speed) :
            if self.playerCanMoveLeft():
                self.xLocation -= 1
                self.updateHitbox()
                count+=1
            else:
                break
    def movePlayerRight(self, event):
        count = 0
        while count < self.speed :
            if self.playerCanMoveRight():
                self.xLocation += 1
                self.updateHitbox()
                count += 1
            else :
                break
    def movePlayerUp(self, event):
        count = 0
        while count < self.speed :
            if self.playerCanMoveUp():
                self.yLocation -= 1
                self.updateHitbox()
                count += 1
            else :
                break
    def movePlayerDown(self, event):
        count = 0
        while count < self.speed :
            if self.playerCanMoveDown():
                self.yLocation += 1
                self.updateHitbox()
                count += 1
            else:
                break

print("Border Hitbox xMin: " + str(borderHitboxes.__getitem__(600).minX) + " Hitbox xMax: " + str(borderHitboxes.__getitem__(600).maxX) + "\n Hitbox yMin: "
              + str(borderHitboxes.__getitem__(600).minY) + "Hitbox yMax: " + str(borderHitboxes.__getitem__(600).maxY))

player = Player(screenWidth/2-numBoxes/2*boxWidth + 1, 11, boxWidth/2)
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