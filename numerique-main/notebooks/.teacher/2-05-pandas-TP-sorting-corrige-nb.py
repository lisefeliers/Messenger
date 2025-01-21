# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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
#     title: TP sur le tri d'une dataframe
# ---

# %% [markdown]
# License CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# # TP sur le tri d'une dataframe

# %% [markdown]
# **Notions intervenant dans ce TP**
#
# * affichage des données par `plot`
# * tri de `pandas.DataFrame` par ligne, par colonne et par index
#
# **N'oubliez pas d'utiliser le help en cas de problème.**

# %% [markdown]
# ## tri et affichage

# %% [markdown]
# 1. importez les librairies `numpy` et `pandas`

# %%
# votre code

# %%
# prune-cell

import numpy as np
import pandas as pd

# %% [markdown]
# 2. importez la librairie `matplotlib.pyplot` avec le nom `plt` 

# %%
# votre code

# %%
# prune-cell

import matplotlib.pyplot as plt

# %% [markdown]
# 3. lors de la lecture du fichier de données `data/titanic.csv`  
#    1. gardez uniquement les colonnes `cols` suivantes `'PassengerId'`, `'Survived'`, `'Pclass'`, `'Name'`, `'Sex'`, `'Age'` et `'Fare'`
#
#    1. mettez la colonne `PassengerId` comme index des lignes
#    1. besoin d'aide ? faites `pd.read_csv?`

# %%
# votre code

# %%
# prune-cell

cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('data/titanic.csv', index_col='PassengerId', usecols=cols)

# %% [markdown]
# 4. en utilisant la méthode `df.plot()`  
#    plottez la dataframe (pas la série) réduite à la colonne des ages  
#    utilisez le paramètre de `style` `'rv'` (`r` pour rouge et `v` pour le style: points triangulaires)
#
#    vous allez voir les points *en vrac*; dans la suite on va s'efforcer de les trier, pour mieux
#    voir la distribution des âges dans la population concernée

# %%
# votre code

# %%
# prune-cell

df[['Age']].plot(style='rv');

# %% [markdown]
# 5. pour commencer on va trier - i.e. mettre les lignes de la  dataframe suivant l'ordre d'une colonne    
#    en utilisant la méthode `df.sort_values()`:
#    1. créez une nouvelle dataframe  dont les lignes sont triées  
#       dans l'ordre croissant des `'Age'` des passagers
#    2. pour constater qu'elles sont triées, affichez les 4 premières lignes de la dataframe  
#       la colonne des `Age` est triée  
#       les lignes ont changé de place dans la table
#    3. remarquez que l'indexation a été naturellement conservée 

# %%
# votre code

# %%
# prune-cell
# on trie dans l'axe des lignes donc `axis=0`

df_sorted = df.sort_values(by='Age', ascending=True, axis=0)
df_sorted.head(4)

# %% [markdown]
# 6. 1. plottez la colonne des ages de la dataframe triée  
#       pour changer un peu on va mettre un style `'b.'`
#    1. Que constatez-vous ?

# %%
# votre code

# %%
# prune-cell

# pas de changement majeur, la sortie n'est pas triée

df_sorted[['Age']].plot(style='b.');

# %% [markdown]
# 7. 1. la logique de `df.plot()` consiste
#
#       * à **utiliser comme abscisses** l'index de la dataframe
#       * et accessoirement à faire autant de plots que de colonnes - ici on n'en a qu'une
#     vous tracez donc le point $(804, 0.42)$ puis le point $(756, 0.67)$ ...  
#     alors que vous voudriez tracer le point $(0, 0.42)$ puis le point $(1, 0.67)$ ...  
#     c'est à dire: le fait d'utiliser le 'PassengerId' n'est pas bon, on voudrait que les abscisses soient les indices de lignes
#    1. une solution: voyez la méthode `reset_index()`
#       qui permet de transformer l'index en une colonne normale  
#    1. utiliser cette méthode et regardez ce que vous avex dans l'index ensuite
#    1. plottez le résultat  
#       normalement à ce stade vous obtenez la visualisation qu'on cherche

# %%
# votre code

# %%
# prune-cell

df_sorted.reset_index()[['Age']].plot(style='b.');

# %% [markdown]
# ## tri des lignes selon plusieurs critères
#
# quand on trie, que faire en cas d'égalité ?  
# en général on choisit plusieurs critères, on trie selon le premier, puis en cas d'égalité selon le second, etc..
#
# *note*: on appelle cela un ordre lexicographique, car c'est - un peu - comme dans un dictionnaire

# %% [markdown]
# 0. rechargez la dataframe

# %%
# votre code

# %%
# prune-cell

cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('data/titanic.csv', index_col='PassengerId', usecols=cols)

# %% [markdown]
# 2. utilisez `df.sort_values()` pour trier la dataframe suivant la colonne (`'Pclass'`)  
#    et trier les lignes identiques (passagers de même classe) suivant la colonne (`'Age'`)  

# %%
# votre code

# %%
# prune-cell 2.

df_sorted = df.sort_values(by=['Pclass', 'Age'])
df_sorted.head(3)

# %% [markdown]
# 3. sélectionnez, dans la nouvelle dataframe, la sous-dataframe des gens dont les ages ne sont pas définis  
#
# *hint*: utiliser la méthode `isna` sur une série, pour créer un masque de booléens, et appliquer ce masque à la dataframe   

# %%
# votre code

# %%
# prune-cell

df_sorted_isna = df_sorted[df_sorted['Age'].isna()]
df_sorted_isna

# %% [markdown]
# 4. combien nous manque-t-il d'ages ?

# %%
# votre code

# %%
# prune-cell

len(df_sorted_isna)

# %% [markdown]
# 5. où sont placés ces passagers dans la data-frame globale triée ?
#    - [ ] en début (voir avec `head`)
#    - [ ] ou en fin (voir avec `tail`)
#    - [ ] ou c'est plus compliqué que ça ?
#
# ````{admonition} *hint*
# :class: dropdown
#
# la façon standard d'afficher un dataframe consiste à montrer le début et la fin  
# il y a des situations, comme celle-ci, où on veut avoir une *vision globale* des données,
# et pour cela le bon réflexe consiste à se ramener à un tableau numpy  
# pour cela voyez par exemple `df.no_numpy()`
# ````

# %%
# votre code

# %%
# prune-cell

# les nan vont plutôt à la fin

df_sorted.tail() 

# %%
# prune-cell

# pour voir un aperçu de tous les résultats, et visualiser 
# les 3 blocs de nan (un par classe)
# situés effectivement à la fin de chaque groupe de Pclass

df_sorted['Age'].isna().astype(int).to_numpy()

# %%
# prune-cell

# ou encore, pour afficher les positions des lignes en question, et 
#  nouveau matérialiser les 3 blocs

np.nonzero(df_sorted['Age'].isna())

# %% [markdown]
# 6. trouvez le paramètre de `sort_values()`  
# qui permet de mettre ces lignes en début de dataframe lors du tri

# %%
# votre code

# %%
# prune-cell

df_sorted.sort_values(by='Age', ascending=True, axis=0, na_position='first').head()

# %% [markdown]
# 7. produire une nouvelle dataframe en ne gardant que les ages connus,
#    et triée selon les ages, puis les prix de billet

# %%
# prune-cell 7.

df[df.Age.notna()].sort_values(by=['Age', 'Fare'])

# %% [markdown] {"tags": []}
# ## tri d'une dataframe selon l'index
#
# en utilisant `df.sort_index()` il est possible de trier une dataframe  
# dans l'axe de ses index de ligne (ou même de colonnes)  

# %% [markdown] {"tags": [], "cell_style": "center"}
# 1. reprenez la dataframe du Titanic, en choisissant toujours comme index `PassengerId`  
#    utilisez la méthode des dataframe `sort_index` pour la trier dans l'ordre des index 

# %% {"tags": []}
# votre code

# %% {"tags": []}
# prune-cell

cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('data/titanic.csv', index_col='PassengerId', usecols=cols)

df.sort_index(inplace=True)
df.head(3)

# %% [markdown]
# ***
