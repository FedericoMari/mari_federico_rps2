# this file was created by Federico Mari on 9/25/2023

# import packages for different modules: time, turtle, random, and os 
from random import randint
import time
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os

# define the working directories with paths and directory names
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
# join the paths for two different folders
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window in turtle
WIDTH, HEIGHT = 1000, 400

# height and width for the three images of rock, paper, or scissors
rock_w, rock_h = 256, 280
paper_w, paper_h = 256, 204
scissors_w, scissors_h = 256, 170 

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8) 
# set a sort of origin point in turtle, or where the center point is focalized
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
# set a screen size using width and height as arguments that are passde through the screensize function
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="red")

# canvas object function
cv = screen.getcanvas()
# "hack" to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image for both user and cpu
rock_image = os.path.join(images_folder, 'rock.gif')
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
# instantiate (create an instance of) the Turtle class for the rock for both user and cpu
rock_instance = turtle.Turtle()
cpu_rock_instance = turtle.Turtle()

# repetition of same code above for paper:
paper_image = os.path.join(images_folder, 'paper.gif')
cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
paper_instance = turtle.Turtle()
cpu_paper_instance = turtle.Turtle()

# repetition of code for scissors:
scissors_image = os.path.join(images_folder, 'scissors.gif')
cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
scissors_instance = turtle.Turtle()
cpu_scissors_instance = turtle.Turtle()

# create six functions, one for user and another for cpu with x, y as parameters to define how turtle functions
def user_show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image with the instance of the rock
    rock_instance.shape(rock_image)
    # create instance for penup function so it does not overlap drawings
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)
    # create instance for penup function

# for cpu only
def cpu_show_rock(x,y):
    screen.addshape(cpu_rock_image)
    cpu_rock_instance.shape(cpu_rock_image)
    cpu_rock_instance.penup()
    cpu_rock_instance.setpos(x,y)

def user_show_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    screen.addshape(cpu_paper_image)
    cpu_paper_instance.shape(cpu_paper_image)
    cpu_paper_instance.penup()
    cpu_paper_instance.setpos(x,y)

def user_show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(cpu_scissors_image)
    cpu_scissors_instance.penup()
    cpu_scissors_instance.setpos(x,y)

# function to randomize cpu selection based on specific choices in a set list
def cpu_select():
    choices = ['rock', 'paper', 'scissors']
    # utilize the randint function from the imported random module
    return choices[randint(0,2)]

# create function with input parameters of message, x, y:
def write_text(message, x, y):
    # remove the text written using hideturtle function
    text.hideturtle()
    # set text color to desired argument color
    text.color('black')
    # make sure turtle doesn't overlap
    text.penup()
    # reset screen without text for new text
    text.clear()
    # define the position of text on screen (will later be called back with individual arguments)
    text.setpos(x,y)
    # define the text's characteristics; what it will look like to user:
    text.write(message, False, "center", ("Times New Roman", 24, "normal"))

# call back all functions with individual arguments for the user image positions:
user_show_rock(-300,0)
user_show_paper(0,0)
user_show_scissors(300,0)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
# set the text color to another color argument:
text.color('deep pink')
# hide each turtle text outside of function
text.hideturtle()

# hide the turtle images, if needed
t.hideturtle()

# this function uses x,y,obj,w,h as input parameters in function
def collide(x,y,obj,w,h):
    # if statement defining pos of three images
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        # boolean defining what to do if True
        return True
        # boolean defining what to do if False
    else: 
        return False
    
  # writes the intial text that will introduce the game...
write_text("Let's play some rock, paper, scissors!!", 0, 150 )

# function that passes through wn onlick
def user_mouse_pos(x,y):
    # create an infinite loop
    while True:
    # call back function for the random cpu selection inside user_mouse_pos function 
        print(cpu_select())
        # define what the code will do for a specific random choice in cpu_select function
        cpu_picked = cpu_select()
        if collide(x,y,rock_instance,rock_w,rock_h):
            # repeat this block of code 3 times:
            write_text("You chose ROCK!", 0, 150 )
            # time function imported from time module, stops code for one second exactly
            time.sleep(1)
            if cpu_picked == "rock":
                write_text("The computer picked rock too!", 0, 150)
                # move/ hide the turtle instance of the scissors image and paper image since rock is the only necessary one
                user_show_scissors(2000, 0)
                user_show_paper(2000, 0) 
                # move rock instances to opposite sides of graphic
                cpu_show_rock(300, 0)
                user_show_rock(-300, 0)
                # tell user what has happened and position it in a specific place
                write_text("Seems it would be a tie...", 0, 150 )
                break
            elif cpu_picked  == "paper":
                write_text("The computer picked paper!!", 0, 150)
                user_show_scissors(-2000, 0)
                user_show_rock(-300, 0)
                user_show_paper(300, 0) 
                time.sleep(0.3)
                user_show_rock(-2000, 0)
                user_show_paper(0, 0)
                write_text("Computer wins!!", 0 , 150)
                break
            elif cpu_picked == "scissors":
                write_text("The computer picked scissors!!", 0, 150)
                user_show_paper(-2000, 0) 
                user_show_rock(-300, 0)
                user_show_scissors(2000, 0)
                user_show_rock(0, 0)
                write_text("Wow, you beat the computer...", 0, 150)
                break
        elif collide(x,y,paper_instance,paper_w,paper_h):
            write_text("You chose PAPER!", 0, 150 )
            time.sleep(1)
            if cpu_picked == "paper":
                write_text("The computer chose paper!!", 0, 150)
                user_show_rock(-2000, 0)
                user_show_scissors(2000, 0)
                cpu_show_paper(300, 0)
                user_show_rock(-300, 0)
                write_text("Oops, looks like there's a tie...", 0, 150)
                break
            elif cpu_picked == "scissors":
                write_text("The computer chose scissors!!", 0, 150)
                user_show_rock(-2000, 0)
                user_show_paper(-300, 0)
                user_show_scissors(300, 0)
                time.sleep(0.3)
                user_show_paper(-2000, 0)
                user_show_scissors(0, 0)
                write_text("Seems you have lost...", 0, 150)
                break
            elif cpu_picked == "rock":
                write_text("The computer uses rock!!", 0,150)
                user_show_scissors(2000, 0)
                user_show_paper(300, 0)
                user_show_rock(-300, 0)
                time.sleep(0.3)
                user_show_rock(-2000, 0)
                user_show_paper(0, 0)
                write_text("You are triumphant!!", 0, 150)
                break
        elif collide(x,y,scissors_instance,scissors_w,scissors_h):
            write_text("You chose SCISSORS!", 0, 150 )
            time.sleep(1)
            if cpu_picked == "scissors":
                write_text("The computer uses scissors!!", 0,150)
                user_show_paper(0, -2000)
                user_show_rock(-2000, 0)
                user_show_scissors(300, 0)
                cpu_show_scissors(-300, 0)
                write_text("It appears we have a tie on our hands...", 0, 150)
                break
            elif cpu_picked == "paper":
                write_text("The computer chose paper!!", 0, 150)
                user_show_rock(-2000, 0)
                user_show_scissors(-300, 0)
                user_show_paper(300, 0)
                time.sleep(0.3)
                user_show_paper(2000, 0)
                user_show_scissors(0, 0)
                write_text("Darn, looks like you beat the computer...", 0, 150)
                break
            elif cpu_picked == "rock":
                write_text("This computer uses rock!!", 0, 150)
                user_show_paper(0, -2000)
                user_show_scissors(300, 0)
                user_show_rock(-300, 0)
                time.sleep(0.3)
                user_show_scissors(2000, 0)
                user_show_rock(0, 0)
                write_text("The computer won!!!", 0, 150)
                break
        else:
            # validate user's input in the first place, if false, then exit code and restart
            write_text("You chose NOTHING dude?!?!", 0, 150 )
            break

# with screen on, where ever user clicks, computer executs a piece of the user_mouse_pos function
screen.onclick(user_mouse_pos)

# runs mainloop for Turtle - required to be last
screen.mainloop()