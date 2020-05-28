#code for sending multiple email a message

import re
import numpy 
import smtplib
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
li = [] 
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
# iterating till the range 
for i in range(0, n): 
    ele = str(input()) 
    li.append(ele)  
    
def check(dest):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex,dest)):  
        return 1 
    else:  
        return 0  
for dest in li: 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("suraksha.pec@gmail.com", "D_V_L_P_RS321") 
    message = "Message_you_need_to_send"
    email_check=check(dest)
    if email_check==1:
        s.sendmail("suraksha.pec@gmail.com", dest, message)
    else:
        print("invalid email")
    s.quit() 

# instead of message we can generate random numbers for otp.. but a method (redirected link) #is what we are looking upon..
#and for that just import random
#ranom.randit() instead of message
