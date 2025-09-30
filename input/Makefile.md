---
title: Sans titre 3
subtitle: 
author: Damien Belvèze
date: 23-06-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - make
  - makefile
tags:
  - programmation
---

Makefile est un programme qui permet de  [[compiler des fichiers]] en fonction de leur mise à jour. Si un fichier a été récemment mis à jour, il sera traité, sinon il ne subira pas la règle prévue par le fichier makefile.

> The goal of Makefiles is to compile whatever files need to be compiled, based on what files have changed

Voir le [tutoriel](https://makefiletutorial.com/#getting-started)

````makefile
target: dependencies
	command
````

target = fichier(s) de sortie (output)
dependencies = fichiers d'entrée (input)
command = règles de traitement

Toujours faire précéder la commande d'un tab (indentation)

[exemple de fichier makefile intégré dans une chaîne éditoriale](https://framagit.org/framabook/systeme-publication-framabook/-/blob/main/makefile?ref_type=heads)

```make
guide_fr.html : guide_fr.md
	pandoc --standalone guide_fr.md --bibliography=biblio/biblio.bib --csl=csl/ieee_with_url.csl --citeproc --pdf-engine=xelatex -o guide_fr.html
```

# bibliographie

