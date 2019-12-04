

class PasswordRule_ExactlyTwoAdjacentDigits:
    
    def __init__(self):
        self

    
    def Validate(self, password):
        passwordStr = str(password)
        matchingValues = {}

        for x in range(0, len(passwordStr) - 1):
            digit1 = int(passwordStr[x])
            digit2 = int(passwordStr[x + 1])

            if digit1 == digit2: 
                if digit1 in matchingValues:
                   matchingValues[digit1] = matchingValues[digit1] + 1

                else:
                    matchingValues[digit1] = 2

        for match in matchingValues:
            if matchingValues[match] == 2:
                return True

        return False