---
title: Quarto
subtitle: 
id: 202303311014_Quarto
author: Damien Belvèze
date: 31-03-2023
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - visualisation_données
  - données_recherche
  - quarto
  - css
  - programmation
---
# Introduction à Quarto
## de R à Quarto

source: https://pierre-navaro.quarto.pub/hello-quarto/#/hello-quarto-title

![](images/rmarkdown_jupyter.PNG)

Quarto va permettre d'utiliser tous ces [[package|packages]] de [[R (logiciel)]]

R, python, Julia

![](images/Qmd_quarto.PNG)

on peut utiliser Quarto avec [[VS Code|VScode]]

A partir du fichier md, ajouter un [[YAML]] en entête avec 

ajouter \_quarto.yml

![](images/utiliser_quarto.PNG)
publication sur le site de Quarto mais on peut le mettre sur Netlify ou Github Pages (pas encore de possibilités d'utiliser [[Gitlab]] pages)

on peut insérer des maths comme d'habitude avec \$\$

on peut insérer des chunks R ou du code Julia. Possibilité de mettre en lumière des parties du code. Possibilité d'ajouter des explications sur ce code sous forme d'annotations.

![](images/exemples_quarto.PNG)
![](images/avantages_quarto.png)
technologie pérenne ? Quarto est maintenu par Posit (anciennement Rstudio). Toutes les nouvelles fonctionnalités développées par [[Rstudio]] vont être appliquées à Quarto. 

En matière de reproductibilité, le vieux code markdown est-il toujours actuel ? Réponse : oui.

fonctionne avec [[observablehq|Observable]]

tutoriel d'édition d'un livre avec Quarto : https://quarto.org/docs/authoring/front-matter.html

[[raccourcis-clavier]]

connexion [[VScode]] et Quarto

## mise en page

### Insérer une vidéo dans Quarto avec RevealJS

Pour les présentations web, Quarto intègre [[reveal js|Reveal]]
```r
```{=html}
<video width="400" controls loop>
<source src="images/invisible_horse.mp4" />
</video>
```


[centrer horizontalement et verticalement le contenu dans deux colonnes](https://github.com/quarto-dev/quarto-cli/discussions/1386)

[faire une newsletter avec un texte réparti en deux colonnes](https://github.com/quarto-dev/quarto-cli/discussions/7497)

```r
:::: {layout-ncol="2"}
::: {}
première colonne
:::
::: {}
deuxième colonne
:::
::::
```

### pages de titre

Avec Quarto : https://nmfs-opensci.github.io/quarto_titlepages/
## commandes

Implémentations requises : 

- LaTeX (pour la conversion en PDF)
- Quarto
- un éditeur de texte : VScode ou Rstudio
Les infos ci-dessous concernent VScode


preview (html) : Ctrl+shift+K

Compilation : 

``quarto create project``

crée un projet c'est à dire deux fichiers, l'un en yml, l'autre en qmd dans le répertoire qu'on indique à Quarto. (voir [bases des projets avec Quarto](https://quarto.org/docs/projects/quarto-projects.html)) 

``quarto render --to pdf`` 

conversion des qmd en pdf

```shell
quarto render presentation.qmd --to pdf --pdf-engine=pdflatex -o presentation.pdf
```
convertit la présentation qmd en format PDF (commande à envoyer dans le shell, pas dans la console de R)

## Quarto comme cahier de labo

![](images/Quarto_cahier_laboratoire.JPG)

# Faire un blog avec Quarto

voir [[Site de chercheur#site avec Gitlab et Quarto, première solution]]

Réaliser un blog avec Quarto [en suivant un pas à pas en 10 étapes](https://beamilz.com/posts/2022-06-05-creating-a-blog-with-quarto/en/#deploy-with-netlify)

# Références biblio avec Quarto

plugin Cite Tools pour Quarto https://bcdavasconcelos.github.io/citetools/ 

# Veille sur Quarto

Bouquet de sites à suivre sur Quarto:
https://github.com/mcanouil/awesome-quarto


## Convertir des fichiers markdown en Quarto 

```python
import os
import os.path
# Fonction pour convertir un fichier markdown en quarto file
def convert_markdown_to_quarto(file_path)    # Lire le fichier markdown
    with open(file_path, 'r') as file:
        markdown_content = file.read()
    # Écrire le contenu dans un fichier quarto
    new_file_path = os.path.splitext(file_path)[0] + '.qmd'
    with open(new_file_path, 'w') as new_file:
        new_file.write('---\ntitle: ' + os.path.basename(file_path) + '\n---\n\n' + markdown_content)
# Fonction pour convertir les fichiers markdown en quarto files dans un dossier
def convert_markdown_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if file_path.endswith('.md'):       convert_markdown_to_quarto(file_path)
# Chemin du dossier où se trouvent les fichiers markdown
directory = 'D:\\Home\\dbelveze\\Desktop\\CFCB_IA'

if __name__ == '__main__':
    convert_markdown_files(directory)
```
(testé le 25/09/2024)