import pygame


class frame_viewer_entity:
	def __init__(self,frame_width,frame_height):
		pygame.init()
		self.width = frame_width
		self.height = frame_height
		self.screen = pygame.display.set_mode((frame_width,frame_height))
		self.types = ['display']
		self.actions =[]
		self.active = True
		return

	def insert_action(self,action):
		action.entity_state = self
		self.actions.append(action)
		return

	def insert_entity(self,entity):
		entity.screen = self.screen
		for action in entity.actions:
			self.actions.append(action)

	def terminate(self):
		from sys import exit
		pygame.quit()
		exit()
		return



		

