import random

def password_generator():
    a = [chr(i) for i in range(97, 122)]  #lower_case
    A = [chr(i) for i in range(65, 91)]   #Upper_case
    one = [i  for i in range(10)]           # Integers
    sc = ['~','!','@','#','$','%','^','*','_','-','+','=','`','|','<','>',  '?',  '/'] #symbols
    p = [a,A,one,sc]
    password = ""
    for _ in range(24):
        a =random.randint(0,len(p) -1 )
        
        password += str((p[a][random.randint(0,len(p[a])- 1)] ))

    return password

print(password_generator())