#Must Install numpy package before runtime
#Must Install easyTinker before runtime
import random

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self.visited = False

class Node:
    def __init__(self,squareOne,squareTwo):
        self.squareOne = squareOne
        self.squareTwo = squareTwo
        self.connectors = list()

tall = 10
wide = 10
maze = list()
visited = list()
nodes = list()
for x in range(0,tall):
    for y in range(0,wide):
        maze.append(Square(x,y))

startX = random.randint(0, tall)
startY = random.randint(0, wide)

def mazeCreate():
    if(findneighbor(startX,startY) == 0 and not visited(maze.index(startX * 10 + startY - 10))):
        createnode(startX, startY, 0)
    elif(findneighbor(startX,startY) == 1 and not visited(maze.index(startX * 10 + startY - 1))):
        createnode(startX, startY, 1)
    elif (findneighbor(startX, startY) == 2 and not visited(maze.index(startX * 10 + startY + 10))):
        createnode(startX, startY, 2)
    elif (findneighbor(startX, startY) == 3 and not visited(maze.index(startX * 10 + startY + 1))):
        createnode(startX, startY, 3)
    else:
        if not allTried():
            backup()
            mazeCreate()
        else:
            #implement graphics here
            temp = -1


def findneighbor(startX,startY):
    neighborWall = random.randint(0,4)
    if neighborWall == 0 and startX != 0:
        return 0
    elif neighborWall == 1 and startY != 0:
        return 1
    elif neighborWall == 2 and startX != 9:
        return 2
    elif neighborWall == 3 and startY != 9:
        return 3
    else:
        return -1


def visited(square):
        return square.visited

def createnode(startX, startY, int):
    startingIndex = (startX * 10 + startY)
    if(int == 0):
        nodes.append(Node(maze.index((startingIndex)),maze.index(startingIndex-10)))
        maze.index(startingIndex - 10).visited = True
        maze.index((startingIndex)).left = False
        maze.index(startingIndex - 10).right = False
        visited.append(maze.index(startingIndex - 10))
        recenter(maze.index(startingIndex-10))

    elif(int == 1):
        nodes.append(Node(maze.index(startingIndex), maze.index(startingIndex - 1)))
        maze.index(startingIndex - 1).visited = True
        maze.index((startingIndex)).top = False
        maze.index(startingIndex - 1).bottom = False
        visited.append(maze.index(startingIndex - 1))
        recenter(maze.index(startingIndex - 1))

    elif (int == 2):
        nodes.append(Node(maze.index(startingIndex), maze.index(startingIndex + 10)))
        maze.index(startingIndex + 10).visited = True
        maze.index((startingIndex)).right = False
        maze.index(startingIndex + 10).left = False
        visited.append(maze.index(startingIndex + 10))
        recenter(maze.index(startingIndex + 10))

    elif (int == 3):
        nodes.append(Node(maze.index(startingIndex), maze.index(startingIndex + 1)))
        maze.index(startingIndex + 1).visited = True
        maze.index((startingIndex)).bottom = False
        maze.index(startingIndex + 1).top = False
        visited.append(maze.index(startingIndex + 1))
        recenter(maze.index(startingIndex + 1))

def allTried():
    if(len(maze) == len(visited)):
        return True
    else:
        return False

def backup():
    temp = -1
def recenter(square):
    startX = square.x
    startY = square.y
