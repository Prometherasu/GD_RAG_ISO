|Col1|Elaboration des fichiers SAM|Version 3.0|
|---|---|---|
|GDB_MOP_13|Extraction|31/05/2024|
|Rédaction :<br>M. BARBET|Vérification :<br>L. LIETAR|Approbation :<br>L. LIETAR|


**Ce protocole s’adresse aux personnes habilitées à l’extraction d’ADN.**

Cette étape fait suite à l’extraction des plaques MATRICE_AAMMJJ-NN éluées en plaques
SAMAAMMNNN.

**Mode opératoire**

Convertir les fichiers GDB_FORM_15_MATRICE_AAMMJJ-NN en fichiers SAMAAMMNNN
(stockage définitif de l’ADN envoyé en génotypage) :

1) Dans **Galaxy** [(http://galaxy.gspp2gdlab.genesdiffusion.com/, compte : production),](http://galaxy.gspp2gdlab.genesdiffusion.com/)

s’identifier et renseigner le mot de passe.
_identifiant :_ **production**

2) Au niveau de la colonne de droite, cliquer sur **“+”** afin de créer un nouvel historique.

Cliquer sur **“Unamed history”** et renommer l’historique : **SAM_semxx_aaaa**, xx
correspondant au numéro de la semaine, et aaaa à l’année. Valider la modification en
appuyant sur **Entrée.**

3) En haut à gauche, cliquer sur la flèche (download), puis sur **“choose local file”**, et

aller rechercher le ou les fichiers extraction GDB_FORM_15_MATRICE_AAMMJJ-NN
dans le dossier partagé partage_labo\Extractions\Fichiers_extraction\Listes (serveur :
gna2gdlabo.genesdiffusion.com). Il est également possible de les faire glisser depuis
le dossier, dans la fenêtre de chargement.

4) Cliquer sur **“Start”**, le ou les fichiers se chargent dans l’historique.

5) Dans la colonne de gauche, cliquer sur **“Outils Preparation Extraction”**, puis

**“Gestion des infos animal / Labo”**, sélectionner l’ **Action** **“Convertir un fichier**

**extraction en fichier SAM”** .

Renseigner le **“Nom du fichier Génotypage (SAM)”** qui correspond à la référence
de plaque SAM attribuée lors de l’extraction.
Si la plaque contient des QC (Quality Check) répétabilité/reproductibilité, cliquer sur
**“Yes”** à l’endroit dédié.

Sélectionner ensuite le **“Type de Liste Identifiant Animal ou Prélèvement”** :

a) **1 Fichier Extraction complet**, pour les fichiers extraction complets à convertir

entièrement en fichier SAM :

1/3

|Col1|Elaboration des fichiers SAM|Version 3.0|
|---|---|---|
|GDB_MOP_13|Extraction|31/05/2024|
|Rédaction :<br>M. BARBET|Vérification :<br>L. LIETAR|Approbation :<br>L. LIETAR|



           - dans “Fichier Excel Extractions”, sélectionner le fichier extraction
chargé précédemment,

           - cliquer sur “Execute”,

b) **2 Fichiers Extractions (48 A01=>H06, 48 A07=>H12)**, pour pooler deux

fichiers extraction équivalents à une demi plaque chacun :

           - dans “Fichier Excel Extractions 1 A01=>H06”, sélectionner le fichier
extraction chargé précédemment dont les échantillons seront disposés
en A01 à H06,

           - dans “Fichier Excel Extractions 2 A07=>H12”, sélectionner le fichier
extraction chargé précédemment dont les échantillons seront disposés
en A07 à H12,

           - cliquer sur “Execute”,

c) **Multiple Fichiers Extractions avec un fichier Position|Code Barre**, pour

pooler des échantillons provenant de différents fichiers extraction pouvant être
répartis aléatoirement (ex : plaques QC, cas de remplacement d’échec
extraction, de places réservées pour regénotypage, …) :

           - créer une liste des échantillons devant figurer dans le fichier SAM (1e
colonne les positions dans l'ordre A01 à H12, et 2e colonne les CAB
correspondants), et l’importer dans l’historique,

           - dans “Fichier Position / Code barre”, sélectionner cette liste,

           - dans “Liste des Fichier Excel Extractions”, après avoir importé dans
l’historique les différents fichiers extraction tels que créés à l’origine
(notamment pour les regénotypages et les QC), cliquer sur “Insert Liste
des Fichier Excel Extractions” autant de fois qu’il y a de fichiers
extraction à pooler et sélectionner ces fichiers extraction,

           - cliquer sur “Execute”.

Répéter pour chaque fichier.

6) Lorsque l’étape de création de la plaque SAM apparaît en rouge, cliquer sur l'œil de

l’étape “log.txt” correspondante pour visualiser la ou les erreurs relevées (ex : erreur
format de date renseignée, …). Corriger ces erreurs, si besoin en lien avec Pierre
Bouvelle (responsable SI), et renouveler les étapes 3) à 5).
Lorsqu’elle apparaît en vert, celle-ci est valide, la plaque SAM a pu être générée.

7) Enregistrer la plaque dans le dossier partagé partage_labo\Extractions\Fichiers_SAM

(serveur : gna2gdlabo.genesdiffusion.com), compléter la fiche extraction (versions
papier et informatique) et l’archiver dans le dossier partagé

2/3

|Col1|Elaboration des fichiers SAM|Version 3.0|
|---|---|---|
|GDB_MOP_13|Extraction|31/05/2024|
|Rédaction :<br>M. BARBET|Vérification :<br>L. LIETAR|Approbation :<br>L. LIETAR|


partage_labo\Extractions\Fichiers_extraction\Archives\aaaa (serveur :
gna2gdlabo.genesdiffusion.com).

**Documents associés :**

GDB_PRS_05_Extraction d'ADN
GDB_FORM_15_MATRICE_AAMMJJ-NN
~~GDB~~ _ ~~FORM~~ _ ~~03~~ _ ~~Habilitation~~ ~~extraction~~ ~~ADN~~

3/3

