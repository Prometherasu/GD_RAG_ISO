|Col1|Elaboration des fichiers d’extraction|Version 2.0|
|---|---|---|
|GDB_MOP_07|Extraction|31/05/2024|
|Rédaction :<br>M. BARBET|Vérification :<br>L.LIETAR|Approbation :<br>L. LIETAR|


**Ce protocole s’adresse aux personnes habilitées à l’extraction d’ADN.**

Préalablement à la réception des prélèvements sur la plateforme de génotypage, ceux-ci ont
été enregistrés en base de données, avec toutes les informations les concernant (sexe, race,
CAB, type de prélèvement, projet, type client projet, lot, …).

**Mode opératoire**
Dans la salle de “Traitement des prélèvements”

1) Disposer les prélèvements à traiter, par date d’arrivée :

        - sang : sur un portoir de tubes, 96 maximum par portoir, 1er tube en bas à
gauche puis les suivants sur la droite et en remontant,

        - poils/cartilage : dans un bac en carton, 96 maximum par bac, 1er prélèvement
sur l’avant puis les suivants derrière, et les numéroter au départ de 1,

        - semence : dans une pochette plastifiée, 1er prélèvement sur l’avant puis les
suivants derrière, et les numéroter au départ de 1.

_Attention : prévoir 2 places libres en B08/C08 de chaque 4e plaque du premier run de chaque_
_semaine pour les tests QC (Quality Check) répétabilité/reproductibilité._

2) Créer un fichier extraction (par type d’extraction et par série maximum de 96

prélèvements) en effectuant une copie du fichier trame
GDB_FORM_15_MATRICE_AAMMJJ-NN se situant sur le dossier partagé
partage_labo\Extractions\Fichiers_extraction (serveur :
gna2gdlabo.genesdiffusion.com).
Le renommer en remplaçant les termes comme suit :

        - MATRICE : BLOOD ou TISSUE ou SEMENCE,

        - AAMMJJ : date de création du fichier extraction,

        - NN : numéro de fichier extraction à la date du jour.
Par exemple : GDB_FORM_15_FORM_BLOOD_211207-03 pour la 3e série
d’extraction de prélèvements de sang du 07/12/2021.

3) Déplacer le fichier extraction nouvellement créé dans
partage_labo\Extractions\Fichiers_extraction\Listes (serveur :
gna2gdlabo.genesdiffusion.com), puis l’ouvrir.

4) Modifier la cellule MATRICE_AAMMJJ-NN (D5) en cohérence avec le nom du fichier,

annoter le portoir/bac en carton de prélèvements de la même façon, et cocher le format
d’extraction adéquate Tube ou Plaque.

1/3

|Col1|Elaboration des fichiers d’extraction|Version 2.0|
|---|---|---|
|GDB_MOP_07|Extraction|31/05/2024|
|Rédaction :<br>M. BARBET|Vérification :<br>L.LIETAR|Approbation :<br>L. LIETAR|


5) Se positionner sur la première cellule de la colonne CAB (colonne C) et scanner les

prélèvements dans l’ordre établi. Renseigner le type de prélèvement et la date de
réception des prélèvements (colonne E et F, sur toute la colonne, même aux
emplacements laissés vides). Enregistrer le fichier.

6) Dans **Galaxy** [(http://galaxy.gspp2gdlab.genesdiffusion.com/, compte : production),](http://galaxy.gspp2gdlab.genesdiffusion.com/)

s’identifier et renseigner le mot de passe.
_identifiant :_ **production**

7) Au niveau de la colonne de droite, cliquer sur **“+”** afin de créer un nouvel historique.

Cliquer sur **“Unamed history”** et renommer l’historique : **Extractions_semxx_aaaa**,
xx correspondant au numéro de la semaine, et aaaa à l’année. Valider la modification
en appuyant sur **Entrée.**
Les fichiers d’extraction de la semaine seront vérifiés et enregistrés dans cet
historique.

8) En haut à gauche, cliquer sur la flèche (download), puis sur **“choose local file”**, et

aller rechercher le ou les fichiers extraction créés précédemment dans le dossier
partagé partage_labo\Extractions\Fichiers_extraction\Listes (serveur :
gna2gdlabo.genesdiffusion.com). Il est également possible de les faire glisser depuis
le dossier, dans la fenêtre de chargement.

9) Cliquer sur **“Start”**, le ou les fichiers se chargent dans l’historique.

10) Dans la colonne de gauche, cliquer sur **“Outils Preparation Extraction”**, puis

**“Gestion des infos animal / Labo”**, sélectionner l’ **Action** **“Vérifier un fichier**
**extraction”** et un fichier extraction puis cliquer sur **“Execute”** .
Répéter pour chaque fichier.

11) Lorsque l’étape de vérification apparaît en rouge, cliquer sur l'œil pour visualiser la ou

les erreurs relevées (ex : erreur type de prélèvement enregistré, prélèvement
inexistant en base de données, …). Corriger ces erreurs, si besoin en lien avec le
service génétique (problème prélèvement), ou avec le responsable SI, et renouveler
les étapes 8) à 10).
Lorsque l’étape de vérification apparaît en vert, celle-ci est valide, toutes les
informations ont pu être vérifiées et enregistrées.

12) Le ou les fichiers extraction peuvent maintenant être imprimés pour accompagner les

prélèvements correspondants lors du processus d’extraction, et complétés pour les
parties traçabilité tâche/opérateur et remarques prélèvement/extraction (versions
papier et informatique).
_Remarque :_ _Pour les semences, spécifier le nom ou l’identifiant de l’animal sur la_
_version papier afin d’assurer la traçabilité._

2/3

|Col1|Elaboration des fichiers d’extraction|Version 2.0|
|---|---|---|
|GDB_MOP_07|Extraction|31/05/2024|
|Rédaction :<br>M. BARBET|Vérification :<br>L.LIETAR|Approbation :<br>L. LIETAR|


**Documents associés :**

~~GDB~~ _ ~~PR0~~ _ ~~5~~ _ ~~Contrôle~~ ~~de~~ ~~répétabilité~~ ~~et~~ ~~de~~ ~~reprodu~~ c ~~tibi~~ l ~~i~~ té ~~:~~ ~~m~~ ét ~~ho~~ de de gé ~~no~~ ty ~~p~~ ag ~~e~~ ~~ha~~ u ~~t~~ ~~débit~~ ~~par~~ ~~puces~~ ~~à~~ ~~ADN~~
~~GDB~~ _ ~~PRS~~ _ ~~05~~ _ ~~Extraction~~ ~~d'ADN~~
~~GDB~~ _ ~~FORM~~ _ ~~15~~ _ ~~MATRICE~~ _ ~~AAMMJJ~~ - ~~NN~~
~~GDB~~ _ ~~FORM~~ _ ~~03~~ _ ~~Habilitation~~ ~~extraction~~ ~~ADN~~

3/3

