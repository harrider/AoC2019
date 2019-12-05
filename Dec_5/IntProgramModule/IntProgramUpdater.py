from IntProgramModule.OpcodeProgram import OpcodeProgram


class IntProgramUpdater:

    def __init__(self):
        self


    def Update(self, opcodes : [], opcodeProgram : OpcodeProgram):
        if isinstance(opcodes, list) == False:
            raise TypeError('ERROR :: "opcodes" must be of type "list"!')
        if len(opcodes) == 0:
            raise ValueError('ERROR :: "opcodes" is EMPTY!')
        if isinstance(opcodeProgram, OpcodeProgram) == False:
            raise TypeError('ERROR :: "opcodeProgram" must be of type "OpcodeProgram"!') 

        updatedOpcodes = opcodes

        updatedOpcodes[opcodeProgram.outputLocation] = opcodeProgram.outputValue

        return updatedOpcodes