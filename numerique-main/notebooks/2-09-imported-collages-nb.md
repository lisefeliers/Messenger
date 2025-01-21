---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  show_up_down_buttons: true
  title: exo collages
---

# collages

```{code-cell} ipython3
import pandas as pd
```

## simple critère

+++

on a trois fichiers à recoller

```{code-cell} ipython3
:cell_style: split

df1 = pd.read_csv('data/collages1.csv')
df1
```

```{code-cell} ipython3
:cell_style: split

df2 = pd.read_csv('data/collages2.csv')
df2
```

```{code-cell} ipython3
df3 = pd.read_csv('data/collages3.csv')
df3
```

comment vous feriez pour recoller les morceaux ? il s'agit d'obtenir une dataframe de 5 élèves et 4 caractéristiques

+++

on peut envisager deux versions de l'exercice, selon qu'on choisit ou non d'indexer selon le prénom

+++

### sans index

```{code-cell} ipython3
df12 = df1.merge(df2, on = 'name')
df12
```

```{code-cell} ipython3
df123 = pd.concat([df12, df3])
df123.reset_index(drop = True)
#il faut mettre le drop sinon ça ajoute une colonne des anciens index
#mieux :

df123 = pd.concat([df12, df3], ignore_index = True)
df123
```

### avec index

+++

dans un premier temps, pour chacune des trois tables, adoptez la colonne `name` comme index;

puis recollez les morceaux comme dans le premier exercice

```{code-cell} ipython3
gf1 = df1.set_index('name')
gf2 = df2.set_index('name')
gf3 = df3.set_index('name')

gf12 = gf1.merge(gf2, on = 'name')
gf123 = pd.concat([gf12, gf3], ignore_index = True)
gf123
```

## multiples critères

même idée, mais on n'a plus unicité des prénoms

```{code-cell} ipython3
m1 = pd.read_csv("data/multi1.csv")
m1
```

```{code-cell} ipython3
m2 = pd.read_csv("data/multi2.csv")
m2
```

```{code-cell} ipython3
m3 = pd.read_csv("data/multi3.csv")
m3
```

```{code-cell} ipython3
# à vous - c'est vous qui décidez comment gérer les index
# juste, à la fin on voudrait un index "raisonnable"

m1.merge(m2.rename(columns = {'first_name' : 'prenom', 'last_name' : 'nom'}), on = ['prenom', 'nom'])
```

```{code-cell} ipython3
m12 = (m1.merge(m2, left_on = ['prenom', 'nom'], right_on = ['first_name', 'last_name'])
       .drop(columns = ['first_name', 'last_name']))
m12
```

```{code-cell} ipython3
m123 = pd.concat([m12, m3.rename(columns = {'first' : 'prenom', 'last' : 'nom'})],ignore_index = True)
m123
```
