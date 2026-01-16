import random

print('''
      
      
      Hey bruh 
      
      Welcome to number game ''')


num = random.radient(1,30)

name = str (input("Enter your name : "))

for i in range(100):
      inputnumber=int(input("Enter your number : "))
    
      if(inputnumber > num):
        print("Your Input Number is big")
      elif(inputnumber < num):
        print("Your Input Number is small")
      elif(inputnumber == num):
       print("You guess the right number ::: Great")
      break
