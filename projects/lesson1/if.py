string1='Привет'
string2='learn1111'

def strings(str1, str2):
    if len(str1) == len(str2):
        return 1
    elif len(str1) > len(str2):
        return 2
    elif len(str1) != len(str2) and str2 == 'learn':
        return 3
    else:
        return -1
 
if __name__ == '__main__':
    num=strings(string1, string2)
    print (num)

