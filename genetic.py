import random
import math

'''
Tool for collecting population information for rendering purposes.
'''

'''
Structure for our genetic controller which will be used as essentially a singleton
'''

class GeneticController:

    def __init__(self, size: int=32):
        # Initializing our controller with a default size of 32.
        # Creating our operand function
        self.size = size
        self.geneticOperand = []

        for i in range(size):
            self.geneticOperand.append(random.choice(['+','-','*','/','pow','sqrt']))

    def calculateOperandValue(self, gc: "GeneticStructure") -> int:
        output, idx = 0, 0
        for operand in self.geneticOperand:
            geneticCodeValue = gc.geneticCode[idx]
            if operand == '+':
                output += geneticCodeValue
            elif operand == '-':
                output -= geneticCodeValue
            elif operand == '*':
                output *= geneticCodeValue
            elif operand == '/':
                output /= geneticCodeValue
            elif operand == 'pow':
                output = pow(output, geneticCodeValue)
            elif operand == 'sqrt':
                output = pow(output, 1/geneticCodeValue)

            idx += 1

        if type(output) == complex:
            output = output.real

        return round(output)

'''
Structure for genetic class
'''
class GeneticStructure:

    def __init__(self, size: int=32):
        # Initializing our genetic structure with a default size of 32.
        # Size is essentially the number of variables within our genetic code.
        self.size = size
        self.geneticCode = []

        for i in range(size):
            value = 0
            while value == 0:
                value = random.uniform(-10, 10)
            self.geneticCode.append(value)


gc = GeneticStructure()
gq = GeneticController()
print(gq.calculateOperandValue((gc)))
