###
import pygame

class draw_hud_action():
	def __init__(self):
		self.types = ['display']
		self.entity_state = None 
		self.verbose = False
		self.name ='draw_hud'
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def draw(self,data):

		my_font = pygame.font.SysFont('Arial', self.entity_state.font_size)
		my_color = (255,0,0)
		my_location_1 = (100, 100)
		my_location_2 = (100, 50)


		if self.entity_state == None:

			print("entity_state is None")

		else:
	
			data.blit(my_font.render(self.entity_state.text + str(self.entity_state.message), True, self.entity_state.color), self.entity_state.location)

		return

	def act(self,data):

		if self.condition_to_act(data):
			self.draw(data)
		return