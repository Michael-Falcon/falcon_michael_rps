# This file was created by: Michael Falcon

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
have t

'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')

# Used this resource to include sound
# https://www.youtube.com/watch?v=w6g8PO-Pqp4
def play_rock():
    winsound.PlaySound(os.path.join(sounds_folder, 'rock.wav'), winsound.SND_ASYNC)
def play_paper():
    winsound.PlaySound(os.path.join(sounds_folder, 'paper.wav'), winsound.SND_ASYNC)
def play_scissors():
    winsound.PlaySound(os.path.join(sounds_folder, 'scissors.wav'), winsound.SND_ASYNC)

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

player_choice = ""

cpu_choice = ""

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
cpu_rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
cpu_paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
cpu_scissors_instance = turtle.Turtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(cpu_rock_image)
    # attach the rock_image to the rock_instance
    cpu_rock_instance.shape(cpu_rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    cpu_rock_instance.penup()
    # set the position of the rock_instance
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(cpu_paper_image)
    # attach the paper_image to the paper_instance
    cpu_paper_instance.shape(cpu_paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    cpu_paper_instance.penup()
    # set the position of the paper_instance
    cpu_paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)
def cpu_show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(cpu_scissors_image)
    # attach the scissors_image to the scissors_instance
    cpu_scissors_instance.shape(cpu_scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    cpu_scissors_instance.penup()
    # set the position of the scissors_instance
    cpu_scissors_instance.setpos(x,y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)


# function that passes through wn onlick

def mouse_pos(x, y):
        # print("it is " + str(collide(x,y,rock_instance,rock_w,rock_h)) +  " that I collided with rock")
        # print("it is " + str(collide(x,y,paper_instance,paper_w,paper_h)) +  " that I collided with paper")
        # print("it is " + str(collide(x,y,scissors_instance,scissors_w,scissors_h)) +  " that I collided with scissors")
    print(cpu_select())
    cpu_picked = cpu_select()
    if collide(x,y,rock_instance,rock_w,rock_h):
        print("I collided with rock...")
        text.clear()
        text.write("you chose rock", False, "left", ("Arial", 24, "normal"))
        scissors_instance.hideturtle()
        paper_instance.hideturtle()
        play_rock()
        if cpu_picked == "rock":
            cpu_show_rock(-300,0)
            show_rock(-300,0)
            text.clear()
            text.write("cpu chose rock; it is a tie, please exit to play again", False, "left", ("Arial", 24, "normal"))
            rock_instance.hideturtle()
            cpu_rock_instance.hideturtle()
            
        elif cpu_picked == "scissors":
            cpu_show_scissors(-300,0)
            show_rock(-300,0)
            text.clear()
            text.write("cpu chose scissors; you win", False, "left", ("Arial", 24, "normal"))
            rock_instance.hideturtle()
            cpu_scissors_instance.hideturtle()
       
        elif cpu_picked == "paper":
            cpu_show_paper(-300,0)
            show_rock(-300,0)
            text.clear()
            text.write("cpu chose paper; you lost", False, "left", ("Arial", 24, "normal"))
            rock_instance.hideturtle()
            cpu_paper_instance.hideturtle()
          
    if collide(x,y,paper_instance,paper_w,paper_h):
            print("I collided with paper")
            text.clear()
            text.write("you chose paper", False, "left", ("Arial", 24, "normal"))
            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            play_paper()
            if cpu_picked == "rock":
                cpu_show_rock(0,0)
                show_paper(0,0)
                text.clear()
                text.write("cpu chose rock; You won", False, "left", ("Arial", 24, "normal"))
                cpu_rock_instance.hideturtle()
                paper_instance.hideturtle()
            elif cpu_picked == "scissors":
                cpu_show_scissors(0,0)
                show_paper(0,0)
                text.clear()
                text.write("cpu chose scissors; You lost", False, "left", ("Arial", 24, "normal"))
                paper_instance.hideturtle()
                cpu_scissors_instance.hideturtle()
            elif cpu_picked == "paper":
                cpu_show_paper(0,0)
                show_paper
                text.clear()
                text.write("cpu chose paper; you tied", False, "left", ("Arial", 24, "normal"))
                paper_instance.hideturtle()
                cpu_paper_instance.hideturtle()
            
    if collide(x,y,scissors_instance,scissors_w,scissors_h):
            print("I collided with scissors")
            text.clear()
            text.write("you chose scissors", False, "left", ("Arial", 24, "normal"))
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            play_scissors()
            if cpu_picked == "rock":
                cpu_show_rock(300,0)
                show_scissors(300,0)
                text.clear()
                text.write("cpu chose rock; You lost", False, "left", ("Arial", 24, "normal"))
                cpu_rock_instance.hideturtle()
                scissors_instance.hideturtle()
            elif cpu_picked == "scissors":
                cpu_show_scissors(300,0)
                show_scissors(300,0)
                text.clear()
                text.write("cpu chose scissors; It is a tie", False, "left", ("Arial", 24, "normal"))
                scissors_instance.hideturtle()
                cpu_scissors_instance.hideturtle()
            elif cpu_picked == "paper":
                cpu_show_paper(300,0)
                show_scissors(300,0)
                text.clear()
                text.write("cpu chose paper; you won", False, "left", ("Arial", 24, "normal"))
                scissors_instance.hideturtle()
                cpu_paper_instance.hideturtle()

    
            

text.setpos(-400,150)
text.write("Select rock, paper, or scissors", False, "left", ("Arial", 24, "normal"))

# user this to get mouse position
screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()














