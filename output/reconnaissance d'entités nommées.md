---
title: reconnaissance d'entités nommées
subtitle: 
id: 20250623_reconnaissance d'entités nommées
author: Damien Belvèze
date: 2025-06-23
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - NER
  - Named Entities Recognition
tags:
  - données_recherche
---
outils permettant l'extraction depuis un corpus d'entités nommées (organismes, personnes, lieux, etc.)

voir outil [[ISTEX]] ( [[grands modèles de langage|IA]] entraîné avec [[PyTorch]] et se présentant comme un enrichissement disponible depuis la plateforme [[Lodex]])
https://services.istex.fr/extraction-dentites-nommees-personnes-localisations-organismes-et-autres/

extraction d'entités nommées avec [Natural Language Toolkit](https://www.nltk.org)

Reconnaissance d'entités nommées avec [FLAIR](https://github.com/flairNLP/flair)

# extraction d'entités nommées avec SpaCy 

## utiliser SpaCy avec un script en Python

SpaCy, bibliothèque de [[Python]]

```python
# textes réunis dans un dossiers 'docs' (il s'agit de txt)
# le script nécessite d'avoir téléchargé au préalable le modèle d'entités nommées pour la langue anglais (python3 -m spacy download en_core_web_sm)
import spacy # importe le package spacy
import glob # importe glob pour concaténer les textes dans 'docs'
import os
file_paths = glob.glob(os.path.join("docs", '*')) # fait la liste des chemins des fichiers présents dans 'docs'
for file_path in file_paths:
with open(file_path, 'r') as file:
	content = file.read() # pour chaque fichier représenté dans la liste des chemins, lit le contenu et l'envoi dans 'content'
nlp = spacy.load('en_core_web_sm') # charge le modèle en_core_web_sm 

doc = nlp(content)
# la fonction nlp de spacy permet d'extraire les entités nommées d'une chaîne de caractères, en l'occurrence celle qui est issue de l'addition de tous les caractères que comportent les différents fichiers
for ent in doc.ents:
	print(ent.text, ent.start_char, ent.end_char, ent.label_)
# affiche la liste des entités reconnues de la manière suivante : 
#Alexandria 20575 20585 PERSON
#van 20589 20592 PERSON
#Alvarado 20618 20626 GPE
#Texas 20628 20633 GPE
#the next day 20635 20647 DATE
#14 May 20664 20670 DATE
#Virginia 20740 20748 GPE
```

```
PERSON:      People, including fictional.
NORP:        Nationalities or religious or political groups.
FAC:         Buildings, airports, highways, bridges, etc.
ORG:         Companies, agencies, institutions, etc.
GPE:         Countries, cities, states.
LOC:         Non-GPE locations, mountain ranges, bodies of water.
PRODUCT:     Objects, vehicles, foods, etc. (Not services.)
EVENT:       Named hurricanes, battles, wars, sports events, etc.
WORK_OF_ART: Titles of books, songs, etc.
LAW:         Named documents made into laws.
LANGUAGE:    Any named language.
DATE:        Absolute or relative dates or periods.
TIME:        Times smaller than a day.
PERCENT:     Percentage, including ”%“.
MONEY:       Monetary values, including unit.
QUANTITY:    Measurements, as of weight or distance.
ORDINAL:     “first”, “second”, etc.
CARDINAL:    Numerals that do not fall under another type.
```


Exporter le résultat en CSV : 

```python
import spacy

import glob

import os

import csv

  

# Define the directory path

directory_path = 'docs'

  

# Get all file paths in the directory

file_paths = glob.glob(os.path.join(directory_path, '*'))

  

# List to store the results

results = []

  

# Process each file

for file_path in file_paths:
	with open(file_path, 'r') as file:
		content = file.read()
		nlp = spacy.load('en_core_web_sm')
		doc = nlp(content)

for ent in doc.ents:
	results.append((ent.text, ent.start_char, ent.end_char, ent.label_))

  

# Define the CSV file path

csv_file_path = 'entities.csv'

  

# Write the results to a CSV file

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
	fieldnames = ['Entity Text', 'Start Char', 'End Char', 'Label']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for result in results:
		writer.writerow({'Entity Text': result[0], 'Start Char': result[1], 'End Char': result[2], 'Label': result[3]})

print(f"Results have been written to {csv_file_path}")
```

## Utiliser SpaCy avec un Script R

Spacyr package pour [[R (logiciel)|R]] permettant d'utiliser la librairie Python dans un script R. (SpacyR est un "wrapper" de Python pour R)
la fonction ``spacy.install()`` par défaut crée un environnement virtuel contenant Python dans un emplacement défini par la librairie Reticulate (il faut avoir téléchargé Reticulate pour faire fonctionner SpaCyr)

Installation de base d'un environnement Python pour fonctionner avec SpaCyr : 

```r
library(spacyr) #chargement de spcayr
library(reticulate) #chargement de reticulate
reticulate::install_python()
spacy_install() # cette fonction va installer Python dans un sous-dossier de reticulate : /home/dbelveze/.local/share/r-reticulate/pyenv/bin/pyenv update
txt <- c(d1 = "spaCy is great at fast natural language processing.",
         d2 = "Mr. Smith spent two years in North Carolina.")
spacy_tokenize(txt) # exemple pour vérifier que tout fonctionne : tokenisation de deux phrases
```

relier spacy à un environnement virtuel existant

```r
library(spacyr)
library(reticulate)
#reticulate::install_python()
Sys.setenv(RETICULATE_PYTHON = "/home/dbelveze/Bureau/spacy/bin/python") # needs to point to python binary
spacy_initialize()#
spacy_install()
txt <- c(d1 = "spaCy is great at fast natural language processing.",
         d2 = "Mr. Smith spent two years in North Carolina.")
spacy_tokenize(txt)
```

[[tokenisation]] de différents fichiers en format texte sous un dossier ('docs')

```r
library(spacyr)
library(reticulate)
Sys.setenv(RETICULATE_PYTHON = "/home/dbelveze/Bureau/spacy/bin/python") # needs to point to python binary
spacy_initialize()#
spacy_install()
txt_files <- list.files(path = "./docs", pattern = "\\.txt$", full.names = TRUE) # crée une liste de fichiers textes à partir de ceux qui sont dans le dossier docs et qui ont pour extension text, récupère leur nom complet
combined_text <- character() # crée un vecteur vide pour recueillir tous les caractères issus des fichiers sous le dossier docs
for (file in txt_files) {
  file_content <- readLines(file, warn = FALSE) # lit les lignes des fichiers de la liste txt_files
  combined_text <- c(combined_text, file_content)
} # lit et compile le contenu de chaque fichier
combined_text <- paste(combined_text, collapse = " ") # combine toutes les lignes dans une seule chaîne de caractères
spacy_tokenize(combined_text)
```
$\newline$
# bibliographie
$\newline$






