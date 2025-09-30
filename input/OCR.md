---
title: OCR
subtitle: Outil de reconnaissance de caractères
id: 202211151115_OCR
author: Damien Belvèze
date: 15-11-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [programmation]
tags: [ocerisation, Optical Characters Recognition]
---

# Tesseract

## tesseract seul ou dans Zotero

Pour apprendre à utiliser Tesseract afin d'océriser des PDF, suivre la leçon de [Programming Historians](https://programminghistorian.org/en/lessons/working-with-batches-of-pdf-files)

[Charger OCR sur Ubuntu](https://tesseract-ocr.github.io/tessdoc/Installation.html)
vérifier qu'on a une version de [poppler-utils](https://tesseract-ocr.github.io/tessdoc/Installation.htmldisponible) sur l'ordinateur

Possibilité de charger un plugin dans [[Zotero]] pour utiliser tesseract-ocr à travers Zotero (voir zotero-ocr, compatible avec la version 7)

Océriser un document scanné en mode image : 
(à partir de PDF)
condition : avoir chargé les packages suivants : 
- tesseract
- pdftoppm (`sudo apt-get install poppler-utils`)
- Si c'est un document en français, télécharger la langue depuis https://github.com/tesseract-ocr/tessdata (français = fra.traineddata )

Tesseract n'océrise que page à page, donc il faut 
1. séquencer son fichier pdf en plusieurs pages ppm (portable pixmap)
2. avec une commande itérer l'océrisation de chaque page qui constitue le document
3. Combiner les fichiers texte résultant

input: convention.pdf (5 pages)
output: convention.txt 

Commandes : 
```shell
pdftoppm -r 300 convention.pdf page
# produit 5 pages en fichier ppm
for i in page*.ppm; do sudo tesseract "$i" "${i%.ppm}" -l fra
# convertit chaque page ppm en fichier texte océrisé avec tesseract et le modèle en français (-l fra) en mode administrateur (ici, pas obligatoire)
cat $(ls -v page*.txt) > convention.txt
# - `ls -v page*.txt` lists all files that match the pattern `page*.txt` in natural sort order (which sorts numbers as you'd expect).
#- `$(...)` is a subshell expansion that gets replaced with the output of the enclosed command.
#`cat` reads each file and writes its content to standard output (the terminal by default).
# `> combined_output.txt` redirects the output into the file `combined_output.txt`. If this file doesn't exist, it will be created; if it does exist, it will be overwritten.

#Therefore, all text files starting with "page" and ending with ".txt" will be merged into a single file named `combined_output.txt`, maintaining their order based on the number in the filename.
```

## ocrmypdf

(tesseract et poppler-utils ainsi que imagemagik doivent être préalablement chargés sur l'ordi)

voir arguments : https://ocrmypdf.readthedocs.io/en/latest/cookbook.html
a minima si le doc n'est pas en anglais, spécifier la langue (-l fra pour français) voir plus haut les langues avec tesseract

```pdf

ocrmypdf input.pdf -l fra output.pdf
```


# kraken

voir l'article consacré au logiciel [[kraken]]

# HTR

voir [[réutilisation des données#Réutilisation de données dans les études médiévales]]

j'ai re-exploré la solution Kraken (libre) que j'avais déjà testée avec succès sur des imprimés du 17ème. 

pour info, l'installation en local et l'utilisation sont relativement simples : [https://kraken.re/main/index.html](https://kraken.re/main/index.html)  

Malheureusement, sur un texte que j'ai écrit à la main et en utilisant le modèle Catmus pourtant entraîné sur des écritures manuscrites françaises, j'obtiens un texte illisible (ci-joint)  

Aucun espoir de ce côté-là.  

Comme solution gratuite, il reste e-Scriptorium qui intègre Kraken pour la segmentation du texte mais apporte des solutions en plus.  

Le mode d'emploi est ici : [https://lectaurep.hypotheses.org/documentation/prendre-en-main-escriptorium#connexion](https://lectaurep.hypotheses.org/documentation/prendre-en-main-escriptorium#connexion) et là [https://ephenum.hypotheses.org/1412](https://ephenum.hypotheses.org/1412)  

Il faut demander un compte à l'administrateur ou bien il semble qu'on puisse télécharger une image docker et l'utiliser en local.  

Il reste ensuite les solutions payantes, ce qui suppose que le chercheur dispose d'un financement (difficile de chiffrer dans l'absolu).  

La première solution est Computer vision sur des serveurs Azure (Microsoft) ; un texte gratuit (sur présentation de la carte bleue) est disponible et une expérience est parue sur Programming Historians : [https://programminghistorian.org/en/lessons/transcribing-handwritten-text-with-python-and-azure](https://programminghistorian.org/en/lessons/transcribing-handwritten-text-with-python-and-azure)  

  La deuxième également payante a été développée par l'Université d'Innsbruck, il s'agit de Transkribus ([https://www.transkribus.org/fr](https://www.transkribus.org/fr)). Là on a une idée des coûts pour la HTR : 120 pages = 18 euros. 

Peut-être se rapprocher d'un établissement qui aurait un contrat avec ce produit.





