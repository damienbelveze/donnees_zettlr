---
title: analyser les données de Mastodon
subtitle: 
id: 20241016_analyser les données de Mastodon
author: Damien Belvèze
date: 2024-10-16
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - réseaux_sociaux
  - Mastodon
  - R_logiciel
---
installation du package Rtoot
```r
{r setup, include=FALSE}
install.packages('rtoot')
library(rtoot)
```

identification (accès en mode anonyme ou authentifié)
```{r}
auth_setup()
```
Dans le cas d'un choix en mode authentifié, indiquer son instance de la manière suivante : "mamot.fr", accepter la demande de Mastodon. 

```{r}
library(rtoot)
df <- search_accounts("plazi_species")
df2 <- get_account_statuses(df$id)
df2 <- apply(df2,2,as.character)
write.csv(df2, file = "plazi_species_toots.csv", row.names=FALSE, na = "", fileEncoding = "UTF-8")
```
récupère les toots du compte "plazi_species" et les mets en forme de tableau CSV dans le dossier
```{r}
df2 <- get_account_statuses("112370075539544475")
df2 <- apply(df2,2,as.character)
write.csv(df2, file = "SO_univrennes_toots.csv", row.names=FALSE, na = "", fileEncoding = "UTF-8")

```

importance de limit = n pour avoir tous les toots (si la limite n'est pas plus grande, on en manque)

```r
```{r}
df2 <- get_account_statuses("112370075539544475", limit = 220, verbose = TRUE)
df2 <- apply(df2,2,as.character)
write.csv(x = df2, file = "SO_Univ_Rennes_toots.csv")
```

[[@stochasticsInteractingMastodonAPI]]

# calculer la longueur moyenne des toots

[[@schochSoftwarePresentationRtoot2023]]


# analyse des toots de Mastodon avec Python

code réalisé avec Python et le package beautifulSoup :
[[@qaziMastodonDataExtraction2024]]


# bibliographie
$\newline