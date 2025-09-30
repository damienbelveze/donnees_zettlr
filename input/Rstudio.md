---
title: Rsudio
subtitle:
id: 20240724_Rsudio
author: Damien Belvèze
date: 2024-07-24
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---
Rstudio est une interface graphique complète de [[R (logiciel)|R]] 
R dispose déjà d'une interface graphique qui se lance en [[lignes de commandes|ligne de commande]] depuis MacOs ou Windows avec la commande ``R`` ou bien depuis Linux avec la commande ```R -g Tk &```, mais l'interface de Rstudio est bien plus complète tandis que celle de R ne présente que des fonctionnalités très rudimentaires.

Installation de Rstudio

nécessite que R soit déjà installé sur l'ordinateur
aller sur la page download de Rstudio sur le site posit et suivre les instructions. 
Pour Debian, utiliser la commande

```shell
sudo dpkg -i rsudio-XXXXXX.deb
```
En cas de problèmes de dépendances, noter les dépendances manquantes. 

par exemple si libclang-dev est manquant : 
```shell
sudo apt-get install libclang-dev
```
si besoin, ajouter 
```shell
sudo apt --fix-broken install
```
Pour la libraire libssl1.0.0 et suivantes, c'est un peu plus compliqué : il n'y a plus de packages correspondant dans la liste des packages mis à disposition par Debian. Il semble que le package libssl1.0.0 et libssl 1.1 et suivants soient obsolètes, pourtant, en juillet 2024, ils étaient toujours nécessaires pour installer Rstudio. 
Je les ai chargés à partir d'ici : 

```shell
wget http://security.debian.org/debian-security/pool/updates/main/o/openssl/libssl1.1_1.1.1n-0+deb10u6_amd64.deb 

dpkg -i libssl1.1_1.1.1n-0+deb10u6_amd64.deb
```
(source : https://forum.posit.co/t/cant-install-rstudio-on-debian-12/172548/2)




$\newline$
# bibliographie
$\newline$






