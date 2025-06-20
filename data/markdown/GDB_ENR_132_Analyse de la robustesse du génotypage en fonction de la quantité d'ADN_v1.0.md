**i** **i**
**i**


**i** **i**
**i**


**i** **i**
**i**


**i** **i**
**i**


**i** **i**
**i**


**i** **i**
**i**

|Col1|Analyse de la robustesse du génotypage en fonction de la quantité d’ADN<br>amenée en début d’opération de génotypage|Version 1.0|
|---|---|---|
|GDB_ENR_132|SMQ|12/07/2024|
|Rédactoi n :<br>C.AUDEBERT|Vérifci atoi n :<br>L. LIETAR|Approbatoi n :<br>C. AUDEBERT|


**Analyse de la robustesse du génotypage en foncton de la quanti** **té di** **’ADN amenée en début**

**d’opératon de génotypage. i**

Il apparaît qu’une composante potentiellement critique liée à la qualité de génotypage puisse être
portée par la quantité – et donc ici la concentration – d’ADN obtenue suite à l’opération d’extraction.
En effet, Illumina recommande une concentration de 50 ng /µL. Néanmoins, eut égard aux méthodes
usuelles utilisées (méthodes reposant sur des kits pour lesquels la prise d’essai d’échantillon matriciel
biologique est relativement faible est comprise entre 100 et 300 µL de sang par exemple).

La présente étude a donc pour objet de caractériser le caractère critique de la concentration d’ADN et
d’apprécier la robustesse de la méthode en fonction de ce critère. Ainsi, 9567 échantillons réalisés
durant l’exercice 2017 sont intégrés à cette étude. Ces échantillons ont subi une extraction ADN, un
dosage par la méthode picogreen et ont subi une opération de génotypage sur puce bovine 10K. Les
valeurs de concentration d’ADN s’étendent de 13 ng/µL à 172,92 ng/µL avec une moyenne de 65,55
ng/µL et un écart moyen de 15,10 ng/µL. Le taux de CallRate inférieur au seuil de 0,95 se situe à 2,25

%.

**i** **i**
**i**


1/2

|Col1|Analyse de la robustesse du génotypage en fonction de la quantité d’ADN<br>amenée en début d’opération de génotypage|Version 1.0|
|---|---|---|
|GDB_ENR_132|SMQ|12/07/2024|
|Rédactoi n :<br>C.AUDEBERT|Vérifci atoi n :<br>L. LIETAR|Approbatoi n :<br>C. AUDEBERT|


Voici un graphique de dispersion montrant la relation entre le "Call Rate" et le "Dosage (ng/µl)".
Comme on peut le voir, il n'y a pas de tendance évidente indiquant une relation claire entre ces deux

variables.

La corrélation entre ces deux variables est de 0,096. Elle tend vers zéro et montre une absence de

liaison entre ces deux variables.

En revanche, si l’on ne s’intéresse à la liaison entre concentration ADN pour des valeurs de
CallRates < 0,95 qui est notre seuil de conformité cette corrélation passe à 0,4. Sans être très élevée
cette corrélation tend à augmenter par rapport à celle précédemment calculée. Ceci laisse à penser
que pour des génotypages non conformes (CallRate <0,95) le paramètre lié à la concentration d’ADN
extrait ait une influence plus marquée.

Cette étude rapide, sur plus de 9500 données couplant concentration et CallRate ne permet pas de
mettre en évidence un lien fort entre la concentration ADN et qualité de génotypage. A la lumière de
cette analyse, il apparaît que la concentration d’ADN amenée en entrée de phase de génotypage puisse
autoriser un grande plage de variations de concentration. Il conviendra néanmoins dans les validations
de méthodes futures d’établir des critères de performances au-delà de 15 ng/µL pour limiter des effets
« bords » pouvant impacter la qualité des génotypages produits. Pour des valeurs de concentrations
strictement inférieures à 15 ng/µL sont observées 18 % de CallRate < 0,95. Ce pourcentage tombe à 11
% pour les valeurs de concentrations comprises de 15 à 19 ng/µL. Ces taux sont très certainement
exacerbés par le fait que la politique de la plateforme GDScan assume un faible taux d’échantillons
biologiques non conformes (souhait de notre client). Il est donc possible de dresser l’hypothèse que
ces échantillons pèsent négativement sur la qualité de l’extraction et du génotypage. Néanmoins, cette
étude élargie sur un volume d’échantillons dépassant les 9500 montrent que le phénomène peut être
considéré comme marginal.

2/2

