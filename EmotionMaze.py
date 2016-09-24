#Must Install numpy package before runtime
#Must Install easyTinker before runtime
import numpy as np
import random

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self.haswall = True
        self.visited = False

class Node:
    def __init__(self,squareOne,squareTwo):
        self.squareOne = squareOne
        self.squareTwo = squareTwo

tall = 10
wide = 10
maze = list()
visited = list()
for x in range(0,tall):
    for y in range(0,wide):
        maze.append(Square(x,y))

startX = random.randint(0, tall)
startY = random.randint(0, wide)
def mazeCreate():
    if(findneighbor(startX,startY) == 0):
        createnode(startX, startY, 0)
    elif(findneighbor(startX,startY) == 1):
        createnode(startX, startY, 1)
    elif (findneighbor(startX, startY) == 2):
        createnode(startX, startY, 2)
    elif (findneighbor(startX, startY) == 3):
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
    if(neighborWall == 0 and startX != 0):
        return 0
    elif(neighborWall == 1 and startY != 0):
        return 1
    elif(neighborWall == 2 and startX != 9):
        return 2
    elif(neighborWall == 3 and startY != 9):
        return 3
    else:
        return -1


def visited(square):
        return square.visited

def createnode():
    ver = 7

def allTried():
    ver = 8
def backup():
    temp = -1