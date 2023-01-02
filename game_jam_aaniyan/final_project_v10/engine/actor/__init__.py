###
### ENTITIES
###
def make_circle():
    import engine.actor.entity.circle as e
    return e.circle()

def make_rectangle():
    import engine.actor.entity.rectangle as e
    return e.rectangle()

def make_particle():
    import engine.actor.entity.particle as e
    return e.particles_entity()

# def make_letter():
#     import engine.actor.entity.letter as e
#     return 

###
### ACTIONS
###
def make_collide_action():
    import engine.actor.action.collide as a
    return a.collide_action()

# def make_rectangle_collide_action(position):
#     import engine.actor.action.rectangle_collisions as a
#     return a.detect_rect_collision_action(position)

# def make_detect_letter_action():
#     import engine.actor.action.detect_letter as a
#     return 

def make_display_letter_action():
    import engine.actor.action.display_letter as a
    return a.display_letter()

def make_draw_circle_action():
    import engine.actor.action.draw_circle as a
    return a.draw_circle_action()

def make_draw_particle_action():
    import engine.actor.action.draw_particle as a
    return a.draw_particle_action()

def make_draw_rectangle_action():
    import engine.actor.action.draw_rectangle as a
    return a.draw_rectangle_action()

def make_update_particle_position_action():
    import engine.actor.action.update_particle_position as a
    return a.update_particle_position_action()

def make_update_particle_velocity_action():
    import engine.actor.action.update_particle_velocity as a
    return a.update_particle_velocity_action()

def make_is_inside_rectangle_action():
    import engine.actor.action.is_inside as i
    return i.IsInsideRectangleAction()

def make_put_position_action():
    import engine.actor.action.put_position as p
    return p.PutPosition()

def make_change_position_action():
    import engine.actor.action.change_position as a
    return a.change_position_action()

def make_move_circle_action(scroll_speed):
    import engine.actor.action.move_circle as a
    return a.move_circle_action(scroll_speed)