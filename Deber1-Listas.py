#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("MULTIPLICACIÓN DE MATRICES- No se pide el numero de filas de la matriz dos porque debe ser el mismo valor de las columnas de la Matriz 1")
f1=int(input("Matriz 1: introduzca numero de filas"))


# In[4]:


c1=int(input("Matriz 1: introduzca numero de columnas"))


# In[5]:


c2=int(input("Matriz 2: introduzca numero de columnas"))


# In[6]:


A=[]
for i in range(f1):
    A.append([0]*c1)


# In[7]:


for i in range(f1):
    print(A[i])


# In[8]:


B=[]
for i in range(c1):
    B.append([0]*c2)


# In[9]:


for i in range(c1):
    print(B[i])


# In[10]:


for a in range(f1):
    for b in range(c1):
        A[a][b]=int (input("Ingrese valor (%d,%d): " % (a,b)))


# In[11]:


for i in range(f1):
    print(A[i])


# In[12]:


for a in range(c1):
    for b in range(c2):
        B[a][b]=int (input("Ingrese valor (%d,%d): " % (a,b)))


# In[13]:


for i in range(c1):
    print(B[i])


# In[14]:


C=[]
for i in range(f1):
    C.append([0]*c2)


# In[15]:


for i in range(f1):
    print(C[i])


# In[16]:


for i in range(f1):
    for j in range(c2):
        for k in range(c1):
            C[i][j]+= A[i][k]*B[k][j]


# In[17]:


for i in range(f1):
    R=[]
    for j in range(c2):
        R.append(C[i][j])
        print("El resultado es:")
    print(R)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




