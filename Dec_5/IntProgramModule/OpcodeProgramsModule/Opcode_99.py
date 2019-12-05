from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_99:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):

        parameter_Opcode = opcodeProgram.opcode

        parameter_Params = []
        parameter_Params[0] = opcodeProgram.params[0]
        parameter_Params[1] = opcodeProgram.params[1]

        parameter_OutputLocation = opcodeProgram.outputLocation
        parameter_OutputValue = 0

        opcodeProgramResult = OpcodeProgram(
            parameter_Opcode, 
            parameter_Params,
            parameter_OutputLocation, 
            parameter_OutputValue
        )

        return opcodeProgramResult