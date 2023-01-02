###
import pygame
from random import randrange

class move_button_action():
	def __init__(self):
		self.types = ['display']
		self.entity_state = None 
		self.verbose = False
		self.name ='move_button'
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
		if self.condition_to_act(data):
			# change button location
			self.entity_state.bounds = [randrange(900),randrange(700),
			self.entity_state.bounds[2],self.entity_state.bounds[3]]
			# change button color
			self.entity_state.color  = (randrange(255),randrange(255),randrange(255) )


		return 