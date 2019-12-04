import json
from SecurityModule.PasswordRuleSet import PasswordRuleSet
from SecurityModule.PasswordRule_NDigitPassword import PasswordRule_NDigitPassword
from SecurityModule.PasswordRule_NeverDecrease import PasswordRule_NeverDecrease
from SecurityModule.PasswordRule_TwoAdjacentDigits import PasswordRule_TwoAdjacentDigits
from SecurityModule.PasswordRule_WithinRange import PasswordRule_WithinRange

if __name__ == '__main__':

    # Open the 'appsettings.json' file
    with open('appsettings.json', 'r') as settingsFile:
        settings = json.load(settingsFile)

    # Initialize configurable variables
    passwordLength = settings['PasswordLength']
    passwordRangeLowerLimit = settings['PasswordRange']['LowerLimit']
    passwordRangeUpperLimit = settings['PasswordRange']['UpperLimit']

    # Create password rule objects
    rule_SixDigitPassword = PasswordRule_NDigitPassword(passwordLength)
    rule_WithinRange = PasswordRule_WithinRange(passwordRangeLowerLimit, passwordRangeUpperLimit)
    rule_DigitsNeverDecrease = PasswordRule_NeverDecrease()
    rule_TwoAdjacentDigitsEqual = PasswordRule_TwoAdjacentDigits()

    # Create list of rules
    ruleList = [
        rule_SixDigitPassword,
        rule_WithinRange,
        rule_DigitsNeverDecrease,
        rule_TwoAdjacentDigitsEqual
    ]

    # Create a password rule set object
    passwordRuleSet = PasswordRuleSet(ruleList)

    # Initialize # of valid passwords to 0
    validPasswords = 0

    # Iterate through all passwords within the given range from the 'appsettings.json' file
    for password in range(passwordRangeLowerLimit, passwordRangeUpperLimit):

        # If the current password has been validated by all password rules
        if passwordRuleSet.Validate(password):
            print(f'Valid password found: {password}')
            
            # Increment # of valid passwords counter
            validPasswords += 1

    # Print the # of valid passwords
    print('======================================================')
    print(f'Number of valid passwords in range({passwordRangeLowerLimit},{passwordRangeUpperLimit}): {validPasswords}')