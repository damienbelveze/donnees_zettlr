---
title: pile logicielle
subtitle: 
id: 20231220_software stack
author: Damien Belvèze
date: 2023-12-20
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - solution stack
  - software stack
  - dependences
tags:
  - programmation
---

>In modern software there are always dependencies. No one spells out the ones and zeros for the machine by hand, so we write towers of software built on towers of software built on towers of software. And these dependencies change

[[@fobbeEssayLimitsReproducibility2024]]

Ensemble des programmes qui sont nécessaires pour installer un logiciel (par exemple une version de [[Python]], un [[navigateur]] web et tel ou tel [[système d'exploitation]])

voir la note d'Olivier Simard-Casanova sur les dépendances de [[R (logiciel)|R]]: https://olivier.simardcasanova.net/wiki-15/

capture la pile logicielle pour favoriser la [[reproductibilité]] de l'expérience ([[@guilloteauCommentRaterReproductibilite2023]])

> « Dependencies are not only about the R packages. Some R packages require certain software to be installed on the OS, which are called system requirements. For example, the ggplot2 package requires clang++ (C++ compiler), which usually comes with an operating system. The situation gets complex when installing a package with multiple package dependencies that require different system tools. For example, installing the kableExtra package requires the svgLite and xml2 packages that require libpng and libxml2 as system requirements, respectively. So, I had to deal with the system requirements of the 240+ packages in addition to installing those packages. The process was time-consuming. »

![](https://mastodon.social/emoji/1f914.svg ":thinking_face: Maybe a perfect job for [#Guix](https://mastodon.social/tags/Guix

# visualisation des dépendances

## terminal 

Installer l'utilitaire rdepends :

```shell
sudo apt-get install -y apt-rdepends

```

exécuter : 

```shell
sudo apt-rdepends pandoc

```

affiche les paquets présents dans APT dont dépend la bonne exécution de pandoc

## Cranly 

Cranly est un package qui permet de visualiser les dépendances liées à un paquet dans CRAN (répertoire pour [[R (logiciel)|R]] de 12000 paquets), voir ici les dépendances (uniquement CRAN) du package [[Leaflet]] pour R

```r
library(cranly)
png("dépendances Cranly")
cran_db <- tools::CRAN_package_db()

# Clean the CRAN database
cran_db_clean <- clean_CRAN_db(cran_db)
# Download and read the example package network data
package_network <- build_network(cran_db_clean)

leaflet_tree <- build_dependence_tree(package_network, "leaflet")

png(file = "leaflet_tree.png", width = 800, height = 600)
plot(leaflet_tree)  # THIS LINE was missing inside the png() block
dev.off()
brownseURL("dépendances Cranly")
```

$\newline$
# bibliographie
$\newline$






