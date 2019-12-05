import os
import json
from IntProgramModule.IntProgramParser import IntProgramParser
from IntProgramModule.ModifiedIntProgramParser import ModifiedIntProgramParser
from IntProgramModule.OpcodeProgram import OpcodeProgram
from IntProgramModule.OpcodeProgramsModule.Opcode_1 import Opcode_1
from IntProgramModule.OpcodeProgramsModule.Opcode_2 import Opcode_2
from IntProgramModule.OpcodeProgramsModule.Opcode_3 import Opcode_3
from IntProgramModule.OpcodeProgramsModule.Opcode_4 import Opcode_4
from IntProgramModule.OpcodeProgramsModule.Opcode_5 import Opcode_5
from IntProgramModule.OpcodeProgramsModule.Opcode_6 import Opcode_6
from IntProgramModule.OpcodeProgramsModule.Opcode_7 import Opcode_7
from IntProgramModule.OpcodeProgramsModule.Opcode_8 import Opcode_8
from IntProgramModule.OpcodeProgramsModule.Opcode_99 import Opcode_99


if __name__ == '__main__':

    # Load app settings
    with open('appsettings.json', 'r') as settingsFile:
        settings = json.load(settingsFile)

        # Create settings variables
        settings_inputFileName = settings['InputFileName']
        settings_resetProgramClock = settings['ResetProgramClock']
        settings_initialNoun = settings['ProgramClockInitialValues']['Noun']
        settings_initialVerb = settings['ProgramClockInitialValues']['Verb']
        settings_useModifiedIntProgramParser = settings['UseModifiedIntProgramParser']
        settings_showInputDataSize = settings['ShowInputDataSize']
        settings_showInitialIntProgramCode = settings['ShowInitialIntProgramCode']
        settings_showIntermediateIntProgramCode = settings['ShowIntermediateIntProgramCode']
        settings_showFinalProgramOutput = settings['ShowFinalProgramOutput']
        settings_showFinalIntProgramCode = settings['ShowFinalIntProgramCode']

    # Create the filepath to the 'Input.txt' file
    dataFilePath = os.path.join(os.getcwd(), settings_inputFileName)

    # Open the 'Input' file and read in data    
    with open(dataFilePath, 'r') as inputDataFile:
        intProgramCodeStrings = inputDataFile.read().split(',')
        
        if settings_showInputDataSize:
            print(f'Input Data size: {len(intProgramCodeStrings)}')

    # Create an empty list
    intProgramCode = []

    # Iterate through input data and convernt to 'int' if necessary
    for x in intProgramCodeStrings:
        if isinstance(x, str):
            validatedX = int(x)
        else:
            validatedX = x

        intProgramCode.append(validatedX)

    #====================
    # Compose program
    #====================

    # Create Opcode objects
    opcode_1 = Opcode_1(4)
    opcode_2 = Opcode_2(4)
    opcode_3 = Opcode_3(2)
    opcode_4 = Opcode_4(2)
    opcode_5 = Opcode_5(3)
    opcode_6 = Opcode_6(3)
    opcode_7 = Opcode_7(4)
    opcode_8 = Opcode_8(4)
    opcode_99 = Opcode_99(1)

    # Create Opcode Program Span Dictionary
    opcodeProgramSpanDict = {
        1 : opcode_1.opcodeProgramSpan,
        2 : opcode_2.opcodeProgramSpan,
        3 : opcode_3.opcodeProgramSpan,
        4 : opcode_4.opcodeProgramSpan,
        5 : opcode_5.opcodeProgramSpan,
        6 : opcode_6.opcodeProgramSpan,
        7 : opcode_7.opcodeProgramSpan,
        8 : opcode_8.opcodeProgramSpan,
        99 : opcode_99.opcodeProgramSpan
    }

    # Create an IntProgramParser object
    if settings_useModifiedIntProgramParser:
        programParser = ModifiedIntProgramParser(0, opcodeProgramSpanDict)
    else:
        programParser = IntProgramParser(0, opcodeProgramSpanDict)

    # Set Program Clock
    if settings_resetProgramClock:
        noun = settings_initialNoun
        verb = settings_initialVerb

        intProgramCode[1] = noun
        intProgramCode[2] = verb

    # Print initial state of the IntProgram
    if settings_showInitialIntProgramCode:
        print(f'Opcode Program: {intProgramCode}')

    # Parse the first Opcode Program to Run from the IntCode Program input
    currentOpcodeProgram = programParser.Parse(intProgramCode)

    # While the current OpcodeProgram does not have Opcode 99
    while currentOpcodeProgram.opcode != 99:
    
        # If Opcode = 1
        if currentOpcodeProgram.opcode == 1:
            opcode_1.Execute(currentOpcodeProgram, intProgramCode)
        # Else If Opcode = 2
        elif currentOpcodeProgram.opcode == 2:
            opcode_2.Execute(currentOpcodeProgram, intProgramCode)
        # Else If Opcode = 3
        elif currentOpcodeProgram.opcode == 3:
            opcode_3.Execute(currentOpcodeProgram, intProgramCode)
        # Else If Opcode = 4
        elif currentOpcodeProgram.opcode == 4:
            opcode_4.Execute(currentOpcodeProgram, intProgramCode)
        # Else If Opcode = 5
        elif currentOpcodeProgram.opcode == 5:
            opcode_5.Execute(currentOpcodeProgram, intProgramCode, programParser)
        # Else If Opcode = 6
        elif currentOpcodeProgram.opcode == 6:
            opcode_6.Execute(currentOpcodeProgram, intProgramCode, programParser)
        # Else If Opcode = 7
        elif currentOpcodeProgram.opcode == 7:
            opcode_7.Execute(currentOpcodeProgram, intProgramCode)
        # Else If Opcode = 8
        elif currentOpcodeProgram.opcode == 8:
            opcode_8.Execute(currentOpcodeProgram, intProgramCode)
        # Else, this is an unknown Opcode
        else:
            raise ValueError(f'ERROR :: opcode "{currentOpcodeProgram.opcode}" is INVALID!')

        # Parse the next Opcode Program
        currentOpcodeProgram = programParser.Parse(intProgramCode)

        # Output the current state of the IntProgram Code
        if settings_showIntermediateIntProgramCode:
            print(f'Opcode Program: {intProgramCode}')

    # Capture the current program output
    currentOutput = intProgramCode[0]

    # Print any final program outputs
    if settings_showFinalProgramOutput:
        print(f'Program Output: {currentOutput}')
    
    if settings_showFinalIntProgramCode:
        print(f'Program Code: {intProgramCode}')

    # Exiting the program
    print('\nExiting program...')