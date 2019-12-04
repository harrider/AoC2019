# Advent of Code 2019

## Day 4

[Advent of Code 2019: Day 4 Problem](https://adventofcode.com/2019/day/4)


### How to Run:

1. On the command line, in the top-level 'Dec_4' directory:
    * type: __"py \_\_main\_\_.py"__


### App Settings:

The 'appsettings.json' file contains the following configurable parameters:

1. **'PasswordLength'**
    * Change the required length of a valid password
    
2. **'PasswordRange'**
    * Change the range of passwords to check:
        * __LowerLimit__ = value determines the lower limit of passwords to check
        * __UpperLimit__ = value determines the upper limit of passwords to check

3. **'UseExactlyTwoAdjacentDigitsRule'**
    * Change the password validation rule to use for validating two adjacent digits are equal
        * __false__ = use the Part 1 validation rule
        * __true__ = use the Part 2 validation rule