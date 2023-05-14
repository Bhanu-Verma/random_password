#password generator
import random as rd
chars = ['abcdefg()hijkl\+=mnopqrstuvwxyz','ABCDEF{}GHIJKL/MNOPQRST~UVWXYZ','!@#$%^&*12-*34567890?']
passwd = ""
for i in range(10):
    x=rd.randint(0,2)
    passwd += rd.choice(chars[x])

print(passwd)