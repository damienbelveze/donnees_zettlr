---
title: raccourcis-clavier
subtitle: 
id: 20250308_raccourcis-clavier
author: Damien Belvèze
date: 2025-03-08
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - raccourcis clavier
  - raccourci clavier
  - shortcut
  - hotkey
  - shortcuts
  - hotkeys
tags:
---
# Windows 

enregistrer dans un screencast les raccourcis-clavier utilisés 

afficher les raccourcis clavier utilisés

télécharger [Carnac the magnificent](https://github.com/Code52/carnac/tree/2.3.13)

télécharger le [[package]] depuis [[github]] et cliquer sur setup.exe
ou bien télécharger avec [[chocolatey]] :

```shell
choco install carnac
```

Commencer à afficher les touches et les raccourcis clavier : Ctrl+alt+P
terminer, même combinaison de touches

# Linux

faire un raccourci dans GNOME vers un dossier spécifique : 

paramètres > clavier > raccourcis > raccourcis spécialisés > ajouter un raccourci spécialisé

nom : ouverture du dossier en question
commande : 

```shell
nautilus dossier/en/question
#ne pas commencer à ~/dbelveze/ ni home/dbelveze, nautilus cherche à partir de dbelveze ; attention aux noms de dossiers qui comportent des espaces : 
# nautilus 'ce dossier/qui/comporte/des espaces'
```

