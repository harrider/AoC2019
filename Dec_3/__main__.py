import copy
import numpy as np

# Generate an updated position based on the instruction tuple input and current position tuple
def GeneratePositionFromInstruction(currentPosition, instruction):
    
    if(instruction[0] == 'R'):
        updatedPosition = (currentPosition[0] + instruction[1], currentPosition[1])
    elif(instruction[0] == 'L'):
        updatedPosition = (currentPosition[0] - instruction[1], currentPosition[1])
    elif(instruction[0] == 'D'):
        updatedPosition = (currentPosition[0], currentPosition[1] - instruction[1])
    elif(instruction[0] == 'U'):
        updatedPosition = (currentPosition[0], currentPosition[1] + instruction[1])
    else:
        raise ValueError(f'ERROR :: Instruction Direction "{instruction[0]}" is INVALID!')

    return updatedPosition


# https://stackoverflow.com/questions/3252194/numpy-and-line-intersections
def GetIntersect(a1, a2, b1, b2):
    """ 
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)


# Calculate the closest Intersection Point
def GetClosestIntersectionPoint(originPosition, intersectionPositions):
    closestDistance = ((float('inf'), float('inf')), float('inf'))

    for position in intersectionPositions:
        distance = CalculateDistance(originPosition, position)

        # print(f'Current Intersection Point: {position} and distance: {distance}')

        if distance < closestDistance[1]:
            closestDistance = (position, distance)

    return closestDistance


# Calculate the Manhattan Distance
def CalculateDistance(position1, position2):
    result = np.abs(position2[0] - position1[0]) + np.abs(position2[1] - position1[1])
    # result = (position2[0] - position1[0]) + (position2[1] - position1[1])

    return result


# https://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
# Determine if a point 'c' is between 2 points, 'a' and 'b'
def IsBetween(a, b, c):
    # https://stackoverflow.com/questions/19141432/python-numpy-machine-epsilon
    epsilon = np.finfo(float).eps

    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > epsilon:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True



# Main
if __name__ == "__main__":

    # Read input from input file
    with open('Input.txt', 'r') as inputFile:

        # Splits the wirepath instructions for the different wires
        wires = inputFile.read().split('\n')
        
        # Create a list to hold the individual wirepath instructions for each wire
        wirePaths = []

        # Iterate through the lists of wirepath instructions for each wire
        for wire in wires:
            # Tokenize string
            wirePath = wire.split(',')
            wirePaths.append(wirePath)

    # Initialize variables
    originPosition = (0, 0)
    wirePathInstructionLists = []

    print('Running...')

    # Iterate through each wire's list of wirepath instructions
    for wirePath in wirePaths:

        # Create a list to hold tuples of instruction actions and distance values
        currentWirePathInstructionList = []

        # Iterate through list of wirepath instructions and create tuples of (instruction action, distance)
        for instruction in wirePath:
            direction = instruction[0:1]        # Strip out first character of string
            distance = int(instruction[1:])     # Convert remaining characters to int() type

            # Create a tuple of (instruction action, distance)
            instructionTuple = (direction, distance)

            # Add new instruction tuple to current wire's wirepath instruction list
            currentWirePathInstructionList.append(instructionTuple)

        # Add current wire's wirepath instruction list to the overall list of wirepath instruction lists
        wirePathInstructionLists.append(currentWirePathInstructionList)

    # Create a list to hold each wire's wirepath positions
    wirePathPositionLists = []

    # Iterate through each wire's wire path instruction list
    for wirePathInstructionList in wirePathInstructionLists:
        
        # Create a list for the current wire's wirepath positions
        currentWirePathPositionList = []

        # Create a copy of the origin position object
        currentPosition = copy.copy(originPosition)

        # Iterate through the current wire's wirepath instruction list
        for instructionTuple in wirePathInstructionList:

            # Create a tuple containing the wire's current position after wirepath instruction is applied 
            # currentPosition = GeneratePositionFromInstruction(currentPosition, instructionTuple)
            updatedCurrentPosition = GeneratePositionFromInstruction(currentPosition, instructionTuple)


            # Add newly update current position to the current wire's wirepath position list
            distance = instructionTuple[1]
            # ====================================================
            # currentWirePathPositionList.append((currentPosition, distance))           # This line will generate the correct 'closest intersection point', but wrong step count
            currentWirePathPositionList.append((updatedCurrentPosition, distance))      # This line will generate the correct 'step count', but wrong closest intersection point
            # ====================================================

            # Update current position reference
            currentPosition = updatedCurrentPosition


        # Add current wire's wirepath position list to overall list of wirepath position lists
        wirePathPositionLists.append(currentWirePathPositionList)


    # Create a list of wirepath segment intersections    
    wirePathPositionIntersections = []

    # Iterate through c wirepath position lists
    for x in range(0, len(wirePathPositionLists)-1):
        for y in range(x + 1, len(wirePathPositionLists)):
            
            # Select the current 2 lists of wirepath positions
            leftWirePositionList = wirePathPositionLists[x]
            rightWirePositionList = wirePathPositionLists[y]

            # Iterate through the current 2 lists of wirepath position tuples
            for leftIndex in range(0, len(leftWirePositionList)-1):
                for rightIndex in range(0, len(rightWirePositionList)-1):

                    # Define the points necessary for the 2 line segments
                    a1 = leftWirePositionList[leftIndex][0]
                    a2 = leftWirePositionList[leftIndex + 1][0]
                    b1 = rightWirePositionList[rightIndex][0]
                    b2 = rightWirePositionList[rightIndex + 1][0]

                    # Calculate the intersection point between 2 line segments
                    # position with ('inf', 'inf') indicates parallel lines
                    result = GetIntersect(
                        a1,
                        a2,
                        b1,
                        b2
                    )

                    # Filter out non-intersection points
                    if float(result[0]) != float('inf') and float(result[1]) != float('inf'):
                        if (IsBetween(a1, a2, result) and IsBetween(b1, b2, result)):

                            # Add actual line segment intersections to wirepath intersection list
                            wirePathPositionIntersections.append(result)


    # Calculate the closest intersection point to the origin position
    closestDistance = GetClosestIntersectionPoint(originPosition, wirePathPositionIntersections)

    # Print the closest intersection point
    print(f'Closest intersection point: {closestDistance}')

    # Create a list to store the lists of intersection points and step counts for each wire
    wirePathsIntersectionPointAndStepCountList = []

    # Iterate through c wirepath position lists
    for wirePathPositionList in wirePathPositionLists:
        # Initialize step count to 0
        stepCount = 0

        # Create a list to store intersection points and step counts for each wire
        currentWirePathIntersectionPointAndStepCountList = []

        # Iterate through the current wire's wire path segments
        for index in range(0, len(wirePathPositionList)-1):
            # Get the start and stop point for the current line segment
            legStartPosition = wirePathPositionList[index][0]
            legStopPosition = wirePathPositionList[index+1][0]

            # Update the total step count up to the current start point
            stepCount += wirePathPositionList[index][1]

            # Iterate through list of intersection positions
            for intersectionPoint in wirePathPositionIntersections:

                # If the current intersection point is on the current leg segment
                if IsBetween(legStartPosition, legStopPosition, intersectionPoint):
                    # calculate the distance from the start point to the intersection point
                    stepDistanceToIntersection = np.abs(intersectionPoint[0] - legStartPosition[0]) + np.abs(intersectionPoint[1] - legStartPosition[1])

                    # Add that distance to the total step count up to the leg segment's start point
                    intersectionStepDistance = stepCount + stepDistanceToIntersection

                    # Add leg segment and step count up to the intersection point to the list
                    currentWirePathIntersectionPointAndStepCountList.append(((intersectionPoint[0], intersectionPoint[1]), intersectionStepDistance))

        # Add the current wire's list of intersection points and step counts to the overall list
        wirePathsIntersectionPointAndStepCountList.append(currentWirePathIntersectionPointAndStepCountList)

    # Set the minimum steps required and corresponding intersection point to infinity
    minimumDelayIntersectionPoint = ((float('inf'), float('inf')), float('inf'))

    # Iterate through wire 1's list of intersection points and step counts
    for x in wirePathsIntersectionPointAndStepCountList[0]:

        # Iterate through wire 2's list of intersection points and step counts
        for y in wirePathsIntersectionPointAndStepCountList[1]:

            # If the current intersection point in wire2's list is the same as the current intersection point in wire1's list
            if (x[0][0] == y[0][0]) and (x[0][1] == y[0][1]):
                
                # Calculate the sum of the step counts for both wires up to the current intersection point
                localSum = x[1] + y[1]

                # If the sum of the current intersection point's step counts is less than the current minimum required step count
                if localSum < minimumDelayIntersectionPoint[1]:

                    # Update the minimum required step count
                    minimumDelayIntersectionPoint = (y[0], localSum)


    # Print the minimum required step count and the corresponding intersection point
    print(f'Intersection with Minimum Delay: ({minimumDelayIntersectionPoint[0]}), # of Step: {minimumDelayIntersectionPoint[1]}')





    # print(f'Example use of GetIntersect (Parallel Lines): {GetIntersect((0, 1), (0, 2), (1, 10), (1, 9))}')
    # print(f'Example use of GetIntersect (Intersecting Lines): {GetIntersect((0, 1), (0, 2), (1, 10), (2, 10))}')