

class PasswordRule_TwoAdjacentDigits:
    
    def __init__(self):
        self

    
    def Validate(self, password):
        passwordStr = str(password)

        for x in range(0, len(passwordStr) - 1):
            if int(passwordStr[x]) == int(passwordStr[x + 1]):
                return True

        return False