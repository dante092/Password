import password, getpass
character_list = []
digit_list = []

print('\n')
print(' PASSWORD STRENGTH TEST'.center(40, '='))

testpassword = getpass.getpass('\nPASSWORD: ')

# Uses Regexes to examine password.
digit_list = password.digitRegex(testpassword, digit_list)
character_list = password.characterRegex(testpassword,character_list)

print('--- PASSWORD HAS ' + str(len(character_list)) + ' CHARACTERS')
print('--- PASSWORD HAS ' + str(len(digit_list)) + ' DIGITS\n')
print('PASWORD RESULTS'.center(40,'='))

# reads the data from the Regexes and determines strength of Password.
password.test(character_list,digit_list)


