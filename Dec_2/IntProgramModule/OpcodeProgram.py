


class OpcodeProgram:

    def __init__(self, opcode, input1, input2, outputLocation, outputValue):
        if isinstance(opcode, int) == False:
            raise TypeError('ERROR :: "opcode" must be of type "Int"!')
        if isinstance(input1, int) == False:
            raise TypeError('ERROR :: "input1" must be of type "Int"!') 
        if isinstance(input2, int) == False:
            raise TypeError('ERROR :: "input2" must be of type "Int"!')
        if isinstance(outputLocation, int) == False:
            raise TypeError('ERROR :: "outputLocation" must be of type "Int"!')
        if isinstance(outputValue, int) == False:
            raise TypeError('ERROR :: "outputValue" must be of type "Int"!')

        self.opcode = opcode
        self.input1 = input1
        self.input2 = input2
        self.outputLocation = outputLocation
        self.outputValue = outputValue