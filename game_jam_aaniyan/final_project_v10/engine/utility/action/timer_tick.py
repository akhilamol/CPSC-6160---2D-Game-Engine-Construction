###
import pygame
class timer_tick_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='timer_tick'
		self.children = []
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def insert_child(self,child):
		self.children.append(child)


	def act(self,data):
		if self.condition_to_act(data):
			#print("\ncurrent time  " , pygame.time.get_ticks())
			self.entity_state.current_time = pygame.time.get_ticks()
			for c in self.children:
				self.entity_state.clock.tick(self.entity_state.fps)
		return