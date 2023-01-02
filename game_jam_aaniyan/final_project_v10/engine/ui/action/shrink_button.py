###
import pygame
from random import randrange

class shrink_button_action():
	def __init__(self,speed):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='shrink_button'
		self.children = []
		self.speed = speed
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
		# changes the button's location on the y-axis by updating its bounds
		if self.condition_to_act(data):
			#print("moving", self.entity_state.bounds[0])
			self.entity_state.bounds[2] = self.entity_state.bounds[2]-self.speed
			self.entity_state.bounds[3] = self.entity_state.bounds[3]-self.speed

		return
