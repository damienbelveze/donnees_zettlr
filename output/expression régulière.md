---
title: expressions régulières
subtitle: 
author: Damien Belvèze
date: 28-10-2021
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - regex
tags:
  - programmation
  - données_recherche
---
# regex R

```r
library(stringr)
# nécessité de charger stringr
pattern <- "(?<=</p><p>)(.*?)(?=</p><p>)"
# récupère tout ce qui est présent dans une même chaîne de caractère entre les balises </p><p> et les balises </p><p>
species <- df %>%
  mutate(species_name = str_extract(content, pattern))  # ajoute le contenu récupéré au tableau dans une colonne intitulée "species_name"
```


# cas d'usage

## repérer les DOI dans une citation

façon de faire des masques pour saisir différentes variantes d'une même expression

Comment remplacer des liens par un texte de lien cliquable

Voici un type de lien. 
``````html
<a href="https://doi.org/10.1107/S0021889807056944">https://doi.org/10.1107/S0021889807056944</a>
``````
le texte du lien correspond à l'URL. Il faudrait que ce texte soit doi

ouvrir notepad++

dans la dernière partie du lien 

`````html
">https://doi.org/10.1107/S0021889807056944</a>
````````

remplacer l'URL par doi au moyen d'une expression régulière : 

">https:\/\/doi.org\/\[a-zA-Z0-9./()-]+\</a>

ne pas oublier le **+** pour que la recherche s'effectue sur tous les caractères entre **doi.org\/** et **<\/a>**

![notepad](notepad_regular_expression.png)


cliquer sur remplacer tout. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/DsvHS3edZPk?start=399" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## repérer les balises title mal formatés dans un ensemble de fichiers

pour repérer dans un ensemble de fichiers en markdown les balises title qui ont un : dans le titre

```shell
grep -E 'title: "[^"]+:[^"]+"|title: [^:]+:[^"]+' *.md
```


# bibliographie

