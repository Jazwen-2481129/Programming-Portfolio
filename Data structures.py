#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Student_Data = {
    
    'Andy':{"Student ID":"0001","Name":"Andy","Year":"1","Modules":["Biomolecules","Animal Organs","Core Skills 1"]},
    'Drew':{"Student ID":"0002","Name":"Drew","Year":"2","Modules":["Anatomy","Cell Communication","Core Skills 2"]},
    'Tom':{"Student ID":"0003","Name":"Tom","Year":"3","Modules":["Gene Expression","Biomembranes","Core Skills 3"]}
    
    }
# A list of Dictionaries that also contain seperate lists


# In[ ]:


Data_Access = input("WHOSE DATA DO YOU WISH TO VIEW:")
# Student's data will be printed accroding to the name inputted

Display_Data = Student_Data.get(Data_Access,"This Student's data was not found")
# If the name of the student is in the Dictionary, all the  data pertaining to that student will be displayed. 
# However if the name of the student is not in the Dictionary the above message will be displayed instead.
print(Display_Data)


# In[ ]:


Data_Input = input("DO YOU WISH TO ADD ANY NEW ENTRIES (Yes or no): ")

if str(Data_Input) == "Yes":
    New_Student_ID = input("ID: ")
    New_Name = input("Name: ")
    New_Year = input("Year: ")
    New_Modules = input("Modules:[]")
    New_Data = {"Student ID":New_Student_ID,"Name":New_Name,"Year":New_Year,"Modules":New_Modules}
    print(New_Data)
# Will allow the user to create an entirely new student entry and will display it in a dictionary format.

