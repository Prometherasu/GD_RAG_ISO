|Col1|Système de Gestion des données de<br>génotypage|Version 1.1|
|---|---|---|
|GDB_PRO_04|SI|28/08/2023|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G. EVEN|Approbation :<br>C. AUDEBERT|


**1.** **OBJECTIFS ET CHAMP D’APPLICATION**

Ce document décrit le cheminement des données de génotypage au travers des différents
serveurs ainsi que leurs stockages et sauvegardes une fois l’analyse terminée par le scanner
ISCAN.

**2.** **DEFINITIONS / ABREVIATIONS**

**3.** **TEXTE DE RÉFÉRENCE**

La présente procédure tient compte des exigences de la norme NF EN ISO/IEC 17025.

**4.** **PERSONNEL CONCERNÉ**

Personnel habilité à l’analyse/transmission des résultats de génotypage
Responsable SI
Responsable Bio-informatique

**5.** **DESCRIPTION DES** **OPÉRATIONS EN SITUATION NORMALE DE**

**FONCTIONNEMENT**
# **5.1 Description du trajet des données**

Une fois les lames scannées, les données brutes du PC ISCAN,  (RAW scans, dmap...) sont
transférées sur le serveur NAS GNA2GDLABO.

Ces données sont ensuite lues par le logiciel génome studio sur un poste de technicien de
labo pour générer les données raffinées de génotypages sous forme de 3 fichiers, TYP et
COM, CORRES.

Ces fichiers sont ensuite déposés sur le serveur NAS GNA2GDLABO. Ils sont ensuite lus par
le serveur de calcul GSPP2GDLAB qui va découper les données par animal et mettre à jour
la base de données.

Les données sont ensuite disponibles et utilisables en production.
# **5.2 Description générale des serveurs **

**5.2.1 GSPP2GDLAB**

Le serveur GSPP2GDLAB est un serveur de calcul, il héberge les données et base de
données de production, il traite les données et génère les résultats.

1/7

|Col1|Système de Gestion des données de<br>génotypage|Version 1.1|
|---|---|---|
|GDB_PRO_04|SI|28/08/2023|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G. EVEN|Approbation :<br>C. AUDEBERT|


Le serveur GSPP2GDLAB est en raid 5 (+1), avec un disque en 'hot spare' pour assurer au
maximum la continuité de service.

Il est **synchronisé** tous les jours sur le serveur NAS GNA2GDLABO et les bases de données
sont également **sauvegardées** quotidiennement.

Il est hébergé à Douai dans la salle serveur de la société Synelia.

**5.2.2 GNA2GDLABO & GNA1GDLABO**

Les NAS GNA2GDLABO et GNA1GDLABO ne servent qu’aux stockages des données brutes,
et aux sauvegardes, aucun calcul n’est effectué par ceux-ci.
Le serveur NAS GNA2GDLABO est en raid 5 (+1), avec un disque en 'hot spare'.

Il est hébergé à Douai dans la salle serveur de la société Synelia.

Il est **répliqué** chaque jour sur un serveur jumeau en tous points GNA1GDLABO.

Le serveur NAS GNA1GDLABO est en raid 5 (+1), avec un disque en 'hot spare'.

Il est hébergé à Paris dans une salle serveur de la société Equinix.

Gènes diffusion dispose des droits d’administrateur sur ces 3 serveurs.

**5.3 Identifications des serveurs permettant la gestion des**
**enregistrements**

|Nom|Modèle|Emplacement|
|---|---|---|
|GSPP2GDLAB|DELLEMC R340|Douai Salle Serveur Synelia|
|GNA2GDLABO|QNAP TS-853DU-RP|Douai Salle Serveur Synelia|
|GNA1GDLABO|QNAP TS-853DU-RP|Paris EQUINIX|



2/7

|Col1|Système de Gestion des données de<br>génotypage|Version 1.1|
|---|---|---|
|GDB_PRO_04|SI|28/08/2023|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G. EVEN|Approbation :<br>C. AUDEBERT|


**5.3.1 GSPP2GDLAB - Caractéristiques**

|Col1|GSPP2GDLAB.genesdiffusion.com|
|---|---|
|Modèle|DELLEMC R340|
|Système|Ubuntu 20.04|
|Processeur|Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz|
|Mémoire|64GO|
|Stockage|RAID 5 + 1|
||/dev/sda1 512MO Système EFI|
||/dev/sda2 14TO Système de fichiers Linux|
|Emplacement|Douai (Synelia)|



**5.3.2** **GNA2GDLABO - caractéristiques**


3/7

|Col1|Système de Gestion des données de<br>génotypage|Version 1.1|
|---|---|---|
|GDB_PRO_04|SI|28/08/2023|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G. EVEN|Approbation :<br>C. AUDEBERT|


|Col1|GNA2GDLABO.genesdiffusion.com|
|---|---|
|Modèle|QNAP TS-853DU-RP|
|Stockage|RAID 5 + 1|
||43TO|
|Emplacement|Douai (Synelia)|


**5.3.3** **GNA1GDLABO - caractéristiques**

|Col1|GNA1GDLABO.genesdiffusion.com|
|---|---|
|Modèle|QNAP TS-853DU-RP|
|Stockage|RAID 5 + 1|
||43TO|
|Emplacement|Paris (Equinix)|

# **5.4  Accessibilité des enregistrements **

Données brutes :


4/7

|Col1|Système de Gestion des données de<br>génotypage|Version 1.1|
|---|---|---|
|GDB_PRO_04|SI|28/08/2023|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G. EVEN|Approbation :<br>C. AUDEBERT|


Stockées sur GNA2GDLABO et GNA1GDLABO

Données enregistrements en Base de données :
Accessible sur GSPP2GDLAB
# **5.5 Gestion des sauvegardes et durée de conservation **

Données brutes :

Stockées sur GNA2GDLABO et dupliquées sur GNA1GDLABO (toutes les 24h)
Durée de conservation : Minimum 5 ans

Données enregistrements en Base de données :
Sauvegardées sur GNA2GDLABO et dupliquées sur GNA1GDLABO (toutes les 24h)
Durée de conservation : Minimum 5 ans


5/7

|Col1|Système de Gestion des données de<br>génotypage|Version 1.1|
|---|---|---|
|GDB_PRO_04|SI|28/08/2023|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G. EVEN|Approbation :<br>C. AUDEBERT|


**5.6 Schéma du trajet des données en routine**


6/7

|Col1|Système de Gestion des données de<br>génotypage|Version 1.1|
|---|---|---|
|GDB_PRO_04|SI|28/08/2023|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G. EVEN|Approbation :<br>C. AUDEBERT|


**6.** **DOCUMENTS ASSOCIÉS**

~~GDB~~ _ ~~FORM~~ _ ~~05~~ _ ~~Habilitatio~~ n a ~~nalyse/transmission~~ ~~des~~ ~~résultats~~ ~~de~~ ~~génotypage~~


7/7

