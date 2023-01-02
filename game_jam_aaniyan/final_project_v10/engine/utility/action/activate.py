###
import pygame
class activate_action():
	def __init__(self):
		self.types = []
		self.entity_state = None 
		self.verbose = False
		self.name ='activate_button'
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def act(self,data):
		if self.condition_to_act(data):
			self.entity_state.active = True
		return