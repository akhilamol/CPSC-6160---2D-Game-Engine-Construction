###
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


class display_letter():
	def __init__(self):
		self.types = ['event']
		self.entity_state = None 
		self.verbose = False
		self.name ='display_letter'
		return

	def condition_to_act(self,event):
		if event.type == QUIT:
			return False

		if event.type == KEYDOWN:
			return True
		

	def display(self,event):
		letter = event.unicode
		font = pygame.font.SysFont(None, 48)
		RED = (255, 0 ,0)
		letter_render = font.render("letter", True, RED)

		return

	def act(self,event):
		if self.condition_to_act(event):
			self.display(event)
		return
