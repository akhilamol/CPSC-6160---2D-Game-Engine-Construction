###
import pygame
class key_pressed_update_position_action():
    def __init__(self):
        self.types = ['event']
        self.entity_state = None 
        self.verbose = False
        self.name ='key_pressed_update_position'
        self.children = []
        return

    def condition_to_act(self,data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def insert_child(self,child):
        self.children.append(child)

    def act(self,data):
        # can use WASD or Arrow keys to move
        # does not allow entity_state to move beyond window bounds
        if self.condition_to_act(data):
            # if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]: # move left
            #     self.entity_state.bounds[0] -= 4
            # if pygame.key.get_pressed()[pygame.K_d or pygame.key.get_pressed()[pygame.K_RIGHT]]: # move right
            #     self.entity_state.bounds[0] += 4
            if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]: # move down
                if self.entity_state.bounds[1] < self.entity_state.height_restriction:
                    self.entity_state.bounds[1] += 5
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]: # move up
                if self.entity_state.bounds[1] > 0:
                    self.entity_state.bounds[1] -= 5
        return 