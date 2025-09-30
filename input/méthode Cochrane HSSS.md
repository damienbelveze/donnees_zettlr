---
title: méthode Cochrane HSSS
subtitle: 
id: 20250502_méthode Cochrane HSSS
author: Damien Belvèze
date: 2025-05-02
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - Cochrane HSSS
  - Cochrane Highly Sensitive Search Strategy
  - stratégie Lefebvre
tags:
  - revue_littérature
  - études_cliniques
---
méthode consistant à retrouver l'ensemble des RCT dans Medline sans passer par le filtre "études cliniques" qui n'est pas assez sensible. Etude mise au point en 1994 par Lefebvre et all. (Dickersin K, Scherer R, and Lefebvre C. Identifying relevant studies for systematic reviews. BMJ. 1994 Nov 12; 309(6964):1286–91.) cité par [[@glanvilleHowIdentifyRandomized2006]]

Exemple d'application de la méthode Cochrane HSSS dans 8 journaux :


|     | Query                                                                                                                                                                                                                                                                                                                                          | Results dated on 12 March 2025 |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 1   | randomized controlled trial [pt]                                                                                                                                                                                                                                                                                                               | 634910                         |
| 2   | controlled clinical trial [pt]                                                                                                                                                                                                                                                                                                                 | 725668                         |
| 3   | randomized [tiab]                                                                                                                                                                                                                                                                                                                              | 747909                         |
| 4   | placebo [tiab]                                                                                                                                                                                                                                                                                                                                 | 264004                         |
| 5   | drug therapy [sh]                                                                                                                                                                                                                                                                                                                              | 2789077                        |
| 6   | randomly [tiab]                                                                                                                                                                                                                                                                                                                                | 455560                         |
| 7   | trial [tiab]                                                                                                                                                                                                                                                                                                                                   | 871033                         |
| 8   | groups [tiab]                                                                                                                                                                                                                                                                                                                                  | 2858975                        |
| 9   | #1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8                                                                                                                                                                                                                                                                                                   | 6317326                        |
| 10  | animals [mh] NOT humans [mh]                                                                                                                                                                                                                                                                                                                   | 5315216                        |
| 11  | #9 NOT #10                                                                                                                                                                                                                                                                                                                                     | 5541635                        |
| 12  | 2018/07/01:2024/12/31[Date - Publication]                                                                                                                                                                                                                                                                                                      | 9585908                        |
| 13  | "the New England journal of medicine"[Journal] OR "Lancet"[Journal] OR "Journal of the American Medical Association"[Journal] OR "JAMA"[Journal] OR "British Medical Journal"[Journal] OR "BMJ"[Journal] OR "Annals of internal medicine"[Journal] OR "JAMA internal medicine"[Journal] OR "PLOS Medicine"[Journal] OR "BMC medicine"[Journal] | 568119                         |
| 14  | #11 AND #12 AND #13                                                                                                                                                                                                                                                                                                                            |                                |

la comparaison entre la stratégie de recherche "filtre RCT + mot-clé" ou la stratégie de recherche Cochrane HSSS ne tourne pas toujours à l'avantage de cette dernière qui dans certains domaines a de moindres scores en [[Spécificité vs sensibilité|spécificité]] et sensibilité

> Surprisingly, the Cochrane HSSS applied to PubMed did not present a higher sensitivity or specificity than open searches

(résultat dans le champ de la neurochirurgie, [[@gorayebElectronicSearchStrategies2019]])

Le problème vient du fait que les auteurs ne signalent pas correctement leurs études comme des RCTs en suivant les bonnes pratiques en la matière

Les bonnes pratiques CONSORT "Consolidated Standards of Reporting Trial"  spécifient que le terme "trial" devrait être présent dans le titre. 

*random* au lieu de *randomly* ou *randomized* ? ([[@cooperEstablishedSearchFilters2019]])



$\newline$
# bibliographie
$\newline$






