from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_2:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        
        param1 = opcodeProgram.params[0]
        param2 = opcodeProgram.params[1]
        param3 = opcodeProgram.params[2]

        input1 = param1[1] if param1[0] == 1 else opcodes[param1[1]]
        input2 = param2[1] if param2[0] == 1 else opcodes[param2[1]]
        
        outputLocation = param3[1]

        result = input1 * input2

        opcodes[outputLocation] = result