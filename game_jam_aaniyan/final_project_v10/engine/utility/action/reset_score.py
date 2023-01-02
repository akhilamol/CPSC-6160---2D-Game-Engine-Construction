###
import pygame
class reset_score_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='reset_score'
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		if self.entity_state.score == self.entity_state.critical_score:
			return True
		return False

	def act(self,data):
		if self.condition_to_act(data):
			self.entity_state.score = 0
		return