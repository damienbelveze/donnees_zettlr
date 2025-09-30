---
title: reactive programming
subtitle: 
id: 20240901_reactive programming
author: Damien Belvèze
date: 2024-09-01
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - programmation réactive
  - declarative programming
tags:
  - programmation
---
Type de programmation dont le résultat n'est pas assertif et dépendant uniquement du code-source, mais dépendant également des entrées réalisées par un tiers, par exemple (dans le cas de [[Shiny]]) d'un utilisateur qui coche des boutons, règle des échelles ou sélectionne des points dans une interface web (via son navigateur web)

```r
ui <- fluidPage(
  textInput("name", "What's your name?"),
  textOutput("greeting")
)

server <- function(input, output, session) {
  output$greeting <- renderText({
    paste0("Hello ", input$name, "!")
  })
}
```

Dans l'exemple ci-dessus (R et Shiny), le serveur qui héberge le code R n'affiche Bonjour + nom de l'utilisateur que lorsque (et chaque fois que) l'utilisateur fournit son nom dans le champ que lui ouvre son navigateur. 

la variable ``output$greeting`` a une relation de **dépendance réactive** à l'égard de la variable ``name``

ce qui s'exprime dans un schéma de programmation de la manière suivante : 

![](images/reactive_dependance.png)
(voir https://mastering-shiny.org/basic-reactivity.html)
voir aussi opposition entre programmation assertive et programmation déclarative


$\newline$
# bibliographie
$\newline$






