from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_3:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        
        param1 = opcodeProgram.params[0]
        
        outputLocation = param1[1]
               
        userInput = input('Input an integer value: ')

        opcodes[outputLocation] = int(userInput)