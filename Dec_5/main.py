import os
from IntProgramModule.IntProgramParser import IntProgramParser
from IntProgramModule.IntProgramUpdater import IntProgramUpdater
from IntProgramModule.OpcodeProgram import OpcodeProgram
from IntProgramModule.OpcodeProgramsModule.Opcode_1 import Opcode_1
from IntProgramModule.OpcodeProgramsModule.Opcode_2 import Opcode_2
from IntProgramModule.OpcodeProgramsModule.Opcode_3 import Opcode_3
from IntProgramModule.OpcodeProgramsModule.Opcode_4 import Opcode_4
from IntProgramModule.OpcodeProgramsModule.Opcode_99 import Opcode_99


if __name__ == '__main__':
    # Target output value
    targetOutput = 19690720
    currentOutput = -1
    finished = False
    noun = 0
    verb = 0


    # Create the filepath to the 'Input.txt' file
    dataFilePath = os.path.join(os.getcwd(), 'Input.txt')

    # Open the 'Input' file and read in data    
    with open(dataFilePath, 'r') as inputDataFile:
        intProgramCodeStrings = inputDataFile.read().split(',')

    # Create an empty list
    intProgramCode = []

    # Iterate through input data and convernt to 'int' if necessary
    for x in intProgramCodeStrings:
        if isinstance(x, str):
            validatedX = int(x)
        else:
            validatedX = x

        intProgramCode.append(validatedX)

    # Reset '1202' program clock
    intProgramCode[1] = 12
    intProgramCode[2] = 2
    # intProgramCode[1] = iterNoun
    # intProgramCode[2] = iterVerb


    # Create Opcode Program Span Dictionary
    opcodeProgramSpanDict = {
        1 : 4,
        2 : 4,
        3 : 2,
        4 : 2,
        99 : 1
    }

    # Compose program
    # programParser = IntProgramParser(0, 4)
    programParser = IntProgramParser(0, opcodeProgramSpanDict)
    programUpdater = IntProgramUpdater()

    # Create Opcode objects
    opcode_1 = Opcode_1()
    opcode_2 = Opcode_2()
    # opcode_3 = Opcode_3()
    # opcode_4 = Opcode_4()
    opcode_99 = Opcode_99()


    # Print initial state of the IntProgram
    # print(f'Opcode Program: {intProgramCode}')

    # Parse the first Opcode Program to Run from the IntCode Program input
    currentOpcodeProgram = programParser.Parse(intProgramCode)

    # While the current OpcodeProgram does not have Opcode 99
    while currentOpcodeProgram.opcode != 99:
    
        # If Opcode = 1
        if currentOpcodeProgram.opcode == 1:
            currentOpcodeProgram = opcode_1.Execute(currentOpcodeProgram, intProgramCode)
        # Else If Opcode = 2
        elif currentOpcodeProgram.opcode == 2:
            currentOpcodeProgram = opcode_2.Execute(currentOpcodeProgram, intProgramCode)
        # Else, this is an unknown Opcode
        else:
            raise ValueError(f'ERROR :: opcode "{currentOpcodeProgram.opcode}" is INVALID!')

        # Update the IntProgramCode
        intProgramCode = programUpdater.Update(intProgramCode, currentOpcodeProgram)

        # Parse the next Opcode Program
        currentOpcodeProgram = programParser.Parse(intProgramCode)

        # Output the current state of the IntProgram Code
        # print(f'Opcode Program: {intProgramCode}')

    # Capture the current program output
    currentOutput = intProgramCode[0]

    # Print current program output
    print(f'Program Output: {currentOutput}')

    # Exiting the program
    print('\nExiting program...')


# if __name__ == '__main__':
#     # Target output value
#     targetOutput = 19690720
#     currentOutput = -1
#     finished = False
#     noun = 0
#     verb = 0

#     # while currentOutput != targetOutput and (noun != 100 and verb != 100):
#     for iterNoun in range(0, 100):
#         for iterVerb in range(0, 100):
#             # Create the filepath to the 'Input.txt' file
#             dataFilePath = os.path.join(os.getcwd(), 'Input.txt')

#             # Open the 'Input' file and read in data    
#             with open(dataFilePath, 'r') as inputDataFile:
#                 intProgramCodeStrings = inputDataFile.read().split(',')

#             # Create an empty list
#             intProgramCode = []

#             # Iterate through input data and convernt to 'int' if necessary
#             for x in intProgramCodeStrings:
#                 if isinstance(x, str):
#                     validatedX = int(x)
#                 else:
#                     validatedX = x

#                 intProgramCode.append(validatedX)

#             # Reset '1202' program clock
#             # intProgramCode[1] = 12
#             # intProgramCode[2] = 2
#             intProgramCode[1] = iterNoun
#             intProgramCode[2] = iterVerb


#             # Create Opcode Program Span Dictionary
#             opcodeProgramSpanDict = {
#                 1 : 4,
#                 2 : 4,
#                 3 : 2,
#                 4 : 2,
#                 99 : 1
#             }

#             # Compose program
#             # programParser = IntProgramParser(0, 4)
#             programParser = IntProgramParser(0, opcodeProgramSpanDict)
#             programUpdater = IntProgramUpdater()

#             # Create Opcode objects
#             opcode_1 = Opcode_1()
#             opcode_2 = Opcode_2()
#             # opcode_3 = Opcode_3()
#             # opcode_4 = Opcode_4()
#             opcode_99 = Opcode_99()

      


#             # Print initial state of the IntProgram
#             # print(f'Opcode Program: {intProgramCode}')

#             # Parse the first Opcode Program to Run from the IntCode Program input
#             currentOpcodeProgram = programParser.Parse(intProgramCode)

#             # While the current OpcodeProgram does not have Opcode 99
#             while currentOpcodeProgram.opcode != 99:
            
#                 # If Opcode = 1
#                 if currentOpcodeProgram.opcode == 1:
#                     currentOpcodeProgram = opcode_1.Execute(currentOpcodeProgram, intProgramCode)
#                 # Else If Opcode = 2
#                 elif currentOpcodeProgram.opcode == 2:
#                     currentOpcodeProgram = opcode_2.Execute(currentOpcodeProgram, intProgramCode)
#                 # Else, this is an unknown Opcode
#                 else:
#                     raise ValueError(f'ERROR :: opcode "{currentOpcodeProgram.opcode}" is INVALID!')

#                 # Update the IntProgramCode
#                 intProgramCode = programUpdater.Update(intProgramCode, currentOpcodeProgram)

#                 # Parse the next Opcode Program
#                 currentOpcodeProgram = programParser.Parse(intProgramCode)

#                 # Output the current state of the IntProgram Code
#                 # print(f'Opcode Program: {intProgramCode}')

#             # Capture the current program output
#             currentOutput = intProgramCode[0]

#             # Print current program output
#             print(f'Current Output: {currentOutput}')
#             print(f'Target Output: {targetOutput}')
#             print('================================')

#             # If the current output is equal to the target output
#             if currentOutput == targetOutput:
#                 # Capture the current noun and verb
#                 noun = iterNoun
#                 verb = iterVerb

#                 # Set flag to exit outer loop
#                 finished = True
#                 break
        
#         # If True, exit loop
#         if finished:
#             break

#     # Print required noun and verb
#     print(f'Required noun: {noun}')
#     print(f'Required verb: {verb}')

#     # Print result of required calculation
#     print(f'\n100 * noun + verb = 100 * {noun} + {verb} = {100 * noun + verb}')

#     # Exiting the program
#     print('\nExiting program...')