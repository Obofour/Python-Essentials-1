#we will say that number handling by modern computers are two types
# 1. Integers that is ,those which are devoid of the fractional part;
# 2.Floating point numbers (Or simply floats) that contain the fraction part.

#This definition is not quite accurate but quite sufficient for now

#Take for example eleven million one hundred one hundred.if you look pencil in your hand right now ,you would write number like this "11,111,111" or like this 11.111.111 or even like this 11 111 111

#It is clear this provision makes it easier to read ,especially when the number consist of many digit
#However Python doesn't accept this what python does allow though is underscores(_) or there can write it number like this (11111111) or this(11_111_111)

#Octal and hexadecimal numbers
#it an integer is preceded by an 00 or Oo(zero-o), it will be treated as an Octal value.This means that the number must contain digit taken the [0..7] range only
print(0o123)#)0o123 is an Octal number with a decimal value 83

#Hexadecimal
#The second conversion allow us to use the hexadecimal numbers,such numbers should be preceded by the prefix 0x (zero-x)
#Try this
print(0x123)

