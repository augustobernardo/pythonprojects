# kick the number
import random

class KickTheNumber:
    def __init__(self):
        self.randomValue = 0
        self.min = 1
        self.max = 2
        self.tryAgain = True
    
    def Start(self):
        self.GenerateTheNumber()
        self.KickValue()
        try:
            while self.tryAgain == True:
                if int(self.kick) > self.randomValue:
                    print('Kick a lower number!')
                    self.KickValue()
                elif int(self.kick) < self.randomValue:
                    print('Kick a higher value!')
                    self.KickValue()
                if int(self.kick) == self.randomValue:
                    self.tryAgain == False
                    print('Congratulations, you got the number right!!')
                    break # used for stop the 'while' if the tryAgain == False
        except:
            print('Please digit only numbers!!')
            self.Start()

    def KickValue(self):
        self.kick = int(input('Kick a number: '))

    def GenerateTheNumber(self):
        self.randomValue = random.randint(self.min, self.max)

kickNumber = KickTheNumber()
kickNumber.Start()