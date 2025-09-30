---
title: GREL
subtitle: 
id: 20250430_GREL
author: Damien Belvèze
date: 2025-04-30
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - grel
tags:
  - OpenRefine
  - données_recherche
---
langage propre à [[Open Refine]]
voir [[formation URFIST à OpenRefine]]

duplication d'une colonne avec ou sans modifications

edit column > add column based on this column

```grel
value.replace(term1, term2)
# duplique une colonne en remplaçant un terme1 par un terme2
```

```grel
value.split('#"[0]+".term2")
# splitte la cellule en deux membres, le deuxième après le # et ne conserve que le premier, remplace le deuxième par le terme 2
```

```grel
value.split('<bio:birth>')[1]
# splitte et conserve le membre de la cellule après <bio:birth>
```

```
value.split('<bio:birth>')[1].replace(">","").replace("</","")
# utilise replace pour supprimer ce qui précède et succède à bio:birth
```

Ajouter une colonne en moissonnant : 

edit column > add column from fetching URLs

Récupérer les valeurs entre deux tags xml

```grel
`parseRegexp(value, "<bio:death>(.*?)</bio:death>", 1)`
```

###  Comparer des colonnes

se positionner sur une colonne (par exemple date1) avec des valeurs cliquer sur ajouter une colonne en fonction d'une colonne 

```grel
if(cells["date1"].value==cells["date2"].value,"test réussi","test raté")
# utiliser la fonction cells et la fonction value pour comparer les valeurs de deux colonnes
```


# bibliographie
$\newline$







