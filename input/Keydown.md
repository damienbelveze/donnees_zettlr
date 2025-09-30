---
title: Keydown
subtitle: 
id: 20231128_Keydown
author: Damien Belvèze
date: 2023-11-28
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
  - css
---
Famille des keyevents

Quand on frappe une touche, cela déclenche une action (ou quand on libère une touche : keyup)

```javascript

<<script>>
// Define an array to store the history of text pieces
var textHistory = [];

// Define an array of text pieces
var textPieces = [
    { content: "This is the first part of the story. Press any key to continue.", style: "left-box" },
    { content: "This is the second part of the story. Press any key to continue.", style: "right-box" },
    { content: "This is the third part of the story. Press any key to continue.", style: "left-box" }
];

// Initialize the index to point to the first text piece
var currentIndex = 0;

$(document).keydown(function() {
    // Store the current text piece in the history array
    textHistory.push(textPieces[currentIndex]);

    // Display the history of text pieces with associated styles
    displayTextWithStyles();

    // Increment the index for the next key press
    currentIndex = (currentIndex + 1) % textPieces.length;
});

function displayTextWithStyles() {
    var styledText = textHistory.map(function(item) {
        return `<div class="${item.style}">${item.content}</div><br>`;
    });

    // Display the styled text on the screen
    $("#story").html(styledText.join("<br>"));
}
<</script>>

```

cf. Le CSS lié à ce script : 

```css
.left-box {
    background-color: #fff; /* Set the background color */
    padding: 10px; /* Add some padding for spacing */
    border: 0px solid #ccc; /* Add a border for visual separation */
    border-radius: 10px; /* Optional: Add rounded corners */
    display: inline-block; /* Display as inline-block to fit content width */
    text-align: left; /* Align the contents to the left */
}

.right-box {
    background-color: #fff; /* Set the background color */
    padding: 10px; /* Add some padding for spacing */
    border: 0px solid #ccc; /* Add a border for visual separation */
    border-radius: 10px; /* Optional: Add rounded corners */
    display: inline-block; /* Display as inline-block to fit content width */
    margin-left: 200px; /* Add space to the left of the right box */
}


```

$\newline$
# bibliographie
$\newline$






