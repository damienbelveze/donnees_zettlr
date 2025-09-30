---
title: testing source code
subtitle: 
id: 20250213_testing source code
author: Damien Belvèze
date: 2025-02-13
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - code_source
---

# données synthétiques pour la formation

générateur de données spatiales pour les [[SIG]] [[@gorryRADIANToolGenerating2025]]


# mock objets

Le test fait partie intégrante du processus d'intégration continue, nous y reviendrons, mais pour des personnes extérieures au groupe de développeurs qui souhaitent simplement tester le logiciel et comprendre comment il fonctionne, il convient de leur mettre à disposition un jeu de données. Il peut s'agir de données réelles (un échantillon de l'ensemble des données collectées) ou bien de données synthétiques forgées de toutes pièces à des fins pédagogiques et pour ne pas diffuser de données réelles si celles-ci doivent être protégées.

  

Pour générer des données de test synthétiques, on pourra avoir recours à des artefacts simulant les données réelles (*mock object*).

Certains générateurs d'objets "mock" sont aux données ce que les machines à produire du *lorem ipsum* sont au texte, avec bien sûr un format et des variables particulières pour correspondre à l'architecture de la base de données ou bien aux spécificiations du code.

  

```python

from faker import Faker

from faker.providers import DynamicProvider

  

nomic_rule_provider = DynamicProvider(

provider_name="nomic_rules", # Renamed to avoid issues with numbers

elements=["6 = 0", "6 x 2", "6/2", "6 change the status of the next rule", "the majority is not required for the next rule"],

)

  

fake = Faker()

  

# Add new provider to Faker instance

fake.add_provider(nomic_rule_provider)

  

# Generate rules

for _ in range(10):

print(fake.nomic_rules())

```

Le script ci-dessous est réalisé avec la bibliothèque Faker pour Python qui permet de générer des données synthétiques. En exécutant ce script, on obtient 10 cas dans lesquelles de manière aléatoires apparaissent l'une des 5 règles faisant partie d'un dictionnaire (ce dictionnaire peut être un fichier externe comportant des milliers de règles). Ce fonctionnement peut être répliqué dans un script plus complexe de sorte à générer des ensemble de décisions, ou des parties entières, et cela de manière aléatoire.


$\newline$
# bibliographie
$\newline$






