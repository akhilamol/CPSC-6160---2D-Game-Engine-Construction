###
### ENTITIES
###
def make_frame_viewer(screen_width, screen_height):
    import engine.play.entity.frame_viewer as e
    return e.frame_viewer_entity(screen_width, screen_height)

def make_game_loop():
    import engine.play.entity.game_loop as e
    return e.game_loop()
    
def make_level(level_entities,critical_score):
    import engine.play.entity.level as e
    return e.level_entity(level_entities,critical_score)

# def make_level_group(level_list):
#     import engine.play.entity.level_group as e
#     return e.level_group_entity(level_list)

###
### ACTIONS
###
def make_terminate_action():
    import engine.play.action.terminate as a
    return a.terminate_action()

def make_increase_level_action():
    import engine.play.action.increase_level as a
    return a.increase_level_action()

def make_update_level_action():
    import engine.play.action.update_level as a
    return a.update_level_action()

def make_screen_display_action():
    import engine.play.action.screen_display as a
    return a.screen_display_action()