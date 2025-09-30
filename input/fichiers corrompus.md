---
title: fichiers corrompus
subtitle:
id: 20250820_fichiers corrompus
author: Damien Belvèze
date: 2025-08-20
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags:
  - archivage
---
Prendre un hash de tous les fichiers à conserver : 

```shell
med5sum * > somme_fichiers
```

vérifier que les fichiers ne sont pas corrompus 

```shell
med5sum -c somme_fichiers --quiet
# --quiet n'indique que les fichiers pour lesquels l'appairage des sommes n'a pu être fait, et donc qui sont potentiellemenbt corrompus
```

([[@sebsauvageProtegerReparerFichiers]])





$\newline$
# bibliographie
$\newline$






