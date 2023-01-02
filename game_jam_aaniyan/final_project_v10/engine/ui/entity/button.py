import pygame

class button_entity:
	def __init__(self,color,bounds,speed):
		self.color = color
		self.bounds = bounds
		self.actions = []
		self.name = 'button'
		self.active = False
		self.speed = speed
		self.height_restriction = None
		self.children_button = []

	def insert_action(self,action):
		action.entity_state = self

		#self.actions.append(action)
		return 

	def insert_child_button(self, child):
		self.children_button.append(child)

	def is_inside(self,pos):
		if pos[0] < self.bounds[0]:
			return False
		if pos[0] > self.bounds[2] + self.bounds[0]:
			return False
		if pos[1] < self.bounds[1]:
			return False
		if pos[1] > self.bounds[3] + self.bounds[1]:
			return False
		return True
