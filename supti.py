
print('''===>--->>>Welcome to calculation<<<---<===


        1. Circle
        2. Triangle
        3. Squre
        4. Rectangle

      ''')


user_Redirect_Input = int(input("Enter Your Choose : "))

py = 3.1416
tri = 1/ 2

if (user_Redirect_Input == 1):

    numberOne = int(input("Enter your Radious value : "))
    answer = py * numberOne ** 2

    print(f"Your answer is : {answer}")



elif (user_Redirect_Input == 2):

    numberOne = int(input("Enter your Base value :"))
    numberTwo = int(input("Enter yout High value : "))
    answer = 1 / 2 * numberOne * numberTwo

    print(f"Your answer is : {answer}")



elif (user_Redirect_Input == 3):
    numberOne = int(input("Enter your Sides value : "))
    answer = numberOne ** 2

    print(f"Your answer is : {answer}")



elif (user_Redirect_Input == 4):
    numberOne = int(input("Enter your Wide value : "))
    numberTwo = int(input("Enter your Hight value : "))
    answer = numberOne * numberTwo

    print(f"Your answer is : {answer}")





else:
    print("YOUR INPUT IS WRONG  , GO AND LEARN BEFORE USE IT")