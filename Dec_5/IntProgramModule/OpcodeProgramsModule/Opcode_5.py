from IntProgramModule.OpcodeProgram import OpcodeProgram
from IntProgramModule.ModifiedIntProgramParser import ModifiedIntProgramParser


class Opcode_5:

    def __init__(self, opcodeProgramSpan : int):
        if isinstance(opcodeProgramSpan, int) == False:
            raise TypeError('ERROR :: "opcodeProgramSpan" must be of type "int"!')
        if opcodeProgramSpan < 0:
            raise ValueError('ERROR :: "opcodeProgramSpan" must be a POSITIVE number!')

        self.opcodeProgramSpan = opcodeProgramSpan

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : [], programParser : ModifiedIntProgramParser):
        
        param1 = opcodeProgram.params[0]
        param2 = opcodeProgram.params[1]

        input1 = param1[1] if param1[0] == 1 else opcodes[param1[1]]
        input2 = param2[1] if param2[0] == 1 else opcodes[param2[1]]
        
        if input1 != 0:
            programParser.UpdateInstructionPointer(input2)
