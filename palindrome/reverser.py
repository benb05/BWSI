
def remove(string):
    return string.replace(" ", "")

def palindromecheck(x):
    i = 0
    array = [0]*len(x)


    while i < len(x):
        array[i] = x[len(x) - 1 - i]
        i+= 1

    reversedword = "".join(array)
    reversedword1 = remove(reversedword)
    reversedword2 = reversedword1.lower()
    ogword = x.lower()
    ogword1 = remove(ogword)
    if reversedword2 == ogword1:
        return True
    else:
        return False

x = "R a c e C a R"


if palindromecheck(x) == False:
    print("This word is not a palindrome")
else:
    print("This word is a palindrome")


    
