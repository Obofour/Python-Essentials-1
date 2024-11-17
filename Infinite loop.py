# while True:
#     print("I am stuck inside a loop") #Infinite loop

largest_Number=-999999999

number=int(input("Enter a number or type -1 to stop: "))

while number !=-1:
    if number>largest_Number:
        largest_Number=number
    number=int(input("Enter a number or -1 to stop: "))

print("The largest number is ",largest_Number)


