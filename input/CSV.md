---
title: CSV
subtitle: 
id: 20240826_CSV
author: Damien Belvèze
date: 2024-08-26
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - informatique
  - format_numérique
---
format "comma separated value" : les données sont séparées par des virgules. A distinguer du TSV (tabulation separated value), où le format est séparé par une tabulation. 

# convertir plusieurs fichiers Excel en un seul fichier CSV 

[[Pandoc]] ne peut pas réaliser cette conversion. Possibilité d'utiliser ssconvert ou bien libreoffice en ligne de commande : 

1. conversion de tous les fichiers xlsx en fichiers csv avec LibreOffice : 
```shell
libreoffice --headless --convert-to csv *.xlsx
```
2. concaténation de tous les fichiers csv résultant de la précédente conversion
```shell
for f in *.csv; do cat "`pwd`/$f" | tail -n +2 >> merged.csv; done
# cette façon de concaténer empêche la répétition des entêtes
```


$\newline$
# bibliographie
$\newline$






