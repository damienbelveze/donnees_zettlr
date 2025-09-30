---
title: éditer des requêtes sur Wikidata avec le langage Sparql
subtitle:
author: Damien Belvèze
date: 20-12-2021
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: [cartographie, opendata, Wikidata, langage_requête, programmation]
---

SQL c'est pour les tableaux, SPARQL, c'est pour les graphes


Le SPARQL est un langage d'interrogation pour chercher des entités liées, ce langage d'interrogation a été mis au point par le consortium World Wide Web et sert de langage d'interrogation à [[Wikidata]]

endpoints permettant du requêtage en SPARQL : theses.fr, CAIRN, Factgrid, data.bnf.fr et bien sûr Wikidata (Actuellement 3 endpoints : https://wikidata4science.dbelveze.fr/presentation.html#/sparql-endpoints)

Analyse d'une requête en Sparql sur Wikidata (https://query.wikidata.org)

# exemple de requête simple : les cimetières de guerre allemands

![](sparql_query.png)

``````sparql
\#cemeteries
SELECT ?item ?itemLabel ?place ?coord
WHERE
{
  ?item wdt:P31 wd:Q1241568 .
  ?item wdt:P137 wd:Q708567 .
  ?item wdt:P625 ?coord.

   SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
``````

première ligne : commentaire (titre de la requête)

SELECT : indique les informations issus des résultats à faire figurer en colonne, en l'occurrence le numéro de l'élément [[Wikidata]], son titre, l'endroit assigné à l'élément, et les coordonnées géographiques de l'endroit

WHERE {} permet de donner les critères de recherche. 

?item wdt:P31 wd:Q1241568 : on retrouve à cet endroit le triplet *item*, *propriété*, *valeur* : tous les items qui ont pour propriété (est une instance de) la valeur "cimetière militaire"

Même chose à la ligne suivante : 

?item wdt:P137 wd:Q708567 . 
tout item qui a pour propriété (est opéré par) l'agence "Volksbund Deutsche Kriegsgräberfürsorge"
  
?item wdtP625 ?coord. 
tout item qui dispose de coordonnées géographiques, pour la [[cartographie]] des points

Les résultats sont téléchargeables

![](sparql_results.png)

Pour avoir en plus les images, on peut ajouter dans le Where {} la condition suivante : 

  ?item wdt:P18 ?image.
  
  et ajouter ?image après SELECT
  
  
# exercices

## les centrales nucléaires en Ukraine

P17 : pays (country)
  
````sparql

#nuclear plants in Ukraine
SELECT ?item ?itemLabel ?place ?coord
WHERE
{
  ?item wdt:P31 wd:Q134447 .
  ?item wdt:P17 wd:Q212 .
  ?item wdt:P625 ?coord.

   SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}

````

## les musées de la marine en France
````sparql

SELECT DISTINCT ?item ?itemLabel ?place ?coord 
WHERE {
      ?item wdt:P17 wd:Q142.
      ?item wdt:P31 wd:Q1863818.
      ?item wdt:P625 ?coord.
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}


````

```sparql
# telescopes in France
SELECT  ?item  ?itemLabel  ?coord
WHERE
{
   ?item wdt:P31 wd:Q4213 . # instances or subclasses of astronomical observatory
   ?item wdt:P17 wd:Q30 .  # located in Chile (Q298)
   ?item wdt:P625 ?coord.
   
   SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
```
## les musées de la marine en France et en Espagne

définir une variable ?o dont les valeurs seront précisées à l'intérieur du champ VALUES { }
en l'occurrence ici les valeurs se rapportant à la France et à l'Espagne.

````sparql
SELECT DISTINCT ?item ?itemLabel
WHERE {

      ?item wdt:P31 wd:Q1863818.
      ?item wdt:P17 ?o.
    VALUES ?o{
    wd:Q142
    wd:Q29
   }

  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}

````

utiliser le booléen OR avec UNION {  }

```sparql
SELECT DISTINCT ?institution ?institutionLabel ?Mastodon ?Bluesky ?LinkedIn ?Facebook ?Threads ?Instagram ?countryLabel WHERE {
  ?institution wdt:P31/wdt:P279* wd:Q31855 ;
    wdt:P17 ?country .

  {
    ?institution wdt:P4033 ?Mastodon
  } UNION {
    ?institution wdt:P12361 ?Bluesky
  } UNION {
    ?institution wdt:P4264 ?LinkedIn
  }  UNION {
    ?institution wdt:P11892 ?Threads
  } 
 #   UNION {
 #   ?institution wdt:P2003 ?Instagram
 # } UNION {
 #   ?institution wdt:P2013 ?Facebook
 # }
  
 # pour ajouter Instagram et Facebook décommenter les lignes 14 à 18 ; attention, cela peut excéder le temps défini par défaut d'une requête (time out) et la requête peut échouer

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}

```

## moulins à eau en France

```sparql
SELECT DISTINCT ?item ?itemLabel
WHERE {

      ?item wdt:P31 wd:Q185187.
      ?item wdt:P17 wd:Q142.

  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr". }
}
```

équivalent de la requête en [[R (logiciel)|R]]: 

```r
#http://www.r-bloggers.com/sparql-with-r-in-less-than-5-minutes/

library(SPARQL) # SPARQL querying package
library(ggplot2)

endpoint <- "https://query.wikidata.org/sparql"
query <- 'SELECT DISTINCT ?item ?itemLabel\nWHERE {\n\n      ?item wdt:P31 wd:Q185187.\n      ?item wdt:P17 wd:Q142.\n\n  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr". }\n}\n\n'
useragent <- paste("WDQS-Example", R.version.string) # TODO adjust this; see https://w.wiki/CX6

qd <- SPARQL(endpoint,query,curl_args=list(useragent=useragent))
df <- qd$results
```


## les ponts supportant des voies ferrées en Allemagne et en Autriche

````sparql

#railway bridges in Germany and Austria
SELECT ?item ?itemLabel ?coord ?image
WHERE
{
  ?item wdt:P31 wd:Q39486269 .
  ?item wdt:P17 ?o .
	
  VALUES ?o{
	  wd:Q183
	  wd:Q40
  }
	
  ?item wdt:P625 ?coord .
  ?item wdt:P18 ?image .
  

   SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}

````


Liste des titres de presse en France

élément : périodique https://www.wikidata.org/wiki/Q41298

début (inception) :  P571

fin (demolished) : P576

```sparql
SELECT DISTINCT ?item ?itemLabel ?place ?coord 
WHERE {
      ?item wdt:P31 wd:Q41298.
      ?item wdt:P571 ?begin
      ?item wdt:P576 ?end
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}

```

Tous les journaux qui ont un identifiants BNF avec leur date de début, de fin, leur lieu de parution et les coordonnées géographiques de ce lieu : 

```sparql
SELECT ?journal ?journalLabel ?bnfID ?startDate ?endDate ?cityLabel ?coordinates WHERE {
  # Récupère les noms des journaux et leurs identifiants dans la bibliographie nationale (id BNF)
  ?journal wdt:P31 wd:Q5633421;  # Q5633421 correspond à "journal"
           wdt:P268 ?bnfID.


  OPTIONAL { ?journal wdt:P580 ?startDate. }
  # Optionel : récupération de la date de début de publication

  OPTIONAL { ?journal wdt:P582 ?endDate. }
  # Optionel : récupération de la date de fin de publication
  # Optionel : récupère la ville où se situe l'éditeur du journal
  OPTIONAL {
    ?journal wdt:P291 ?city.
    ?city wdt:P625 ?coordinates.  
    
      # Optionel : récupère la ville où se situe l'éditeur du journal et récupère les  Coordinées géographique de cette ville
  }


  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }
}
# Récupère la version française du label de chaque élément
ORDER BY ?journalLabel
# classe par ordre alphabétique de nom de journal 
```
519 résultats
Si on ne veut que des champs remplis : 

```sparql
SELECT ?journal ?journalLabel ?bnfID ?startDate ?endDate ?cityLabel ?coordinates WHERE {
  # Retrieve the journal entity and its BNF ID
  ?journal wdt:P31 wd:Q5633421;  # Q5633421 corresponds to "journal"
           wdt:P268 ?bnfID.
  ?journal wdt:P580 ?startDate. 

  ?journal wdt:P582 ?endDate. 
  ?journal wdt:P291 ?city.
  ?city wdt:P625 ?coordinates.  # Coordinates of the city
 

  # Service to retrieve English labels for entities
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY ?journalLabel
```

On n'a plus que 4 résultats.

## accidents d'avions

[élément wikidata](https://www.wikidata.org/wiki/Q3149875)  

```sparql
#Accidents d'avion
SELECT ?item ?itemLabel ?date ?deaths ?country ?countryLabel ?coord ?lon ?lat
# affiche dans l'ordre les items, leurs labels (nom de l'événement), la date, le nombre de morts, l'identifiant du pays, le nom du pays, les coordonnées géographiques
WHERE
{
  ?item wdt:P31 wd:Q744913 .
# cherche tous les éléments qui correspondent à des accidents d'avion
  MINUS { ?item wdt:P31 wd:Q898712 . }
# enlève de la liste les accidents survenus après une piraterie
  OPTIONAL { ?item wdt:P585 ?date. }
# s'il y a la date affiche-la
  OPTIONAL { ?item wdt:P625 ?coord. }
# s'il y a les coordonnées géographiques, affiche-les
	    ?coords_sample ps:P625 ?coord;
            psv:P625 [
            wikibase:geoLatitude ?lat;
            wikibase:geoLongitude ?long
                 ] .
# affiche les coordonnées géographiques sous la forme de longitude et de latitude
  OPTIONAL { ?item wdt:P1120 ?deaths.}
# si le nombre de morts est précisé, affiche-le
  OPTIONAL { ?item wdt:P17 ?country.
# si le pays est précisé affiche-le
  ?country rdfs:label ?countryLabel .
  FILTER(lang(?countryLabel) = "en") 
# affiche seulement ces noms de pays en anglais
  }
   SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
# langue de base des résultats : l'anglais
}
```


conversion latitude et longitude > pays : 

```r
```R
# Load the geography package
library(geography)

# Create a data frame with two columns of longitude (lon) and latitude (lat)
df <- data.frame(lon = c(-123, -122, -121, -120), lat = c(37.7749, 37.7651, 37.7558, 37.7461))

# Convert the coordinates to country names using the country_from_coords() function
country_names <- country_from_coords(df$lon, df$lat)

# View the resulting vector of country names
country_names
```

## Liste des films qui ont un président des Etats-Unis comme personnage

```sparql
SELECT ?film ?filmLabel ?character ?characterLabel ?date WHERE {
  ?film wdt:P31 wd:Q11424;        # The film should be an instance of a movie
        wdt:P161 ?character; # The film has a cast member playing a character
        wdt:P577 ?date .

  ?character wdt:P39 wd:Q11696;       # The character is a human


  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY ?filmLabel
```
# Faire des requêtes vers des endpoints sans connaître SPARQL

C'est possible au moyen d'un package conçu pour [[R (logiciel)|R]] : GlittR : https://github.com/lvaudor/glitter



# bibliographie

