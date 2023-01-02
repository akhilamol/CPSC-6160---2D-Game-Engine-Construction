###
### ENTITIES
###



# def make_level_group(level_list):
#     import engine.play.entity.level_group as e
#     return e.level_group_entity(level_list)

###
### ACTIONS
###
def make_play_sound_action(sound):
    import engine.sound.action.sound as a
    return a.sound_action(sound)