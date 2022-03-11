# Dice simulator no PySimpleGUI
import random
import time
import PySimpleGUI as sg

class ScreenProgram:
    def __init__(self):
        self.min = 1
        self.max = 6
        self.message = 'Você gostaria de gerar um novo valor para o dado?'

        # Layout
        self.layout = [
            [sg.Text('ROLL THE DICE')],
            [sg.Button('YES'), sg.Button('NO')],

            [sg.Output(size=(17,4))],
        ]

    def Start(self):
        # Create the window
        self.window = sg.Window('Dice simulator', layout=self.layout, text_justification=('c'), element_justification='c')

        # Read screen values
        self.events, self.values = self.window.Read()

        # Do something with the values
        try:
            if self.events == 'YES' or self.events == 's' or self.events == 'yes':
                self.ValueGenerator()
            elif self.events == 'NO' or self.events == 'n' or self.events == 'no':
                print('Thank you for the participation!')
            else:
                print('Please, digit yes or no.')
        except:
            print('An error has occurred, please try again')

    def ValueGenerator(self):
        print(random.randint(self.min, self.max))
        time.sleep(5)

simulator = ScreenProgram()
simulator.Start()
