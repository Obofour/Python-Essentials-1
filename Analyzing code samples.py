# How to identify the larger of two numbers
First_num=int(input("Enter your first number: "))
Second_num=int(input("Enter your Second number: "))

if First_num >Second_num:
    print(f'{First_num} is the largest')
elif First_num == Second_num:
    print("They are equal")
else:
    print(f'{Second_num} is the largest')

