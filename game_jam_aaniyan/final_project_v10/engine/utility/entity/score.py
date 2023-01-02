import pygame

class score_entity:
	def __init__(self,critical_score):
		self.score = 0
		self.actions = []
		self.active = True
		self.critical_score = critical_score

	def insert_action(self,action):
		action.entity_state = self
		#self.actions.append(action)
		return 
