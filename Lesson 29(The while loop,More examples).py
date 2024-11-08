#Let look at another example employing the while loop.

# odd_number=0
# even_number=0
#
# number=int(input('Enter a number or type 0 to stop: '))
# while number !=0:
#     if number % 2==1:
#         odd_number +=1
#     else:
#         even_number+=1
# number=int(input('Enter a number or type 0 to stop: '))
# print('Odd numbers count: ',odd_number)
# print('Even number count: ',even_number)

counter=5
while counter !=0:
    print('Inside the loop',counter)
    counter -=1
print("Outside the Loop",counter)
