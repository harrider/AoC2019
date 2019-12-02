from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_2:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        
        result = opcodes[opcodeProgram.input1] * opcodes[opcodeProgram.input2]

        opcodeProgramResult = OpcodeProgram(
            opcodeProgram.opcode, 
            opcodeProgram.input1, 
            opcodeProgram.input2, 
            opcodeProgram.outputLocation, 
            result
        )

        return opcodeProgramResult