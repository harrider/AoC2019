

class PasswordRule_NDigitPassword:
    
    def __init__(self, requiredPasswordLength):
        if isinstance(requiredPasswordLength, int) == False:
            raise TypeError('ERROR :: "requiredPasswordLength" must be of type "int"!')
        if requiredPasswordLength < 0:
            raise ValueError('ERROR :: "requiredPasswordLength" must be a POSITIVE number!')

        self.requiredPasswordLength = requiredPasswordLength


    def Validate(self, password):
        passwordStr = str(password)

        return len(passwordStr) == self.requiredPasswordLength