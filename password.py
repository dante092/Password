import re

def digitRegex(testpassword, digit_list):
    digitRegex = re.compile(r'\d')
    digit_list = digitRegex.findall(testpassword)
    return digit_list

def characterRegex(testpassword, character_list):
    characterRegex = re.compile(r'\w')
    character_list = characterRegex.findall(testpassword)
    return character_list

def test(character_list, digit_list, number_of_tests_passed =0):
    if len(character_list) >= 8:
        print('MINIMUN CHARACTER TEST PASSED')
        number_of_tests_passed = number_of_tests_passed +1
    else:
        print('MINIMUM CHARACTER TEST: FAILED')

    if digit_list != []:
        print('NUMERICAL TEST: PASSED')
        number_of_tests_passed = number_of_tests_passed +1
    else:
        print('NUMERICAL TEST: Failed ')

    if number_of_tests_passed == 2:
        print('\nPASSWORD SECURED')
    else:
        print('\nPASSWORD WEAK')





