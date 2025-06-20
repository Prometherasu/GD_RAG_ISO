|Col1|Dosage ADN|Version 2.0|
|---|---|---|
|GDB_MOP_08|Extraction|19/06/2024|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT|Approbation :<br>L.LIETAR|


**Ce protocole s’adresse aux personnes habilitées à l’extraction d’ADN.**

**Mode opératoire**

Dans la salle ““Extraction ADN” :

1) préalablement :

a) allumer l’ordinateur, puis le SPARK,

_Remarque : il se peut que l’appareil ne se connecte pas au PC (lumière bleue 1 minute après_
_allumage). Dans ce cas, il faut redémarrer le PC sans éteindre l’appareil, une lumière rose_
_s’affiche après connexion._

b) sortir le Kit Picogreen stocké à 4°C contenant l’ADN témoin et le picogreen,

_Remarque : éviter l'exposition à la lumière du picogreen (sensible à la lumière)._

c) préparer du TE1X (non filtré) à partir du TE 100X si nécessaire,

2) **préparation des échantillons**

a) prévoir le nombre de plaques de dosage selon le nombre d’échantillons et les

identifier,

b) dans les plaques de dosage, dispenser **49 µL de TE1X**,

c) mettre **1 µL d’échantillon** dans chaque puits,

3) **préparation de la gamme étalon**

a) prévoir une colonne pour la gamme,

b) dispenser **12,5 µL de TE1X** dans le **puits A**, puis **50 µL de TE1X** dans les

**puits B à H**,

c) diluer l’ADN témoin* au **1/50e** dans un tube 1,5 mL : **98 µL TE1X + 2 µL ADN**

**témoin**,

d) dans le **puits A** ajouter **37,5 µL d’ADN** **dilué** et faire des up & down,

e) réaliser une **dilution en série** du **puits B à G :** dans le puits **B**, dispenser **50µL**

**d’ADN dilué**, puis faire des up & down (x10), **transférer 50µL** de ce puits **vers**
**le puits suivant C**, continuer ainsi **jusqu’en G**,

f) **en G, jeter les 50 µL** de reliquat,

1/4

|Col1|Dosage ADN|Version 2.0|
|---|---|---|
|GDB_MOP_08|Extraction|19/06/2024|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT|Approbation :<br>L.LIETAR|


g) **rien ne doit être transféré dans le puits H, contenant uniquement le TE1X**

_Remarque : * La concentration de départ de l’ADN témoin est de 100 ng/µL dans le TE. En_
_diluant, la concentration de la solution est à 2 ng/µL. En complétant la colonne de la gamme_
_sur la plaque, on obtient les concentrations suivantes :_

➔ _Puits A : 12.5 µL de TE + 37.5 µL d’ADN témoin (C=2 ng/µL) → 75 ng_

➔ _Puits B : 50 µL de TE + 50 µL d’ADN témoin → 50 ng_

➔ _Puits C : 50 µL de TE + 50 µL du puits B → 25 ng_

➔ _Puits D : 50 µL de TE + 50 µL du puits C → 12.5 ng_

➔ _Puits E : 50 µL de TE + 50 µL du puits D → 6.25 ng_

➔ _Puits F : 50 µL de TE + 50 µL du puits E → 3.125 ng_

➔ _Puits G : 50 µL de TE + 50 µL du puits F → 1.5625 ng (retirer 50 µL du mélange)_

➔ _Puits H : 50 µL de TE → 0 ng_

4) **préparer la dilution du picogreen au 1/200e**

La solution mère de Picogreen doit être diluée au 1/200e dans du TE1X, et 50 µL de la solution
de Picogreen diluée doit être dispensée dans chaque puits

a) préparer la dilution du picogreen dans un tube Falcon (15 mL, ou 50 mL selon

les besoins),

➔ pour **N dosages** à effectuer (nombre d’échantillons + gamme étalon (8 puits) + volume

mort (5 puits))

➔ le volume total de solution de Picogreen diluée à réaliser correspond à N x 50 (volume

de Picogreen dilué à dispenser par puits)

**Calcul dilution au 200** **[ème]** **: (N x 50)/200 = volume de Picogreen solution mère à diluer**

b) **homogénéiser** par retournement du tube Falcon,

c) **dispenser 50 µL de Picogreen dilué** **dans chaque puits,**

_Remarque : protéger les plaques de la lumière le temps qu’elles passent en analyse. La_
_gamme doit être analysée en premier._

5) **SPARK : lancement de l'analyse**

a) ouvrir le logiciel **SPARKCONTROL Dashboard** (étoile blanche dans rectangle

bleu) et cliquer sur la flèche à gauche,

b) choisir “ **method editor** ” → **open** → “ **plusieurs plaques** ”,

c) vérifier les paramètres suivants :

2/4

|Col1|Dosage ADN|Version 2.0|
|---|---|---|
|GDB_MOP_08|Extraction|19/06/2024|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT|Approbation :<br>L.LIETAR|


i) sélectionner l’ensemble des puits (A01-H12) et sur **Kinetic loop** :
indiquer le nombre de cycles correspondant au nombre de plaques,

ii) **Shaking** : time : 5 min (300 secondes) / mode : orbital / amplitude 1,

iii) **Fluorescence intensity** : mode : top / fluorophore : picogreen /
excitation : 485 nm / emission : 535 nm,

iv) **Show advanced settings** : flash 30, gain : optimal,

d) mettre la plaque dans l’appareil et cliquer sur **start** pour lancer,

e) lorsque la plaque a été lue, placer la seconde plaque et cliquer sur “nouvelle

plaque”,

6) **Analyse et calcul**

a) une fois toutes les plaques lues, un **fichier excel est extrait** [(1)] avec les

informations de lecture d’intensité de fluorescence,

b) associer les valeurs RFU (Relative Fluorescence Units) de la gamme étalon

avec les quantités d’ADN théoriques :

              - RFU puits A -> 75 ng,

              - RFU puits B -> 50 ng,

              - RFU puits C -> 25 ng,

              - RFU puits D -> 12,5 ng,

              - RFU puits E -> 6,25 ng,

              - RFU puits F -> 3,125 ng,

              - RFU puits G -> 1,5625 ng,

              - RFU puits H -> 0 ng,

c) insérer un graphique en nuage de points avec courbe de tendance

(visualisation de l’équation + coefficient de détermination R [2] ) pour la gamme
étalon. La courbe de régression linéaire doit présenter un R [2] supérieur ou égal
à 0,99 pour que l’analyse soit validée. Si ce n’est pas le cas, refaire le dosage
depuis le début,

d) convertir les valeurs RFU des échantillons dosés en concentrations (ng/µL) à

partir de l’équation de la courbe de tendance,

e) enregistrer si besoin et fermer le fichier ainsi que le logiciel.

_Remarque_ _: indications du SPARK_

_1) Une lumière bleue indique que l’appareil est allumé, en veille, non connecté au PC_

3/4

|Col1|Dosage ADN|Version 2.0|
|---|---|---|
|GDB_MOP_08|Extraction|19/06/2024|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT|Approbation :<br>L.LIETAR|


_2) Une lumière rose indique que l’appareil est allumé, et connecté au PC_
_3) Une lumière verte indique que l’appareil est en fonction_
_4) Une lumière orange indique que l’appareil est en attente_
_5) Une lumière rouge indique que l’appareil est en défaut, il faut l’éteindre ou le_

_débrancher, puis le rallumer_

(1) **fichier Excel SPARK** enregistré automatiquement dans : Ce PC / Disque local (C:) /

Utilisateurs / Public / Documents publics / Tecan / Sparkcontrol / Export / xlsc sous le
nom “plusieurs plaques_AAAAMMJJ_NNNNNN”







|Col1|Noms|Références /<br>Fournisseur|Conditions de stockage|
|---|---|---|---|
|Matériel|Spark|Tecan||
|Matériel|Ordinateur|Dell||
|Réactifs|Tampon TE (100X) pH<br>8.0 500 mL|348659 (Dutscher) ou<br>équivalent|Température ambiante|
|Réactifs|Quant-iT™ PicoGreen™<br>dsDNA Invitrogen|P7581 (P7589 avec<br>ADN) (Life<br>Technologies)|5°C +/- 3°C, à l’obscurité|
|Réactifs||||


**Documents associés :**

~~GDB~~ _ ~~FORM~~ _ ~~03~~ _ ~~Habilitation~~ ~~extraction~~ ~~ADN~~
~~GDB~~ _ ~~PRO~~ _ ~~06~~ _ ~~Contrôle~~ ~~de~~ ~~reproductibilité~~ ~~et~~ ~~répétab~~ i ~~l~~ i ~~té~~ de ~~l~~ a ~~ph~~ as ~~e~~ d'ex ~~tr~~ ac ~~ti~~ o ~~n~~


4/4

