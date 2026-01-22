#xarg

'''def student(*details):
    
    
    print(details[1])
    
    
student(102,"Avishkah",3.75)

'''



def add (*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    
    
    print(sum)
    
add (90,10)
add(20,50,90)
add(100,89,87,56)


