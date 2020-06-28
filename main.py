
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


#Explorando as 5 primeiras linhas
black_friday.head()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[12]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[13]:


def q2():
    # Retorne aqui o resultado da questão 2.
    gender_f = black_friday['Gender'] == 'F'
    age_26_35 = black_friday['Age'] == '26-35'
    women = black_friday[gender_f & age_26_35]
    return int(women['User_ID'].count())
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[15]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[16]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[17]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return float(black_friday.isna().any(axis=1).sum()/black_friday.shape[0])
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[125]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(black_friday.isna().sum().max())
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[171]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday['Product_Category_3'].mode()[0]
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[232]:


def q8():
    # Retorne aqui o resultado da questão 8.
    black_friday['Normalized Purchase'] = (black_friday['Purchase']-(black_friday['Purchase'].min()))/(black_friday['Purchase'].max()-black_friday['Purchase'].min())
    return black_friday['Normalized Purchase'].mean()
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[252]:


def q9():
    # Retorne aqui o resultado da questão 9.
    black_friday['Standarized Purchase'] = (black_friday['Purchase']-black_friday['Purchase'].mean())/black_friday['Purchase'].std()
    less_1 = black_friday['Standarized Purchase'] < 1
    greater_1neg = black_friday['Standarized Purchase'] > -1
    return int(black_friday['Standarized Purchase'][less_1 & greater_1neg].count())
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[280]:


def q10():
    qt_null_2_3 = black_friday[['Product_Category_2', 'Product_Category_3']].isna().all(axis=1).sum()
    qt_2_null = black_friday[['Product_Category_2', 'Product_Category_3']]['Product_Category_2'].isna().sum()
    if qt_2_null == qt_null_2_3:
        return True
    else:
        False
    pass


# In[281]:


q10()

