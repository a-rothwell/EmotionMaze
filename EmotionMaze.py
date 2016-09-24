#Must Install numpy package before runtime
#Must Install easyTinker before runtime
#update
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
    if int == 1:
        path = maze[startX][startY-1]
    if int == 2:
        path = maze[startX+1][startY]
    if int == 3:
        path = maze[startX][startY+1]
    if int == -1:
        path = current.before
        visited -= 1
    current.beenTo = True
    current.left = False
    path.right = False
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