#Do you agree with the statement presented below
# while there is something to do.
    #do it
#Note that this record also declare that if there is nothing to do, nothing will happen

#in general in python, a loop can be represented as follows:
#while
    #instruction

#An Infinite Loop
#This is called the endless loop,is a sequence of sequence of instruction in which a program which repeat indefinitely(loop endlessly).
#Here is an example of loop that is not able to finish its execution

# while True:
#      print("I am stuck inside a loop")

#The loop will indefinitely print "I am stuck in a loop" on the screen.
largest_number=-999999999
number=int(input("Enter a number or type -1 to stop: "))
while number !=-1:
    if number>largest_number:
        largest_number=number
    number=int(input("Enter a number or type -1 to stop:  "))
print("The Largest number is",largest_number)
