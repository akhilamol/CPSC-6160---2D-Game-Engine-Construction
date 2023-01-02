###
import pygame
from pygame.locals import *

class inside_button_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.name ='inside_button'
		self.children =[]
		self.verbose = False
		return

	def condition_to_act(self,pos):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False

		return self.entity_state.is_inside(pos)

	def insert_child(self,child):
		self.children.append(child)

	def act(self,data):
		if self.condition_to_act(data):
			for child in self.children:
				child.act(data)			
		return