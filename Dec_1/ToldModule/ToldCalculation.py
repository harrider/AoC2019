import math
from typing import Union, List


def RequiredFuelCalc(mass : Union[int, float]):
    if mass == None:
        raise ValueError('ERROR :: "mass" was None!')
    if isinstance(mass, int) == False and isinstance(mass, float) == False:
        raise TypeError('ERROR :: "mass" must be of type "int" or "float"!')
    if mass < 0:
        raise ValueError('ERROR :: value for "mass" was NEGATIVE!')

    requiredFuel = __FuelCalcFormula(mass)

    return requiredFuel


# =======================================================================================

def BatchRequiredFuelCalcFirstPoll(inputData):
    if inputData == None:
        raise ValueError('ERROR :: "inputData" list was None!')
    if isinstance(inputData, list) == False:
        raise ValueError('ERROR :: "inputData" list is not of type "List[int]" or "List[float]"!')

    calculatedFuelRequirements = []

    for mass in inputData:
        if isinstance(mass, str):
            validatedMass = float(mass)
        else:
            validatedMass = mass

        requiredFuel = __FuelCalcFormula(validatedMass)
        calculatedFuelRequirements.append(requiredFuel)

    return calculatedFuelRequirements

# =======================================================================================
# =======================================================================================

def BatchRequiredFuelCalcSecondPoll(inputData):
    if inputData == None:
        raise ValueError('ERROR :: "inputData" list was None!')
    if isinstance(inputData, list) == False:
        raise ValueError('ERROR :: "inputData" list is not of type "List[int]" or "List[float]"!')

    calculatedFuelRequirements = []

    for mass in inputData:
        if isinstance(mass, str):
            validatedMass = float(mass)
        else:
            validatedMass = mass

        requiredFuel = __FuelRequirementRecurssive(validatedMass)
        calculatedFuelRequirements.append(requiredFuel)

    return calculatedFuelRequirements


def __FuelRequirementRecurssive(mass):
    result = __FuelCalcFormula(mass)

    if result <= 0:
        return 0
    else:
        result += __FuelRequirementRecurssive(result)

    return result

# =======================================================================================



def TotalFuelCalc(fuelRequirements):
    if fuelRequirements == None:
        raise ValueError('ERROR :: "fuelRequirements" list was None!')
    if isinstance(fuelRequirements, list) == False:
        raise ValueError('ERROR :: "fuelRequirements" list is not of type "List[int]" or "List[float]"!')

    totalFuelRequirement = 0

    for fuelRequirement in fuelRequirements:
        totalFuelRequirement += fuelRequirement

    return totalFuelRequirement


def __FuelCalcFormula(mass):
    divisor = 3
    subtractor = 2

    result = math.floor((mass / divisor)) - subtractor

    return result