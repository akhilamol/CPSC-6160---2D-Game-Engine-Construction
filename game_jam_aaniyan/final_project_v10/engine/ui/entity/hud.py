import pygame

class hud_entity:
	def __init__(self,color,font_size,location,text,name = 'hud'):
		self.color = color
		self.location = location
		self.actions = []
		self.name = name
		self.font_size = font_size
		self.active = True
		self.message = ''
		self.text = text

	def insert_action(self,action):
		action.entity_state = self
		#self.actions.append(action)
		return 

	def assign_hud(self,action):
		action.hud = self
		return 