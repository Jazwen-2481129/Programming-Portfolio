#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input("What is your Name: ")

Greetings = str("Hello")

for Greet in Greetings:
    print(Greet)
    
for character in name:              
    print(character) 
# The name inputted will be turned into a list in addition to the greeting Hello.


# In[ ]:


with open('Text.txt','w') as f:
    f.write("This is the to do list for today")
# Creates a new text file and writes the above text.


# In[ ]:


Mourning_Mood = input("How are you feeling today? Good or Bad: ")


# In[ ]:


if Mourning_Mood == "Good":
    print("This is your to do list for the day")
    with open ('Plan.txt','r') as f_Plan:
        sometext=f_Plan.read()
    
    print(sometext,end = "")
# Takes data written in the Plan.txt file and displays it on the terminal for the user to view without having to open
# the file.

if Mourning_Mood == "Bad":
    import mymodule
    Response = mymodule.Bad_Day
    print(Response)
# Imports the data written in the mymodule.py and prints it in response to the 'if' conditional. 

