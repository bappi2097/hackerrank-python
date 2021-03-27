if __name__ == '__main__':
    s = input()
    validations = {
        'alnum': False,
        'alpha': False,
        'digit': False,
        'lower': False,
        'upper': False
    }
    for i in s:
        if i.isalnum():
            validations['alnum'] = True
        if i.isalpha():
            validations['alpha'] = True
        if i.isdigit():
            validations['digit'] = True
        if i.islower():
            validations['lower'] = True
        if i.isupper():
            validations['upper'] = True
    for i in validations:
        print(validations[i])
