import pygame

class level_entity:
	def __init__(self,entitys,critical_score):
		self.level = 1
		self.level_max = 1
		self.actions = []
		self.active = True
		self.entitys = entitys
		self.critical_score = critical_score

	def insert_action(self,action):
		action.entity_state = self
		self.actions.append(action)
		return 
