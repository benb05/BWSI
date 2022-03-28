

def palindromecheck(x):
    i = 0
    array = [0]*len(x)


    while i < len(x):
        array[i] = x[len(x) - 1 - i]
        i+= 1

    reversedword = "".join(array)
    if x == reversedword:
        return True
    else:
        return False

if palindromecheck(x) == False:
    print("This word is not a palindrome")
else:
    print("This word is a palindrome")


    
