import os 
import smtplib 
import random
import math

digits = "0123456789"
OTP=""
for i in range(6):
  OTP+=digits[math.floor(random.random()*10)]
otp = OTP+" is your otp"
msg = otp
s = smtp.SMTP('smtp.gmail.com',587)
s.startttls()
s.login(("user_mail","user_password")
email = input("Enter your email-id for verification")
s.sendmail('&&&&&&&&',email,msg)
a = input("Enter you OTP")
if a==OTP:
  print("Verified")
else :
  print("Plese Check Your OTP and Try Again")
