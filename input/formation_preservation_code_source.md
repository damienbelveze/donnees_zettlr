---
title: formation_preservation_code_source
subtitle:
id: 20240405_formation_preservation_code_source
author: Damien Belvèze
date: 2024-04-05
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---


## Réunion du 5 avril - Damien, Jozefina, Claire

Formation prévue le 13 juin dans le cadre du Printemps de la donnée : https://salles.bu.univ-rennes2.fr/event/4150487.

=> orienter la formation sur la préservation du code - faire passer du code d'une forge vers HAL puis vers SWH 
Biotools: https://bio.tools/
scicrunch: https://scicrunch.org/resources/data/source/nlx_144509-1/search
approche communautaire

**possibilité de faire une démo**
utiliser un [repo sur Github](https://github.com/moranegg/deposit-template) pour le déposer dans SWH

### déroulement possible de la formation

A partir du repo présent sur "Github Wonderland App", montrer aux participants le chemin suivant: 

#### rapide introduction sur la préservation du code de recherche

- archivage (forge = pas pérenne)
- reproductibilité

#### démo

- présentation du repo Github
- rédaction du codemeta.json dans l'interface du codemeta generator, à partir des informations présentes dans le repo (readme, licence, authors/CFF)
- envoi du repo vers Software Heritage
- référencer le code envoyé dans SWH dans HAL en utilisant le codemeta (au moyen du Software-hID, version longue [^1])
- ajouter certains champs qui manquent dans la notice de HAL (voir informations qui ne se trouveraient pas dans le codemeta)
- montrer comment ça se présente dans le CV-HAL

Prévoir un diaporama avec l'intro et la conclu et quelques planches qui décrit le parcours de la forge vers SWH et de SWH vers HAL


[^1]: pour avoir des éléments contextuels
_______

**Demande:**
- Présenter en juin seul ou avec un binôme un court atelier d'une heure sur la conservation et le partage du code de recherche. 
- Dans un deuxième temps un atelier de 2 heures pour les doctorants (avec des exercices pratiques pas encore conçus). 

- **proposition IES:**
- nous accompagnons les ateliers de la donnée sur ce sujet d'ouverture des codes et des logiciels de différentes manières :
- en proposant des formations aux membres de l'atelier
- en participant à la création des supports de formations - notamment dans le cadre des écoles doctorales (en cours à Lille)
- en animant (en collaboration avec les collègues des SCD) les formations ou les ateliers à l'occasion des journées thématiques, écoles doctorales.

Notre objectif est toujours le transfert de compétences vers les membres de l'atelier afin de leur permettre d'avancer en autonomie après une période d'accompagnement. C'est la seule logique que nous essayons de suivre et sommes souples en fonction du contexte et des besoins de chaque atelier.

**projet:**
- comment gérer le code de recherche en lien avec SO et le PGD
- 2ème besoin: mettre en place des formations pour les doctorants
- ateliers à distance. Sous forme de présentation .
- REX IES: comment faire en sorte que le code source puisse se placer au même niveau que les publications et le données de recherche?
- Comment appliquer les principes FAIR au code de données? REX SWH - complexité d'appliquer ces principes FAIR aux codes sources
    - précisions et ressources : 
    - appliquer les principes FAIR au logiciel c'est bien mais ça ne suffit pas car le logiciel est plus complexe qu'un dataset
    - présentation Fair4ResearchSoftware - RDA France : https://www.canal-u.tv/chaines/rda/fair-for-research-software-0
    - https://zenodo.org/records/10047401
    - Comment évaluer la conformité d'un logiciel avec les principes FAIR ? - https://openscience.pasteur.fr/2024/02/14/comment-evaluer-la-conformite-dun-logiciel-avec-les-principes-fair/
        - cet article donne les pointeurs vers plusieurs sources très intéressantes au sujet des principes FAIR appliquées aux logiciels
    - au sujet de la reproductibilité : 
        - comment savoir qu'est-ce qu'il faut archiver en plus du code source ?
        - pour répondre à ce besoin Software Heritage a un partenariat avec [[Guix]] pour assurer la reproductibilité à long terme :
            - https://www.softwareheritage.org/2019/04/18/software-heritage-and-gnu-guix-join-forces-to-enable-long-term-reproducibility/
            - https://guix.gnu.org/blog/2019/connecting-reproducible-deployment-to-a-long-term-source-code-archive/
            
- Doc rédigée par l'IES: recommandations sur comment le code doit être décrit à minima (en lien avec le travail de modération derrière)
- il peut aussi y avoir des réponses différentes selon l'importance du code
- A partir de quand on sépare le logiciel des données? A partir de quand on peut le considérer comme un objet indépendant? 
- échange sur ou déposer : Github/Gitlab/RDGR
- HAL permet de décrire et de rendre trouvable - SWH: assure la perennité et la fiabilité
- Préconiser des bonnes pratiques en terme de description 
- visibilité du code: plus facile à retrouver dans HAL que dans SWH
- faire le lien entre publications/données/logiciels 
- ambassadeurs SWH: https://www.softwareheritage.org/ambassadors/

***atelier Publics chercheurs (en général) :***
- 13/06 de 13h à 14h. Présentation à 2 : Damien + IES 

***Ateliers doctorants***
- faire des propositions de formation au mois de juillet. 
- proposition de travail commun avec Dominique Launay (RSSI INRIA Rennes) - membre de la cellule "données@inria"

