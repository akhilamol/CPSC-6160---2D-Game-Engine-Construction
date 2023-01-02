###
from random import randrange

class reset_button_position_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='reset_button_position'
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		if self.entity_state.bounds[0]<0:
				return True
		return False

	def act(self,data):
		if self.condition_to_act(data):		
			self.entity_state.bounds[0] = 1000
			self.entity_state.bounds[1] = randrange(100,600)		
		return
