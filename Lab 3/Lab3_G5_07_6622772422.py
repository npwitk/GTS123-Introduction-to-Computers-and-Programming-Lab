import random as r

a = r.choice([9, 8])
a = str(a)
b = r.choice([7, 6])
b = str(b)
c = r.choice([5, 4])
c = str(c)
d = r.choice([3, 2])
d = str(d)
e = r.choice([1, 0])
e = str(e)

otp =  a + b + c + d + e

print("Your OTP is", otp + ". This password will be expired within 5 minutes.")