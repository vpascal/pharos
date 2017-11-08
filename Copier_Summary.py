
# coding: utf-8

# In[35]:


import pandas as pd
import glob


# In[36]:


files = glob.glob("*.csv")


# In[37]:


myheader = ['Copier','User','Cost Center','Total Copies','Color Copies','Cost']
cols = [6]+list(range(18,23))
df = pd.concat((pd.read_csv(f,encoding='latin1',header=None,usecols=cols, names=myheader) for f in files))
df.Cost = df.Cost.replace('[\$,]', '', regex=True).astype(float)


# In[38]:


df = df.fillna("N/A")
grouped = df.groupby(['Copier','User','Cost Center'],as_index=False)['Total Copies','Color Copies','Cost'].sum()


# In[39]:


for printer in grouped.Copier.unique():
      grouped[grouped["Copier"]==printer].to_excel((printer+".xlsx")[10:],index=False) 
        
print("Done!")

