from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_4:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        
        param1 = opcodeProgram.params[0]
        
        outputLocation = param1[1]

        result = opcodes[outputLocation]

        print(f'Opcode 4: {result}')