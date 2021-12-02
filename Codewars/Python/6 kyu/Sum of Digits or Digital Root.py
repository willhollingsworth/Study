def digital_root(n):    
    while(len(str(n))) > 1:
        count = 0
        for x in str(n):
            count += int(x)
        n = count
    return n
        
    # if (len(str(n))) > 1:
        
            
    
    # 
    #     print
    
    
    
print(digital_root(493193), 2)
print(digital_root(16), 7)
print(digital_root(942), 6)
print(digital_root(132189), 6)