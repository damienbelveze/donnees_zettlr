---
title: test unitaire
subtitle: 
id: 20250522_test unitaire
author: Damien Belvèze
date: 2025-05-22
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
---
### Tests unitaires

  

Le type le plus basique de tests pour un logiciel. Son objectif est de vérifier l'implémentation correcte des méthodes et fonctions uniques sur lesquelles un logiciel est construit.

Généralement, il s'agit d'une suite de petits appels de fonctions mettant en évidence des cas particuliers et l'utilisation générale des fonctions implémentées.

Par exemple, supposons qu'une fonction ait été construite pour calculer le rapport entre deux nombres entiers.
```

// langage: JavaScript

function divide_integers(a, b){

return a / b;

}

```

Nous voyons clairement que cette fonction est à peine terminée et qu'elle fonctionne correctement. Par exemple, que se passe-t-il si deux nombres décimaux sont donnés ? Ou que se passe-t-il si l'on donne deux chaînes de caractères ?

  

La mise en œuvre d'un test unitaire pour cette fonction aidera le développeur à.. :

1. identifier les cas particuliers

2. décider de ce qu'il faut faire lorsque cela se produit

3. assurer la stabilité et la justesse de l'implémentation

4. vérifier tout ce qui précède en une seule fois, sans avoir à appeler la fonction à plusieurs reprises avec tous les cas possibles.

```

// langage: JavaScript

[...]

test("Check correctness with Integers", () => {

expect(divide_integers(8,2)).toBe(4);

})

  

test("Check throw error with Strings", () => {

expect(divide_integers("hello", "world")).toThrow(TypeError);

})

```

Si nous exécutons ce petit extrait de code, nous constatons que le deuxième test échoue, car notre fonction ne lance pas d'erreur de type (TypeError) lorsqu'elle est appelée avec des chaînes de caractères. Cette contrainte a peut-être été établie lors de la phase de conception. En voyant le test échouer, nous pouvons immédiatement voir ce qui ne fonctionne pas et corriger le code en conséquence.

```

// langage: JavaScript

function divide_integers(a, b){

if (typeof a === 'string' || typeof b === 'string') {

throw new TypeError('Inputs must not be strings');

}

return a / b;

}

```

$\newline$
# bibliographie
$\newline$






