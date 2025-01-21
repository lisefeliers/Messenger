# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: manipulations de base
# ---

# %% [markdown]
# License CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# # création de dataframe
#
# *ne pas faire en cours, lire en autonomie*

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# de très nombreuses voies sont possibles pour créer une dataframe par programme  
# en voici quelques-unes à titre d'illustration  
# voyez la documentation de `pd.DataFrame?` pour les détails  

# %% [markdown] tags=["framed_cell"]
# ### à partir du dict Python des colonnes
#
# ````{admonition} →
# avec la méthode `pandas.DataFrame`  
# on peut créer un objet de type `pandas.DataFrame`
#
#
# le dictionnaire des colonnes
#
# ```python
# cols_dict = {'names' : ['snail', 'pig', 'elephant', 'rabbit',
#                         'giraffe', 'coyote', 'horse'],
#              'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
#              'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }
# ```
#
#
# création de la `pandas.DataFrame`
#
# ```python
# df = pd.DataFrame(cols_dict)
# df
#
# ->  names     speed   lifespan
# 0    snail    0.1     2.0
# 1    pig      17.5    8.0
# 2    elephant 40.0    70.0
# 3    rabbit   48.0    1.5
# 4    giraffe  52.0    25.0
# 5    coyote   69.0    12.0
# 6    horse    88.0    28.0
# ```
# ````

# %%
# le code
import pandas as pd
import numpy as np
cols_dict = {'names' : ['snail', 'pig', 'elephant', 'rabbit',
                        'giraffe', 'coyote', 'horse'],
             'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
             'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }

df = pd.DataFrame(cols_dict)
df

# %% [markdown] tags=["framed_cell"]
# ### à partir du `dict` des colonnes et d'une `list` (d'index) des lignes
#
# ````{admonition} →
# avec la méthode `pandas.DataFrame`
#
# le `dictionnaire` des id des colonnes  
# la `liste` des id des lignes
#
# ```python
# cols_dict = {'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
#              'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }
#
# line_ids =  ['snail', 'pig', 'elephant', 'rabbit',
#              'giraffe', 'coyote', 'horse']
# ```
#
# création de la `pandas.DataFrame`
#
# ```python
# df = pd.DataFrame(cols_dict, index = line_ids)
# df
# ->       speed   lifespan
# snail    0.1     2.0
# pig      17.5    8.0
# elephant 40.0    70.0
# rabbit   48.0    1.5
# giraffe  52.0    25.0
# coyote   69.0    12.0
# horse    88.0    28.0
# ```
#
# on peut ne pas lui passer la liste des id des lignes
# ````

# %%
cols_dict = {'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
             'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }

line_ids =  ['snail', 'pig', 'elephant', 'rabbit',
             'giraffe', 'coyote', 'horse']

df = pd.DataFrame(cols_dict, index = line_ids)
df.values

# %% [markdown] tags=["framed_cell"]
# ### à partir d'un `numpy.ndarray`
#
# ````{admonition} →
# avec la méthode `pandas.DataFrame`
#
# à partir d'un `numpy.ndarray` qui décrit la *table désirée*  
# attention à la forme
#
# et attention au `type`  
# le type des éléments d'un `numpy.ndarray` est homogène  
# (si vous mélangez des `float` et des `str` vous n'avez plus que des string à-la-`numpy`...)
#
# le `numpy.ndarray`
#
# ```python
# nd = np.array([[ 0.1,  2. ],
#                [17.5,  8. ],
#                [40. , 70. ],
#                [48. ,  1.5],
#                [52. , 25. ],
#                [69. , 12. ],
#                [88. , 28. ]])
#
# ```
#
# la `pandas.DataFrame`
#
# ```python
# df = pd.DataFrame(nd)
# df
# ->    0     1
# 0    0.1   2.0
# 1   17.5   8.0
# 2   40.0  70.0
# 3   48.0   1.5
# 4   52.0  25.0
# 5   69.0  12.0
# 6   88.0  28.0
# ```
#
# **remarquez**, sans index
#
# * les index des `2` colonnes sont leurs indices `0` à `1`
# * les index des `7` lignes sont leurs indices `0` à `6`
#
# on peut passer les index (colonnes et/ou lignes)  
# au constructeur de la `pandas.DataFrame`
#
# ```python
# df = pd.DataFrame(nd,
#                   index=['snail', 'pig', 'elephant',
#                          'rabbit', 'giraffe', 'coyote', 'horse'],
#                   columns = ['speed', 'lifespan'])
# df
# ->       speed   lifespan
# snail    0.1     2.0
# pig      17.5    8.0
# elephant 40.0    70.0
# rabbit   48.0    1.5
# giraffe  52.0    25.0
# coyote   69.0    12.0
# horse    88.0    28.0
# ```
# ````

# %%
# le code
nd = np.array([[ 0.1,  2. ],
               [17.5,  8. ],
               [40. , 70. ],
               [48. ,  1.5],
               [52. , 25. ],
               [69. , 12. ],
               [88. , 28. ]])

df = pd.DataFrame(nd)
df

# %%
# le code
nd = np.array([[ 0.1,  2. ],
               [17.5,  8. ],
               [40. , 70. ],
               [48. ,  1.5],
               [52. , 25. ],
               [69. , 12. ],
               [88. , 28. ]])

df = pd.DataFrame(nd,
                  index=['snail', 'pig', 'elephant',
                         'rabbit', 'giraffe', 'coyote', 'horse'],
                  columns = ['speed', 'lifespan'])
df['Names'] = df.index
df.values

# %% [markdown]
# ### **exercice** : création de df et type des éléments

# %% [markdown]
# 1. créer un `numpy.ndarray` à partir de la liste suivante

# %%
animals = [['snail', 0.1, 2.0],
           ['pig', 17.5, 8.0],
           ['elephant', 40.0, 70.0],
           ['rabbit', 48.0, 1.5],
           ['giraffe', 52.0, 25.0],
           ['coyote', 69.0, 12.0],
           ['horse', 88.0, 28.0]]

# %%
# votre code

# %%
# prune-cell 1.

import numpy as np

nd = np.array(animals)

# %% [markdown]
# 2. Affichez le type des éléments de la table  
#    Que constatez-vous ? (U = Unicode)
#    Que se passe-t-il si on essaie d'affecter dans la case (2, 0) la chaine `"grey elephant more than 32 charaters long"`
#    Remettez-y le mot `"elephant"`

# %%
# votre code

# %%
# prune-cell 2.

# all elements in the array have type <U32
# which means
# a little-endian Unicode string of 32 characters

print(nd.dtype)

# %%
# prune-cell 2.

# strings get chopped off if too long

nd[2, 0] = "grey elephant more than 32 charaters long"
nd

# %%
# prune-cell 2.

# reset to the original value

nd[2, 0] = "elephant"
nd

# %% [markdown]
# 3. créez une `pandas.DataFrame` **à partir du tableau numpy**  
#    et avec pour noms de colonnes `'names'`, `'speed'` et `'lifespan'`
#
# ````{admonition} le passage par numpy est-il une bonne idée ?
# :class: dropdown
#
# dans cet exercice on vous impose de passer par le tableau numpy, ce qui en l'espèce n'est pas forcément la meilleure idée  
# mais ça peut être intéressant de voir ce que ça donne ... :)
# ````

# %%
# votre code

# %%
# prune-cell 3.

import pandas as pd

df = pd.DataFrame(nd, columns=['names', 'speed', 'lifespan'])
df

# %% [markdown]
# 4. affichez la valeur et le type du `'lifespan'` de l'éléphant  
# Que constatez-vous ?  
# (`object` signifie ici `str`)

# %%
# votre code

# %%
# prune-cell 4.

x = df.loc[2, 'lifespan']
x, df.lifespan.dtype, type(x)

# %% [markdown]
# 5. affichez la valeur et le type du `'names'` de l'éléphant  
# Que constatez-vous ?

# %%
# votre code

# %%
# prune-cell 5.

x = df.loc[2, 'names']
x, df.names.dtype, type(x)

# %% [markdown]
# 6. avec `loc` ou `iloc`, modifiez la valeur `elephant` par `'grey elephant more than 32 charaters long'`  
# affichez la valeur et le type du `'names'` de l'éléphant  
# un constat ?

# %%
# votre code

# %%
# prune-cell 6.

# pas de souci pour mettre une chaine plus longue

df.loc[2, 'names'] = 'grey elephant more than 32 charaters long'
df

# %% [markdown]
# 7. affichez le type des colonnes  
# utilisez l'attribut `dtypes` des `pandas.DataFrame`

# %%
# votre code

# %%
# prune-cell 7.

df.dtypes

# %% [markdown]
# 8. avec la méthode `pandas.DataFrame.to_numpy`  
# affichez le tableau `numpy` sous-jacent de votre data-frame  
# affichez le type du tableau  
# que constatez-vous ?

# %%
# votre code

# %%
# prune-cell 8.

df.to_numpy()

# %% [markdown]
# 9. modifiez les colonnes `'speed'` et `'lifespan'` de manière à leur donner le type `float`  
# (utilisez `pandas.Series.astype` voir les **rappels** en fin d'exercice)

# %%
# votre code

# %%
# prune-cell 9.

df['speed'] = df['speed'].astype(float)
df['lifespan'] = df['lifespan'].astype(float)
df.dtypes

# %% [markdown]
# 10. pour comparer, construisez directement une dataframe à partir de l'objet liste  
#     a-t-on besoin dans ce cas de convertir les types des colonnes ?

# %%
# your code

# %%
# prune-cell 10.

df2 = pd.DataFrame(animals, columns=df.columns)
df2.head(2)

# %%
# prune-cell

# much simpler: we get the right types right away

df2.dtypes

# %% [markdown]
# ````{admonition} rappels
#
# * `astype`  
# la méthode `pandas.Series.astype`, à laquelle vous indiquez un type `float`  
# crée (si c'est possible) une nouvelle `pandas.Series` dont les éléments sont de type `float`
#
# * rajouter ou modifier une colonne dans une `pandas.DataFrame`  
# revient à modifier ou rajouter une clé à un `dict`
# ````

# %% [markdown]
# ````{admonition} explications
#
# * quand les types des colonnes `numpy` ne sont pas homogènes  
# `numpy` met un tableau de caractères `Unicode` avec une taille qui permet de tout contenir
#
# * quand les types des colonnes `pandas` ne sont pas homogènes  
# sans indication, `pandas` met un `str` Python
#
# * quand dans une data-frame `pandas` on mélange des types de colonnes - genre `float` et `str`  
# `pandas` et son tableau `numpy` sous-jacent indiqueront `O` ou `object`  
# pour **mixed data types in columns**
# ````
