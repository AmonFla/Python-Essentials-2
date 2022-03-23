def mysplit(strng):
    temp = ''
    lst =[] 
    for i in strng:
        if i != " ":
            temp += i
        elif temp != '':
            lst.append(temp)
            temp = ''
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
