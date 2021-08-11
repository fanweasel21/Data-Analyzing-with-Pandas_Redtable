#!/usr/bin/env python
# coding: utf-8

# In[86]:


import numpy as np
import pandas as pd


# In[87]:


pet = pd.read_csv("/content/drive/MyDrive/RT_PET_ACP_POSBL_RSTRNT_INFO.csv")


# In[88]:


pet.head()


# In[89]:


pet_copy = pet.copy()
pet_copy.head()


# In[90]:


pet_copy['RSTRNT_TEL_NO']


# In[91]:


tel_no_0 = pet_copy[pet_copy['RSTRNT_TEL_NO'] == 0 ].index
tel_no_0


# In[92]:


# 전화번호 0 삭제
pet_copy = pet_copy.drop(tel_no_0)
pet_copy


# In[93]:


# 치킨 체인점 확인
target_string = ["치킨", "점"]
pet_copy[pet_copy["RSTRNT_NM"].map(lambda x: all(string in x for string in target_string))]


# In[94]:


# 치킨 체인점 삭제
pet_copy = pet_copy[~pet_copy["RSTRNT_NM"].map(lambda x: all(string in x for string in target_string))]
pet_copy


# In[95]:


# 갈비 체인점 확인
target_string = ["갈비", "점"]
pet_copy[pet_copy["RSTRNT_NM"].map(lambda x: all(string in x for string in target_string))]


# In[96]:


# 갈비 체인점 삭제
pet_copy = pet_copy[~pet_copy["RSTRNT_NM"].map(lambda x: all(string in x for string in target_string))]
pet_copy


# In[ ]:


# # 전골집 확인
# jeongol = pet_copy[pet_copy['RSTRNT_NM'].str.contains("전골", na=False)]
# jeongol


# In[97]:


# 피자 체인점 확인
target_string = ["피자", "점"]
pet_copy[pet_copy["RSTRNT_NM"].map(lambda x: all(string in x for string in target_string))]


# In[98]:


# 피자 체인점 삭제
pet_copy = pet_copy[~pet_copy["RSTRNT_NM"].map(lambda x: all(string in x for string in target_string))]
pet_copy


# In[99]:


# 지점 확인
jeom = pet_copy[pet_copy['RSTRNT_NM'].str.contains("점", na=False)]
jeom


# In[100]:


# 모든 지점 삭제
pet_copy = pet_copy[~pet_copy["RSTRNT_NM"].str.contains("점", na=False)]
pet_copy


# In[101]:


pet_copy.tail(20)


# In[ ]:


sample = pet_copy.sample(n=20)
sample


# In[102]:


pet_copy_copy = pet_copy.copy()


# In[103]:


pet_copy_copy


# In[104]:


pet_copy_copy.reset_index(drop=True, inplace=True)
pet_copy_copy


# In[105]:


pet_copy_copy.index=pet_copy_copy.index+1


# In[106]:


pet_copy_copy


# In[107]:


pet_copy_copy = pet_copy
pet_copy


# In[108]:


pet_copy.reset_index(drop=True, inplace=True)
pet_copy.index=pet_copy.index+1
pet_copy


# In[ ]:


# pet_copy_copy['RSTRNT_TEL_NO'] = pet_copy_copy['RSTRNT_TEL_NO'].astype(str).str.zfill(10)
# print(pet_copy_copy['RSTRNT_TEL_NO'])


# In[66]:


len(str(pet_copy.loc[:, 'RSTRNT_TEL_NO'][5]))


# In[67]:


len(pet_copy['RSTRNT_TEL_NO'])


# In[109]:


pet = pet_copy
pet


# In[110]:


pet["RSTRNT_TEL_NO"]= pet["RSTRNT_TEL_NO"].astype(str)


# In[111]:


for i in range(1, len(pet['RSTRNT_TEL_NO'])+1):
  if len(str(pet.loc[:, 'RSTRNT_TEL_NO'][i])) == 8:
    pet.loc[:, 'RSTRNT_TEL_NO'][i] = str(pet.loc[:, 'RSTRNT_TEL_NO'][i]).zfill(9)
  elif len(str(pet.loc[:, 'RSTRNT_TEL_NO'][i])) == 9:
    pet.loc[:, 'RSTRNT_TEL_NO'][i] = str(pet.loc[:, 'RSTRNT_TEL_NO'][i]).zfill(10)
  elif len(str(pet.loc[:, 'RSTRNT_TEL_NO'][i])) == 10:
    pet.loc[:, 'RSTRNT_TEL_NO'][i] = str(pet.loc[:, 'RSTRNT_TEL_NO'][i]).zfill(11)
  elif len(str(pet.loc[:, 'RSTRNT_TEL_NO'][i])) == 11:
    pet.loc[:, 'RSTRNT_TEL_NO'][i] = str(pet.loc[:, 'RSTRNT_TEL_NO'][i]).zfill(12)


# In[69]:


pd.options.mode.chained_assignment = None


# In[112]:


pet


# In[113]:


pet.to_excel('반려동물_동반_가능_여부.xlsx')


# In[ ]:





# In[ ]:




