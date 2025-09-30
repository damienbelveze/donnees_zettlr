---
title: Twine système de magasin
subtitle: 
id: 20240821_Twine système de magasin
author: Damien Belvèze
date: 2024-08-21
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - Twine
  - programmation
---
# étapes

3 passages : 
1 passage où on expose la marchandise
1 panier
1 passage où on attribue des variables pour chaque item acquis

- dans le système présenté ici, le joueur peut espérer obtenir une ristourne en convainquant le fournisseur de matériel
- le joueur peut rendre un item pour récupérer assez d'argent pour en acheter un autre. 

# premier passage ("36bis")

```sugarcube
L'agence de renseignement du 36bis OstseeStrasse est en réalité un dépôt de matériel que le commandement soviétique de Berlin-est met de temps à temps à disposition des services secrets Est-Allemands notoirement sous-équipés par rapport à leurs collègues Russes beaucoup mieux dotés. 
Par chance, on vous a donné le contact d'un certain Anatoli Madankulov qui gère l'attribution de ces équipements. Vous ne le connaissez pas personnellement, mais on vous a dit qu'il était d'humeur lunatique, à moins que ce ne soient ses chefs qui peuvent se montrer plus ou moins généreux ou plus ou moins radins selon les jours. 
<<nobr>>
  <<set $marks to 500>>
  <<set $anatoli to random(7,14)>>
  <<set $inventory to []>>
<</nobr>>
Vous vous présentez donc au 36bis avec un peu d'appréhension et l'agent que vous avez conservé de la liasse une somme qui accompagnait l'enveloppe de Müller que vous jugez insuffisante, mais c'est tout ce dont vous disposez :  marks est-Allemands. 

Anatoli, dans un mauvais allemand, vous demande ce que vous êtes venus chercher et vous tend une liste des articles disponibles : 
<<nobr>>
<<if $langue eq "russe">>Vous passez au russe pour avoir plus de chance de convaincre Anatoli de vous vendre à moindre prix certains objets dont vous pourriez avoir besoin

	<<if $anatoli <= $persuasion +3>> Anatoli, gagné par votre bagoût, vous consent des ristournes importantes. 
    	<<set $ristourne to true>>
    <<else>> Anatoli reste insensible à vos tentatives de faire baisser les prix "pour la bonne cause". Rien à faire, vous allez devoir acheter les articles au prix qui sont indiqués sur le catalogue 
    	  <<set $ristourne to false>>
     <</if>>
<<else>> 
		<<if $anatoli <= $persuasion>> En dépit du fait que vous ne connaissiez pas le russe et que vous ne pouvez utiliser que l'allemand qu'il comprend mal, Anatoli, gagné par votre bagoût, est peu à peu gagné par votre enthousiasme et vous consent des ristournes importantes. 
        	<<set $ristourne to true>>
        <<else>>Ne maîtrisant pas bien le russe, vous ne disposez que de peu d'arguments dans la négociation. Anatoli coupe rapidement les arguments en Allemand que vous essayer de formater pour qu'ils soient compris de lui. 
        	<<set $ristourne to false>>
		<</if>>
<</if>>
<</nobr>>
<<nobr>>
<<if $ristourne is true>>
	<<set $prix_parapluie to 200>>
    <<set $prix_polaroid to 80>>
	<<set $prix_grappin to 50>>
 	<<set $prix_puce to 350>>
 	<<set $prix_fusil to 300>>
 	<<set $prix_serum to 250>>
 	<<set $prix_antidote to 150>>
<<else>>
	<<set $prix_parapluie to 250>>
	<<set $prix_polaroid to 120>>
	<<set $prix_grappin to 80>>
	<<set $prix_puce to 400>>
	<<set $prix_fusil to 250>>
	<<set $prix_serum to 300>>
	<<set $prix_antidote to 200>>
<</if>>
<</nobr>>
	<h2>Voici les articles disponibles à l'achat</h2>
<<nobr>>
<div id="shopMessage"></div>
 <</nobr>>
* parapluie bulgare - $prix_parapluie marks 
   <<nobr>>
    <<button "acheter">>
        <<if $marks >= $prix_parapluie>>
            <<set $marks -= $prix_parapluie>>
            <<set $inventory.push("parapluie bulgare")>>
            <<replace "#shopMessage">>Vous avez acheté le parapluie bulgare, il vous reste $marks marks<</replace>>
             <<replace "#inventorySection">><<include "panier">><</replace>>
        <<else>>
            <<replace "#shopMessage">>Vous n'avec plus assez d'argent pour vous offrir cet objet. Il vous reste $marks marks<</replace>>
        <</if>>
    <</button>>
  <</nobr>>
* Polaroid - $prix_polaroid marks 
  <<nobr>>  
    <<button "acheter">>
        <<if $marks >= $prix_polaroid>>
            <<set $marks -= $prix_polaroid>>
            <<set $inventory.push("polaroid")>>
            <<replace "#shopMessage">>Vous avez acheté le polaroid, il vous reste $marks marks<</replace>>
            <<replace "#inventorySection">><<include "panier">><</replace>>
        <<else>>
            <<replace "#shopMessage">>Vous n'avec plus assez d'argent pour vous offrir cet objet. Il vous reste $marks marks<</replace>>
        <</if>>
    <</button>>
  <</nobr>>
* Grappin - $prix_grappin marks
  <<nobr>>
    <<button "acheter">>
        <<if $marks >= $prix_grappin>>
            <<set $marks -= $prix_grappin>>
            <<set $inventory.push("grappin")>>
            <<replace "#shopMessage">>Vous avez acheté le grappin, il vous reste $marks marks<</replace>>
            <<replace "#inventorySection">><<include "panier">><</replace>>
        <<else>>
            <<replace "#shopMessage">>Vous n'avec plus assez d'argent pour vous offrir cet objet. Il vous reste $marks marks<</replace>>
        <</if>>
    <</button>>
  <</nobr>>
 * Puce radio et récepteur - $prix_puce marks 
  <<nobr>>
    <<button "acheter">>
        <<if $marks >= $prix_puce>>
            <<set $marks -= $prix_puce>>
            <<set $inventory.push("puce et récepteur")>>
            <<replace "#shopMessage">>Vous avez acheté la puce radio et le récepteur, il vous reste $marks marks<</replace>>
            <<replace "#inventorySection">><<include "panier">><</replace>>
        <<else>>
            <<replace "#shopMessage">>Vous n'avec plus assez d'argent pour vous offrir cet objet. Il vous reste $marks marks<</replace>>
        <</if>>
    <</button>>
  <</nobr>>
* Fusil à lunettes Carcano - $prix_fusil marks 
  <<nobr>>
    <<button "acheter">>
        <<if $marks >= $prix_fusil>>
            <<set $marks -= $prix_fusil>>
            <<set $inventory.push("fusil")>>
            <<replace "#shopMessage">>Vous avez acheté le fusil à lunettes, il vous reste $marks marks<</replace>>
            <<replace "#inventorySection">><<include "panier">><</replace>>
        <<else>>
            <<replace "#shopMessage">>Vous n'avec plus assez d'argent pour vous offrir cet objet. Il vous reste $marks marks<</replace>>
        <</if>>
    <</button>>
  <</nobr>>
* Serum de vérité (Penthotal) - $prix_serum marks 
  <<nobr>>
    <<button "acheter">>
        <<if $marks >= $prix_serum>>
            <<set $marks -= $prix_serum>>
            <<set $inventory.push("serum")>>
            <<replace "#shopMessage">>Vous avez acheté le sérum de vérité, il vous reste $marks marks<</replace>>
            <<replace "#inventorySection">><<include "panier">><</replace>>
        <<else>>
            <<replace "#shopMessage">>Vous n'avec plus assez d'argent pour vous offrir cet objet. Il vous reste $marks marks<</replace>>
        <</if>>
    <</button>>
  <</nobr>>
* Antidote - $prix_antidote marks 
  <<nobr>>
    <<button "Acheter">>
        <<if $marks >= $prix_antidote>>
            <<set $marks -= $prix_antidote>>
            <<set $inventory.push("antidote")>>
            <<replace "#shopMessage">>Vous avez acheté un antidote contre les morsures de serpent, il vous reste $marks marks<</replace>>
             <<replace "#inventorySection">><<include "panier">><</replace>>
        <<else>>
            <<replace "#shopMessage">>Vous n'avec plus assez d'argent pour vous offrir cet objet. Il vous reste $marks marks<</replace>>
        <</if>>
    <</button>>
  <</nobr>>
<div id="inventorySection">
    <<include "panier">>
</div>



Il est temps à présent de [[quitter les lieux|tramway]] avec vos emplettes

```

# Deuxième passage ("panier")

```sugarcube
<<if $inventory.length > 0>>
    Voici les objets que vous avez dans votre panier:
<<nobr>>
    <<for _item range $inventory>>
        <<print _item>>
        <<if _item == "parapluie bulgare">>
            <<button "rendre le parapluie">>
                <<set $marks += $prix_parapluie>>
                <<set $inventory.delete("parapluie bulgare")>>
                <<replace "#shopMessage">>Vous avez rendu le parapluie bulgare,, il vous reste $marks marks<</replace>>
                <<replace "#inventorySection">><<include "panier">><</replace>>
            <</button>>
             <br>
        <</if>>

        <<if _item == "polaroid">>
            <<button "rendre le polaroid">>
                <<set $marks += $prix_polaroid>>
                <<set $inventory.delete("polaroid")>>
                <<replace "#shopMessage">>Vous avez rendu le polaroid, il vous reste $marks marks<</replace>>
                <<replace "#inventorySection">><<include "panier">><</replace>>
            <</button>>
           <br>
        <</if>>
        
          <<if _item == "grappin">>
             <<button "rendre la corde et le grappin">>
                <<set $marks += $prix_grappin>>
                <<set $inventory.delete("grappin")>>
                <<replace "#shopMessage">>Vous avez rendu la corde et le grappin, il vous reste $marks marks<</replace>>
                <<replace "#inventorySection">><<include "panier">><</replace>>
            <</button>>
          <br>
        <</if>>
        
         <<if _item == "puce et récepteur">>
            <<button "rendre la puce et le récepteur">>
                <<set $marks += $prix_puce>>
                <<set $inventory.delete("puce et récepteur")>>
                <<replace "#shopMessage">>Vous avez rendu la puce et le récepteur, il vous reste $marks marks<</replace>>
                <<replace "#inventorySection">><<include "panier">><</replace>>
            <</button>>
          <br>
        <</if>>
        
         <<if _item == "fusil">>
            <<button "rendre le fusil à lunette">>
                <<set $marks += $prix_fusil>>
                <<set $inventory.delete("fusil")>>
                <<replace "#shopMessage">>Vous avez rendu le fusil à lunettes, il vous reste $marks marks<</replace>>
                <<replace "#inventorySection">><<include "panier">><</replace>>
            <</button>>
           <br>
        <</if>>
        
      <<if _item == "serum">>
            <<button "rendre le sérum">>
                <<set $marks += $prix_serum>>
                <<set $inventory.delete("serum")>>
                <<replace "#shopMessage">>Vous avez rendu le serum de vérité, il vous reste $marks marks<</replace>>
                <<replace "#inventorySection">><<include "panier">><</replace>>
            <</button>>
          <br>
        <</if>>

        <<if _item == "antidote">>
            <<button "Rendre l'antidote">>
                <<set $marks += $prix_antidote>>
                <<set $inventory.delete("antidote")>>
                <<replace "#shopMessage">>Vous avez rendu l'antidote, il vous reste $marks marks<</replace>>
                <<replace "#inventorySection">><<include "panier">><</replace>>
            <</button>>
             <br>
        <</if>>
    <</for>>
   <</nobr>>
<<else>>
    Votre panier est vide
<</if>>
```

# troisième passage ("Tramway")

```sugarcube
<<nobr>>
<<if $inventory.length > 0>>
    <<for _item range $inventory>>
            <<if _item == "polaroid">><<set $polaroid to true>><</if>>
        <<if _item == "parapluie bulgare">><<set $parapluie to true>><</if>>
	  <<if _item == "grappin">><<set $grappin to true>><</if>>
	  <<if _item == "puce et récepteur">><<set $puce to true>><</if>>
	  <<if _item == "fusil">><<set $fusil to true>><</if>>
        <<if _item == "serum">><<set $serum to true>><</if>>
        <<if _item == "antidote">><<set $antidote to true>><</if>>
    <</for>>
<</if>>
<</nobr>>

Sortir du 36bis peut vous exposer, sachant que les gardes à l'entrée signalent qu'il s'agit d'un bâtiment de la Sécurité. Vous prenez un tramway, puis changez deux fois de lignes de métro en étant vigilant  aux visages qui vous environnent pour vous assurer que vous n'êtes pas suivis. 
```
$\newline$
# bibliographie
$\newline$






