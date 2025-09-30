---
title: hyperparamètres
subtitle:
id: 20240912_hyperparamètres
author: Damien Belvèze
date: 2024-09-12
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---
> `n`: This parameter indicates the number of texts you would like to generate at one time in response to your prompt. Set this to “1” and the model will produce only one response to the given prompt, set this to “5” and the model will produce five responses.
- `batch_size`: In this case, adding a batch size that matches `n` allows for multiple samples to be generated simultaneously, speeding up the generation of text.
- `prompt`: This is the key component of this exercise — the `prompt` is where you can place the question to which you would like your model to respond. If this is phrased as a question, it will attempt to respond, but your prompt may also be given in the form of a phrase that you would like the model to complete and continue (e.g., “Theresa May is…”).
- `max_length`: The maximum length is the number of tokens generated in response to your prompt — essentially, the word count. GPT-2 allows for up to 1024 tokens to be generated at one time.
- `temperature`: Temperature sets how “crazy” the text generated will be by adjusting how many random completions the model allows while generating the text. At 0.7 the text generated is relatively “normal” while still remaining unique. The highest value of 1.0 results in highly random text, while values below 0.7 up until zero will result in more deterministic text that may simply parrot some of the contents from the original dataset.
- `top_p`: The `top_p` value generates a set of words related to the prompt where the total probability of these words occurring in association with the words within the prompt is greater than or equal to the value given.

(source : [[@brousseauInterrogatingNationalNarrative2022]])


$\newline$
# bibliographie
$\newline$






