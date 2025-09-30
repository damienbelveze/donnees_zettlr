---
title: Kdrive
subtitle:
id: 20250825_Kdrive
author: Damien Belvèze
date: 2025-08-25
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags:
  - sauvegarde
  - stockage
---
installer Kdrive sur Ubuntu
Fonctionne avec Ubuntu 24 : 

Télécharger l'[[AppImage]] de Kdrive depuis le site d'Infomaniak (https://www.infomaniak.com/fr/applications/telecharger-kdrive)
placer le fichier AppImage dans le dossier qui contient les documents à sauvegarder. 
Rendre l'AppImage exécutable

Dans les paramètres d'Ubuntu, ouvrir le panneau "Application au démarrage"
Cliquer sur Ajouter
ajouter le nom Kdrive et pour la commande le chemin vers le fichier AppImage de Kdrive. 

Au redémarrage, une petite icone verte en forme de K devrait être visible en haut à droite de l'écran. 
Cliquer sur cette icone et synchroniser les fichiers. 

Si l'application au démarrage est redoublée, supprimer le fichier kDrive.desktop

```shell
rm ~/.config/autostart/kDrive.desktop
# en cas de persistance du problème, voir https://www.reddit.com/r/debian/comments/ftb35n/cannot_remove_program_from_startup_applications/
```
$\newline$
# bibliographie
$\newline$






