###
import pygame
from pygame.locals import *

class press_button_action():
	def __init__(self):
		self.types = ['event']
		self.entity_state = None 
		self.name ='press_button'
		self.children =[]
		self.verbose = False
		return

	def condition_to_act(self,event):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		if event.type == MOUSEBUTTONDOWN:
			pos = event.pos
			return self.entity_state.is_inside(pos)

		return False

	def insert_child(self,child):
		self.children.append(child)

	def act(self,event):
		#print("press_button~~~event",event.type, event.key)
		if self.condition_to_act(event):
			for child in self.children:
				child.act(None)
			
		return