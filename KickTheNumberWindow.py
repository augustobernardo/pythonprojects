import random
import PySimpleGUI as sg

class KickTheNumber:
	def __init__(self):
		self.randomValue = 0
		self.min = 1
		self.max = 20
		self.tryAgain = True

	def Start(self):	
		# Layout
		self.layout = [
			[sg.Text('Kick The Number', size=(39,0))],
			[sg.Input(size=(18,0), key='KickValueInput')],
			[sg.Button('Kick')],
			[sg.Output(size=(39,10))]
		]
	
		# Create a window
		self.window = sg.Window('Kick the Number', layout=self.layout)
		self.GenerateTheNumber()
		try:
			while True:
				# getting the values
				self.ReadTheValues()

				if self.event == 'Kick':
					self.kick = self.values['KickValueInput']

					# Game logic
					while self.tryAgain == True:
						if int(self.kick) > self.randomValue:
							print('Kick a lower number!')
							break
						elif int(self.kick) < self.randomValue:
							print('Kick a higher value!')
							break
						if int(self.kick) == self.randomValue:
							self.tryAgain == False
							print('Congratulations, you got the number right!!')
							break # used for stop the 'while' if the tryAgain == False
		except:
			print('Please digit only numbers!!')
			self.Start()

	def ReadTheValues(self):
		# Getting the values
		self.event, self.values = self.window.Read()

	def GenerateTheNumber(self):
		self.randomValue = random.randint(self.min, self.max)

kickNumberGame = KickTheNumber()
kickNumberGame.Start()
