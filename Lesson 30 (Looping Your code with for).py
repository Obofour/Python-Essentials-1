#Another Kind of Loop available in Python comes  from the Observation that sometimes it's more important to
#count the "turns" of the loop

#imagine that a loop's body needs to be executed exactly one hundred times

#i=0
#while i < 100:
 #do_something()
    #i+=1
#Actually te for loop is designed to do more complicated task it can browse large collection of data item by item
 # for i in range(100)
    #do_something()
        #pass

#Take note
# 1.the for key opens for loop;there's is no condition after it,you don't have to think after a condition
# 2.any variable after the keyword is the control variable of the loop; it counts the loops turns and does it automatically
# 3.the in keyword introduces a syntax element describing the range of possible values being assigned to the control variable
# 4.the range() responsible for generating all the desire values of control variables

for i in range(10):
    print("The value of i is currently",i)