from IntProgramModule.OpcodeProgram import OpcodeProgram


# Day 5 - IntProgramParser with Paramter Modes
class ModifiedIntProgramParser:

    opcodeLength = 2


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
        stepSize = 1

        currentOpcodeAndModes = opcodes[self.instructionPointer]
        currentOpcodeAndModesStr = str(currentOpcodeAndModes)

        currentOpcode = currentOpcodeAndModes % 100
        parameterModes = []

        if len(currentOpcodeAndModesStr) > self.opcodeLength:
            parameterModeStr = currentOpcodeAndModesStr[ : len(currentOpcodeAndModesStr) - self.opcodeLength : stepSize]

            for parameterMode in reversed(parameterModeStr):
                parameterModes.append(int(parameterMode))

        opcodeProgramSpan = self.opcodeProgramSpanDict[currentOpcode]

        startLocation = self.instructionPointer
        stopLocation = startLocation + opcodeProgramSpan

        rawOpCodeProgram = opcodes[startLocation : stopLocation : stepSize]

        if currentOpcode == 99:
            parameter_Opcode = 99
            parameter_Params = []

            opcodeProgram = OpcodeProgram(
                parameter_Opcode,
                parameter_Params
            )
        else:
            positionModeDefaultValue = 0
            paramStartPosition = 1
            paramEndPosition = len(rawOpCodeProgram) - 1 

            parameter_Opcode = currentOpcode
            parameter_Params = rawOpCodeProgram[paramStartPosition : len(rawOpCodeProgram) : stepSize]

            for index in range(0, len(parameter_Params)):
                
                if index < len(parameterModes):
                    parameter_Params[index] = (parameterModes[index], parameter_Params[index])
                else:
                    parameter_Params[index] = (positionModeDefaultValue, parameter_Params[index])

            self.instructionPointer += opcodeProgramSpan

            opcodeProgram = OpcodeProgram(
                parameter_Opcode,
                parameter_Params
            )

        return opcodeProgram


    def UpdateInstructionPointer(self, instructionPointerPosition : int):
        self.instructionPointer = instructionPointerPosition