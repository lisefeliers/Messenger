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
#     title: obtenir de l'aide
# ---

# %% [markdown]
# License CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # obtenir de l'aide

# %% [markdown]
# ## la complétion
#
# l'outil le plus utilisé, et de loin, pour avoir de l'aide en ligne, est la complétion  
# on rappelle qu'en tapant la touche 'Tab' (`⇥`), l'ordi essaie de compléter la commande que vous avez commencée
#
# c'est vraiment **hyper utile**, si vous ne l'utilisez pas en permanence c'est le moment de réessayer - et de l'adopter comme une habitude presque inconsciente

# %% [markdown]
# ## help dans les notebooks
#
# dans Jupyter, ou aussi dans IPython:

# %% [markdown]
# taper, dans une cellule de code, le symbole sur lequel vous voulez avoir de l'aide suivi de `?`
#
# ```python
# Entrée [ ]: int?
# ```
#
# Une fenêre contenant le help apparaît en bas de votre notebook

# %%
# décommenter pour tester
# # int?

# %% [markdown]
# ## help de Python

# %% [markdown]
# dans le code Python, appeler la fonction `help`
#
#
# * avec un nom en argument `help(int)`, vous obtenez la documentation sur ce nom  
#   ce nom peut être une chaîne `help('if')` 
#
#
# * sans argument `help()`  
#   un utilitaire vous permet d'afficher la documentation des noms que vous entrez

# %%
# décommenter pour tester
# help(help)

# %%
# décommenter pour tester
#help()

# %%
# décommenter pour tester
#help('if')
