import re

def digitRegex(testpassword, digit_list):
    'Returns a list of Digits in password.'
    digitRegex = re.compile(r'\d')
    digit_list = digitRegex.findall(testpassword)
    return digit_list

def characterRegex(testpassword, character_list):
    'Returns a list of characters in password.'
    characterRegex = re.compile(r'\w')
    character_list = characterRegex.findall(testpassword)
    return character_list

def AlphaRegex(testpassword, alpha_list):
    'Returns a list of CAPITALIZED characters in password'
    AlphaRegex = re.compile(r'[A-Z]')
    alpha_list =AlphaRegex.findall(testpassword)
    return alpha_list

def test(character_list, digit_list, alpha_list, number_of_tests_passed =0):
    'Checks the strength of the password'
    if len(character_list) >= 8:
        print('MINIMUN CHARACTER TEST: PASSED')
        number_of_tests_passed = number_of_tests_passed +1
    else:
        print('MINIMUM CHARACTER TEST: FAILED')

    if digit_list != []:
        print('NUMERICAL TEST: PASSED')
        number_of_tests_passed = number_of_tests_passed +1
    else:
        print('NUMERICAL TEST: FAILED ')

    if len(alpha_list) >= 1:
        print('ALPHA TEST: PASSED')
        number_of_tests_passed=number_of_tests_passed +1
    else:
        print('ALPHA TEST: FAILED')

    if number_of_tests_passed == 3:
        print('\nPASSWORD SECURED')
    else:
        print('\nPASSWORD WEAK')





