###
import pygame
class timer_reset_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='timer_reset'
		self.children = []
		self.counter = 0


		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		if data == True:
			return True
		return 	False

	def act(self,data):
		#print("data = ", data)
		if self.condition_to_act(data):
			self.entity_state.start_time = self.entity_state.current_time
			print("timer reset", self.entity_state.current_time/1000)

		return