
def encoder(x):
    i = 0
    result = []
    while i < (len(x)-1):
        j = 1
        ctr = 1
        if x[i] == x[i+1]:
            while (i+j) < len(x) and x[i] == x[i+j]:
                ctr +=1
                j+=1
            result.append(x[i])
            result.append(x[i])
            result.append(ctr)
            i+= (ctr-1)
            
        else:
            result.append(x[i])
            
            
        i+=1
    y = len(x)-1
    z = len(x)-2
    if x[y] != x[z]:
        result.append(x[len(x)-1])
    print(result)
    return result
        
          
        
encoder("Hello Worldddd!!!")