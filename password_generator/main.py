import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!~@#$%^&*(){}/?"

passwd = ""

for i in range(10):
    passwd += random.choice(chars)

#print(passwd)   
#don't print the password just have it.
