str1 = input("Enter the first string: ").upper()
str2 = input("Enter the second string: ").upper()


def check(string1, string2) :
    string1 = sorted(string1)
    string2 = sorted(string2)

    for n in range(len(string1)) :
        if string1[n] != string2[n] : 
            return False
    return True

print(check(str1, str2))
