---
title: méthodes de modélisation de la pharmacocinétique
subtitle:
id: 20240829_méthodes de modélisation de la pharmacocinétique
author: Damien Belvèze
date: 2024-08-29
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---
voir [[revue systématique]]


P: greffé adulte
I : tacrolimus 
C: N/A
O: modèles pharmacocinétiques
S: revue de littérature sur la comparaison de modèles pharmacocinétiques en rapport avec le tacrolimus

critères d'inclusion : 
- modèles descriptifs
- modèles prédictifs

organes solides

critères d'exclusion : 

enfants, femmes enceintes


Mots [[MeSH]]: 

- Models, Biological
- pharmacokinetics
- tacrolimus


# requêtes et outils

```r
# Search Pubmed AI assistant : https://www.yeschat.ai

("comparison"[All Fields] OR "comparisons"[All Fields]) AND ("populate"[All Fields] OR "populated"[All Fields] OR "populates"[All Fields] OR "populating"[All Fields] OR "population"[MeSH Terms] OR "population"[All Fields] OR "population groups"[MeSH Terms] OR ("population"[All Fields] AND "groups"[All Fields]) OR "population groups"[All Fields] OR "populations"[All Fields] OR "population s"[All Fields] OR "populational"[All Fields] OR "populous"[All Fields]) AND ("pharmacokinetic"[All Fields] OR "pharmacokinetical"[All Fields] OR "pharmacokinetically"[All Fields] OR "pharmacokinetics"[MeSH Subheading] OR "pharmacokinetics"[All Fields] OR "pharmacokinetics"[MeSH Terms]) AND ("model"[All Fields] OR "model s"[All Fields] OR "modeled"[All Fields] OR "modeler"[All Fields] OR "modeler s"[All Fields] OR "modelers"[All Fields] OR "modeling"[All Fields] OR "modelings"[All Fields] OR "modelization"[All Fields] OR "modelizations"[All Fields] OR "modelize"[All Fields] OR "modelized"[All Fields] OR "modelled"[All Fields] OR "modeller"[All Fields] OR "modellers"[All Fields] OR "modelling"[All Fields] OR "modellings"[All Fields] OR "models"[All Fields])

# non significant number of results
```


```r

# add Pharmacokinetics as major topic

"Pharmacokinetics"[Majr] AND ("methods"[All Fields] OR "methodology"[All Fields] OR "methodologies"[All Fields]) AND ("model"[All Fields] OR "models"[All Fields] OR "modeled"[All Fields] OR "modeler"[All Fields] OR "modelers"[All Fields] OR "modelers"[All Fields] OR "modeling"[All Fields] OR "modelings"[All Fields] OR "modelization"[All Fields] OR "modelizations"[All Fields] OR "modelize"[All Fields] OR "modelized"[All Fields] OR "modelled"[All Fields] OR "modeller"[All Fields] OR "modellers"[All Fields] OR "modelling"[All Fields] OR "modellings"[All Fields] OR "models"[All Fields]) 

# 4008 results
```

```r
# replace all forms of model* by Mesh terms Models, Biological and Models, Theoretical

"models, theoretical"[MeSH Terms] AND "models, biological"[MeSH Terms] AND "Pharmacokinetics"[Majr]

# 4228 results
```

```r
# adding population concept to pharmacokinetics (non existing MeSH term for population pharmacokinetics)

"models, theoretical"[MeSH Terms] AND "models, biological"[MeSH Terms] AND ("Pharmacokinetics"[Majr] AND "population"[All fields])

# 415 results
```

```r
# adding assessment or comparison concept 

"models, theoretical"[MeSH Terms] OR "models, biological"[MeSH Terms] AND ("Pharmacokinetics"[Majr] AND "population"[All Fields]) AND ("comparison"[All Fields] OR "compare"[All Fields] OR "assessment"[All Fields] OR "assess"[All Fields])

# results : 125
```

$\newline$
# bibliographie
$\newline$






