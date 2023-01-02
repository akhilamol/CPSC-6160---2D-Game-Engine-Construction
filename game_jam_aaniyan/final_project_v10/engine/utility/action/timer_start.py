###
import pygame
class timer_start_action():
	def __init__(self):
		self.types = []
		self.entity_state = None 
		self.verbose = False
		self.name ='timer_start'
		self.children = []
		self.counter = 0

		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		if self.entity_state.elapsed_time > self.entity_state.alarm_interval:
			return True
		if self.entity_state.start_time ==0:
			return True

		return False

	def act(self,data):
		if self.condition_to_act(data):
			self.entity_state.start_time = pygame.time.get_ticks()
			#print("\n~~~~~~~~~~~~~~~ start time " , self.entity_state.start_time)
		return