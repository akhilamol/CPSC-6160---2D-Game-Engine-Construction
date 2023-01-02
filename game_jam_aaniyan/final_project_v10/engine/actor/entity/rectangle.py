import pygame

class rectangle:
	def __init__(self,color,bounds,name = 'rectangle'):
		self.color = color
		self.bounds = bounds
		self.actions = []
		self.name = name
		self.active = True

	def insert_action(self,action):
		action.entity_state = self
		self.actions.append(action)
		return 
