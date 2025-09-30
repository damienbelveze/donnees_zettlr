
<<silently>> ... <</silently>>
(éviter de générer des espaces blancs là où il y a du script)



<audio id="audioPlayer" controls>
  <source src="sons/bruit_restaurant.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<<if $pseudo_feminin eq true>>
    <<set $prp to "elle">>
    <<set $prp2 to "e">>
    <<set $prp3 to "celle-ci">>
    <<set $prp4 to "ve">>
    <<set $prp5 to "ère">>
<<elseif $camille_masculin>>
    <<set $prp to "il">>
    <<set $prp2 to "">>
    <<set $prp3 to "celui-ci">>
    <<set $prp4 to "f">>
    <<set $prp5 to "er">>
 <<else>>
        <<set $prp to "elle">>
   		<<set $prp2 to "e">>
    	<<set $prp3 to "celle-ci">>
    	<<set $prp4 to "ve">>
<</if>>

<<if $admin eq 4672 >>[[admin1|médias]]<</if>>
<<if $admin eq 4672 >>[[admin2|dialogues]]<</if>>

@@color:black;
Lundi 20 janvier, à la caféteria du département de sciences environnementales. C'est "blue monday", c'est à dire en théorie le jour le plus déprimant de l'année et il faut bien dire que ça ne commence pas très fort pour toi. Tu étais déjà bien déprimé$prp2, et voilà qu'il se met à pleuvoir  dehors ; la machine à café est en panne et surtout tu viens de recevoir un mauvais signal de l'un de tes enseignants. 
Arnold, un étudiant du même groupe que le tien avance à grands pas vers toi ; lui semble plutôt sous pression, limite excité.
@@

<<script>>
// Define an array to store the history of text pieces
var textHistory = [];

// Define an array of text pieces
var textPieces = [
    { content: "Hey salut  ! T’as déposé sur l’espace cours de Madame Green ton devoir sur les microplastiques ?", style: "left-box" },
    { content: "Oui, je l’ai déposé, mais je ne comprends pas, j’ai reçu un mail de la prof pour me dire que le logiciel anti-plagiat de l’université, Plagiator, avait détecté du plagiat sur mon devoir.", style: "right-box" },
    { content: "Ah bon, mais qu’est-ce que ça veut dire ? Tu as copié ou tu n’as pas cité tes sources ? Mais alors, tu n’auras pas la moyenne ?", style: "left-box" },
    { content: " Je ne sais pas trop, la prof me laisse 24 heures pour me rattraper et retravailler le devoir.", style: "right-box" },
    { content: "Ouah, le stress. Tu vas devoir refaire tout le travail en fait ? J'aimerais pas être à ta place...", style: "left-box" },
    { content: "Oui, bon si tu n'as rien de plus constructif à me dire, autant qu'on en reste là... Merci beaucoup, je suis bien flippé.e maintenant.", style: "right-box" },
    { content: " Attends je voulais pas en rajouter, mais c'est vrai que c'est chaud et il te reste plus beaucoup de temps. Tiens, je pense que, tu devrais en parler à Camille. C'est LA personne qui pourrait t'aider à gérer ça. Sur un truc de ce genre, je l'ai fait l'an dernier et ça m'a carrément sauvé la mise.", style: "left-box" },
    { content: "Ouais, merci pour le tuyau; je vais voir." , style: "right-box"},,
    { content: "Tu me tiens au courant ? ", style: "left-box" },
    { content: "Ouais, sûr, salut." , style: "right-box"},
];

// Initialize the index to point to the first text piece
var currentIndex = 0;

$(document).keydown(function() {
	 // Check if it's the last text piece
    if (currentIndex < textPieces.length - 1) {
    
    // Store the current text piece in the history array
    textHistory.push(textPieces[currentIndex]);

    // Display the history of text pieces with associated styles
    displayTextWithStyles();

    // Increment the index for the next key press
    currentIndex = (currentIndex + 1) % textPieces.length;
} else {
 // If it's the last text piece, stop the keydown event listener
        $(document).off('keydown');

        // Display the final text with a link to another passage
        $("#story").html("fin du dialogue");
    }

    // Scroll to the bottom of the page
    window.scrollTo(0, document.body.scrollHeight);
});

function displayTextWithStyles() {
    var styledText = textHistory.map(function(item) {
        return `<div class="${item.style}">${item.content}</div><br>`;
    });

    // Display the styled text on the screen
    $("#story").html(styledText.join("<br>"));
}

<</script>>

