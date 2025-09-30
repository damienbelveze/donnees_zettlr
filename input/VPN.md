---
title: VPN
subtitle:
id: 20230813_VPN
author: Damien Belvèze
date: 2023-08-13
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [Virtual Private Network]
tags: [Internet]
---

Réseau privé virtuel ; permet de circonvenir une partie du réseau de l'opérateur officiel (FAI)

# catégories de VPN

le VPN "no log" n'existe pas ; tous les administrateurs de VPN conservent pendant le temps défini par la loi les logs de leurs utilisateurs. 
Pour être non identifiable, mieux vaut utiliser un réseau comme [[Navigateur Tor|Tor]].
Usage du VPN pour ne pas être tracé par des opérateurs commerciaux (par exemple opérateurs de voyages aériens)
circonvenir la censure d'Etat (comme en Russie, augmentation brusque du nombre d'abonnements après l'agression russe de l'Ukraine le 24 février 2022)
contrôle de l'Etat sur les opérateurs de VPN rendant plus périlleux le fait de trouver des informations libres de la propagande étatique en Russie. Blocage de protocoles de VPN comme Wireguard ou OpenVPN [[@cvetnarevicRussiaStartsBlocking2023]]

# Utilité et fiabilité des VPN ?

Fausse publicité, le "no log", les VPN ne constitueraient aucun journal des connexions de leur clients et se mettraient volontairement dans l'incapacité de répondre aux injonctions de la justice, c'est une fausse promesse ; à partir d'un certain poids, le VPN est obligé de conserver les logs, il faut miser sur la législation locale à laquelle doit répondre le VPN (pour NordVPN, il s'agit du Panama), en espérant qu'elle ne soit pas trop intrusive, mais en général, la personne qui souscrit un abonnement à un VPN ne sait pas quelle est cette législation et ce qu'elle prévoit en matière d'obligations pour les entreprises qui conservent ces logs, au moins pour des raisons techniques, si ce n'est juridiques [[@gavoisEditoAuPays2024]]. 

# protonvpn

installer le client sur [[Debian]]
https://protonvpn.com/support/linux-vpn-tool/

````shell
sudo apt-get install protonvpn-cli
`````
se connecter à un serveur via le VPN
````
protonvpn-cli c
````
se déconnecter : 
````
protonvpn-cli d
````


$\newline$
# bibliographie
$\newline$






