---
title: raccourcisseurs de liens
subtitle: 
id: 20250317_raccourcisseurs de liens
author: Damien Belvèze
date: 2025-03-17
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - URL shortener
  - URL shorteners
  - raccourcisseur de liens
  - raccourcisseur de lien
tags:
  - réseaux_sociaux
---
# Pourquoi il ne faut pas raccourcir les liens 

(texte : Rich Kulawiec, posté sur CODE4LIB@LISTS.CLIR.ORG le 17 mars 2025)

Speaking from one infosec perspective: URL shorteners are a worst practice in  
computing.  Here's why (briefly) (very briefly) with some references below:  
  
1. Any functional piece of software should be able to handle fairly  
long URLs -- roughly: 2000 characters, which most contemporary browsers  
can handle.  (RFC 3986 doesn't specify a maximum length for URLs,  
but does set the domain part's maximum length at 255 in section 3.3.2.)  
  
2. General URL shorteners (such as those operated by various operations)  
facilitate surveillance and are subject to manipulation.  (Or they may  
*be* surveillance/manipulation, i.e., they may not be what they claim.)  
They're also impermanent: when they go away, all the links using them  
stop working -- or worse, the domain may be re-registered by a malicious  
actor so that all the links keep working, just not for their originally  
intended purposes.  They're also single-points-of-failure, which make  
them excellent targets for various kinds of attacks -- and not just  
technical ones, see one of the links below.  
  
3. Specific URL shorteners (such as those operated by a company or  
university) represent a single point of failure.  In other words,  
if a university with 8 schools and 62 departments decides to use a  
single URL shortener for the institution instead of publishing full URLs  
(which presumably would use subdomains for those schools and departments)  
then what the university has built isn't a resource: it's a target  
whose compromise allows an attacker to go after all 8 schools/62 departments  
simultaneously.  
  
4. URL shorteners discourage users from scrutinizing links before  
following them.  Some users, of course, don't do this anyway; but careful  
users stare at and evaluate URLs before using them.  Shortened links are  
inscrutable and discourage this useful/judicious habit -- in other words,  
they help train users to be victims.  Note that this problem has been  
exacerbated in recent years by the proliferation of ~1000 new TLDs  
and by the accelerating trend of very bad UI designs that obfuscate URLs,  
domains, and email addresses -- so there's plenty of blame to go around.  
  
5. I recommend permanently banning all general URL shorteners the moment  
you're aware of their existence.  Depending on context/application, this  
could mean things like using DNS RPZ to keep them from resolving, blocking  
them in HTTP proxies, etc.  I recommend not building a specific URL  
shortener and instead making judicious choices in hostnames, subdomains,  
and URL RHS strings [1] -- because doing so obviates the need for a URL  
shortener.  And finally, I recommend training users -- as much  
as possible, and that may not be much -- to never use URL shorteners.  
  
Some references/supplemental material (by no means complete):  
  
        This URL shortener situation is officially out of control - Scott Hanselman  
        [http://www.hanselman.com/blog/ThisURLShortenerSituationIsOfficiallyOutOfControl.aspx](http://www.hanselman.com/blog/ThisURLShortenerSituationIsOfficiallyOutOfControl.aspx)  
  
        Why I Don't Like URL Shorteners | Altmode  
        [https://altmode.wordpress.com/2013/10/07/why-i-dont-like-url-shorteners/](https://altmode.wordpress.com/2013/10/07/why-i-dont-like-url-shorteners/)  
  
        on url shorteners -- joshua schachter&#39;s blog  
        [http://joshua.schachter.org/2009/04/on-url-shorteners](http://joshua.schachter.org/2009/04/on-url-shorteners)  
  
        Libya Seizes URL Shortener Vb.ly | PCMag  
        [https://www.pcmag.com/archive/libya-seizes-url-shortener-vbly-255360](https://www.pcmag.com/archive/libya-seizes-url-shortener-vbly-255360)  
  
        URL Shorteners: Convenient But a Potential Security Risk | News &amp; Opinion | PCMag.com  
        [https://www.pcmag.com/news/343781/url-shorteners-convenient-but-a-potential-security-risk](https://www.pcmag.com/news/343781/url-shorteners-convenient-but-a-potential-security-risk)  
  
        Massive cybercrime URL shortening service uncovered via DNS data  
        [https://www.bleepingcomputer.com/news/security/massive-cybercrime-url-shortening-service-uncovered-via-dns-data/](https://www.bleepingcomputer.com/news/security/massive-cybercrime-url-shortening-service-uncovered-via-dns-data/)  
  
        Google URL Shortener Links Will Return a 404 Response - Slashdot  
        [https://news.slashdot.org/story/24/07/18/216211/google-url-shortener-links-will-return-a-404-response](https://news.slashdot.org/story/24/07/18/216211/google-url-shortener-links-will-return-a-404-response)  
  
---rsk  
  
[1] For instance: "projects.geology.example.edu/glacial-rebound" might be  
a project studying glacial rebound in the geology department of Example  
University, while "projects.geology.example.edu/pacific-rim" might be  
a different project studying volcanic activity on the Pacific Rim.  
These aren't particularly long URLs, they're communicative, they're  
somewhat memorizable, and they use hostnames, subdomains, and RHS URLs  
to maximize the information conveyed per character.



$\newline$
# bibliographie
$\newline$






