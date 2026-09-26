import pgzrun
import random
W=700
H=700
CENTER_X = W/2
CENTER_Y = H/2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"]

game_over = False
game_complete = False
current_level = 1

item_list = []
animation_list = []

def draw():
    global game_over, game_complete, current_level, item_list
    screen.clear()
    screen.blit("bground",(0,0))
    if game_over:
        display_message("gameover","try again")
    elif game_complete:
        display_message("congrats you won the game!")
    else:
        for item in item_list:
            item.draw()
    










pgzrun.go()