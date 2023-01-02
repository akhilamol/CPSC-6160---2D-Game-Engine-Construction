###
import pygame
class decrease_score_action():
	def __init__(self):
		self.types = ['']
		self.entity_state = None 
		self.verbose = False
		self.name ='decrease_score'
		self.children = []
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		# check if hit red or pink button
		if (data ==[139,0,0] or data ==[255,228,225]):
			return True
		return False

	def insert_child(self,child):
		self.children.append(child)

	def act(self,data):
		print("data = ", data)
		if self.condition_to_act(data):
			#hit red button, score reset to 0
			if data ==[139,0,0]:
				deduct_score = self.entity_state.score
			# hit pink button, score - 1
			if data ==[255,228,225]:
				if self.entity_state.score >=1:
					deduct_score = 1
				elif self.entity_state.score ==0:
					deduct_score = 0

			self.entity_state.score = self.entity_state.score - deduct_score
			for child in self.children:
				child.act(self.entity_state.score)
			
		return