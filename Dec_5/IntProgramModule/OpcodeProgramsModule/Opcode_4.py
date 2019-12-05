from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_4:

    def __init__(self, opcodeProgramSpan : int):
        if isinstance(opcodeProgramSpan, int) == False:
            raise TypeError('ERROR :: "opcodeProgramSpan" must be of type "int"!')
        if opcodeProgramSpan < 0:
            raise ValueError('ERROR :: "opcodeProgramSpan" must be a POSITIVE number!')

        self.opcodeProgramSpan = opcodeProgramSpan

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        
        param1 = opcodeProgram.params[0]
        
        result = param1[1] if param1[0] == 1 else opcodes[param1[1]]

        print(f'Opcode 4: {result}')