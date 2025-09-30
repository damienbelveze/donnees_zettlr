---
title: comment chiffrer ses mails
subtitle: utiliser maivelope
---
ajouter l'extension mailvelope au navigateur : 
cliquer sur *retirer*, puis sur *installer pour Firefox*

		épingler l'extension pour la faire apparaître dans la barre d'outils du navigateur (pièce-puzzle, engrenage > ajouter à la barre d'outils)


cliquer sur l'extension
cliquer sur *Commençons*
cliquer sur générer une clé

Nom : Marin Belvèze
mail : marin.belveze@telemak.fr

saisir une phrase de passe
*créer une phrase de passe dans Clipperz.is et l'utiliser ici*

Cela génère un jeu de clé. 
Un jeu de clé comporte : 

- une clé publique qui sera accessible à d'autres (à tous ou à ceux avec qui on veut correspondre)
- une clé privée qui ne doit jamais être donnée à quiconque et qu'il faut protéger. 

ta clé publique permet aux autres de chiffrer des messages que tu vas pouvoir déchiffrer avec ta clé privée. 
Ta clé privée, en plus de déchiffrer les messages qui te sont adressés et ont été chiffrés à ton intention avec ta clé publique vont aussi permettre de démontrer que c'est bien toi qui envoie des messages chiffrés à un.e correspondant.e et pas quelqu'un.e qui se fait passer pour toi. 

une clé publique comporte les éléments suivants : 
- un identifiant
- un algorithme de chiffrement (RSA par exemple)
- une longueur de clé (4096 = 4096 bits)
- une empreinte (=fingerprint), par exemplel l'empreinte de la clé publique Alicia Lancet est 4EA0 668F EA00 2AAB 2A50 80EF FA0B FC6C D2EC B0E4 (le compte d'Alicia Lancet (lancetalicia@gmail.com existe, mais Alicia Lancet n'existe pas, je l'ai inventée))

Un message t'indique que ta clé publique n'a pas vraiment été rendue publique, pour qu'elle le soit, il faut synchroniser ton jeu de clés à peine créé avec le serveur de mailvelope, ce qui permettra à n'importe qui de trouver ta clé publique depuis ce serveur ou bien un autre serveur de clés avec lequel mailvelope est en contact. 
Rendre ta clé publique accessible encore une fois, permet à tout le monde de t'envoyer des mails chiffrés, donc sécurisés, inviolables par des personnes qui auraient accès à ta boîte mail ou celle de ton correspondant. 

clique sur *synchroniser*

![](images/mailvelope1.png)cela envoie un message chiffré sur la messagerie qui a permis la création du jeu de clé (en l'occurrence ici celui d'Alicia Lancet lancetalicia@gmail.com)

![](images/mailvelope2.png)Il faut entrer la phrase de passe choisie pour afficher un message chiffré reçu automatiquement. 

Le message une fois déchiffré dira à peu près ceci : 

>   please verify your email address [lancetalicia@gmail.com](mailto:lancetalicia@gmail.com) by clicking on the following link: ss, your public key is available in our key directory.  
  
You can find more info at [keys.mailvelope.com](https://keys.mailvelope.com).  
  
Greetings from the Mailvelope Team

confirmer le compte et l'envoi de la clé publique vers les serveurs de clés publiques à commencer par celui de mailvelope. 

