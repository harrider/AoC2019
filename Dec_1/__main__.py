import os
import json
from FileIoModule.TextFileReader import TextFileReader
from ToldModule.ToldCalculation import RequiredFuelCalc, BatchRequiredFuelCalcFirstPoll, BatchRequiredFuelCalcSecondPoll, TotalFuelCalc

# Main
if __name__ == '__main__':
    
    # Read in app configs
    appsettingsJsonFilePath = os.path.join(os.getcwd(), 'appsettings.json')
    with open(appsettingsJsonFilePath, 'r') as settingsFile:
        configs = json.load(settingsFile)

        if configs == None:
            raise ValueError('ERROR :: Problem reading "appsettings.json"!')
        if isinstance(configs['DataInputFileName'], str) == False:
            raise ValueError('ERROR :: appsettings parameter "DataInputFileName" must be of type "str"!')
        if configs['DataInputFileName'].lower().endswith('.txt') == False:
            raise ValueError('ERROR :: appsettings parameter "DataInputFileName" must a ".txt" file!')
        if isinstance(configs['UseSecondPollFuelCalculation'], bool) == False:
            raise ValueError('ERROR :: appsettings parameter "UseSecondPollFuelCalculation" must be of type "bool"!')


    # Create the filepath to the input file
    inputTextFilePath = os.path.join(os.getcwd(), configs['DataInputFileName'])
    
    # Create a 'TextFileReader' object
    textFileReader = TextFileReader(inputTextFilePath)

    # Read the data from the input file
    inputData = textFileReader.Read()

    # Calculate a list of fuel requirements based on mass of each module
    if configs['UseSecondPollFuelCalculation']:
        fuelRequirements = BatchRequiredFuelCalcSecondPoll(inputData)
    else:
        fuelRequirements = BatchRequiredFuelCalcFirstPoll(inputData)
        
    # Calculate the total fuel requirement as the sum of fuel requirements for all modules
    totalFuelRequirement = TotalFuelCalc(fuelRequirements)

    # Print the total fuel requirement
    print(f'Total fuel requirement: {"{:,}".format(totalFuelRequirement)}')
    print()