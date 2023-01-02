###
import pygame,os



class draw_background_action():
	def __init__(self):
		self.types = ['display']
		self.entity_state = None
		self.verbose = False
		self.name ='draw_background'
		return

	def insert_action(self, action):
		action.entity_state = self
		# self.actions.append(action)
		return


	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		return True

	def draw(self,data):
		data.blit(self.entity_state.image, (self.entity_state.scroll,0))
		# print("bg printed")
		self.entity_state.scroll-=self.entity_state.scroll_speed
		if abs(self.entity_state.scroll) > 100:
			self.entity_state.scroll=0
		return

	def act(self,data):
		if self.condition_to_act(data):
			self.draw(data)
		return