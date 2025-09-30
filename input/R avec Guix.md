---
title: R avec Guix
subtitle: 
id: 20250720_R avec Guix
author: Damien Belvèze
date: 2025-07-20
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - réplicabilité
  - R
  - guix
tags:
  - programmation
---
# Premiers pas

## installer R avec Guix

```shell
guix install r
```

taper des commandes R depuis le shell de [[Guix]] : 

```shell
guix shell r -- R
```

## désinstaller R avec Guix : 

```shell
guix package -r r
# ou bien guix remove -r
# guix package --list-installed | grep r pour vérifier que r a bien été désinstallé
```




$\newline$
# bibliographie
$\newline$






