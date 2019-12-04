

class PasswordRule_NeverDecrease:
    
    def __init__(self):
        self

    
    def Validate(self, password):
        passwordStr = str(password)

        for x in range(0, len(passwordStr) - 1):
            for y in range(x + 1, len(passwordStr)):
                if int(passwordStr[y : y+1]) < int(passwordStr[x : x+1]):
                    return False

        return True