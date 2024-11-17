#break-exist the loop immediately and unconditionally ends the loop's operation;the program begin to execute the nearest instruction after the loop's body;
#continue-behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression in tested immediately
#both are keywords
print("the break instruction ")
for i in range(1,6):
    if i==3:
        break
    print("Inside the loop",i)
print("outside the loop.")

#continue -example
print("\n the continue instruction")
for i in range(1,6):
    if i==3:
        continue
    print("Inside the loop",i)
print("Outside the loop",i)