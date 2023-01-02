###
### ENTITIES
###
def make_score(critical_score):
    import engine.utility.entity.score as e
    return e.score_entity(critical_score)

def make_success_counter():
    import engine.utility.entity.success_counter as e
    return e.success_counter_entity()

def make_timer(alarm_interval):
    import engine.utility.entity.timer as e
    return e.timer_entity(alarm_interval)

def make_total_counter():
    import engine.utility.entity.total_counter as e
    return e.total_counter_entity()

###
### ACTIONS
###
def make_activate_action():
    import engine.utility.action.activate as a
    return a.activate_action()

def make_add_score_action():
    import engine.utility.action.add_score as a
    return a.add_score_action()

def make_deactivate_action():
    import engine.utility.action.deactivate as a
    return a.deactivate_action()

def make_deduct_score_action():
    import engine.utility.action.deduct_score as a
    return a.deduct_score_action()

def make_increase_score_action():
    import engine.utility.action.increase_score as a
    return a.increase_score_action()

def make_decrease_score_action():
    import engine.utility.action.decrease_score as a
    return a.decrease_score_action()

def make_reduce_alarm_interval_action():
    import engine.utility.action.reduce_alarm_interval as a
    return a.reduce_alarm_interval_action()

def make_reset_score_action():
    import engine.utility.action.reset_score as a
    return a.reset_score_action()

def make_success_counter_increment_action():
    import engine.utility.action.success_counter_increment as a
    return a.success_counter_increment_action()

def make_timer_reset_action():
    import engine.utility.action.timer_reset as a
    return a.timer_reset_action()

def make_timer_alarm_action():
    import engine.utility.action.timer_alarm as a
    return a.timer_alarm_action()

def make_timer_elapsed_action():
    import engine.utility.action.timer_elapsed_time as a
    return a.timer_elapsed_time_action()

def make_timer_start_action():
    import engine.utility.action.timer_start as a
    return a.timer_start_action()

def make_timer_tick_action():
    import engine.utility.action.timer_tick as a
    return a.timer_tick_action()

def make_total_counter_increment_action():
    import engine.utility.action.total_counter_increment as a
    return a.total_counter_increment_action()

def make_update_message_action():
    import engine.utility.action.update_message as a
    return a.update_message_action()

def make_update_score_action():
    import engine.utility.action.update_score as a
    return a.update_score_action()

def make_update_time_action():
    import engine.utility.action.update_time as a
    return a.update_time_action()

def make_update_timestep_action():
    import engine.utility.action.update_timestep as a
    return a.update_timestep_action()