
![](date_format.png)

[[Zotero]] utilise la norme ISO 8601, norme généralement utilisée en informatique : 

2021-11-09T14:12:39.572Z
YYYY-MM-DD | T(ime)HHMMSS Z = Zulu time (UTC)

2021-11-09T14:12:39.572+04
+04 = UTC+4

![](images/iso_date.png)

# Unix epoch

nombre de secondes qui se sont écoulées depuis le 1er janvier 1970 - temps de référence pour les systèmes informatiques UNIX : 

> The UNIX epoch is a time reference point that denotes the precise moment at 00:00:00 Coordinated Universal Time (UTC) on 1 January 1970. In UNIX-based systems, time is often represented as the total number of seconds that have transpired since this specific moment. This convention is widely used in computing for time-stamping and date-time representations.

(https://www.swhid.org/specification/v1.1/3.Terms_and_definitions/#310-unix-epoch)

# Gérer les formats de date avec R

package Lubridate pour [[R (logiciel)|R]]

```r
# supposons que df$Date se présente de la manière suivante : 2023-01-24 00:00:00
library(dplyr)
library(lubridate)
annee <- ymd_hms(df$Date)
annee <- lubridate::year(annee)
df <- df %>% 
  mutate(annee=paste(annee))
# ajoute une colonne "année" à df avec juste l'année (2023) gâce à la fonction year de lubridate et la fonction mutate de dplyr

```