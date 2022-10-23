
""" 
print("* * * * *")  
print("*       *")
print("*")
print("  *")
print("     *")
print("        *")
print("*       *")
print("* * * * *")

 """
count = -1
for i in range(0,9):
    if i == 0 or i == 8:
        print("* * * * *")
    elif i == 1 or i == 7:
        print("*       *")
    else:
        count += 1
        
        if count == 1:
            print('  ',end='')
        
        if count == 2:
            print('    ',end='')
        
        if count == 3:
            print('      ',end='')
             
        
        if count == 4:
            print('        ',end='')
             
        
        print('*')

