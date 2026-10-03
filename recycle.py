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

item_list = []#to store the list of final items we're going to display
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

def update():
    global item_list
    if len(item_list) == 0:
        items_list = make_items(current_level)
#it will generate items based on the current level
def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items


#this function is to select item to create for a label
def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper_bag"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

#this is of all created actors for the given name
def create_items(items_to_create):
    new_items=[]
    for pic in items_to_create:
        item = Actor(pic + "img")
        new_items.append(item)
    return new_items

#to decide the layout of the items on the screen
def layout_items(items_to_layout):
    num_of_gaps = len(items_to_layout)+1
    gap_size = W/num_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1)*gap_size
        item.x = new_x_pos

#how to animate the items
def animate_items(items_to_animate):
    pass

#if you hit any other item execpt paper bag it will end game
def handle_game_over():
    pass

#to check the collision detection for mouse click on items
def on_mouse_down(pos):
    pass

#handle the game completion
def handle_game_complete():
    pass

#control the animation
def stop_animation(animations_to_stop):
    pass



    










pgzrun.go()
