# least eight characters long,
# at least one digit.
# contains both uppercase and lowercase characters, a

import re


def strongPassword(pwd):
    regExp = re.compile(r'.{8,}')
    if regExp.search(pwd) is not None:
        regExp = re.compile(r'.[\d]+')
        if regExp.search(pwd) is not None:
            regExp = re.compile(r'.[A-Z]+')
            if regExp.search(pwd) is not None:
                regExp = re.compile(r'.[a-z]+')
                if regExp.search(pwd) is not None:
                    return True

    return False


passList = ['password.', '123456', '1234Abl56789',
            'guest', 'qwert1yA', '12345678', '111111', '12345']

for password in passList:
    print(password, ' : ', strongPassword(password))
