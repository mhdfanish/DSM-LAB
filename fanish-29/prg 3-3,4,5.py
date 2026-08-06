#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,5])
y=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
a=np.array([1,2,7,9])
b=np.array([3,8,6,10])
plt.subplot(1,2,2)
plt.plot(a,b)
plt.show()


# In[5]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[1,4,9,16,25]
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("linear")
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("square")
plt.tight_layout()
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
men=(22,30,35,35,26)
women=(25,32,30,35,29)
group=["G1","G2","G3","G4","G5"]
x=np.arange(len(group))
width=0.35
plt.bar(x - width/2,men,width,label="men")
plt.bar(x + width/2,women,width,label="women")
plt.xlabel("group")
plt.ylabel("Scores")
plt.title("Scores by group and gender")

plt.show()


# In[6]:


import matplotlib.pyplot as plt
x=[3,5,6,8]
y=[1,3,5,7]
z=[2,4,3,5]
plt.plot(x,y,label="Line 1")
plt.plot(x,z,label="Line 2")
plt.title("graph")
plt.xlabel("horizontal")
plt.ylabel("vertical")
plt.legend()
plt.show()


# In[7]:


import matplotlib.pyplot as plt

language=["Java","Python","PHP","JavaScript","C#","C++"]
popularity=[22.2,17.6,8.8,8,7.7,6.7]

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.pie(popularity,labels=language,autopct="%1.1f%%")

plt.subplot(1,3,2)
plt.scatter(language,popularity)
plt.xticks(rotation=45)

plt.subplot(1,3,3)
plt.barh(language,popularity)
plt.grid()

plt.tight_layout()
plt.show()


# In[ ]:




