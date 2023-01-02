import pygame


class game_loop:
	def __init__(self):
		self.name = 'game_loop'
		self.display_content = []
		self.event_content = []
		self.loop_content = []
		return

	def insert_action(self,action):
		if 'display' in action.types:
			self.display_content.append(action)
		if 'event' in action.types:
			self.event_content.append(action)
		elif 'loop' in action.types:
			self.loop_content.append(action)
		return

	def insert_entity(self,entity):
		for action in entity.actions:
			self.insert_action(action)
		return


	def loop(self):

		#print('display_content:', self.display_content)
		#print('\nevent_content:', self.event_content)
		#print('\nloop_content:', self.loop_content)

		while True:
		
			events = pygame.event.get()

			for event in events:
				for action in self.event_content:
					action.act(event)
					#print("event",event, event.type)

			for action in self.display_content:
				action.act(None)
			for action in self.loop_content:
				action.act(None)


		return










