from IntProgramModule.OpcodeProgram import OpcodeProgram


class IntProgramParser:

    def __init__(self, initialCounterValue, opcodeProgramSpan):
        if isinstance(initialCounterValue, int) == False:
            raise TypeError('ERROR :: "initialCounterValue" must be of type "Int"!')
        if initialCounterValue < 0:
            raise ValueError('ERROR :: "initialCounterValue" must be a positive number!')
        if isinstance(opcodeProgramSpan, int) == False:
            raise TypeError('ERROR :: "opcodeProgramSpan" must be of type "Int"!') 
        if opcodeProgramSpan < 0:
            raise ValueError('ERROR :: "opcodeProgramSpan" must be a positive number!')

        self.opcodeCounter = initialCounterValue
        self.opcodeProgramSpan = opcodeProgramSpan


    def Parse(self, opcodes : []):

        startLocation = self.opcodeCounter
        stopLocation = startLocation + self.opcodeProgramSpan
        stepSize = 1

        rawOpCodeProgram = opcodes[startLocation : stopLocation : stepSize]

        if len(rawOpCodeProgram) < self.opcodeProgramSpan:
            opcodeProgram = OpcodeProgram(
                99,
                0,
                0,
                0,
                0
            )
        else:
            opcodeProgram = OpcodeProgram(
                rawOpCodeProgram[0],
                rawOpCodeProgram[1],
                rawOpCodeProgram[2],
                rawOpCodeProgram[3],
                0
            )

            self.opcodeCounter += self.opcodeProgramSpan

        return opcodeProgram