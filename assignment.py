import pyautogui as p
import time as t

def click1(coord):
    p.moveTo(coord[0],coord[1])
    p.mouseDown()
    
    p.mouseUp()
    
    p.moveTo(coord[0],coord[1]-75)
    p.mouseDown()
    p.mouseUp()
def click(coord):
    p.moveTo(coord[0],coord[1])
    p.mouseDown()
    p.mouseUp()

def gameopen():
    coord1=p.locateCenterOnScreen("1rcade.png")
    click1(coord1)


    click1(coord1)

def gameplay():
    coord2=p.locateCenterOnScreen("play.png")
    click(coord2)
    colour=()
    colour2=()
    colour3=()
    colour4=()
    while colour!=(219,0,0) and colour2!=(219,0,0) and colour3!=(219,0,0) and colour4!=(219,0,0):
        square=p.locateCenterOnScreen("square.png")
        click(square)
        colour=p.pixel(350,750)
        colour2=p.pixel(435,750)
        colour3=p.pixel(545,750)
        colour4=p.pixel(600,750)



gameopen()
gameplay()