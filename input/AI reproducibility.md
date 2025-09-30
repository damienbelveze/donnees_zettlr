---
title: AI reproducibility
subtitle: 
id: 20240912_AI reproducibility
author: Damien Belvèze
date: 2024-09-12
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - IA
  - reproductibilité
---
short presentation by [[Stephane Bortzmeyer]]
a lot of scientific results are produced thanks to AI
hability of reproduce the result if we give them all the information we need. 
What do we need to reproduce the results. 
Sometines depending of the exact type you need, some have some randomness which make the reproducibility challenging

things we need to publish

- software
- training set (all the documents that have been eaten by the IA LLM open source sometimes a part of training set have been made public but it's not sufficient [^1])
- various paramaters of training (weights)
- hardware ([[CPU]], GPU). Even if we document exactly the hardware you use, experiment wont be reproducible. Size matters. Not everyone will be able to reproduce the training
- durability : LLM are on Huggingfaces but how much time will they be kept online?

![[ai_reproducibility_bortzmeyer.pdf]]


$\newline$
# bibliographie
$\newline$
[^1]: according to the definition of [[Open Source]] Initiative (OSI) released in october 2024, for a LLM to be considered as "open source", if the training set is not provided itself, then, a complete description of this training set should be made available and by complete OSI means that information given should make possible for "a skilled person" to "build a substantially equivalent system" ([[@claveyLIAOpensourceSa2024a]])





