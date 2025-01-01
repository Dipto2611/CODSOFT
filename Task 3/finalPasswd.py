"""TASK 3"""

#Password Generator

import random
import string



lower_ = string.ascii_lowercase   # i.e abcde
upper_ = string.ascii_uppercase   # i.e ABCDE
nos_ = string.digits              # i.e 012345
Special_char = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

#passwd criteria:

def easy_pass():
    return lower_+nos_

def medium_pass():
    return lower_+upper_ + nos_

def strong_pass():
    return lower_+upper_+nos_+Special_char

#here the level of difficulty is defined for the user to their passwd:

def desired_passwd():
    type_of_pass = input("Enter the level of passwd:- Easy/Medium/Hard:").lower()
    if type_of_pass == "easy":
        return easy_pass()
    elif type_of_pass == "medium":
        return medium_pass()
    else:
        return strong_pass()

#define main func:

def main():
    while (1):
        n = int(input("Enter the length of the reqd pass:")) #reqd len of passwd
        res = random.choices(desired_passwd(), k=n)  #here random func will selects the out of it random chars
        print(''.join(res))

        #for continuation of new-new passwd!!
        progress=int(input("Do you want a new passwd: (YES=1 / NO=0)"))
        if progress==0:
            break

main()