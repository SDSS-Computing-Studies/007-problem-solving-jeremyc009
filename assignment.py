import pyautogui as p
import time as t
# To run game, put the link on the left half of the screen 
#https://games.cdn.famobi.com/html5games/p/piano-steps/v080/?fg_domain=play.famobi.com&fg_aid=A-BESTARCADE&fg_uid=3261efa7-0ff9-4016-af38-d5afa79f2211&fg_pid=3df41947-b71e-4659-b3ae-c1afe0508e57&fg_beat=844&original_ref=https%3A%2F%2Fgames.cdn.famobi.com%2F
#Navigate to the screen with all the game modes(Classic, arcade, etc.)
#Run the program, and it will continue going through the classic mode with 25 tiles before you stop it.
#If you want to change the amount of tiles the game will go through:
#Go to line 41 and change (0,25) to (0,50) or (0,75)
#Go to line 16 and change coord[1]-75 to coord[1] for 50 tiles and coord[1]+75 for 75 tiles.
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
def click2(coord):
    p.moveTo(coord[0]+100,coord[1]+290)
    p.mouseDown()
    p.mouseUp()
def click3(coord):
    p.moveTo(coord[0]-40,coord[1]+100)
    p.mouseDown()
    p.mouseUp()
def gameopen():
    coord1=p.locateCenterOnScreen("1rcade.png")
    click1(coord1)


    

def gameplay():

    coord2=p.locateCenterOnScreen("play.png")
    click(coord2)
    for i in range(0,25):

        coord=[]
        if p.pixelMatchesColor(365,625,(5,5,5)):
                coord=[365,625]
                click(coord)
        elif p.pixelMatchesColor(445,630,(5,5,5)):
                coord=[445,630]
                click(coord)
        elif p.pixelMatchesColor(520,630,(5,5,5)):
                coord=[520,630]
                click(coord)
        elif p.pixelMatchesColor(600,630,(5,5,5)):
                coord=[600,630]
                click(coord)

                
 

                
gameopen()
while True:
        gameplay()
        t.sleep(2)
        coord1=[475,600]
        coord2=[475,630]
        click(coord1)
        t.sleep(0.5)
        click(coord2)        


