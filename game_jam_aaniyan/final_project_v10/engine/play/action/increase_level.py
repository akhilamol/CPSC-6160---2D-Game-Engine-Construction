###
import pygame
class increase_level_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='increase_level'
		self.hud = None
		self.children = []
		return
	def insert_child(self,child):
		self.children.append(child)

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		if self.entity_state.level == self.entity_state.level_max:
			return False
		if data == self.entity_state.critical_score:
			return True
		return False

	def act(self,data):
		if self.condition_to_act(data):

			# deactivate last level entity: 

			for entity in self.entity_state.entitys[self.entity_state.level-1]:
				entity.active = False

			# active next level entity
			for entity in self.entity_state.entitys[self.entity_state.level]:
				if self.entity_state.level > self.entity_state.level_max:
					self.entity_state.credit_hud = True
				else:
					entity.active = True

			# level + 1

			self.entity_state.level = self.entity_state.level + 1

			for child in self.children:
				child.act(True)

		return
