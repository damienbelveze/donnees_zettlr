---
title: inclure des font-awesome dans des documents markdown
subtitle: 
id: 20250329_inclure des font-awesome dans des documents markdown
author: Damien Belvèze
date: 2025-03-29
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
---
inclure des fa-icons dans des documents markdown en vue d'une conversion en html avec [[Pandoc]]. 

```markdown
---
title: Font Awesome Animated Icons
description: Example of Font Awesome animated icons in markdown
---
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/js/all.min.js"></script>
<script>
console.log('Font Awesome CSS linked:', document.querySelector('link[rel="stylesheet"][href*="all.min.css"]'));
console.log('Font Awesome JS linked:', document.querySelector('script[src*="all.min.js"]'));
function animateIcon() {
const icon = document.querySelector('.fa-icon-name');
icon.classList.add('fa-spin');
}
animateIcon();
</script>

### Font Awesome Animated Icons

#### Icon 1

<span class="fa fa-spinner fa-spin" style="font-size: 24px;"></span>

#### Icon 2

<span class="fa fa-circle-notch fa-spin" style="font-size: 24px;"></span>
  
#### Icon 3

<span class="fa fa-spinner fa-spin" style="font-size: 24px;"></spa
```

commande pandoc : 
```shell
pandoc -s -t html -o fa_icons.html fa_icons.md
```

Il est possible de mettre à part tout le code qui se situe sous le frontmatter et au dessus du corps du texte dans un fichier javascript et de faire appel à ce fichier js dans l'entête du document en markdown : 

```yaml
title: "Font Awesome Animated Icons"
description: "Example of Font Awesome animated icons in markdown"
customjs:
	- script.js
```

Si dans cette dernière disposition, les icones ne s'affichent pas, faire un lien dans le frontmatter [[YAML]] avec le [[CSS]] des font-awesomes icons : 

```markdown

---
title: "Font Awesome Animated Icons
description: Example of Font Awesome animated icons in markdown"
customjs:
	- script2.js

header-includes:
	- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
---

### Font Awesome Animated Icons

#### Icon 1

<span class="fa fa-spinner fa-spin" style="font-size: 24px;"></span>

#### Icon 2

<span class="fa fa-circle-notch fa-spin" style="font-size: 24px;"></span>

#### Icon 3

<span class="fa fa-spinner fa-spin" style="font-size: 24px;"></span>

#### hearbeat

<span class="fa fa-circle-plus fa-beat" style="font-size: 24px;"></span>
```

le script script2.js sera le suivant : 

```javascript
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
<script>
console.log('Font Awesome CSS linked:', document.querySelector('link[rel="stylesheet"][href*="all.min.css"]'));

function animateIcons() {
// Select all icons with specific classes (you can add more classes if needed)
const icons = document.querySelectorAll('.fa-spinner, .fa-circle-notch, .fa-heart, .fa-circle-plus');
// Loop through each icon and add animation classes
icons.forEach(icon => {
icon.classList.add('fa-spin', 'fa-beat');

});

}

// Ensure DOM is loaded before running the animation
document.addEventListener("DOMContentLoaded", animateIcons);
</script>
```

voir les documents suivants : 

- <a href="scripts/animated_font_awesome/fa_icons2.md" download>document markdown</a>
- <a href="scripts/animated_font_awesome/script2.js" download>fichier javascript</a>
- <a href="scripts/animated_font_awesome/fa_icons2.html">résultat</a>


$\newline$
# bibliographie
$\newline$






