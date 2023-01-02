import pygame

class screen_display_action:
	def __init__(self):
		self.entity_state = None
		self.types = ['display']
		self.actions =[]
		self.children =[]
		return

	def insert_entity(self,entity):
		entity.screen = self.entity_state.screen
		for action in entity.actions:
			self.actions.append(action)


	def insert_child(self,child):
		self.children.append(child)

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def act(self,data):
		
		if(self.condition_to_act(data)):
			self.entity_state.screen.fill((255,255,255))
			

		for child in self.children:
			child.act(self.entity_state.screen)

		pygame.display.flip()

		return

