---
title: Anaconda
subtitle: 
id: 20250623_Anaconda
author: Damien Belvèze
date: 2025-06-23
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - gestionnaire_paquets
  - programmation
  - python
---
Gestionnaire de paquets pour Python (par rapport à pip permet de gérer de dépendances provenant également d'autres logiciels)

juillet 2024, changement de politique commerciale d'Anaconda inc : les établissements de plus de 200 personnes dont universités et labos doivent s'adapter à la nouvelle politique tarifaire et payer une licence. 

Conséquence : miser sur des forges entièrement libres : conda-forge. cf recommandation du CEA : 

***************
il faut utiliser **miniconda** et des channels communautaires comme **conda-forge**

1.  voici les commandes pour utiliser ce channel/canal:

    conda config --add channels conda-forge
    conda config --set channel_priority strict
    conda config --remove channels defaults

2.  Pour voir quels channels vous utilisez: `conda config --show channels`
    
3.  Vous pouvez aussi [exclure le canal defaults dans votre fichier environnement](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually) (`environment.yml`) en ajoutant nodefaults à la liste de canaux:
    

    channels:
     - javascript
     - nodefaults

4.  Enfin, [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) est une alternative à `miniconda` facile à installer et performante qui propose une configuration par défaut sans le canal `defaults`.

*****************
$\newline$
# bibliographie
$\newline$






