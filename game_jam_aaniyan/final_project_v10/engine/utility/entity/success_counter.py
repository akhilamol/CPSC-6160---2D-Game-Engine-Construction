import pygame

class success_counter_entity:
	def __init__(self,name = 'success_counter'):
		self.actions = []
		self.name = name
		self.active = True
		self.counter = 0

	def insert_action(self,action):
		action.entity_state = self
		self.actions.append(action)
		return 
