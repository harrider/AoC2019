


class OpcodeProgram:

    def __init__(self, opcode, params, outputLocation, outputValue):
        if isinstance(opcode, int) == False:
            raise TypeError('ERROR :: "opcode" must be of type "Int"!')
        if isinstance(params, list) == False:
            raise TypeError('ERROR :: "params" must be of type "list"!')
        if isinstance(outputLocation, int) == False:
            raise TypeError('ERROR :: "outputLocation" must be of type "Int"!')
        if isinstance(outputValue, int) == False:
            raise TypeError('ERROR :: "outputValue" must be of type "Int"!')

        self.opcode = opcode
        self.params = params
        self.outputLocation = outputLocation
        self.outputValue = outputValue