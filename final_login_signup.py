import json 
import string

def password():
    pwd=input('create your password:\n')
    # for  letter in string.ascii_lowercase or (letter in string.ascii_uppercase):
    #     if letter in pwd:
    #         sp_list=['@','.','#','!','*','$','&','_','-']
    #         for s_char in sp_list:
    #             if s_char in pwd:
    #                 for num in range(0,10):
    #                     # if str(num) in pwd:
    #                         return pwd
    #                     # else:
    #                     #     print('add some digit in your password:')
    #                     #     password()
    #             else:
    #                 print('add some s_char in your password:')
    #                 password()
    #     else:
    #         print('add some alphebets,num,special character in your password to make it stronger:')
    #         password()

    for item in pwd:
        upper_case=0
        lower_case=0
        num=0
        sp_char=0
        if item >='a' and item<='z':
            lower_case+=1
        elif item>='A' and item<='Z':
            upper_case+=1
        # elif int(item)>=0 and int(item)<=9:
        elif item in ['1','2','3','4','5','6','7','8','9','0']:
            num+=1
        elif item in ['@','.','#','_']:
            sp_char+=1
    if lower_case>0 and upper_case>0 and num>0 and sp_char>0:
        return pwd
    else:
        print('add upper_case,lower_case , num and any special character to your password')
        password()
# password()

def login():
    mob_no=int(input('enter your mob no:'))

    pwd=input('enter your password:')

    file=open('text_new.json','r')
    a=json.load(file)
    # print(a)
    # print(type(a))
    if a['mob. no.']==mob_no:
        if a['password']==pwd:
            f=open('info.text','w')
            f.write('congratulation!, You did it.')
            print('successfully logined!')

        else:
            print('enter the correct password:')
    else:
        print('this no. is not resistered')





def sign_up():
    global dict
    dict={}
    Name=input('enter your name:')
    dict['Name']=Name
    def mob():
        mob_no=int(input('enter your phone no:'))
        if len(str(mob_no))==10 :
            dict['mob. no.']= mob_no
        else:
            print('please , enter correct mob no. of 10 digits!')
            mob()

    def email():
        email_id=input('enter your email id:')
        return email_id
    mob()
    dict['email']=email()

    a = password()
    def testing_password():
        confirm_password=input('enter your password again:')
        if a==confirm_password:
            dict['password']=a
            print('Cogreats!,successfully resistered!')

        else:
            print('password unmatched')
            testing_password()

    testing_password()

    f=open('text_new.json','w')
    json.dump(dict,f, indent = 4)


def already_registered(a):
    if a=='yes':
        login()
    else:
        sign_up()

already_registered(input("Have you already resistered yourself here? if yes enter 'yes', else enter 'no':\n"))


