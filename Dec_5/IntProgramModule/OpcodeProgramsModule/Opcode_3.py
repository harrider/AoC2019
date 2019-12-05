from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_3:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        
        outputLocation = opcodeProgram.params[0]
               
        userInput = input('Input an integer value: ')

        opcodes[outputLocation] = int(userInput)