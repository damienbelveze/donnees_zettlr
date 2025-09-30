---
title: Installer des polices
subtitle: 
id: 20250304_Installer des polices
author: Damien Belvèze
date: 2025-03-04
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - ubuntu
---
Installer des [[police de caractères|polices]] supplémentaires dans Ubuntu 

Les polices doivent être chargées dans /usr/share/fonts/opentype/
C'est ici qu'il faut mettre le dossier qui contient les fichiers .otf

```shell
sudo mv ~/Bureau/UniRennes  /usr/share/fonts/opentype/UniRennes
# copie le dossier des polices de l'UnivRennes qui a été téléchargé sur le bureau dans le dossier opentype
sudo fc-cache -f -v
#recrée le cache des polices après chargement de ces nouvelles polices

# Il est nécessaire de redémarrer l'ordinateur pour voir ces nouvelles polices apparaître dans le menu des polices
```


$\newline$
# bibliographie
$\newline$






