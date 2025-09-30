---
title: scanner avec hplip
subtitle: 
id: 20250511_scanner avec hplip
author: Damien Belvèze
date: 2025-05-11
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - impression
---
commande : hp-scan

```shell
dbelveze@pr030165:~$ hp-scan

HP Linux Imaging and Printing System (ver. 3.23.12)
Scan Utility ver. 2.2

Copyright (c) 2001-18 HP Development Company, LP
This software comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to distribute it
under certain conditions. See COPYING file for more details.


-----------------
| SELECT DEVICE |
-----------------

  Num       Scan device URI                                             
  --------  ------------------------------------------------------------
  0         escl:https://192.168.1.21:443                               
  1         hpaio:/net/officejet_3830_series?ip=192.168.1.21&queue=false
  2         airscan:e0:HP OfficeJet 3830 series [7C69AE]                

Enter number 0...2 for device (q=quit) ?1
warning: No destinations specified. Adding 'file' destination by default.
Using device hpaio:/net/officejet_3830_series?ip=192.168.1.21&queue=false
Opening connection to device...

Resolution: 300dpi
Mode: gray
Compression: JPEG
Scan area (mm):
  Top left (x,y): (0.000000mm, 0.000000mm)
  Bottom right (x,y): (215.900009mm, 297.010681mm)
  Width: 215.900009mm
  Height: 297.010681mm
Destination(s): file
Output file: 
warning: File destination enabled with no output file specified.
Setting output format to PNG for greyscale mode.
warning: Defaulting to '/home/dbelveze/hpscan001.png'.

Warming up...
 

Scanning...
Reading data: [******************************************] 100%  8.5 MB     
Read 8.5 MB from scanner.
Closing device.

Outputting to destination 'file':

Done.

```



$\newline$
# bibliographie
$\newline$






