---
title: site statique
subtitle:
id: 202212281826_site statique
author: Damien Belvèze
date: 28-12-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [sites_statiques]
tags: [programmation]
---
<iframe src="https://mas.to/@j9t/112608838913878195/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" allowfullscreen="allowfullscreen"></iframe>

Un site statique génère des pages telles qu'elles se présentent dans l'espace où elles sont conservées, au contraire d'un site dynamique qui utilise une application web pour générer des pages différentes d'un utilisateur à l'autre. 

Hugo, Jekyll, Netlify et [[Mkdocs]] sont quelques générateurs de sites statiques. 
Ces logiciels permettent de générer des sites web à partir de répertoires hébergés par exemple sur github ou gitlab. 

Possibilité de déployer un site statique depuis [[Github]] sans connaître [[Git|git]] avec une [[interface graphique]], voir le projet Publii : https://github.com/GetPublii/Publii 
Utile pour aider les chercheurs à se créer un [[Site de chercheur]]

Générateur de sites statiques pour la campagne des législatives 2024 mis à disposition des candidat.e.s du Front populaire : https://legislatives-2024-maiwann-a1cb0e879ab8bab2bc243d3e9f46955f92cb8.monpetitsite.org/

# site avec Hugo 

voir [[Stretching_Hugo_MaximilienPetit_28032025.odt| démonstration de Maximilien Petit]] pendant le stretching numérique

voir méthode proposée par carnet de notes Hypotheses : https://bibliopea.hypotheses.org/979

ajouter le thème papermod : 

```yaml
variables:
GIT_SUBMODULE_STRATEGY: recursive
THEME_URL: "github.com/adityatelange/hugo-PaperMod"
```

# site avec DecapCMS

voir [[DecapCMS]]

