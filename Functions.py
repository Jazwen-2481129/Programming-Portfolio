#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print=("This is a mini calculator.")


# In[ ]:


Value_1 = input = ("What is the first value you would like to use: ")
Value_2 = input = ("What is the second value you would like to use: ")
# The two values from these inputs will be used in the defining of functions for the calculator


# In[ ]:


def add(Value_1,Value_2):
    return Value_1 + Value_2
# The function add has been defined to add the two inputs

def subtract(Value_1,Value_2):
    return Value_1 - Value_2
# The function subtract has been defined to subtract the second value from the first input 

def multi(Value_1,Value_2):
    return Value_1 * Value_2
# The function multi has been defined to multiply the two inputs

def divi(Value_1,Value_2):
    return Value_1 / Value_2
# The function divi has been defined to divide the first input by the second one

print("The value from adding the two values is:")
Final_Addition = add(Value_1,Value_2)
print(Final_Addition)

print("The value from subtracting the second value from the first is:")
subtract(Value_1,Value_2)
Final_Subtraction = subtract(Value_1,Value_2)
print(Final_Subtraction)

print("The value from multiplying the two values is:")
multi(Value_1,Value_2)
Final_Multiplication = multi(Value_1,Value_2)
print(Final_Multiplication)

print("The value from dividing the first value by the second is:")
divi(Value_1,Value_2)
Final_Divison = divi(Value_1,Value_2)
print(Final_Divison)
# The above messages will be printed and will display all the answers to the basic operartions carried out using 
# the two input values

