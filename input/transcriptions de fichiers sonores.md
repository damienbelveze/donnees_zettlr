---
title: transcriptions d'entretiens
subtitle:
id: 202211271427_transcriptions d'entretiens
author: Damien Belvèze
date: 27-11-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [interview transcripts]
tags: [transcription]
---

transcription manuelle avec [[Sonal]]

transcription automatique avec l'outil libre [Scribe](https://scribe.cemea.org/) du CEMEA (Centre d'entraînement par les méthodes actives)
[Plus sur Scribe](https://cemea.asso.fr/salle-de-presse/la-presse-parle-des-cemea/un-logiciel-libre-100-cemea-rentre-au-sill-socle-interministeriel-de-logiciels-libres)
Scribe repose sur la base de textes lus [commonvoice](https://commonvoice.mozilla.org/fr)de Mozilla, de même que [Vosk](https://alphacephei.com/vosk/)interpréteur de texte lu. 

[L'atelier de la donnée ARDoISE](https://scienceouverte.univ-rennes.fr/atelier-rennais-de-la-donnee-information-et-soutien-aux-equipes-de-recherche "https://scienceouverte.univ-rennes.fr/atelier-rennais-de-la-donnee-information-et-soutien-aux-equipes-de-recherche") commence à voir dans les Plans de Gestion de Données qui lui sont soumis (par des chercheurs et chercheuses des deux universités)  des projets qui utilisent Whisper d'OpenAI, par exemple pour retranscrire des entretiens réalisés dans un cadre de recherche. ARDoISE n'a pas vocation à discuter ce recours sur le plan politique, au sens où OpenAI occupe déjà une position ultradominante sur le marché des IAG et n'a pas besoin des chercheurs pour renforcer toujours plus cette hégémonie. 

Jusqu'à présent, on discutait surtout la question sur l'angle de la confidentialité des données soumises. OpenAI n'a aucun engagement à respecter le RGPD, et toute latitude apparemment pour réutiliser les données qui lui sont soumises. C'est pourquoi, nous conseillons plutôt d'utiliser [Scribe](https://scribe.cemea.org/ "https://scribe.cemea.org/") l'outil du CEMEA qui lui se présente comme un sous-traitant responsable au sens du RGPD. le CEMEA déclare ne livrer les données à aucun partenaire et est un acteur fiable, Scribe, basé sur Vosk-Server a son code source diffusé sous licence libre. Peut-être connaissez-vous d'autres alternatives qui pourraient apporter les mêmes garanties et que nous pourrions conseiller ? 

Je n'ai essayé Scribe que des enregistrements audio assez courts. Il doit y avoir pour des enregistrements plus longs des erreurs de transcription. Scribe est transparent là-dessus. Whisper en revanche se présente comme une solution définitive (quoiqu'OpenAI ait la précaution de nous rappeler qu'elle ne doit pas être utilisée dans des cas sensibles). A l'enjeu RGPD, la recherche récente sur le sujet pointe à présent des erreurs de transcription (comme dans Scribe) mais qui relèvent également de ce qu'on appelle généralement des "hallucinations" : même lorsque l'enregistrement audio semble clair, Whisper ajoute des bouts de texte qui n'ont pas été prononcés. Le piège est qu'un outil de transcription assisté par une IA, contrairement à une transcription réalisée "à la main" avec un outil comme Sonal, a vocation à nous faire gagner en productivité. Or cette recherche de productivité nous amène fréquemment à faire l'impasse sur les relectures surtout quand le marketing autour de l'outil nous assure qu'il est "error-free". De là viennent un certain nombre de conséquences fâcheuses pour certaines communautés comme celle des médecins outre-atlantiques qui se servent de cet outil pour retranscrire (sans vérification donc) des diagnostics enregistrés avec un dictaphone. Voir à ce sujet [cet article](https://apnews.com/article/ai-artificial-intelligence-health-business-90020cdf5fa16c79ca2e5b6c4c9bbb14 "https://apnews.com/article/ai-artificial-intelligence-health-business-90020cdf5fa16c79ca2e5b6c4c9bbb14") sur Associated Press. L'article se base sur une étude publiée dans [ACM](https://dl.acm.org/doi/abs/10.1145/3630106.3658996 "https://dl.acm.org/doi/abs/10.1145/3630106.3658996") où l'on apprend que le texte injecté par le LLM dans la transcription concerne surtout des personnes ayant des difficultés à parler, Whipser comblerait les lacunes dans le discours à sa façon. Les injections sont de trois ordres : 1. violence et insinuations à caractère sexuel 2. invention d'états de santé et de médicaments 3. fausse autorité (des propos de Youtubers s'invitent dans la transcription). 

Il est normal que ces outils soient faillibles même si dans le cas de Whisper, le caractère des "hallucinations" laisse songeur, par contre, dans le contexte de la course à la publication, il est probable qu'à court terme des équipes de chercheurs se fassent abuser par l'exactitude alléguée des productions de Whisper ou d'outils du même type disposant d'une grande renommée et s'appuyant sur un marketing offensif.

# Whisper installé sur Humanum

# applications de bureau

## Parlatype

https://launchpad.net/~gabor-karsay/+archive/ubuntu/parlatype

## Buzz (comporte Whisper)

https://github.com/chidiwilliams/buzz




