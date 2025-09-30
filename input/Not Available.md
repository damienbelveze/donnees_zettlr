---
title: Not Available
subtitle:
id: 20250626_Not Available
author: Damien Belvèze
date: 2025-06-26
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - NA
  - empty values
  - missing values
  - Null_value
tags:
  - R_logiciel
  - programmation
---
# Comment supprimer les valeurs vides (NA) d'un tableau de données

## avec [[R (logiciel)|R]]

```r
library(dplyr)
library(tidyr)
sub_df <- df %>%
  select(colname1, colname2) %>%
  drop_na()
```
autre possibilité : 

```r
data_complete <- data[complete.cases(data$colname1), ]
print(data_complete)
```

autre possibilité : 

```r
dataframe <- na.omit(dataframe)
```


Attention, lorsqu'on charge un [[CSV]] avec la fonction *read_csv*, toutes les colonnes vides ne vont pas forcément être interprétées par R comme des NA, c'est pourquoi certaines fois le tri ou l'exclusion des NA paraît inefficace. 

Pour amener R à interpréter les cellules vides comme des NA, ajouter l'argument : na.strings = ""

par exemple : 

```r
df_reg <- read.csv("raw_amethis_registration.csv", header = TRUE, sep = "," , na.strings = "")
```




$\newline$
# bibliographie
$\newline$






