import password, getpass
character_list = []
digit_list = []
alpha_list=[]

print('\n')
print(' PASSWORD STRENGTH TEST'.center(40, '='))

testpassword = getpass.getpass('\nPASSWORD: ') # USes getpass to hide password when typing in terminal. 
print('PASWORD RESULTS'.center(40,'='))

# Uses Regexes to examine password.
digit_list = password.digitRegex(testpassword, digit_list)
character_list = password.characterRegex(testpassword,character_list)
alpha_list= password.AlphaRegex(testpassword, alpha_list)

# reads the data from the Regexes and determines strength of Password.
password.test(character_list,digit_list, alpha_list)

print('     -- PASSWORD HAS ' + str(len(character_list)) + ' CHARACTERS')
print('     -- PASSWORD HAS ' + str(len(digit_list)) + ' DIGITS')
print('     -- PASSWORD HAS ' + str(len(alpha_list))+ ' UPPERCASE LETTERS')







