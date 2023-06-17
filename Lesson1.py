def palindrom_check(string):
    if string[::-1] == string:
        print(True)
    else:
        print(False)
palindrom_check('лепспел')
palindrom_check('helloworld')
