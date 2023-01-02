import pygame

class timer_entity:
	def __init__(self,alarm_interval,name = 'timer'):
		self.actions = []
		self.name = name
		self.active = True
		self.current_time = None
		self.start_time = 0
		self.elapsed_time = 0
		self.alarm_interval = alarm_interval
		self.time_step = None
		self.clock = pygame.time.Clock()
		self.fps = 90
		return


	def insert_action(self,action):
		action.entity_state = self
		self.actions.append(action)
		#print("actions:", self.actions)
		return







