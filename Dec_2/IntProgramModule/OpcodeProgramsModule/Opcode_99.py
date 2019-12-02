from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_99:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):

        opcodeProgramResult = OpcodeProgram(
            opcodeProgram.opcode, 
            opcodeProgram.input1, 
            opcodeProgram.input2, 
            opcodeProgram.outputLocation, 
            0
        )

        return opcodeProgramResult