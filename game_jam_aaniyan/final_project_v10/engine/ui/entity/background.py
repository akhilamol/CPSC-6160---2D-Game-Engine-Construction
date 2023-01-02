import pygame.image


class background_entity:
    def __init__(self,scroll_speed,path):
        self.scroll = 0
        self.scroll_speed= scroll_speed
        self.actions = []
        self.name = 'background'
        self.active = False
        self.image = pygame.image.load(path)

    def set_bg_size(self):
        self.image = pygame.transform.scale(self.image, (2000,768))


    def insert_action(self, action):
        action.entity_state = self

        #self.actions.append(action)
        return