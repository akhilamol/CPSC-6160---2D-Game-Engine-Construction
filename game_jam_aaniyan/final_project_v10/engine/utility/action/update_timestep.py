###
import pygame
class update_timestep_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='update_time_step'
		self.children = []
		self.last_time = 0

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
			
			if (self.entity_state.elapsed_time - self.last_time > self.entity_state.time_step):
				self.last_time = self.entity_state.elapsed_time
				print("Alarm~~~~~~~\n",self.entity_state.elapsed_time)
				for child in self.children:
					child.act(self.entity_state.time_step)

		return 