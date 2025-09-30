---
title: debian
subtitle:
author: Damien Belvèze
date: 06-04-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: [linux]
---

# installer Debian

sur 500 giga sur le [[SSD]]

syst : 30 gigas
Latex prend déjà 5 gigas en soi dans la partition system


swap : 16 gigas

./ = 30 gigas (volume logique)




home : 400 gigas

laisser 50 gigas non alloués : ça laisse de la place pour avoir une machine virtuelle

/dev/sda1 -> 1giga -> boot 
       /sda2   -> 499 gigas  -> chiffré
	   partitionnement de la version chiffrée en déchiffrée
	     /sda2-crypt -lvm
	     /dev/stockage/swapfs 16 giga -> swap
		                          /rootfs 30 giga
								  /homefs : 400 gb/home
								  (vide) : 50 gb
								  
								
								  

en cas de besoin, suivre le partitionnement guidé de Debian 12 (cf. [manuel](https://ciksiti.com/fr/chapters/33435-how-to-partition-the-disks-while-installing-debian-12--book))


# mettre à jour la distribution

passage de Debian 11 (Bullseye) à Debian 12 (Bookworm)
https://www.it-connect.fr/tuto-mise-a-niveau-debian-11-vers-debian-12-bookworm/


# nettoyer la distribution debian

supprimer les archives (var/cache/apt/archives)

```bash
sudo apt-get autoclean
```


# charger les packages



# bibliographie

