import pygame

class total_counter_entity:
	def __init__(self,name = 'total_counter'):
		self.actions = []
		self.name = name
		self.active = True
		self.counter = 1

	def insert_action(self,action):
		action.entity_state = self
		self.actions.append(action)
		return 
