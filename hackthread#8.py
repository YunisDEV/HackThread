if __name__ == '__main__':
    s = input()
    # isalnum
    for i in s:
        if i.isalnum():
            isalnum = True
    print(isalnum | False)
    # isalpha
    for i in s:
        if i.isalpha():
            isalpha = True
    print(isalpha | False)
    # isdigit
    for i in s:
        if i.isdigit():
            isdigit = True
    print(isdigit | False)
    # islower
    for i in s:
        if i.islower():
            islower = True
    print(islower | False)
    # isupper
    for i in s:
        if i.isupper():
            isupper = True
    print(isupper | False)
