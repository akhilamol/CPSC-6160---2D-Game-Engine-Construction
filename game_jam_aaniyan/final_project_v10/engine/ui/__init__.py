###
### ENTITIES
###
def make_button(color, bounds=[0,0,0,0], speed=0):
    import engine.ui.entity.button as e
    return e.button_entity(color, bounds, speed)

def make_hud(color,font_size, location,text):
    import engine.ui.entity.hud as e
    return e.hud_entity(color, font_size, location, text)

def make_background(scroll_speed, path):
    import engine.ui.entity.background as a
    return a.background_entity(scroll_speed,path)

###
### ACTIONS
###
def make_draw_button_action():
    import engine.ui.action.draw_button as a
    return a.draw_button_action()

def make_draw_hud_action():
    import engine.ui.action.draw_hud as a
    return a.draw_hud_action()

def make_inside_button_action():
    import engine.ui.action.inside_button as a
    return a.inside_button_action()

def make_key_pressed_action():
    import engine.ui.action.key_pressed_update_position as a
    return a.key_pressed_update_position_action()

def make_move_button_action():
    import engine.ui.action.move_button as a
    return a.move_button_action()

def make_move_button_left_action():
    import engine.ui.action.move_button_left as a
    return a.move_button_left_action()

def make_press_button_action():
    import engine.ui.action.press_button as a
    return a.press_button_action()

def make_check_collision_action():
    import engine.ui.action.check_collision as a
    return a.check_collision_action()

# def make_change_position_action():
#     import engine.ui.action.change_position as a
#     return a.change_position_action()

def make_reset_position_action():
    import engine.ui.action.reset_button_position as a
    return a.reset_button_position_action()

def make_jump_button_action(speed):
    import engine.ui.action.jump_button as a
    return a.jump_button_action(speed)

def make_change_button_size_action(speed):
    import engine.ui.action.change_button_size as a
    return a.change_button_size_action(speed)

def make_draw_background_action():
    import engine.ui.action.draw_background as a
    return a.draw_background_action()