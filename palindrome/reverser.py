

def reverser(x):
    i = 0
    array = [0]*len(x)


    while i < len(x):
        array[i] = x[len(x) - 1 - i]
        i+= 1

    reversedword = "".join(array)



reverser("hell")
print(reversedword)
