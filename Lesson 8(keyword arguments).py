#Python offers another mechanism for te passing of argument,which can be helpful when you want to convince the print() function to change its behaviour

print("My name is","Python.",end="") #no newlines have been sent to the output
print("Monty Python")

#This mechanism is called keyword argument

#The keyword argument sep(as in separator)
print("My","name","is","python",sep="-")
print("My","name","is","python",sep=" ")#the sep value may be an empty string

#Both Keyword argument maybe mixed in one invocation just like here in the editor
print("My","name","is",sep="_",end="*")
print("Monty","Python",sep='*',end='\n')
