

class PasswordRule_WithinRange:
    
    def __init__(self, lowerLimit, upperLimit):
        if isinstance(lowerLimit, int) == False:
            raise TypeError('ERROR :: "lowerLimit" must be of type "int"!')
        if lowerLimit < 0:
            raise ValueError('ERROR :: "lowerLimit" must be a POSITIVE number!')
        if isinstance(upperLimit, int) == False:
            raise TypeError('ERROR :: "upperLimit" must be of type "int"!')
        if upperLimit < 0:
            raise ValueError('ERROR :: "upperLimit" must be a POSITIVE number!')

        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit

    
    def Validate(self, password):
        return self.lowerLimit <= password <= self.upperLimit