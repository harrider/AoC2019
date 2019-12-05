from IntProgramModule.OpcodeProgram import OpcodeProgram


# Day 2 - IntProgramParser
class IntProgramParser:

    def __init__(self, initialInstructionPointerValue, opcodeProgramSpanDict):
        if isinstance(initialInstructionPointerValue, int) == False:
            raise TypeError('ERROR :: "initialInstructionPointerValue" must be of type "Int"!')
        if initialInstructionPointerValue < 0:
            raise ValueError('ERROR :: "initialInstructionPointerValue" must be a positive number!')
        if isinstance(opcodeProgramSpanDict, dict) == False:
            raise TypeError('ERROR :: "opcodeProgramSpanDict" must be of type "dict"!')
        if len(opcodeProgramSpanDict) == 0:
            raise ValueError('ERROR :: "opcodeProgramSpanDict" dictionary is EMPTY!')

        self.instructionPointer = initialInstructionPointerValue
        self.opcodeProgramSpanDict = opcodeProgramSpanDict


    def Parse(self, opcodes : []):

        currentOpcode = opcodes[self.instructionPointer]
        opcodeProgramSpan = self.opcodeProgramSpanDict[currentOpcode]

        startLocation = self.instructionPointer
        stopLocation = startLocation + opcodeProgramSpan
        stepSize = 1

        rawOpCodeProgram = opcodes[startLocation : stopLocation : stepSize]

        if len(rawOpCodeProgram) < opcodeProgramSpan:
            parameter_Opcode = 99
            parameter_Params = []

            opcodeProgram = OpcodeProgram(
                parameter_Opcode,
                parameter_Params
            )
        else:
            opcodePosition = 0
            paramStartPosition = 1
            paramEndPosition = len(rawOpCodeProgram) - 1 

            parameter_Opcode = rawOpCodeProgram[opcodePosition]
            parameter_Params = rawOpCodeProgram[paramStartPosition : len(rawOpCodeProgram) : stepSize]

            opcodeProgram = OpcodeProgram(
                parameter_Opcode,
                parameter_Params
            )

            self.instructionPointer += opcodeProgramSpan

        return opcodeProgram