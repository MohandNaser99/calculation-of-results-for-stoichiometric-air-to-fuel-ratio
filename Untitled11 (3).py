#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


print ("Input number of carbon molecules in fuel")
n= int(input())
print ("Input number of hydrogen molecules in fuel")
m = int(input ())
xx= n +(m/4)
print(xx)


# In[13]:


x_co2_1= [0] 
x_co_1= [0]
x_o2_1= [0]
x_h2o_1= [0]
x_n2_1= [0]
lamda_1= [0]


# In[14]:


count_1= 0
x =.1
while x<1 and x>= 0 : 
    lamda = x+.1
    x= lamda 
    n_co2 = xx*(2*lamda - 1 ) -(m/4)
    n_co = 2*xx*(1-lamda) 
    n_h2o= m/2 
    n_n2 = 3.76*xx*lamda
    n_total = 4.76 *xx*lamda +(m/4)
    x_co2 =  n_co2 / n_total 
    x_co = n_co / n_total 
    x_h2o=  n_h2o/ n_total 
    x_n2 =  n_n2/ n_total 
    x_co2_1.append(x_co2)
    x_co_1.append(x_co)
    x_n2_1.append(x_n2)
    x_h2o_1.append(x_h2o)
    lamda_1.append(lamda)
    count_1 +=1
    print( x_co2_1,x_co_1,x_h2o_1,x_n2_1, lamda_1,count_1)


# In[15]:


count = count_1
while x>1 and x < 1.8: 
    lamda = x+.1 
    x=lamda
    n_co2 = n 
    n_o2 = xx*(lamda-1)
    n_h2o= m/2 
    n_n2 = 3.76*xx*lamda
    n_total = 4.76 *xx*lamda +(m/4)
    x_co2 =  n_co2 / n_total 
    x_o2 = n_o2/ n_total 
    x_h2o=  n_h2o/ n_total 
    x_n2 =  n_n2/ n_total
    x_o2_1.append(x_o2)
    x_co2_1.append(x_co2)
    x_n2_1.append(x_n2)
    x_h2o_1.append(x_h2o)
    lamda_1.append(lamda)
    count+=1 
    print( x_co2_1,x_o2_1,x_h2o_1,x_n2_1,lamda_1,count)
    


# In[16]:


lamda_3=[]
lamda_3.extend(lamda_1)
del lamda_3[0]
del x_co2_1[0]
x = np.array(lamda_3)
y = np.array(x_co2_1)
plt.figure(figsize=(23,10))
plt.plot(x, y,alpha= 1)
plt.title("a relation between x for co2 and lamda")
plt.xlabel("V")
plt.ylabel("a")
plt.show()


# In[17]:


x_co_1.remove(0)
lamda_2 = []
lamda_2.extend(lamda_1)
del lamda_2[count_1:]
x = np.array(lamda_2)
y = np.array(x_co_1)
plt.figure(figsize=(23,10))
plt.plot(x, y,alpha= 1)
plt.title("a relation between x for co and lamda ")
plt.xlabel("lamda")
plt.ylabel("co")
plt.show()


# In[18]:


lamda_3 = []
lamda_3.extend(lamda_1)
del lamda_3[:count_1]
x = np.array(lamda_3)
y = np.array(x_o2_1)
plt.figure(figsize=(23,10))
plt.plot(x, y,alpha= 1)
plt.title("the relation between tbetween x for o2 and lamda ")
plt.xlabel("V")
plt.ylabel("a")
plt.show()

