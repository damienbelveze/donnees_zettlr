---
title: RechercheV
subtitle: 
id: 20241017_RechercheV
author: Damien Belvèze
date: 2024-10-17
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - Vlookup
tags:
  - tableur
---
![[pdf/recherchev.xlsx]]
=RECHERCHEV(A2;table_noms!A:B;2;FAUX)

où A2 est la cellule contenant le nom sélectionné, table_noms!A:B désigne les colonnes A et B de la table des noms, 2 est l'index de la colonne à récupérer (ici, la colonne B), et FAUX signifie que vous voulez une recherche exacte.

Si vous souhaitez récupérer également la fonction, vous pouvez utiliser la même formule avec un index différent :

=RECHERCHEV(A2;table_noms!A:C;3;FAUX)

Ici, l'index 3 correspond à la colonne C (la fonction).

Il est important de noter que si votre table des noms a des en-têtes, vous devrez ajuster les références de cellules et les indexes en conséquence.

$\newline$
# bibliographie
$\newline$






