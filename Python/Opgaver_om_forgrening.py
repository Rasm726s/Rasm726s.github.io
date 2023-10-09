username='Rasmus'
password ='1234'  
username_input=input() 
if username == username_input:
    print('Rasmus')
    password_input =input()
    if password == password_input:
        print('Access granted.')
    else:
        print('Wrong password')
else:
    print('worng name')