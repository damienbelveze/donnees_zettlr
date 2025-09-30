---
title: RDG et RAGaRenn
subtitle: Réunion
id: 20250114_RDG et RAGaRenn
author: Damien Belvèze
date: 2025-01-14
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
---
voir [[RAGaRenn]], [[RAG]] et [[Recherche data gouv]]
Docapost (OpenValue): presta pour faire un RAG pour les Juristes. 
AI factory


embeddings créés avec un petit LLM multilingue (3B suffit) : paraphrase-mulilingual-npmnet-v2

Le LLM utilisé pour les [[embeddings]] doit comporter tout le champ sémantique du jeu de données, ne pas choisir un modèle trop petit. 
Or les abstracts sont pluridisciplinaires, donc toutes les disciplines sont représentées mais cela reste limité dans la mesure où c'est de langue scientifique qu'on parle ici et pas la langue naturelle. 



autre modèle utilisé pour l'inférence (Llama 3.2)

assistance à la curation des données

Moissonnage d'une partie des métadonnées de l'entrepôt INRIA (3100 enregistrements en xml)

transformation du XML en JSON format plus plat 
PDF vers text : la performance du RAG va pas mal dépendre des scories qui resteront (par exemple balises html)

transformation avec un modèle d'embeddings de l'ensemble des abstracts, titres, mots-clé

usage de [cross-encoders](https://www.sbert.net/examples/applications/cross-encoder/README.html)


chatbot (avec Virgile Jarrige)

modèle Lucy (7B)
essais avec une VM qui a une carte graphique "grand public"
Est-ce que ce serait possible de requêter sur RAGaRenn
Laurent Morin : en principe, c'est ok. 



$\newline$
# bibliographie
$\newline$






