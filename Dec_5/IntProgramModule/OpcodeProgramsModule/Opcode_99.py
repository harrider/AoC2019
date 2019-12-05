from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_99:

    def __init__(self, opcodeProgramSpan : int):
        if isinstance(opcodeProgramSpan, int) == False:
            raise TypeError('ERROR :: "opcodeProgramSpan" must be of type "int"!')
        if opcodeProgramSpan < 0:
            raise ValueError('ERROR :: "opcodeProgramSpan" must be a POSITIVE number!')

        self.opcodeProgramSpan = opcodeProgramSpan

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        pass