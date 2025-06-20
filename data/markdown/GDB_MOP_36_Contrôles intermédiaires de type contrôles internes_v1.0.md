|Col1|Contrôles intermédiaires de type<br>contrôles internes|Version 1.0|
|---|---|---|
|GDB_MOP_36|SMQ|12/09/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>K. LE ROUX, M. BARBET|Approbation :<br>C. AUDEBERT|


**Ce protocole s’adresse aux personnes habilitées à l’extraction et/ou au génotypage**
**concernées par le suivi des appareils contrôlés en interne dans le cadre de leurs**
**missions (se référer au document GDB_ENR_63_Gestion du personnel).**

Ce mode opératoire concerne les appareils de niveau de criticité C2 contrôlés en interne, dont
le récapitulatif, incluant la périodicité des contrôles, figure dans le document
GDB_FI_31_Récapitulatif appareils suivis en contrôle interne.
Sur chacun de ces appareils figure la(les) valeur(s) de consigne en état de fonctionnement,
la(les) valeur(s) de réglage de l’appareil, ainsi que les EMT (informations figurant également
dans les fiches de vie) à respecter pour effectuer le contrôle interne.
Les valeurs mesurées sont à reporter dans les fiches de vie correspondantes.
Pour ce qui nous concerne, cela comprend différentes grandeurs telles que la température, la
conductivité, la vitesse de rotation, le volume et le temps.

**Mode opératoire**

_Remarque : attention, s’assurer que l’appareil n’est pas, et ne sera pas utilisé au cours de_
_l’opération._
_Remarque : s’assurer que la date d’étalonnage des appareils de mesure servant à réaliser les_
_contrôles internes est valide._

**1) Mesurage de la température, à l’aide d’une sonde individuelle filaire**

Dans la salle où se situe l’appareil :

a) Allumer l’appareil et le régler pour le contrôle.
b) Disposer l’embout de la sonde au centre de l’appareil (au fond d’un puits

concernant les incubateurs à microplaques).
_Remarque : dans le cas d’une cartographie réalisée en interne d’autres points_
_supplémentaires seront contrôlés, se référer à la fiche de vie, onglet_
_cartographie)._
c) Après 15 minutes de stabilisation :

           - Allumer le thermomètre,

           - Relever la température,

           - Reporter la valeur mesurée dans la fiche de vie.
d) En cas de contrôle interne non valide, différentes actions peuvent être

effectuées (se référer au 5.4.4. Non conformités / dysfonctionnements des
appareils de la procédure GDB_PRO_29_Gestion des équipements), comme
un ajustage de la température de réglage de l’appareil.

1/7

|Col1|Contrôles intermédiaires de type<br>contrôles internes|Version 1.0|
|---|---|---|
|GDB_MOP_36|SMQ|12/09/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>K. LE ROUX, M. BARBET|Approbation :<br>C. AUDEBERT|


Dans ce cas, il conviendra de veiller à ce que la valeur de réglage de l’appareil
dans la fiche de vie ainsi qu’au niveau de l’étiquetage de l’appareil soit mise à
jour.

Cas particuliers : certains contrôles internes sont effectués différemment du présent mode
opératoire, ils sont :

   - Réalisés en automatique pour nos salles et enceintes thermostatiques critiques (C2 et
C3), via une centrale de surveillance des températures : VIGITEMP (logiciel VIGITEMP
10), reliée à des sondes, installées par un technicien spécialisé. Elles effectuent des
relevés toutes les 15 minutes (toutes les heures en mode mémoire, en cas de défaut,
sur une amplitude de 48h, puis écrasement de la mesure la plus ancienne). Une alarme
se déclenche après 4 mesures en dehors des EMT définis.
L’intervention du personnel n’a lieu qu’en cas d’alarme.
Dans ce cas, il faudra vérifier l’origine de l’écart (ex : porte congélateur restée trop
longtemps ouverte, problème de climatisation, etc…) et acquitter l’alarme sur le logiciel
en précisant le motif de l’écart, sa résolution, toute autre information utile, et, pour les
sessions logiciel communes (EXTRACTION et POST-PCR), les initiales de la
personne ayant traité l’alarme.
Lorsque le risque d’impact sur les résultats qui découle de cet écart est nul à faible,
tout étant tracé dans le logiciel, ce mode opératoire se substitue au remplissage du
fichier GDB_ENR_72_Gestion des incidents et des non-conformités.
Cependant, pour le reste de la gestion de cet écart ou en cas de risque d’impact moyen
à fort, il faudra se référer au 5.4.4. Non conformités / dysfonctionnements des appareils
de la procédure GDB_PRO_29_Gestion des équipements.

   - Réalisés et tracés lors des analyses de génotypage pour les fours et le bain circulant
chauffant/réfrigérant. Il s’agit de mesurages de températures effectués à l’aide de

sondes individuelles :

      Filaire min/max, installées sur chaque four (sonde disposée au plus près du
centre de l’appareil) afin de contrôler les variations de température durant les
périodes d’incubation.
Lors des incubations, une fois que le four a atteint la température de consigne,
réinitialiser le min et le max en appuyant sur « min reset » et « max reset ». A
l’issue de la période d’incubation, relever les valeurs min et max mesurées et
les reporter dans le formulaire de suivi des génotypages
GDB_FORM_16_Génotypage Infinium Illumina - Tracking form de l’analyse en

cours,

      Spécifique, à disposer sur l’incubateur de puces à ADN (Te-flow) relié au bain
circulant (milieu/à droite des lames pour éviter l’accrochage du câble par les
aiguilles du robot pipeteur) lors de chaque utilisation. Lors de chaque

2/7

|Col1|Contrôles intermédiaires de type<br>contrôles internes|Version 1.0|
|---|---|---|
|GDB_MOP_36|SMQ|12/09/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>K. LE ROUX, M. BARBET|Approbation :<br>C. AUDEBERT|


incubation, effectuer un mesurage en début et fin d’incubation. Reporter les
valeurs mesurées dans le formulaire de suivi des génotypages
GDB_FORM_16_Génotypage Infinium Illumina - Tracking form de l’analyse en

cours.

En cas de contrôle interne non valide, différentes actions peuvent être effectuées (se
référer au 5.4.4. Non conformités / dysfonctionnements des appareils de la procédure
GDB_PRO_29_Gestion des équipements), comme un ajustage de la température de
réglage de l’appareil.
Dans ce cas, il conviendra de veiller à ce que la valeur de réglage de l’appareil dans la
fiche de vie ainsi qu’au niveau de l’étiquetage de l’appareil soit mise à jour.

**2) Mesurage de la conductivité de l’eau pure produite par la station d’eau purifiée,**

**à l’aide d’un conductimètre**

Dans la salle « Post-PCR génotypage » :

a) Vérifiez que le mode de relevé Conductivité du conductimètre est sélectionné

(appuyer sur Mode pour passer d’un mode à l’autre).
b) Sélectionner une bouteille d’eau purifiée par la station d’eau purifiée et

autoclavée (présente dans la pièce depuis au moins 2h (à température
ambiante), et non entamée).
c) Rincer la cellule à l’eau distillée (ou directement avec l’eau pure à contrôler)

puis la plonger dans la bouteille et appuyer sur Read pour lancer la mesure.
Le signe décimal clignote.
L'écran indique la conductivité de l'échantillon.

Lorsque le signal est stable, l'écran se fige, s'affiche et le point décimal
s'arrête de clignoter.
e) Reporter la valeur mesurée dans la fiche de vie.
f) Sécher la sonde précautionneusement, sans toucher la cellule de détection. La

ranger dans le placard n° 8 (à l’abri de la lumière).
g) En cas de contrôle interne non valide, différentes actions peuvent être

effectuées (se référer au 5.4.4. Non conformités / dysfonctionnements des
appareils de la procédure GDB_PRO_29_Gestion des équipements).
Un ajustage de l’appareil n’est pas possible.

**3) Mesurage de la vitesse de rotation, à l’aide d’un tachymètre optique**

Dans la salle où se situe l’appareil :

a) Allumer l’appareil et le régler pour le contrôle.

3/7

|Col1|Contrôles intermédiaires de type<br>contrôles internes|Version 1.0|
|---|---|---|
|GDB_MOP_36|SMQ|12/09/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>K. LE ROUX, M. BARBET|Approbation :<br>C. AUDEBERT|


b) Allumer le tachymètre et effectuer le zéro :

        - Disposer le tachymètre au-dessus de l’appareil en visant le repère présent
sur l’appareil,
_Remarque : pour une centrifugeuse, le couvercle doit être fermé, viser à_

_travers le hublot._

        - Régler la hauteur du tachymètre jusqu’à l’obtention d’un point lumineux net.
c) Démarrer l’appareil et effectuer 3 mesurages de vitesse :

        - Attendre que l’appareil soit stabilisé à la vitesse désirée,

        - Appuyer sur le bouton hold pour prendre une mesure,

        - Reporter la valeur mesurée dans la fiche de vie,

        - Repartir de l’étape b) pour chaque mesure.
d) En cas de contrôle interne non valide, différentes actions peuvent être

effectuées (se référer au 5.4.4. Non conformités / dysfonctionnements des
appareils de la procédure GDB_PRO_29_Gestion des équipements), comme
un ajustage de la vitesse de réglage de l’appareil.
Dans ce cas, il conviendra de veiller à ce que la valeur de réglage de l’appareil
dans la fiche de vie ainsi qu’au niveau de l’étiquetage de l’appareil soit mise à
jour.

**4) Mesurages des volumes distribués par le robot pipeteur, à l’aide d’une pipette**

Dans la salle « Post-PCR génotypage » :

a) Allumer le robot pipeteur puis l’ordinateur.
b) Démarrer le logiciel Tecan et s’identifier avec login et mot de passe.
c) Sélectionner “Edit an existing script”, puis Start et choisir le programme

“Controle_interne_Tecan”.
d) Effectuer un rinçage et une purge des aiguilles : sur le logiciel, dans la partie

“Control Bar”, cliquer sur l’onglet “COMMANDS”, puis sur “Flush”. La fenêtre
“Flush Tips” s’ouvre, cliquer sur “START Flushing Tips” et valider l’étape
d’initialisation du positionnement des aiguilles.
e) Placer les 24 tubes de 15 mL prévus à cet effet (tubes annotés aiguille/volume,

portoir “tubes métrologie Tecan”), ouverts, sur les portoirs de tubes du plan de
travail du robot pipeteur :

        - 1 [ère] rangée : positions 1, 3, 5, 7, 9, 11, 13, 15,

        - 2 [ème] rangée : positions 1, 3, 5, 7,

        - 3 [ème] rangée : positions 1, 3, 5, 7, 9, 11, 13, 15,

        - 4 [ème] rangée : positions 1, 3, 5, 7,
en respectant les annotations sur les tubes selon le schéma suivant :

4/7

|Col1|Contrôles intermédiaires de type<br>contrôles internes|Version 1.0|
|---|---|---|
|GDB_MOP_36|SMQ|12/09/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>K. LE ROUX, M. BARBET|Approbation :<br>C. AUDEBERT|


f) Dans un réservoir Tecan type XC3, verser environ 20 mL d’eau pure autoclavée

et le positionner à l'emplacement dédié sur le plan de travail du robot pipeteur.
g) Sur l’ordinateur, cliquer sur ► Run, la fenêtre “Runtime controller” s’ouvre,

cliquer sur Run, vérifier et valider le positionnement des tubes.
_Remarque : veiller au bon démarrage du programme en étant prêt à cliquer sur_
_le bouton pause de l’interface, en cas de problème, cela permettra d’intervenir_
_sur le robot puis de relancer le programme._
h) Une fois le programme exécuté, récupérer les tubes en veillant à repérer à

quelle aiguille ils correspondent (voir schéma ci-dessus), et vérifier les volumes
dispatchés à l’aide d’une pipette étalonnée COFRAC :

   - Les deux premières rangées de tubes correspondent aux 150 µL distribués
3 fois pour chaque aiguille :

     - aiguille 1 en positions 1 et 9,

     - aiguille 2 en positions 3 et 11,

     - aiguille 3 en positions 5 et 13,

     - aiguille 4 en positions 7 et 15,

   - Les 3 [e] et 4 [e] rangées de tubes correspondent aux 300 µL distribués 3 fois
pour chaque aiguille, de la même façon :

     - aiguille 1 en positions 1 et 9,

     - aiguille 2 en positions 3 et 11,

     - aiguille 3 en positions 5 et 13,

     - aiguille 4 en positions 7 et 15.
e) Reporter les valeurs mesurées dans la fiche de vie.
f) Vider ensuite les 24 tubes, les faire sécher, les refermer et les stocker sur le

portoir dédié “tubes métrologie Tecan" pour la prochaine mesure de métrologie.

5/7

|Col1|Contrôles intermédiaires de type<br>contrôles internes|Version 1.0|
|---|---|---|
|GDB_MOP_36|SMQ|12/09/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>K. LE ROUX, M. BARBET|Approbation :<br>C. AUDEBERT|


g) En cas de contrôle interne non valide, différentes actions peuvent être

effectuées (se référer au 5.4.4. Non conformités / dysfonctionnements des
appareils de la procédure GDB_PRO_29_Gestion des équipements). Il faudra
notamment évaluer la possibilité d’effectuer des réglages pour atteindre les
volumes de consigne.

**5) Mesurage du temps, à l’aide du service de l’horloge parlante**

A partir d’un ordinateur, sur le site internet horlogeparlante.com, vérifier l’intervalle de
temps écoulé :

a) Déclencher le minuteur de 0 (sur l’écran affichant l’heure) en relevant l’heure

de l’horloge parlante.
b) Au bout du temps de consigne écoulé sur celle-ci, stopper le minuteur et relever

le temps écoulé sur celui-ci.
c) Reporter la valeur mesurée dans la fiche de vie.
d) En cas de contrôle interne non valide, différentes actions peuvent être

effectuées (se référer au 5.4.4. Non conformités / dysfonctionnements des
appareils de la procédure GDB_PRO_29_Gestion des équipements).
Un ajustage de l’appareil n’est pas possible, cependant le changement des
piles peut suffire à corriger l’écart.



|Col1|Noms|Conditions de stockage|
|---|---|---|
|Matériel|Enceintes thermostatiques critiques C2 et C3||
|Matériel|Salles critiques (Extraction, Post-PCR<br>Génotypage, Stockage)||
|Matériel|Centrale de surveillance des températures -<br>VIGITEMP + logiciel VIGITEMP 10||
|Matériel|Fours - Illumina/VWR - Hybridization oven||
|Matériel|Thermomètre min/max – Fisherbrand - Jumbo<br>traceable||
|Matériel|Bain circulant chauffant/réfrigérant - VWR -<br>1167P||
|Matériel|Thermocouple + sonde spécifique Te-flow -<br>OMEGA - 869C||
|Matériel|Agitateur chauffant - LabNet - Vortemp 56||
|Matériel|Incubateur à microplaque - SciGene - Hybex||
|Matériel|Thermocouple + sonde filaire - Hanna<br>Instruments - HI935003||


6/7

|Col1|Contrôles intermédiaires de type<br>contrôles internes|Version 1.0|
|---|---|---|
|GDB_MOP_36|SMQ|12/09/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>K. LE ROUX, M. BARBET|Approbation :<br>C. AUDEBERT|





|Col1|Station eau purifiée - AquaPart / Pro Life -<br>OMC-LAB|Col3|
|---|---|---|
||Conductimètre - Mettler Toledo - FiveGo F3 +<br>électrode LE703 IP67|À l’obscurité|
||Centrifugeuse de paillasse - Eppendorf -<br>Minispin plus||
||Plateforme d’agitation - Illumina - High speed<br>microplate shaker||
||Tachymètre - Fisherbrand - 02-401-3 /<br>11744276||
||Robot pipeteur - Tecan - Freedom EVO||
||Pipette monocanal P1000||
||Minuteurs||
|Consommables|Tubes 15 mL||
|Réactifs|Eau distillée en bouteille|Température ambiante (placard n°8)|
|Réactifs|Eau pure autoclavée|Température ambiante (paillasse<br>génotypage)|


**Documents associés :**

GDB_ENR_63_Gestion du personnel
GDB_PRO_29_Gestion des équipements
GDB_FI_31_Récapitulatif appareils suivis en contrôle interne
Fiches de vie de type : GDB_ENR_XX_Fiche de vie_GDD-APPAREIL-000
GDB_FORM_16_Génotypage Infinium Illumina - Tracking form
GDB_MOP_37_Etalonnage interne conductimètre GDD-CONDUC-001
GDB_PRO_08_Gestion des incidents et non-conformités
GDB_ENR_72_Gestion des incidents et des non conformités
GDB_FORM_01_Fiche de non conformité
GDB_FI_19_Affiche matériel HORS SERVICE
GDB_FI_59_Affiche matériel NON CONFORME


7/7

