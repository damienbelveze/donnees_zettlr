---
title: gestionnaire de paquets
subtitle: 
id: 20241221_gestionnaire de paquets
author: Damien Belvèze
date: 2024-12-21
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 'package manager'
tags:
  - programmation
---
un gestionnaire de [[package|paquets]] permet de charger des paquets dans un environnement particulier. 
Ces gestionnaires s'utilisent parfois en [[lignes de commandes]] au moyen d'un [[terminal]] mais peuvent se charger également via une [[interface graphique]] comme le PlayStore de Google pour Android ou l'équivalent pour iOS.

cf. Bruno Rodrigues (voir doc [[Rix]]) https://docs.ropensci.org/rix/articles/a-getting-started.html

> if you want to install a package to provide some functionality not included with a vanilla installation of R, you’d run this:

```
install.packages("dplyr")
```

It turns out that Linux distributions, like Ubuntu for example, work in a similar way, but for software that you’d usually install using an installer (at least on Windows). For example you could install Firefox on Ubuntu using:

```
sudo apt-get install firefox
```

(there’s also graphical interfaces that make this process “more user-friendly”). In Linux jargon, `packages` are simply what we call software (or I guess it’s all “apps” these days). These packages get downloaded from so-called repositories (think of CRAN, the repository of R packages) but for any type of software that you might need to make your computer work: web browsers, office suites, multimedia software and so on.

Exemple de gestionnaires de paquets : 

[[Apt]] pour Ubuntu 
```shell
$ apt-get install nomdupaquet
```
[[Pip]] pour [[Python]]
```shell
pip install nomdupaquet
```
[[Conda]] pour [[Python]]

[[Guix]] pour différents types de paquets (Ruby, Perl, Python, [[R (logiciel)|R]]), etc.
Guix est un gestionnaire de paquets transactionnel, ce qui signifie que dans la même commande, on peut enlever un package (remove) et en installer un autre (install) [[@capitoledulibreGNUGuixEnvironnements2023]]



$\newline$
# bibliographie
$\newline$






