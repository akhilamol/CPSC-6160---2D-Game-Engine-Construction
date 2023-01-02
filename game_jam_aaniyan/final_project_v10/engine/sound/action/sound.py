import pygame

class sound_action():
	def __init__(self,sound_effect):
		self.types = []
		self.entity_state = None 
		self.verbose = True
		self.name ='sound'
		self.children = []
		self.sound_effect = sound_effect
		return

	def condition_to_act(self,data):
		if self.verbose == False:
			return False
		return True

	def insert_child(self,child):
		self.children.append(child)

	def act(self,data):
		if self.condition_to_act(data):
			pygame.mixer.init()
			sound = pygame.mixer.Sound(self.sound_effect)
			sound.play(0)

		return 
