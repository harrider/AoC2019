from IntProgramModule.OpcodeProgram import OpcodeProgram


class Opcode_1:

    def __init__(self):
        self

    
    def Execute(self, opcodeProgram : OpcodeProgram, opcodes : []):
        
        result = opcodes[opcodeProgram.params[0]] + opcodes[opcodeProgram.params[1]]

        parameter_Opcode = opcodeProgram.opcode

        parameter_Params = []
        parameter_Params.append(opcodeProgram.params[0])
        parameter_Params.append(opcodeProgram.params[1])

        parameter_OutputLocation = opcodeProgram.outputLocation
        parameter_OutputValue = result

        opcodeProgramResult = OpcodeProgram(
            parameter_Opcode, 
            parameter_Params,
            parameter_OutputLocation, 
            parameter_OutputValue
        )

        return opcodeProgramResult