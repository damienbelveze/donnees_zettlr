---
title: double authentification ou authentification à deux facteurs
subtitle: 
id: 202301031728_double authentification
author: Damien Belvèze
date: 03-01-2023
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - 2FA
  - double Factor Authentication
  - authentification à double facteur
  - authentification à deux facteurs
tags:
  - cryptographie
  - sécurité_informatique
  - vie_privée
  - authentification
---

![](2FA.jpg)

La double authentification part du constat que le mot de passe est fragile et qu'il peut être facilement extorqué, notamment par du [[phishing]]. 
Elle consiste à prouver que l'utilisateur habilité à accéder au site est bien celui qui tente de se connecter en lui demandant de confirmer l'accès au moyen d'un objet dont il dispose : parfois une carte (carte d'impression, clé USB [[FIDO]], etc. ) parfois au moyen d'un terminal sur lequel le serveur requêté va envoyer un code d'accès temporaire (One Time Password, OTP). 
Cet OTP peut être un code envoyé par SMS ou bien un accès généré par une app de double authentification comme Authy. 



# limites de cette protection

## perte de l'accès à l'application qui gère la double authentification

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">if my phone is lost I can&#39;t:<br>-go to work (2FA)<br>-go to school (online LMS 2FA)<br>-get government services (2FA + phone-only systems) <br>-access my data (gdrive, icloud 2FA) <br>-get a taxi/rideshare (2FA)<br>-order food (2FA)<br>-access banking (2FA) <br>-use my watch <br><br>such a risky bottleneck.</p>&mdash; leon (@towheretobegin) <a href="https://twitter.com/towheretobegin/status/1713961754210783424?ref_src=twsrc%5Etfw">October 16, 2023</a></blockquote>

voir [[partage de Shamir]]

## attaque Meddler in the Middle

Depuis juillet 2022, on observe une recrudescence de comptes piratés qui disposaient pourtant d'une double authentification. 
Il s'agit d'une attaque type Meddler in the Middle ([[MitM]])
L'attaquant utilise un proxy inverse (reverse proxy) pour intercepter le code d'accès envoyé par le serveur. 
Ces reverse proxy sont apparemment assez faciles à trouver sur le marché et à utiliser. 
Des attaques contre Microfost (Office365) et Dropbox ont manifesté l'ampleur du phéonomène qui a fait l'objet d'une étude par l'unité 42 de Palo Alto ([[@longPhishingAttacksThat2022]])

Autre modèle d'attaque [ici](https://www.smtechub.com/ss7-attack/)


