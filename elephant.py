

#Here I can import date and month

A = int(input("Enter the date :"))

B = input("Enter the month name :")



#It'll count total times and ammount

today_spend = []

for info in range(500):     #loop will count the total calculation


    time   = input("Enter the time: ")

    amount = input("Enter the amount: ")


#Here it'll break all the condition of the loop

    if time == "end":
        break
    today_spend.append(amount)


print(today_spend)



sum = 0
for i in today_spend:
    sum += int(i)


print(sum)


with open("Project Spending history.txt" ,"a") as saver:
    saver.write(f"{A} {B} = {sum} taka \n ")

