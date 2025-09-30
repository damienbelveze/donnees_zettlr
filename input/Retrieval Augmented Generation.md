---
title: Retrieval Augmented Generation
subtitle: 
id: 20240217_Retrieval Augmented Generation
author: Damien Belvèze
date: 2024-02-17
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - RAG
tags:
  - IA
---
Catégorie d'outils entraînés à générer des textes à partir de littérature scientifique convoquée au moyen de mots-clé. 

Possibilité d'avoir des réponses plus fiables parce que basées sur un corpus documentaire et de minimiser ce que les concepteurs de LLM appellent des [[hallucination|hallucinations]] (mais pas de les supprimer)

![](images/raglogo.png)

Un outil de génération de texte basée sur une extraction de données (retrieval augmented generation) assume deux tâches successives : 

- mobilisation de textes ou bouts de textes à partir de mots-clé présents dans une question
- constitution d'une réponse à partir des bouts de texte mobilisés sous forme de prompt au moyen d'un outil comme GPT3 ou GPT4

Un RAG poussé dans ses retranchements génère des réponses textuelles en citant des textes qui n'ont pas de rapport avec le thème si on restreint trop les textes citables (cf. constat de Aaron Tay à propos de Scite.ai [[@tayThingsAmStill2024]])

Pour Arthur Perret, les RAG couplent une technique d'interrogation fiable et contrôlable par mots-clé, à une autre basée entièrement sur les rapprochements sémantiques entre métadonnées et qui ajoutent une partie non fiable et non maîtrisable : 

> RAG, présentée comme la solution aux erreurs factuelles, est en fait une recherche d’information classique avec en supplément une génération de texte non fiable, coûteuse en temps et en attention

[[@perretLintelligenceArtificielleGenerative2025]]

# Evaluer un RAG

niveau de pertinence

## critères  :

### recall

nombre de documents cités sur l'ensemble des documents jugés pertinents dans la base. Si 3 documents pertinents et 3 documents cités, alors on un a recall de 1 (meilleur score possible). Le recall ne tient pas compte de l'ordre de mention des sources mais seulement de leur pertinence. 

### Mean Reciprocal Rank (MMR)

tient compte de l'ordre de citation. Le RAG permet-il au LLM d'envoyer la meilleure référence en tête de la réponse ? 

### Mean average precision (mAP)

ordre d'apparition de l'ensemble des réponses attendues (combinaison du recall et du MMR)

(source : https://www.deepset.ai/blog/rag-evaluation-retrieval)

# RAG local usages de recherche

#### outil d'exploration de la littérature scientifique

charger des articles et extraire de cette liste d'articles les concepts principaux. 

Test 1. Poser une question ou plusieurs questions à partir d'un set d'articles qu'on a uploadés (par exemple, "de quoi parlent ces articles ?"). Mesurer la pertinence de la réponse, vérifier que les textes les plus pertinents sont effectivement les plus cités ou mis en avant.

Test 2. extraire une liste de concepts (avec une colonne pour le concept, une colonne pour la source). Limiter la recherche à l'abstract et comparer avec les résultats si on ne limite pas la recherche à l'abstract (full text)

Test 3. extraire les jeux de données reliés aux articles sous la forme de feuilles de calcul

Test 4. Dans ce set d'articles, trouver les études dont les résultats dont divergents

Test 5. faire un résumé d'une sous-sélection d'articles

Test 6. Prendre plusieurs RCT et demander au RAG de résumer de synthétiser ces articles selon la méthode PICO (Patient, Intervention, Comparator, Outcome)

#### Autres usages dans un cadre de recherche

traduction d'une présentation en markdown ou LaTeX du français à l'anglais (vérifier que la syntaxe et les balises ne sont pas affectées dans l'output) et que le résultat est "prêt à servir"





$\newline$
# bibliographie
$\newline$






