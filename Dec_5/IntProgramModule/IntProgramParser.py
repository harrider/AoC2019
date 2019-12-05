from IntProgramModule.OpcodeProgram import OpcodeProgram


class IntProgramParser:

    def __init__(self, initialCounterValue, opcodeProgramSpanDict):
        if isinstance(initialCounterValue, int) == False:
            raise TypeError('ERROR :: "initialCounterValue" must be of type "Int"!')
        if initialCounterValue < 0:
            raise ValueError('ERROR :: "initialCounterValue" must be a positive number!')
        if isinstance(opcodeProgramSpanDict, dict) == False:
            raise TypeError('ERROR :: "opcodeProgramSpanDict" must be of type "dict"!')
        if len(opcodeProgramSpanDict) == 0:
            raise ValueError('ERROR :: "opcodeProgramSpanDict" dictionary is EMPTY!')

        self.opcodeCounter = initialCounterValue
        self.opcodeProgramSpanDict = opcodeProgramSpanDict


    def Parse(self, opcodes : []):

        currentOpcode = opcodes[self.opcodeCounter]
        opcodeProgramSpan = self.opcodeProgramSpanDict[currentOpcode]

        startLocation = self.opcodeCounter
        stopLocation = startLocation + opcodeProgramSpan
        stepSize = 1

        rawOpCodeProgram = opcodes[startLocation : stopLocation : stepSize]
        
        # TODO - REMOVE AFTER REFACTOR
        print(f'rawOpcodeProgram: {rawOpCodeProgram}')
        print(f'opcodeProgramSpan: {opcodeProgramSpan}')


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

            # TODO - REMOVE AFTER REFACTOR
            for param in parameter_Params:
                print(f'Current Param: {param}')

            opcodeProgram = OpcodeProgram(
                parameter_Opcode,
                parameter_Params
            )

            self.opcodeCounter += opcodeProgramSpan

        return opcodeProgram