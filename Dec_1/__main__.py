import os
from FileIoModule.TextFileReader import TextFileReader
from ToldModule.ToldCalculation import RequiredFuelCalc, BatchRequiredFuelCalc, TotalFuelCalc

# Main
if __name__ == '__main__':

    # Create the filepath to the input file
    textFilePath = os.path.join(os.getcwd(), 'Input.txt')
    
    # Create a 'TextFileReader' object
    textFileReader = TextFileReader(textFilePath)

    # Read the data from the input file
    inputData = textFileReader.Read()

    # Calculate a list of fuel requirements based on mass of each module
    fuelRequirements = BatchRequiredFuelCalc(inputData)

    # Calculate the total fuel requirement as the sum of fuel requirements for all modules
    totalFuelRequirement = TotalFuelCalc(fuelRequirements)

    # Print the total fuel requirement
    print(f'Total fuel requirement: {"{:,}".format(totalFuelRequirement)}')
    print()