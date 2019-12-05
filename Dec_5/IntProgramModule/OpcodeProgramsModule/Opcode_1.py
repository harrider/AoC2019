from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_1:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        
        input1 = opcodeProgram.params[0]
        input2 = opcodeProgram.params[1]
        outputLocation = opcodeProgram.params[2]

        result = opcodes[input1] + opcodes[input2]

        opcodes[outputLocation] = result