i_s = input()         #i_s=Input String   
os = ''               #os=Output String
error = 0

for i in input_str:
    if i.islower():  
        os += os.join(i.upper())  
    elif i.isupper(): 
        os += os.join(i.lower())  
    elif i == ' ':
        os += os.join(i)  
    elif i.isdigit():  
        print('Numbers not allowed')
        error = 1 
        break
    else: 
        print('Invalid Input')
        error = 1  
        break

if error != 1:  
    print(os)
