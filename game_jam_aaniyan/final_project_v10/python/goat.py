import sys
import os
import pygame
from pygame.locals import *
import random

sys.path.insert(0, os.path.dirname(os.getcwd())) # goes to user's main directory
import engine.play as pl
import engine.utility as util
import engine.ui as ui
import engine.sound as sound
import engine.asset as asset
import engine.physics as phy
import engine.actor as act



SCREEN_HEIGHT = 768
SCREEN_WIDTH = 1000

CREDIT_NAMES = 'Wenting Xu, Akhila Mol Aniyan, Miranda Sandoval'

def create_right_button(color, button_x_start_pos, scroll_speed, button_width, \
	button_height):
	right_rect_width = button_width
	right_rect_height = button_height
	right_rect_x_start_pos = button_x_start_pos
	right_rect_y_start_pos = random.randrange(50, 750)

	right_rect_bounds = [right_rect_x_start_pos,right_rect_y_start_pos, \
	right_rect_width,right_rect_height]
	right_button = ui.make_button(color,right_rect_bounds,scroll_speed)
	draw_right_button = ui.make_draw_button_action()
 
	my_move_left_action = ui.make_move_button_left_action()
	my_reset_button_position = ui.make_reset_position_action()
	press_right_button = ui.make_press_button_action()

	right_button.insert_action(draw_right_button)
	my_screen_display.insert_child(draw_right_button)
	right_button.insert_action(my_reset_button_position)
	right_button.insert_action(my_move_left_action)
	right_button.insert_action(press_right_button)

	my_loop.insert_action(my_reset_button_position)
	my_loop.insert_action(my_move_left_action)
	my_loop.insert_action(press_right_button)

	my_loop.insert_entity(right_button)

	right_button.active = False

	return right_button

#-----------------  frame viewer -----------------------
########################################################

my_screen = pl.make_frame_viewer(SCREEN_WIDTH,SCREEN_HEIGHT)
my_screen_display = pl.make_screen_display_action()
my_screen.insert_action(my_screen_display)

my_terminate = pl.make_terminate_action()
my_screen.insert_action(my_terminate)

my_loop = pl.make_game_loop()
my_loop.insert_entity(my_screen)


####################################################
# -------- Display Background and set fps ---------- 
####################################################

#parent_dir = os.path.dirname(os.getcwd()) + "\\assets\\textures\\"
#background = ui.make_background(4, (os.path.join(parent_dir, "bg.png")))
background = ui.make_background(4,"./../assets/textures/bg.png")
background.set_bg_size()
draw_background = ui.make_draw_background_action()
background.insert_action(draw_background)
my_screen_display.insert_child(draw_background)
my_loop.insert_entity((background))


#-----------------  colors ----------------------------
########################################################

green_color = [37,139,34]
red_color = [139,0,0]
white_color = [255,255,255]
light_coral_color = [240,128,128]
khaki_color = [240,230,140]
power_blue_color=[176,224,230]
misty_rose_color=[255,228,225]
saddle_brown_color=[139,69,19]
black_color=[0,0,0]


#------------------- entitys for all levels-------------
########################################################


#------- 1: player button moves up and down to collect right buttons------------

basic_bounds = [00,50,100,200]
player_button = ui.make_button(power_blue_color, basic_bounds,0)
player_button.active=True
player_button.height_restriction = SCREEN_HEIGHT - player_button.bounds[3] # restricts button movement to bottom of the screen
draw_basic_button = ui.make_draw_button_action()
player_button.insert_action(draw_basic_button)
my_screen_display.insert_child(draw_basic_button) 
my_loop.insert_entity(player_button)

# moves player button up and down 
my_key_pressed_update_position = ui.make_key_pressed_action()
player_button.insert_action(my_key_pressed_update_position)
my_screen_display.insert_child(my_key_pressed_update_position)

# check if player collects star button
my_check_collision = ui.make_check_collision_action()
player_button.insert_action(my_check_collision)
my_loop.insert_action(my_check_collision)


#----  2: star buttons with different score credit, size, velocity, jump speed----

my_jump_button_action_faster = ui.make_jump_button_action(20) # 15 jump velocity
my_loop.insert_action(my_jump_button_action_faster)


#------ 2.1 green buttons: if collide, score = score +1 
# fast button
button_green_fast = create_right_button(green_color,800,6,50,50) 
button_green_fast.active = True # only set level button to True
# medium button
button_green_medium = create_right_button(green_color,800,5,50,50) 
button_green_medium.active = True # only set level button to True
# slow button
button_green_slow = create_right_button(green_color,800,4,50,50) 
button_green_slow.active = True # only set level button to True
# random speed button
button_green_random_speed = create_right_button(green_color,800,random.randrange(2,7),50,50) 
button_green_random_speed.active = True # only set level button to True
# big button
button_green_big = create_right_button(green_color,800,6,100,100) 
button_green_big.active = True # only set level button to True

button_green_big = create_right_button(green_color,800,6,random.randrange(100,150),random.randrange(100,150)) 
button_green_big.active = True # only set level button to True

#------ 2.2 pink buttons :if collide, score = score -1 

button_pink_fast = create_right_button(misty_rose_color,800,3,random.randrange(50,100),random.randrange(50,150)) # fast button
button_pink_medium = create_right_button(misty_rose_color,800,2,random.randrange(50,100),random.randrange(50,150)) # fast button
button_pink_slow = create_right_button(misty_rose_color,800,1,random.randrange(50,100),random.randrange(50,150)) # slow button
button_pink_big = create_right_button(misty_rose_color,800,5,random.randrange(50,100),random.randrange(100,200)) # fast button


#------ 2.3 red buttons :if collide, score = 0

button_red_fast = create_right_button(red_color,800,3,50,50) # fast button
button_red_medium = create_right_button(red_color,800,2,50,50) # fast button
button_red_slow = create_right_button(red_color,800,1,50,50) # slow button
button_red_big = create_right_button(red_color,800,5,random.randrange(50,100),random.randrange(100,150)) # fast button


#------ 2.4 green buttons: shrink size as move; if collide, score = score +1

## action to shrink buttons with fast medium slow speed
my_shrink_button_action_fast = ui.make_change_button_size_action(0.3) 
my_loop.insert_action(my_shrink_button_action_fast)

my_shrink_button_action_slow = ui.make_change_button_size_action(0.1) 
my_loop.insert_action(my_shrink_button_action_slow)

# green button shrink fast
button_green_shrink_fast = create_right_button(green_color,800,2,50,50) # normal
button_green_shrink_fast.insert_action(my_shrink_button_action_fast)

# green button shrink slow
button_green_shrink_slow = create_right_button(green_color,800,2,50,50) # normal
button_green_shrink_slow.insert_action(my_shrink_button_action_slow)


#------ 2.5 red buttons: shrink size as move; if collide, score = 0

button_red_shrink_fast = create_right_button(red_color,800,2,50,50) # normal
button_red_shrink_fast.insert_action(my_shrink_button_action_fast)

button_red_shrink_slow = create_right_button(red_color,800,2,50,50) # normal
button_red_shrink_slow.insert_action(my_shrink_button_action_slow)


#------ 2.6 green buttons: increase size as move; if collide, score = score + 1


my_enlarge_button_action_fast = ui.make_change_button_size_action(-0.3) 
my_loop.insert_action(my_enlarge_button_action_fast)

my_enlarge_button_action_slow = ui.make_change_button_size_action(-0.1) 
my_loop.insert_action(my_enlarge_button_action_slow)

button_green_enlarge_fast = create_right_button(green_color,800,100,50,50) # normal
button_green_enlarge_fast.insert_action(my_shrink_button_action_fast)

button_green_enlarge_slow = create_right_button(green_color,800,100,50,50) # normal
button_green_enlarge_slow.insert_action(my_shrink_button_action_slow)

#------ 2.6 pink buttons: increase size as move; if collide, score = 0

button_pink_enlarge_fast = create_right_button(misty_rose_color,800,2,50,50) # normal
button_pink_enlarge_fast.insert_action(my_shrink_button_action_fast)

button_pink_enlarge_slow = create_right_button(misty_rose_color,800,6,50,50) # normal
button_pink_enlarge_slow.insert_action(my_shrink_button_action_slow)


#------ 2.6 red buttons: increase size as move; if collide, score = 0

button_red_enlarge_fast = create_right_button(red_color,800,20,50,50) # normal
button_red_enlarge_fast.insert_action(my_shrink_button_action_fast)

button_red_enlarge_slow = create_right_button(red_color,800,30,50,50) # normal
button_red_enlarge_slow.insert_action(my_shrink_button_action_slow)


#-------2.7  green buttons that jump to the left with step of 10: score +1
# actions to jump with speed of 10
my_jump_button_action_fast = ui.make_jump_button_action(10) # 10 jump velocity/speed
my_loop.insert_action(my_jump_button_action_fast)
# actions to jump with speed of 5
my_jump_button_action_slow = ui.make_jump_button_action(5) # 10 jump velocity/speed
my_loop.insert_action(my_jump_button_action_slow)

#green button jump with speed of 10
button_green_jump_fast = create_right_button(green_color,800, 10,80,80) # appear ealier
button_green_jump_fast.insert_action(my_jump_button_action_fast) # add this to alarm as child

#green button jump with speed of 10
button_green_jump_slow = create_right_button(green_color,800, 11,80,80) # appear ealier
button_green_jump_slow.insert_action(my_jump_button_action_slow) # add this to alarm as child


#-------2.7  pink buttons that jump to the left with step of 10: score +1

#pink button jump with speed of 10
button_pink_jump_fast = create_right_button(misty_rose_color,800, 12,80,80) # appear ealier
button_pink_jump_fast.insert_action(my_jump_button_action_fast) # add this to alarm as child

#pink button jump with speed of 5
button_pink_jump_slow = create_right_button(misty_rose_color,800, 12,80,80) # appear ealier
button_pink_jump_slow.insert_action(my_jump_button_action_slow) # add this to alarm as child



#--------------------- level definiation----------------------
# level advances when score = 5
critical_score = 5

# buttons are arranged according to dangerous level , 0 is safest

safe_buttons = [button_green_random_speed,button_green_shrink_fast,button_green_shrink_slow,button_green_slow,\
				button_green_medium,button_green_fast,button_green_big,\
				button_green_jump_slow,button_green_jump_fast,\
				button_green_enlarge_slow, button_green_enlarge_fast
				]

dangerous_buttons = [button_pink_slow,button_pink_medium,button_pink_fast, button_pink_big, \
					button_red_shrink_fast,button_red_shrink_fast,\
					button_pink_jump_slow, button_pink_jump_fast,\
					button_red_slow,button_red_medium,button_red_fast,\
					button_pink_enlarge_slow,button_pink_enlarge_fast,\
					button_red_enlarge_slow,button_red_shrink_fast, button_red_big]

all_star_buttons = safe_buttons + dangerous_buttons


# add safe and dangerous buttons as children to player button to detect collision
for star_button in all_star_buttons:
	player_button.insert_child_button(star_button)


#--- all levels

level_1 = safe_buttons[0:2]
level_2 = safe_buttons[0:2] +dangerous_buttons[0:1]
level_3 = safe_buttons[0:2] +dangerous_buttons[0:2]
level_4 = safe_buttons[1:2] +dangerous_buttons[1:2]
level_5 = safe_buttons[1:3] +dangerous_buttons[1:3]
level_6 = safe_buttons[2:3] +dangerous_buttons[2:3]
level_7 = safe_buttons[2:3] +dangerous_buttons[2:4]
level_8 = safe_buttons[3:4] +dangerous_buttons[3:4]
level_9 = safe_buttons[3:4] +dangerous_buttons[3:5]
level_10 = safe_buttons[4:5] +dangerous_buttons[4:5]
level_11 = safe_buttons[4:5] +dangerous_buttons[4:5]
level_12 = safe_buttons[5:7] +dangerous_buttons[5:6]
level_13 = safe_buttons[5:7] +dangerous_buttons[5:6]
level_14 = safe_buttons[6:7] +dangerous_buttons[6:7]
level_15 = safe_buttons[6:7] +dangerous_buttons[6:7]
level_16 = safe_buttons[7:8] +dangerous_buttons[7:8]
level_17 = safe_buttons[7:8] +dangerous_buttons[7:8]
level_18 = safe_buttons[8:9] +dangerous_buttons[8:9]
level_19 = safe_buttons[8:9] +dangerous_buttons[8:9]
level_20 = safe_buttons[9:10] +dangerous_buttons[9:10]
level_21 = safe_buttons[9:10] +dangerous_buttons[9:10]
level_22 = safe_buttons[9:10] +dangerous_buttons[10:13]
level_23 = safe_buttons[9:10] +dangerous_buttons[10:15]


level_entitys = [level_1,level_2,level_3,level_4,level_5,level_6,level_7,level_8,level_9,
				level_10,level_11,level_12,level_13,level_14,level_15,level_16,level_17,
				level_18,level_19,level_20,level_21,level_22,level_23]

my_level = pl.make_level(level_entitys,critical_score) # advance to next level if score == 10
my_level.level_max = len(level_entitys)
my_increase_level = pl.make_increase_level_action()
my_level.insert_action(my_increase_level)

####################################################

#-----------------  first hud -------------------------

#  first hud for timer
# textcolor, font, position, display text
first_hud = ui.make_hud(green_color,30, (10,10),'Time: ')
draw_first_hud = ui.make_draw_hud_action()
first_hud.insert_action(draw_first_hud)
## insert child to my_screen_display to show hud
my_screen_display.insert_child(draw_first_hud)
my_loop.insert_entity(first_hud) # first_hud action is empty, this do nothing


#-----------------  second hud -------------------------
#  second hud for level
# textcolor, font, position, display text
second_hud = ui.make_hud(white_color,30, (790,10),'Level: ')
draw_second_hud = ui.make_draw_hud_action()
second_hud.insert_action(draw_second_hud)
## insert child to my_screen_display to show hud
my_screen_display.insert_child(draw_second_hud)
my_loop.insert_entity(second_hud) # first_hud action is empty, this do nothing



#-----------------  third hud -------------------------
#  third hud for score
# textcolor, font, position, display text
third_hud = ui.make_hud(misty_rose_color,30, (650,10),'Score: ')
draw_third_hud = ui.make_draw_hud_action()
third_hud.insert_action(draw_third_hud)
## insert child to my_screen_display to show hud
my_screen_display.insert_child(draw_third_hud)
my_loop.insert_entity(third_hud) # first_hud action is empty, this do nothing

#-----------------  credit names hud -------------------------
#  hud for crdit names
# textcolor, font, position, display text
name_hud = ui.make_hud(green_color,30, (0,SCREEN_HEIGHT-35),CREDIT_NAMES)
draw_name_hud = ui.make_draw_hud_action()
name_hud.insert_action(draw_name_hud)
## insert child to my_screen_display to show hud
my_screen_display.insert_child(draw_name_hud)
my_loop.insert_entity(name_hud) # first_hud action is empty, this do nothing


#-----------------  timer -------------------------
####################################################

#alarm time
alarm_interval = 500
my_timer = util.make_timer(alarm_interval) 
my_timer_start = util.make_timer_start_action()
my_timer_tick = util.make_timer_tick_action()
my_timer_elapsed_time = util.make_timer_elapsed_action()
my_timer_reset = util.make_timer_reset_action()


my_timer_alarm = util.make_timer_alarm_action()
my_timer.insert_action(my_timer_start) # type [] so this won't be added to loop twice, child of my_timer_alarm
my_timer.insert_action(my_timer_tick) # type loop
my_timer.insert_action(my_timer_elapsed_time) # type loop  
my_timer.insert_action(my_timer_alarm) #type loop
my_timer.insert_action(my_timer_reset) #type 'loop'


#-----------------  score -------------------------
####################################################

# advance to next level if score = critical_score
my_score = util.make_score(critical_score) 

# green button: score = score +1 
my_increase_score = util.make_increase_score_action()

# pink button: score = score  -1 
my_decrease_score = util.make_decrease_score_action()

# red button: score = 0
my_reset_score = util.make_reset_score_action()

my_score.insert_action(my_increase_score)
my_score.insert_action(my_decrease_score)
my_score.insert_action(my_reset_score)
my_loop.insert_action(my_reset_score)


#---- when collision happens, increase score or decrease score
my_check_collision.insert_child(my_increase_score)
my_check_collision.insert_child(my_decrease_score)

#---- level = level +1 when score  == critical score
my_increase_score.insert_child(my_increase_level)
#---- reset timer when level changes
my_increase_level.insert_child(my_timer_reset)




#---- button jump when alarm is off
my_timer_alarm.insert_child(my_jump_button_action_fast)
my_timer_alarm.insert_child(my_jump_button_action_slow)


#-----------------  update message in hud for timer-----------
####################################################

my_update_time_action = util.make_update_time_action()
# set my_update_timer.hud = first_hud
first_hud.assign_hud(my_update_time_action)
# set my_update_timer.entity_state = my_timer
my_timer.insert_action(my_update_time_action)
my_loop.insert_entity(my_timer)


#--------------------update message in hud for level-----------
my_update_level_action = pl.make_update_level_action()
# set my_update_level.hud = second_hud
second_hud.assign_hud(my_update_level_action)
# set my_update_level.entity_state = my_timer
my_level.insert_action(my_update_level_action)
my_loop.insert_entity(my_level)

#--------------------update message in hud for score-----------
my_update_score_action = util.make_update_score_action()
# set my_update_score.hud = third_hud
third_hud.assign_hud(my_update_score_action)
# set my_update_level.entity_state = my_timer
my_score.insert_action(my_update_score_action)
my_loop.insert_entity(my_score)
my_loop.insert_action(my_update_score_action)


#--------------------  sound  ----------------
####################################################
#sound for collect green button
beep_1 = os.path.dirname(os.getcwd()) + '/assets/sounds/beep1.ogg'
alarm_sound  = sound.make_play_sound_action(beep_1)
my_increase_score.insert_child(alarm_sound)

#sound for collect red button

beep_2 = os.path.dirname(os.getcwd()) + '/assets/sounds/beep2.ogg'
button_sound  = sound.make_play_sound_action(beep_2)
my_decrease_score.insert_child(button_sound)

#sound for change level 

beep_3 = os.path.dirname(os.getcwd()) + '/assets/sounds/beep3.ogg'

level_sound = sound.make_play_sound_action(beep_3)
my_increase_level.insert_child(level_sound)


#-----------------  loop -------------------------
####################################################

my_loop.loop()



