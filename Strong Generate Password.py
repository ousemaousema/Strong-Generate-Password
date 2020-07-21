import random
s = "abcdefghijkl\
        mnopqrstuvwxyz1234\
        567890ABCDEFGHIJKLM\
        NOPQRSTUVWXYZ!@$£%<>&*\
        ()_-+[]{};/'.,-/=~µ "

passwordlen = 20
password = "".join(random.sample(s,passwordlen))
print(password)

print("Say Thank You For Oussama")