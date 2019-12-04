

class PasswordRuleSet:

    def __init__(self, rules):
        if isinstance(rules, list) == False:
            raise TypeError('ERROR :: "rules" must be of type "list"!')
        if len(rules) == 0:
            raise ValueError('ERROR :: "rules" list is EMPTY!')

        self.rules = rules

    
    def Validate(self, password):

        for rule in self.rules:
            if rule.Validate(password) == False:
                return False

        return True