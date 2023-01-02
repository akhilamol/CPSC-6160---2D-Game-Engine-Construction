import pygame
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT
)


class terminate_action:
	def __init__(self):
		self.name ='terminate'
		self.entity_state = None
		self.types = ['event']
		self.children = None
		return 

	def condition_to_act(self,event):

		if event.type == QUIT:
			return True
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				print("KEY is ESCAPE")
				return True
		return False

	def act(self,event):
		if self.condition_to_act(event):
			self.entity_state.terminate()
