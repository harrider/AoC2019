


class OpcodeProgram:

    def __init__(self, opcode, params):
        if isinstance(opcode, int) == False:
            raise TypeError('ERROR :: "opcode" must be of type "Int"!')
        if isinstance(params, list) == False:
            raise TypeError('ERROR :: "params" must be of type "list"!')

        self.opcode = opcode
        self.params = params