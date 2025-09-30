---
title: plan de gestion de logiciel
subtitle: 
id: 20231003_plan de gestion de logiciel
author: Damien Belvèze
date: 2023-10-03
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - Software Management Plan
  - SMP
  - PGL
  - software management plan
tags:
  - données_recherche
  - code_source
---

# Définition

> More recently, software management plans35 (SMPs) have been proposed for managing software lifecycles. Like data management plans (DMPs), SMPs are documents describing what the aim of the software is, how the research software will be managed, both during a project’s lifetime and after a project has ended. By making this information explicit, SMPs help to set up a proper development cycle for research software, provide insight into the necessary resources during development, and ensure the long-term accessibility of the software is properly considered.

(source: [[@courbebaisseResearchSoftwareLifecycle]])




travaux du Groupe de Travail 5 des Ateliers de la donnée

[[FAIR]] et logiciel de recherche [[@gruenpeterD4GuidelinesRecommended2023]]

version allégée de Présoft pour du logiciel de recherche ([Presoft](https://dmp.opidor.fr/public_templates?page=1&search=presoft) est un résumé du développement de logiciel complet et autonome). Le logiciel dont il s'agit ici est du logiciel de recherche, décrit comme un produit de recherche ; distinct des données de recherche en cela que les données ne sont pas dynamiques, le code l'est par définition (mise à jour)
# Pratiques sociales : Partager le logiciel

Le partage du code est très loin d'être ancré dans les moeurs des chercheurs (dans 95% des cas, le code utilisé n'est pas partagé ) apporte un bénéfice de citation


Partager le code dans un répertoire de code qui autorise un contrôle de version.


# Structure du PGL

### 1.1 Basic description

**Describe your code by mentioning what it was designed for, to what kind of users it was designed**

in which field your code has a relevant role (discipline, sub-discipline)

give some keywords to describe the possible uses of your software (use relevant ontologies such as https://www.loterre.fr/ or https://cran.r-project.org/web/classifications/ACM-2012.html#code:10011445)

Is your code already available to all or will it be made available soon, when and by which means?


### 1.2 link to data

Could you link this SMP(Software Management Plan) to other documents (source code, publication, dataset, Data Management Plan). Put the links (DOI) here.

<div class="red">Do you provide a data sample to check that your software works well and to make easier for the user to see how your code can be used ?</div>

### 1.3 development history

when did the project start, when was the first version released? 

which is the current (linked to this SMP) version number

## 2 Tools 

- code repository : Do you use a forge, and which one ?
- continuous integration : workflow including automatic test of the code when a commit is done. How can somebody contribute to your code or test it, under which rules?

## 3 Preservation

is your source code available in one of the trusted repo ([[Zenodo]] / [[HAL]]) ? (add links)
is your code archived (and which version) in the [[Software Heritage]] archive? (add SWHID)
How should your source code be cited by other researchers (CFF, codemeta)

## 4 Legal issues

Which Licence? why?

## 5 Valorisation

Will the source code be maintained in the future, will it be transfered to other stakeholders
did you use a development methodology?
did you use technical specifications for development?

## 6 software management adventure

[serious game](https://nlesc.github.io/softwarehorrorgame/SoftwareHorrorGame.html) made with [[Twine]] by Vrije Universiteit Amsterdam; Leiden University; Netherlands eScience Center.
voir également [Open Science Escape Room](https://sites.google.com/vu.nl/open-science-escape-room/fair-software-intro?authuser=0) 

[EURISE checklist](https://github.com/eirini-zormpa/cyborg-revolution) to check if the source code is shared accordingly with the [[FAIR]] principles


$\newline$
## 7 Ressources
$\newline$
[Zotero library on software management](https://www.zotero.org/groups/4684302/software_management_plan_smp/library)
$\newline$
# bibliographie
$\newline$






