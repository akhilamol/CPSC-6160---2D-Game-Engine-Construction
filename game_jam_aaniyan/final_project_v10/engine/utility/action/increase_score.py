###
import pygame
class increase_score_action():
	def __init__(self):
		self.types = ['']
		self.entity_state = None 
		self.verbose = False
		self.name ='increase_score'
		self.children = []
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		if data[0] == 37 and data[1] ==139 and data[2]== 34:
			return True
		return False

	def insert_child(self,child):
		self.children.append(child)

	def act(self,data):
		if self.condition_to_act(data):
			self.entity_state.score = self.entity_state.score + 1
			for child in self.children:
				child.act(self.entity_state.score)

		return