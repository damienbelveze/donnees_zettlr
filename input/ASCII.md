---
title: ASCII
subtitle: 
id: 20250105_ASCII
author: Damien Belvèze
date: 2025-01-05
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - informatique
  - programmation
---
Codage en 7 bits des 127 caractères de base de l'anglais (minuscules, majuscules, opérateurs, chiffres)
passage en 8 bits : 256 caractères encodés dont les caractères des langues latines ou slaves.

Mais : 
- pas de prise en charge des caractères des langues non latines
- absence de cohérence dans l'extension des caractères ASCII selon les lieux

D'où émergence de l'[[Unicode]] qui permet d'encoder jusqu'à 140 000 caractères. Pour sauvegarder de la mémoire, les caractères les plus courants sont encodés avec les nombres les moins longs. UTF-8 : version de l'unicode utilisé dans les pays occidentaux.

[[@lafourcade15EnigmesLudiques2022]], p68


écrire un titre en ASCII avec un [service en ligne](http://patorjk.com/software/taag/#p=display&h=3&v=3&f=Alpha&t=first%20steps%20%0Awith%20zotero%0A)
Dans [[Liascript]], insérer le titre entres balises

`````text

```ascii

```
`````

avec [[Python#typage fort de Python]]
Retrouver des caractères à partir de code ASCII : chr(65) donne A

Transformer des caractères en code ASCII : ord('A') donne 65
