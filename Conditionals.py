#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("WELCOME TO THE SURVEY TO DECIDE WHICH BOXING WEIGHT CLASS YOU BELONG TOO BEFORE YOU START TRAINING.")


# In[ ]:


Weight = input("WHAT IS YOUR WEIGHT IN KILOGRAMS: ")

Height = input ("WHAT IS YOUR HEIGHT IN CENTIMETRES:")
#The two inputs are needed in order for the conditionals used in the program to run


# In[ ]:


if int(Weight)>=90 and int(Height)>=200:
    print("YOU ARE QUALIFIED TO ENTER THE HEAVYWIEGHT DIVISION")

elif int(Weight) >=80 and  int(Height)>=180:
    print("YOU ARE QUALIFIED FOR THE MIDDLEWEIGHT DIVISION")

elif int(Weight)>=70 and int(Height)>=150:
    print("YOU ARE QUALIFIED FOR THE LIGHTWEIGHT DIVISION")

else :
    print("YOU ARE QUALIFIED FOR THE FEATHERWEIGHT DIVISON")
# The if function will be carried out using the data from the inputs to match the criteria that best fufiles the 
# input condition


# In[ ]:


print("IF YOU DO NOT MEET ANY OF THE ABOVE AVERAGE CRIERIA DO THIS SURVEY INSTEAD.")


# In[ ]:


if int(Weight)>=90:
    print("YOU ARE QUALIFIED TO ENTER THE HEAVYWIEGHT DIVISION")
        
elif int(Weight) >=80:
    print("YOU ARE QUALIFIED FOR THE MIDDLEWEIGHT DIVISION")

elif int(Weight)>=70:
    print("YOU ARE QUALIFIED FOR THE LIGHTWEIGHT DIVISION")

else :
    print("YOU ARE QUALIFIED FOR THE FEATHERWEIGHT DIVISON") 
# A more simple conditional function in order to deal with any gaps in the original function.


# In[ ]:


print("THIS IS BASED SOLEY ON YOUR WEIGHT AND SHOULD BE SUFFIECENT IN ORDER TO START YOUR TRAINING.")

