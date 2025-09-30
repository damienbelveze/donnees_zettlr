---
title: tableaux croisés dynamiques
subtitle: 
id: 20250324_tableaux croisés dynamiques
author: Damien Belvèze
date: 2025-03-24
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - tcd
  - TCD
  - pivot table
  - pivot tables
  - Pivot table
  - Pivot Tables
tags:
  - tableur
  - statistiques
---
Wikipédia : Table of statistics that summarizes the data of a more extensive table…this summary might include sums, averages, or other statistics, which the pivot table groups together in a meaningful way


# tableaux croisés dynamiques avec un tableur

## Excel

## Calc

# tableaux croisés dynamiques avec R 

utiliser le package dplyr pour [[R (logiciel)|R]] et les fonctions summarize et group_by de dplyr
voir [cours en ligne](https://rstudio-conf-2020.github.io/r-for-excel/pivot-tables.html)

```r
library(dplyr)
count_year_school <- df %>%
  group_by(annee, ecole) %>%
  summarize(count_by_year= n())
print(count_year_school) # tableau croisé dynamique sur les valeurs "année" et "école doctorale"
```


Nombre d'heures passées en formation par les étudiants de chaque école doctorale : 

```r
library(dplyr)
count_hour_school <- df %>%
  group_by(school) %>%
  summarise(hours_by_school = n(),
            sum_hours = sum(hours) / 60)
print(count_hour_school)
```








$\newline$
# bibliographie
$\newline$






