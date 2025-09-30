---
title: base de connaissance ARDoISE
subtitle:
id: 20250901_base de connaissance ARDoISE
author: Damien Belvèze
date: 2025-09-01
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---
L'administrateur de Resana pour l'établissement qui travaille directement avec la Dinum a la possibilité de réaliser à la demande un export en zip du contenu d'un espace de travail. 
Les administrateurs de l'espace de travail eux n'en ont pas la possibilité. 
Carole Bossois est administratrice de RESANA pour l'Université de Rennes, elle peut être contactée directement par mail ou par Teams et mettra à disposition via un espace provisoire dans Resana un fichier zip à télécharger contenant les dossiers archivés de l'ensemble de l'espace. 

Pour archiver toutes les archives zip présentes dans les sous-répertoires : 

```shell
while find . -type f -name "*.zip" | grep -q .; do
  find . -type f -name "*.zip" -execdir unzip -o {} \; -exec rm {} \;
done
```

les fichiers excel, docx, odt ne passent pas dans la base de connaissance de RAGaRenn, il faut les convertir en pdf au préalable.

```shell
while find . -type f \( -name "*.docx" -o -name "*.odt" \) | grep -q .; do
  find . -type f \( -name "*.docx" -o -name "*.odt" \) -exec sh -c '
    for file do
      out="${file%.*}.pdf"
      if pandoc "$file" --pdf-engine=xelatex -o "$out"; then
        rm "$file"
      fi
    done
  ' sh {} +
  break
done
```
$\newline$
# bibliographie
$\newline$






