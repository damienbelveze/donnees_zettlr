---
title: How to use Tor
subtitle: show and tell (5 minutes)
id: 20230613_How to use Tor
author: Damien Belvèze
date: 2023-06-13
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: [cryptography, Tor]
---

![](images/Alice_Bob.png)

Can you all see what I have in my hand <!--showing an onion-->
And this symbolises a key, at least an encryption key. 

What is the purpose of showing you an onion if I am to tell you a bit about privacy (as announced last tuesday)? 

# Tor, how does it work?

The Onion stands for Tor (<!--spell the acronym-->) which is called The Onion Router. 

<!--first slide-->

![](images/tor_onion_layers.png)

All the cryptographic layers are special routers
![](images/Tor_onion_layers1.png)
When Alice sends a request to Bob's server, everything is encrypted so that if anybody eavedrops the message, they won't be able to use it. 

First designed by the US Navy to secure its communications and funded by US governement, Tor is now a common good, easily downloadable on your computer, that may be used by everyone to safely navigate on the web and send messages to others.

<!-- downloading the software -->

For the end-user, Tor is basically a web navigator just as Mozilla Firefox or Chrome, and it's very easy to download it from the [Torproject website](https://www.torproject.org/)whatever is your operating system. 

# What is it used for? 

Thank to Snowden, we know how massive and systematic is the online surveillance today wether it is led by corporations or States. 
Therefor, in democratic western countries, most of the people use Tor in order to send requests to commonplace servers without being tracked. As you know we all something to hide, which is our privacy which allow us to get information, to try ideas and share opinions, and prevent ourselves to be targeted by advertisers or politicians. 

I may for instance try to read The Guardian through Tor
<!-- showing the circuits -->
As you may observe, the connection to servers is a bit slower than usual, but the more Tor nodes are in use all around the world and the faster the websites will be displayed. 

My request entered the Tor circuit through a United States > Singapore > Netherlands > France : only the exit node may be recognized by authorities, that why in France for instance they are ran by associations under Law contract.

Let's assume now I live in a country where the Guardian is censored. it's still possible to circumvent this censorship by using the [guardian hidden service](https://www.guardian2zotagl6tmjucg3lrhxdk4dw3lhbqnkvvkywawy3oqfoprid.onion) also know as an onion website. 

<!-- look for guardian inurl:.onion -->

If you live in a non democratic country or even if you are citizen of a democratic country but are some kind of wistleblower, the most secure way to connect to a newspaper to get information or contact journalists is to use Tor and these hidden services. 

# governments attitude towards Tor

That would be counterproductive for me to conceal the fact that Tor may also be used by malinvolent persons to access weapons, drugs and to lead different kinds of attacks against legitimate websites, but the problem is that the Authorities tend to reduce its use to these mischievous purposes, while Tor is everyday also used to allow freedom of information and whitleblowing. Without Tor and a photograph known as Cesar, we never would have been able to measure the harm made by Bachar el Assad to the Syrian population. 

In a case happened last december involving leftist militants against whom there is absolutely no charge, their use of privacy tools such as Tor, Signal, and Linux were presented as a serious reason for their arrest. French policemen also made clear that everybody who will train people to use these tools could be considered as suspects.

# conclusion.

That's why I am here today in front of you speaking about Tor : let's not make this police narrative about those tools shape the future repressive laws. In order to empower people and emancipate them from the governements abuses, we all need to protect our privacy. If you think you do not need it for yourself, do it for the minorities, the persons who struggle against the status quo, do it for others. 

presentation here : [[Why and how to use Tor]]
















