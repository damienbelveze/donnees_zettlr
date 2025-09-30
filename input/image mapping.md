---
title: image mapping
subtitle: 
id: 20241210_image mapping
author: Damien Belvèze
date: 2024-12-10
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
---
Rendre une image cliquable

voir [[Twine#définir des zones cliquables sur une image]]

# html + css

## html
```html
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="image_hotspot.css">
</head>
<body>
	<div id="image-hotspot">
		<a id="the-sun" href="#the-sun">the sun</a>
		<a id="mercury" href="#mercury">mercury</a>
		<a id="venus" href="#venus">venus</a>
		<a id="earth" href="#earth">earth</a>
		<a id="mars" href="#mars">mars</a>
		<a id="jupiter" href="#jupiter">jupiter</a>
		<a id="saturn" href="#saturn">saturn</a>
		<a id="uranus" href="#uranus">uranus</a>
		<a id="neptune" href="#neptune">neptune</a>
		<!-- <a id="pluto" href="#pluto">pluto</a> -->
	</div>
</body>
```
## css

```css
#image-hotspot {
    /* backup url */
    /* background: url(https://i.sstatic.net/ajt0f.jpg); */
    background: url(http://upload.wikimedia.org/wikipedia/commons/c/c4/Planets2008.jpg);
    height: 720px;
    width: 1280px;
    position: relative;
    top: 0px;
    left: 0px;
  }
  
  #image-hotspot a#the-sun {
    display: block;
    text-indent: -10000px;
    height: 720px;
    width: 200px;
    position: absolute;
    left: 0px;
    top: 0px;
  }
  
  #image-hotspot a#mercury {
    display: block;
    text-indent: -10000px;
    height: 25px;
    width: 25px;
    position: absolute;
    left: 225px;
    top: 275px;
  }
  
  #image-hotspot a#venus {
    display: block;
    text-indent: -10000px;
    height: 75px;
    width: 40px;
    position: absolute;
    left: 265px;
    top: 250px;
  }
  
  #image-hotspot a#earth {
    display: block;
    text-indent: -10000px;
    height: 75px;
    width: 45px;
    position: absolute;
    left: 325px;
    top: 250px;
  }
  
  #image-hotspot a#mars {
    display: block;
    text-indent: -10000px;
    height: 75px;
    width: 45px;
    position: absolute;
    left: 383px;
    top: 250px;
  }
  
  #image-hotspot a#jupiter {
    display: block;
    text-indent: -10000px;
    height: 125px;
    width: 135px;
    position: absolute;
    left: 450px;
    top: 225px;
  }
  
  #image-hotspot a#saturn {
    display: block;
    text-indent: -10000px;
    height: 125px;
    width: 195px;
    position: absolute;
    left: 610px;
    top: 225px;
  }
  
  #image-hotspot a#uranus {
    display: block;
    text-indent: -10000px;
    height: 75px;
    width: 60px;
    position: absolute;
    left: 805px;
    top: 250px;
  }
  
  #image-hotspot a#neptune {
    display: block;
    text-indent: -10000px;
    height: 75px;
    width: 60px;
    position: absolute;
    left: 887px;
    top: 250px;
  }
```

## hotspots



# bibliographie