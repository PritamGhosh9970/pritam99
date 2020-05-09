#!/usr/bin/env python
# coding: utf-8

# # TASK 1:

# # 1.

# In[4]:


a = 5
b =6
print(a+b)


# #  2. Write a program which will find all such numbers which are divisible by 7 but are not a multipleof 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
# 
# 

# In[5]:


x = 0
for i in range(2000,3200,7):
    if (i % 5 != 0):
        x = i
        print(x, end=",")
        


# # 3. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
# 

# In[8]:


a = input("Enter the first name:- ")
b = input("Enter the last name:- ")
c = a[::-1]
d = b[::-1]
print(d+" "+c)


# # 4. Write a Python program to find the volume of a sphere with diameter 12 cm.  
#  
# Formula: V=4/3 * π * r 3 

# In[7]:


v = 4/3*3.14*(12/2)**3
print("volume of sphere = ", v)


# # Task 2:  
#  
#  
# # 1.  
#  
# # Write a program which accepts a sequence of comma-separated numbers from console and generate a list. 
#  
#  

# In[11]:


list = []
a = int(input("Enter the number of elements should be present in list: "))
for i in range(a):
    m = int(input("Enter any number: "))
    list.append(m)

print("Generated list: ",list)


# # 2.  Create the below pattern using nested for loop in Python. 

# In[26]:


for i in range(5):                                                   
   for j in range(i):                                                     
       print("*",end=" ")                              
       j+=1                                                                       
   print("*")
   i+=1
for i in range(5):
   for j in range(4-i):
       print("*",end=" ")
       j+=1
   print("*")
   i+=1


#  # 3.  Write a Python program to reverse a word after accepting the input from the user. 

# In[27]:


a = input("Enter any word: ")

print(a[::-1])


# # 4.  Write a Python Program to print the given string in the format specified in the ​sample output. 
#  WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens 

# In[38]:


#Trying to insert new lines using \n , spaces using \t
print('WE, THE PEOPLE OF INDIA,','\n','\t','having solemnly resolved to constitute India into a SOVEREIGN,','!','\n','\t','\t','SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC','\n','\t','\t','\t','and to secure to all its citizens')


# In[ ]:




