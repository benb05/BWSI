def decoder(x):
    i = 0
    result = []
    while i < len(x) - 2:
        while i < len(x) - 2 and isinstance(x[i + 2], int) == True :
                        j = 0 
                        while j < x[i + 2]:
                            result.append(x[i])
                            j+= 1
                        i+= 1
        while i < len(x) -2 and isinstance(x[i + 2], int) == False :
                result.append(x[i])
                i+=1
        
    i+=1
    if isinstance(x[i], int) == False:
        result.append(x[i])
    print(result)
    string = ""
    string = string.join(result)
    return string

decoder(["a","b", "c", "c", 4, "d" ])