print('''  ====>Welcome to Siiuuuuuuuuuu COffee====<   

        --==^HERE is OUR MENU CARD^==--

       1 : Cold coffee 
       2 : Pasta
       3 : Americano
       4 : Mango juice 
       5 : Ice Tea


       ''')

name = str(input("Your name sir : "))

cell = int(input("Your phone number sir : "))

user_input = int(input("Which one would you like to order sir :"))

if (user_input == 1):
    print("Thank you so much sir. Your order is confirm now. You have to pay 20$")


elif (user_input == 2):
    print("Thank you so much sir. Your order is confirm now. You have to pay 22$")


elif (user_input == 3):
    print("Thank you so much sir. Your order is confirm now. You have to pay 13$")


elif (user_input == 4):
    print("Thank you so much sir. Your order is confirm now . You have to pay 28$")


elif (user_input == 5):
    print("Thank you so much sir. Your order is confirm now.You have to pay 29$")


else:
    print("Sorry sir , We don't have this item right now")
