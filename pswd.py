import random

alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','%','^','&','*','(',')','-','_']

print("WELCOME TO THE PASSWORD GENERATOR..")
print("CREATE YOUR CUSTOMIZED PASSWORD")
pswd_len=int(input("enter the length of the password: "))
n_alph=int(input("alphabets:\t"))
n_num=int(input("numbers:\t"))
n_sym=int(input("symbols:\t"))

if n_alph+n_num+n_sym==pswd_len:
    print("choose the level of complexity\n1.Easy\n2.strong\n")
    choice=int(input("enter your choice 1 or 2\n"))
    if choice==1:
        pswd=''
        for i in range(1,n_alph+1):
            char=random.choice(alph)  #generates random alphabets
            pswd+=char                   #adds that randomly generated alphabet to the empty string 
        for i in range(1,n_num+1):      
            char=random.choice(num)         #generates random numberes
            pswd+=char                          #adds that randomly generated number to the empty string 
        for i in range(1,n_sym+1):
            char=random.choice(sym)         #generates random symbols
            pswd+=char                              #adds that randomly generated symbol to the empty string 
        print("THE PASSWORD IS: ",pswd)
    
    else:
        pswd_list=[]
        for i in range(1,n_alph+1):
            char=random.choice(alph)
            pswd_list+=char
        for i in range(1,n_num+1):
            char=random.choice(num)
            pswd_list+=char
        for i in range(1,n_sym+1):
            char=random.choice(sym)
            pswd_list+=char
        random.shuffle(pswd_list)       #using "SHUFFLE" to shuffle the randomly generated password
             #here,in this case, if we print ....then the password will be in the form of list
        
        pswd=''                                   #to convert LIST to String
        for item in pswd_list:
            pswd+=item
        print("THE PASSWORD IS: ",pswd)
else:
    print("Password length is out of range.\nPlease kindly choose the no.of letters once again!")
 
