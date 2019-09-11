


Skip to content
Using Gmail with screen readers
maze 

6 of 17
maze
Inbox
x

ronak patel <ronpatel279@gmail.com>
Attachments
Dec 8, 2018, 10:29 PM
to me


Attachments area

import turtle                    # import turtle library
import time
import sys

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.setup(1300,700)                  # setup the dimensions of the working window

S = [[0,1,1000,5,6,7],
    [1,2,3,4,5,1000],
    [2,3,1000,1000,6,7],
    [1000,4,5,1000,7,8]]

G = [[8,7,1000,5,4,5],
    [7,6,5,4,3,1000],
    [8,7,1000,1000,2,1],
    [1000,8,9,1000,1,-2]]

V = [[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

f = 8

# class for the Maze turtle (white square)
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)                   # sets the speed that the maze is written to the screen

# class for the End marker turtle (green square)
class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Path(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

# class for the sprite turtle (red turtle)
class sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("classic")
        self.color("red")
        self.setheading(90)  # point turtle to point down
        self.penup()
        self.speed(0)
        self.turtlesize()

    def idaStar(self, row, column):
        time.sleep(0.2)

        if(row == 3 and column == 5):
            print("done")
            endProgram()

        V[row][column] = 1;
        screen_x = -564 + (column * 24)  # assign screen_x to screen starting position for x ie -588
        screen_y = 263 - (row * 24)
        path.goto(screen_x, screen_y)
        path.stamp()

        # F of Right-----------------------------------------------------
        if (column < 5):
            f1 = S[row][column+1] + G[row][column+1]
        else:
            f1 = 1000

        # F of Up ------------------------------------------------------
        if(row > 0):
            f2 = S[row-1][column] + G[row-1][column]
        else:
            f2 = 1000

        # F of Down ----------------------------------------------------
        if(row < 3):
            f3 = S[row+1][column] + G[row+1][column]
        else:
            f3 = 1000

        # F of Left ---------------------------------------------------
        if (column > 0):
            f4 = S[row][column-1] + G[row][column-1]
        else:
            f4 = 1000

        # Compare all Fs and find the lowest one -----------------------------------------------------------

        if(f1 <= f2):
            if(f1 <= f3):
                if(f1 <= f4):
                    lowestf = "f1"
                else:
                    lowestf = "f4"
            else:
                if (f3 <= f4):
                    lowestf = "f1"
                else:
                    lowestf = "f4"
        else:
            if(f2 <= f3):
                if (f2 <= f4):
                    lowestf = "f2"
                else:
                    lowestf = "f4"
            else:
                if (f3 <= f4):
                    lowestf = "f3"
                else:
                    lowestf = "f4"

        # If going Right is the cheapest
        if(lowestf == "f1" and column < 5 and V[row][column+1] != 1):
            self.move("right")
            self.idaStar(row, column + 1)

        # If going Up is the cheapest
        elif (lowestf == "f2" and row > 0 and V[row-1][column] != 1):
            self.move("up")
            self.idaStar(row - 1, column)

        # If going Down is the cheapest
        elif (lowestf == "f3" and row < 3 and V[row+1][column] != 1):
            self.move("down")
            self.idaStar(row + 1, column)

        # If going left is the cheapest
        elif (lowestf == "f4" and column > 0 and V[row][column-1] != 1):
            self.move("left")
            self.idaStar(row, column - 1)

        else:
            self.move("down")
            self.idaStar(row + 1, column)

    def move(self, direction):
         if(direction == "right"):
             if (self.heading() == 0):
                 self.forward(24)
             elif (self.heading() == 90):
                 self.turnRight(1)
             elif (self.heading() == 180):
                 self.turnRight(2)
             elif (self.heading() == 270):
                 self.turnRight(3)

         if (direction == "up"):
             if (self.heading() == 0):
                 self.turnLeft(1)
             elif (self.heading() == 90):
                 self.forward(24)
             elif (self.heading() == 180):
                 self.turnRight(1)
             elif (self.heading() == 270):
                 self.turnRight(2)

         if (direction == "down"):
             if (self.heading() == 0):
                 self.turnRight(1)
             elif (self.heading() == 90):
                 self.turnRight(2)
             elif (self.heading() == 180):
                 self.turnLeft(1)
             elif (self.heading() == 270):
                 self.forward(24)

         if (direction == "left"):
             if (self.heading() == 0):
                 self.turnRight(2)
             elif (self.heading() == 90):
                 self.turnLeft(1)
             elif (self.heading() == 180):
                 self.forward(24)
             elif (self.heading() == 270):
                 self.turnRight(1)

    def turnRight(self, turn):
        for x in range(turn):
            self.right(90)
        self.forward(24)

    def turnLeft(self, turn):
        for x in range(turn):
            self.left(90)
        self.forward(24)


def endProgram():
    wn.exitonclick()
    sys.exit()


grid = [
"++++++++",
"+s +   +",
"+     ++",
"+  ++  +",
"++  + g+",
"++++++++",
]


def setupMaze(grid):
    for y in range(len(grid)):                       # select each line in the grid
        for x in range(len(grid[y])):                # identify each character in the line
            character = grid[y][x]                   # assign the grid reference to the variable character
            screen_x = -588 + (x * 24)               # assign screen_x to screen starting position for x ie -588
            screen_y = 288 - (y * 24)                # assign screen_y to screen starting position for y ie  288

            if character == "+":                     # if grid character contains an +
                maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                walls.append((screen_x, screen_y))   # add coordinate to walls list

            if character == "g":                     # if grid character contains an e
                end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                finish.append((screen_x, screen_y))  # add coordinate to finish list

            if character == "s":                     # if the grid character contains an s
                sprite.goto(screen_x, screen_y)      # move turtle to the x and y location

# ############ main program starts here  ######################

maze = Maze()                # enable the maze class
path = Path()
sprite = sprite()            # enable the sprite  class
end = End()                  # enable End position class
walls =[]                    # create walls coordinate list
finish = []                  # enable the finish array

setupMaze(grid)              # call the setup maze function
sprite.idaStar(0,0)
time.sleep(0.8)
Test.py
Displaying Test.py.