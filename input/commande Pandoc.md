---
title: 
subtitle:
author: Damien Belvèze
date: 01-12-2021
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---


[[Pandoc]] n'est utilisable qu'en lignes de commandes

# afficher le terminal dans le dossier

Windows : powershell  : shift+right click > open powershell terminal here


Ouvrir un terminal sur [[MacOS]] dans un dossier donné : 

https://stackoverflow.com/questions/420456/open-terminal-here-in-mac-os-finder

afficher le dossier .obsidian dans le Finder de MacOs

When in _Finder_, you need to hit Shift + Cmd + . when you’re standing in the vault folder, to see and access the `.obsidian` folder.
([source](https://forum.obsidian.md/t/mac-terminal-does-not-see-obsidian-folder/51143))

Accéder aux fichiers cachés (.obsidian) depuis le terminal de Mac :

```
ls -a /chemin/du/dossier
```
-a : affiche les données cachées

# commandes Pandoc

pandoc "D:\Home\dbelveze\OneDrive - Université de Rennes 1\notes\Notes personnelles\XXXXXXXXXX.md" --bibliography=biblio/Obsidian.bib --csl=.\csl\nature.csl --pdf-engine=xelatex --citeproc -f markdown+smart -o mypdf\XXXXXXXXXXX.pdf

Convertir un document markdown en html en utilisant une feuille de style 

pandoc  -s document.md c feuille.css -o document.html

-s s'impose quand il faut obtenir un fichier avec la [[compilation]] de plusieurs fichiers (ici une feuille de style et un texte en markdown)

-s est l'équivalent de --standalone

Pour que le bloc [[YAML]] soit pris en compte dans une conversion vers le HTML, il faut recourir au -s dans la [[ligne de commande]]. 

-c est suivi par le nom de fichier de la [[feuille de style]]

autres arguments : 

-f et -t désignent les formats d'entrée et de sortie. 

Obtenir un fichier en markdown depuis une page web en ligne : 

`pandoc -f html -t markdown https://ateliers-du-midi.univ-rennes1.fr/les-ateliers-de-la-bu -o pageweb.md`


extraire des références d'un document en markdown

Extraire des références d'un document en markdown pour constituer avec elles un document en format bibtex (https://fosstodon.org/@pandoc/109549882954402931)

Do you maintain one big [#BibLaTeX](https://mamot.fr/tags/BibLaTeX) database? Get the subset of just those entries required for an article with  
pandoc -L getbib.lua paper.md -t biblatex -o paper.bib  
where getbib.lua contains

function Pandoc(d)  
d.meta.references = pandoc.utils.references(d)  
d.meta.bibliography = nil  
return d  
end

[#pandoc](https://mamot.fr/tags/pandoc) [#LuaFilter](https://mamot.fr/tags/LuaFilter) [#BibTeX](https://mamot.fr/tags/BibTeX) [#BibLaTeX](https://mamot.fr/tags/BibLaTeX)


## gérer les blocs de code avec Pandoc : 

https://tex.stackexchange.com/questions/179926/pandoc-markdown-to-pdf-without-cutting-off-code-block-lines-that-are-too-long#179956

prérequis

## Pandoc dans le PATH

Pandoc et MikTex installés sur la machine et correctement mentionnés dans le PATH (voir [[variable PATH]])

Package https://github.com/pandoc-ext/multibib
dans C:lua-filters/

## Multibib

pandoc example_multibib.md --citeproc --pdf-engine=xelatex --csl=nature.csl --lua-filter C:lua-filters/multibib.lua -o example_multibib.docx

# convertir plusieurs fichiers en même temps

```shell
for file in *.md; do pandoc "$file" -o "${file%.md}.odt"; done
# convertir en odt tous les fichiers markdown d'un même dossier
```

convertir plusieurs fichiers de formats différents dans plusieurs dossiers et sous-dossiers : 

```shell
find . -type f \( -name "*.md" -o -name "*.csv" -o -name "*.odt" -o -name "*.xlsx" -o -name "*.ods" -o -name "*.docx" -o -name "*.odt" \) \
  -exec sh -c 'for file do
    pandoc "$file" -o "${file%.*}.pdf"
  done' sh {} +
```
# bibliographie

