

chaine = "123456789"
k = 1
i = 0

for z in range (0,9) : 
    

    if i == 0 :
        print(chaine[int(z)])
        i+= 1
    
    elif  i == k:
        i = 0
    
    else :
        i+=1
