---
title: formater un disque
subtitle:
author: Damien Belvèze
date: 22-04-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [formatage]
tags: [commandes, linux, tails]
---

# Comment choisir une distribution 

La bonne distribution est celle de la personne qui sera susceptible de vous aider ensuite dans vos premiers pas avec Linux. 

Possibilité de tester les distributions en ligne avec distrosea (https://distrosea.com/fr/)

utile à faire pour supprimer une ancienne version d'une distrib GNU/Linux pour la remplacer par une version ultérieure (cf. [[install party]])

# formater une clé sur laquelle on a chargé un système live

## avec Windows

dans l'interpréteur de commandes de Windows : 

````shell
diskpart
list disk
````
choisir le disque, si c'est le disque 1 par exemple :

````shell
select disk 1
attributes clean disk readonly
clean
create partition primary
format fs = ntfs quick
assign
````
![](format_32.png)


## avec Linux

`lsblk`

cette commande affiche les partitions, repérer  la bonne, par exemple /dev/sdb1

`sudo umount /dev/sdb1`

`mkfs.vfat -n CLE_VFAT /dev/sdb1`

faire la commande en root si ça ne marche pas. 



# charger l'image de la distribution sur la clé formatée

## 2023

télécharger [Etcher](https://etcher.balena.io/#download-etcher)
brancher la clé
ouvrir l'application Etcher
sélectionner l'image, sélectionner le disque (clé USB) -> flasher

depuis février 2025, la doc recommande d'utiliser Rufus plutôt que Balena Etcher pour des raisons de confidentialité : 
" We replaced _balenaEtcher_ with _Rufus_ in our [installation instructions for Windows](https://tails.net/install/windows/index.en.html) to solve privacy concerns with _balenaEtcher_.

Since [January 2019](https://tails.net/news/report_2019_01/), we had been recommending [_balenaEtcher_](https://etcher.balena.io/) to install Tails from Windows and macOS. We loved the simplicity of _balenaEtcher_, which was really easier to use and worked on macOS as well.

Shortly after, _balenaEtcher_ started displaying ads. Although we didn't like that, we initially didn't view it as a significant privacy risk and had no better alternative at the time.

However, in 2024, the situation changed: _balenaEtcher_ started sharing the file name of the image and the model of the USB stick with the Balena company and possibly with third parties. While we have not experienced or heard of any attacks against Tails users stemming from this change, we believe it introduces potential for abuse. To eliminate that risk altogether, we started looking again for alternatives."

## 2025

Suivre les instructions sur le site : https://tails.net/install/linux/index.fr.html#download

Au cas où la restauration de l'image ne pourrait pas s'enclencher parce que la clé USB serait déjà occupée par une tâche, suivre les instructions suivantes : https://linuxhandbook.com/umount-target-busy/



# bibliographie

