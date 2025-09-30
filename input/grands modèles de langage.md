---
tags:
  - algorithmes
  - IA
aliases:
  - intelligences artificielles
  - IA
  - intelligence artificielle
  - LLM
  - large language model
  - grand modèle de langage
  - gros modèle de langage
  - large modèle de langage
  - larges modèles de langage
"":
---
Définition selon Marcello Vitali-Rosati : 

> Un LLM permet de réaliser une série de calculs sur la langue. Je peux par exemple savoir où se trouve un mot ou une phrase dans un espace linguistique particulier, calculer sa distance par rapport à d’autres mots ou d’autres phrases et donc chercher des synonymes, des contraires, etc. Je peux chercher un mot ou une phrase qui a une position semblable dans une autre langue et donc essayer de trouver une traduction, etc. Je peux par exemple prendre une série de mots et chercher les mots les plus probables qui suivent ces mots.

(source: [[@vitali-rosatiChatGPTTronconneuse2024]])


# le contrôle sur les choses par le langage naturel

> A lot of the current hype around LLMs revolves around one core idea, which I blame on Star Trek:

> Wouldn't it be cool if we could use natural language to control things?
>The problem is that this is, at the fundamental level, a terrible idea.
>A lot of the current hype around LLMs revolves around one core idea, which I blame on Star Trek:
>   *Wouldn't it be cool if we could use natural language to control things?*
>The problem is that this is, at the fundamental level, a terrible idea.
>There's a reason that mathematics doesn't use English. There's a reason that every professional field comes with its own flavour of jargon. There's a reason that contracts are written in legalese, not plain natural language. _Natural language is really bad at being unambiguous_.>There's a reason that mathematics doesn't use English. There's a reason that every professional field comes with its own flavour of jargon. There's a reason that contracts are written in legalese, not plain natural language. _Natural language is really bad at being unambiguous_.

https://infosec.exchange/@david_chisnall/113752873453490050

recherche avec un LLM : antithèse de la recherche avec un [[thesaurus|thésaurus]] ?





## performances des LLM

https://artificialanalysis.ai/

Modèles de langage de [OpenLLM (souverains, explicables, sobres, dotés de sources ouvertes)](https://huggingface.co/OpenLLM-France)


# qu'est-ce qui caractérise un LLM

## paramètres

règles que suit le LLM pour faire les choix les plus adaptés au contexte (donné par le prompt). Ces règles évoluent en fonction de l'apprentissage

## nombre de paramètres

Plus le nombre de paramètres augmente et plus les réponses seront adaptées, en revanche, plus il faudra de ressource (GPU) pour faire tourner le modèle. 
Des modèles de 2 milliards de paramètres peuvent être téléchargés sur des ordinateurs, mais des modèles à 70 milliards de paramètres demandent au contraire beaucoup de [[GPU]] et doivent être installés sur des serveurs pour bien fonctionner. 
## données d'entraînement

Ce sont les données (images ou textes) avec lesquelles le LLM est entraîné. 
## poids (weights)

importance donnée à certaines propriétés des objets. Par exemple, pour une IA classificatoire qui doit déterminer si une photo d'animal représente un chat ou un chien, le poids accordé à la forme des oreilles et à la longueur de la queue sont déterminantes : si les oreilles sont pointues, il y a plus de chances qu'il s'agisse d'un chat. On va donc majorer le poids de cet élément dans l'activité de l'IA. (voir https://blog.fotiecodes.com/explaining-llm-model-weights-and-parameters-like-im-10-llama-clrx7o6hq000109js4t0w4tej)


## ouverture

Modèles clos vs modèles ouverts, mais la question n'est pas binaire : il existe en réalité une grande variété de situations et plusieurs gammes d'ouverture :

Meta recalé au test d'ouverture de LLama par l'OSI (Open Source Initiative) au motif que si le set d'entraînement n'est pas accessible, il n'est néanmoins pas assez décrit [[@claveyLIAOpensourceSa2024]]. 

Mise au point d'un schéma de métadonnées pour les LLM afin de les rendre [[FAIR]] : Croissant [[@carey-wilsonBringingOpenSource2024]]



