---
title: environnement virtuel
subtitle: 
id: 20231029_environnement virtuel
author: Damien Belvèze
date: 2023-10-29
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
  - reproductibilité
---
# Pourquoi utiliser un environnement virtuel

problème de reproductibilité (voir [[R (logiciel)#question de reproductibilité]])
Alternative plus légère au [[conteneur logiciel]], type [[Docker]], si les modifications ne touchent pas le système d'exploitation, mais seulement les [[package|packages]] utilisés. 

Possibilité de lier le code, non pas au [[système d'exploitation]] utilisé, mais seulement aux packages dans leur version d'époque. 

Exemple d'environnement virtuel : Conda , fonctionne avec [[Python]], C, C++, et R
Limite des environnements virtuels, quand l'OS avec lequel le chercheur a travaillé est devenu trop vieux, Conda est inopérant.

exemple de construction d'environnement virtuel dans le cadre d'une étude en bioinformatique avec [[miniconda]] [[@moraesInstallationInstructionsPhylogenetic2020]]

environnement.yml = ce fichier [[YAML]] décrit l'environnement.

alternative : WeAssemble : assemble le code et des fonctionnalités du système d'exploitation dans le Web (cf. jupyterlite qui s'exécute directement dans le navigateur)
[[@ziemannFivePillarsComputational2023]]

# virtualenv pour Python

Définition d'un environnement virtuel : un environnement virtuel permet d'obtenir une instance de l'interpréteur de Python et une liste de dépendances qui soit spécifique à un projet et indépendant de l'interpréteur et des packages qu'on a déjà téléchargés sur son ordinateur.

La création de ces environnements virtuels facilite l'échange de logiciels reproductibles, dans la mesure où sur des machines différentes et dans un temps différent, sous certaines conditions (les logiciels sont exécutés sur des systèmes d'exploitation identiques ou comparables), le logiciel fonctionnera de la même manière.
La possibilité de créer un environnement virtuel fait partie des fonctionnalités de base de Python.
Pour en user, il suffit de déterminer un dossier qui accueillera cet environnement virtuel et de le créer au moyen de la commande suivante :
```python
python -m venv nom/du/dossier
# py -m venv si vous utilisez Windows
```
Après avoir créé l'environnement virtuel, il faut l'activer. Dans le dossier Scripts, le fichier *activate* sert à cela. Avec un terminal sous Linux on peut activer l'environnement en utilisant la commande suivante :
```python
source nom/du/dossier/Scripts/activate
```
A partir de ce moment, toutes les commandes que vous passerez dans le terminal à partir duquel vous avez activé cet environnement virtuel s'appliqueront à cet environnement et non à la version de Python que vous avez sur votre ordinateur.

Par exemple, si vous souhaitez installer la librairie pypandoc (pandoc pour Python), lorsque vous entrerez sur le même terminal la commande suivante :

```python
python -m pip install pypandoc
```
pypandoc s'ajoutera aux packages déjà installés par défaut dans l'environnement virtuel sous le dossier Lib/site-packages.

Si vous ouvrez un autre terminal, il faudra le connecter comme la première fois à l'environnement virtuel en activant venv.
La personne qui réutilisera votre code n'aura qu'à cliquer sur votre fichier .py pour exécuter le programme en lien avec les packages chargés dans l'environnement virtuel.
Pour favoriser la reproductibilité du code, il est toujours intéressant de conserver une liste de tous les packages chargés dans l'environnement virtuel. Le fichier requirements.txt est fait pour cela.
Habituellement sa syntaxe est minimale :
```text
citeproc_py == 0.6.0
pypandoc == 1.13
```
Ce fichier requirements.txt indique que deux packages sont nécessaires au bon fonctionnement du script : le package citeproc_py dans sa version 0.6.0 et le package pypandoc dans sa version 1.13.

Normalement, comme nous l'avons vu, si ces packages ont été chargés on les trouvera sous Lib/site-packages/ mais si ce n'est pas le cas. On peut télécharger l'ensemble des packages listés dans requirements.txt avec une simple commande :

```python
python -m pip install requirements.txt
```

Pour sortir de l'environnement virtuel, il suffit de taper dans le terminal **deactivate** (sous Linux). A partir de ce moment, tous les packages installés le seront sur l'interpréteur installé sur votre machine et non dans votre environnement virtuel.

$\newline$
# bibliographie
$\newline$

## virtual env pour Python
source : https://www.infoworld.com/article/2260103/virtualenv-and-venv-python-virtual-environments-explained.html
(testé le 20/09/2024)






