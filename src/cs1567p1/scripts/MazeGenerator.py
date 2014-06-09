#!/usr/bin/python
import rospy
from cs1567p1.srv import *
from std_srvs.srv import * 
import sys
from random import randint
from random import shuffle

MazeGrid = [[]]
Columns = 0
Rows = 0

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def createGrid(rows,cols):
    global MazeGrid, LEFT, RIGHT, UP, DOWN
    global Columns 
    Columns = cols
    global Rows 
    Rows = rows
#index col,then row
    MazeGrid = [[[LEFT, RIGHT, UP, DOWN] for x in xrange(rows)] for y in xrange(cols)]
    for i in xrange(cols):
        MazeGrid[i][0].remove(UP)
        MazeGrid[i][rows-1].remove(DOWN)
    for j in xrange(rows):
        MazeGrid[0][j].remove(LEFT)
        MazeGrid[cols-1][j].remove(RIGHT)
    #print MazeGrid #printing each column left to right

def getWall(col, row, direction):
    if row == 0 and direction == UP:
        return True
    if row == Rows-1 and direction == DOWN:
        return True
    if col == 0 and direction == LEFT:
        return True
    if col == Columns-1 and direction == RIGHT:
        return True
    return MazeGrid[col][row].count(direction) > 0

def printMaze():
    s = ""
    for j in xrange(0,Columns):
        s = s+" _"
    s = s+"\n"
    for i in xrange(0,Rows):
        s = s+"|"
        for j in xrange(0,Columns):
            if MazeGrid[j][i].count(DOWN) > 0 or i == Rows-1:
                s = s+"_"
            else:
                s = s+" "
            if MazeGrid[j][i].count(RIGHT) > 0 or j == Columns-1:
                s = s+"|"
            else:
                s = s+" "
            if j == Columns-1:
                s = s+"\n"
    return s

def makeMaze():
    global LEFT, RIGHT, UP, DOWN

    visited = []
    stack = []

    while len(visited) < Rows*Columns:
        if len(stack) > 0:
            [col,row] = stack[0]
            
            neighbors = MazeGrid[col][row]
            shuffle(neighbors)
            nextidx = -1
            neighbordirection = LEFT
            for i in xrange(len(neighbors)):
                [neighborcol,neighborrow] = [col,row]
                if neighbors[i] == LEFT:
                    neighborcol = col-1
                    neighbordirection = RIGHT
                elif neighbors[i] == RIGHT:
                    neighborcol = col+1
                    neighbordirection = LEFT
                elif neighbors[i] == UP:
                    neighborrow = row-1
                    neighbordirection = DOWN
                elif neighbors[i] == DOWN:
                    neighborrow = row+1
                    neighbordirection = UP
                else:
                    print "ERROR"
                if visited.count([neighborcol,neighborrow]) == 0:
                    nextidx = i
                    break

            if len(neighbors) > 0 and nextidx > -1:
                #pick unvisited neighbor, remove line, add neighbor to stack
                stack.insert(0,[neighborcol,neighborrow])
                visited.append([neighborcol,neighborrow])
                #print "removing "+str([neighborcol,neighborrow,neighbordirection])+" and "+str([col,row,MazeGrid[col][row][nextidx]])
                MazeGrid[neighborcol][neighborrow].remove(neighbordirection)
                MazeGrid[col][row].remove(neighbors[nextidx])

            else:
                stack.pop(0)
        else:
            randrow = randint(0,Rows-1)
            randcol = randint(0,Columns-1)
            visited.append([randcol,randrow])
            stack = [[randcol,randrow]]
    #print MazeGrid

def make_maze(parameters):
    createGrid(parameters.rows,parameters.cols)
    makeMaze()
    return 1

def print_maze(parameters):
    print printMaze()
    return EmptyResponse()

def get_maze_wall(parameters):
    if getWall(parameters.col, parameters.row, parameters.direction):
        return 1
    return 0

def initialize_commands():
    rospy.init_node('mazegenerationnode', anonymous=True)
    
    s1 = rospy.Service('make_maze', MakeNewMaze, make_maze)
    s2 = rospy.Service('print_maze', Empty, print_maze)
    s3 = rospy.Service('get_wall', GetMazeWall, get_maze_wall)

    rospy.spin()

     
if __name__ == "__main__":   
    try: 
        initialize_commands()
    except rospy.ROSInterruptException: pass

