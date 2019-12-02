import os
from IntProgramModule.IntProgramParser import IntProgramParser
from IntProgramModule.IntProgramUpdater import IntProgramUpdater
from IntProgramModule.OpcodeProgram import OpcodeProgram
from IntProgramModule.OpcodeProgramsModule.Opcode_1 import Opcode_1
from IntProgramModule.OpcodeProgramsModule.Opcode_2 import Opcode_2
from IntProgramModule.OpcodeProgramsModule.Opcode_99 import Opcode_99


if __name__ == '__main__':
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

    # Compose program
    programParser = IntProgramParser(0, 4)
    programUpdater = IntProgramUpdater()

    # Create Opcode objects
    opcode_1 = Opcode_1()
    opcode_2 = Opcode_2()
    opcode_99 = Opcode_99()

    # Print initial state of the IntProgram
    print(f'Opcode Program: {intProgramCode}')

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
        print(f'Opcode Program: {intProgramCode}')

    # Exiting the program
    print('Exiting program...')