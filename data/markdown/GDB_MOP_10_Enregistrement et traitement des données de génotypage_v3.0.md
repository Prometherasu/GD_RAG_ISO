|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


**Ce protocole s’adresse au personnel habilité au traitement des données de génotypage**

**Attention, certains éléments ne sont pas concernés par l’ISO 17025 mais sont présents**
**dans ce mode opératoire par souci de fluidité dans l'exécution de celui-ci. Ces éléments**
**sont surlignés en** ~~**orange**~~

**Mode opératoire**

**PHASE I : Enregistrement des échantillons**

**1)** **Renseigner la fiche de suivi**

Pour l’enregistrement et le traitement des génotypages, il existe une fiche de suivi,
correspondant aux génotypages de la semaine, à remplir tout au long du traitement. Celle-ci
permet de revenir aux différentes étapes en cas de besoin et permet également le suivi du
bon déroulement de la chaîne informatique. La trame de cette feuille de suivi correspond au
document GDB_FORM_26_Fiche suivi indexation. Avant l’enregistrement des plaques dans
l’interface GDBoard, reporter le nom des plaques SAM génotypées, leur numéro MSA
associé, ainsi que les dates du run dans les cases correspondantes, et cocher la case contrôle
qualité (QC) correspondante en précisant la référence de la plaque SAM d'où le QC
reproductibilité provient. Plus de précisions sur le mode opératoire des contrôles qualité dans
GDB_PRO_05_Contrôle de répétabilité et de reproductibilité : méthode de génotypage hautdébit par puces à ADN.

**2)** **Enregistrement des plaques SAM dans le fichier de suivi des échantillons**

**(étape 1)**

Pour rappel, les fichiers de suivi des échantillons de chaque année sont situés sur l’espace
numérique partagé dans le dossier
GD_GDSCAN\Genotypage\Gestion_echantillons\Suivis_echantillons.

Avant l’enregistrement des plaques via l’interface GDBoard, ajouter toute information précisée
lors des étapes de génotypage dans la colonne I « Commentaire genotypage » de l’onglet
« Fichier gestion labo » de chaque plaque SAM concernée (ex : plaque et position d’origine
pour les échantillons re-génotypés, information concernant l’échantillon, non conformités
relevées comme des puits vides ou des erreurs de manipulation, échecs de scan, …). Ces
informations figureront dans le fichier de suivi des échantillons en colonne AS.

Vérifier le nom des projets et le « type client projet » des contrôles qualité (QC) dans la plaque
correspondante :

1/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|



   - colonne PROJET (AN) : projets « QUALITY CHECK REPETA » (puits B08) et
« QUALITY CHECK REPRO » (puits C08),

   - colonne Type_client_PROJET (AR) : « RECHERCHE » (puits B08 et C08).

Dans **GDBoard** (Compte : p.nom@genesdiffusion.com) :

a) Dans le tableau de bord à gauche, onglet « MONITORING », cliquer sur « SUIVI

GENOTYPAGE », puis sur « Créer un groupe de génotypage » et le nommer comme
suit : **Genotypages_semxx_aaaa** (où « xx » correspond au numéro de la semaine et
« aaaa » à l’année).

b) Une fois le groupe créé, cliquer dessus pour l’ouvrir. Est représenté le tableau de suivi

des plaques qui seront génotypées.

c) Pour enregistrer les fichiers SAM, dans étape « 1 : Enregistrement SAM », cliquer sur

« Enregistrer une plaque SAM », renseigner les informations demandées : l’identifiant
du run : (RUN_aaaaSEMss_xx où « aaaa » représente l’année, « ss » le numéro de
semaine et « xx » le numéro du run), le nom de la plaque (WGXXXXXXX-MSA7), la
date du début du génotypage et le format de puce. Insérer le fichier SAM disponible
sur le serveur en cliquant sur « Choisir le Fichier à importer ». Les fichiers sont stockés
dans le dossier partagé partage_labo\Extractions\Fichiers_SAM\Semaine génotypage
(serveur : gna2gdlabo.genesdiffusion.com).

d) Cliquer sur « Enregistrer le fichier SAM », et le message « insertion : ok » s’affichera

en cas de succès (ainsi qu’une bulle temporaire verte « Enregistrement de la plaque
WGXXXXXXX-MSA7 réussi »).

e) Cette étape est à réaliser pour chaque plaque. Enregistrer les plaques une à une dans

l’ordre de génotypage, et attendre la confirmation d’insertion évoquée ci-dessus. Il est
possible de rester sur la même page d’insertion pour l’enregistrement suivant et de
changer uniquement le MSA7 ainsi que la SAM correspondante.

f) Surveiller le fichier de suivi des échantillons qui doit intégrer les 96 lignes

correspondantes pour chaque plaque. Tracer des lignes noires pour délimiter cellesci, rouges pour délimiter les semaines.

**3)** **Récapitulatif et déclaration (étape 1)**

Une fois les fichiers SAM insérés, ceux-ci sont visibles sur la page principale avec les
informations enregistrées. Pour obtenir le récapitulatif des plaques insérées, cliquer sur le
menu vache en haut à droite (annexe 2), puis sur « Statistiques ». Vous y trouverez un
décompte des génotypages par projet pour la semaine en cours.

Pour obtenir le fichier de déclaration, dans étape « 1 : Enregistrement SAM », cliquer sur
« Télécharger le fichier de déclaration Declaration_semxx_aaaa ». Ce fichier est à faire

2/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


parvenir au client au format .xlsx avec copie à l’attention des personnes habilitées au rendu
de résultats de génotypages. Cette liste sera la liste de référence pour la déclaration ANI
nécessaire au dépôt des génotypages chez Valogène. Le client confirmera la validité du projet
associé à chaque échantillon ou notifiera les erreurs relevées. Dans ce dernier cas, il
conviendra d’apporter les corrections en base de données, via l’interface GDBoard ou via le
responsable SI, dans le fichier de suivi des échantillons et dans le fichier SAM en créant une
copie.

Correction de projet via GDBoard :

a) Dans la liste des plaques de la semaine, cliquer sur l’ puis sur « voir la plaque »
permettant de visualiser la plaque avec les informations animaux pour chaque position.
Sélectionner la(es) coordonnées concernée(s) par une correction de projet, puis
cliquer sur « Mettre à jour le Projet pour la sélection » sur .
b) Sélectionner le projet correctif et cliquer sur « Modifier le Projet en … (nom du nouveau

projet », le message « Mise à jour Projet Réussie » confirme la correction.

Correction de projet dans le fichier de suivi des échantillons :

a) Colonne AD et AZ (PROJET) : corriger le nom du projet (couleur du texte en rouge)
b) Insérer une note en précisant :

      - Initialement projet (nom du projet)

     - Demande de modification par (initiales de la personne à l’origine de la

demande)

      - Correction effectuée par (initiales de la personne ayant effectué la correction)

+ date (format jj/mm/aaaa)

Correction de projet dans le fichier SAM :

a) Dans le dossier partagé partage_labo\Extractions\Fichiers_SAM\Semaine
génotypage (serveur : gna2gdlabo.genesdiffusion.com), ouvrir le fichier SAM
concerné par la correction
b) Dans l’onglet « Fichier origine », en colonne AN, modifier le projet de l’animal concerné

(couleur du texte en rouge)
c) Insérer une note en précisant :

      - Initialement projet (nom du projet)

     - Demande de modification par (initiales de la personne à l’origine de la

demande)

      - Correction effectuée par (initiales de la personne ayant effectué la correction)

+ date (format jj/mm/aaaa)
d) Enregistrer le fichier
L’ensemble de ces corrections est également applicable au type client qui peut parfois
changer lors de la correction du projet (correction de type client via GDBoard : « Mettre à jour
le Type Client pour la sélection »).

3/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


**4)** **Création des samplesheets .csv (étape 2)**

Dans l’interface GDBoard, dans le groupe de génotypage :

a) Aller sur « 2 : Génération Samplesheet », et cliquer sur « Générer une samplesheet ».
b) Dans le formulaire « Génération des samplesheet » compléter l’identifiant Sentrix, la

date de scan, et choisir la plaque de génotypage (MSA), ainsi que le type de puce, à
l’aide des réponses au formulaire GDB_FORM_16_Génotypage Infinium Illumina Tracking form.
c) Cliquer sur « Générer la samplesheet ». Le message « insertion : ok » s’affichera en

cas de succès (ainsi qu’une bulle temporaire verte « Génération de la samplesheet
réussie »).

Récupérer ensuite les samplesheets en allant dans la colonne action du tableau, puis en

cliquant sur l’ puis « Télécharger la samplehseet » et les enregistrer sur le serveur
gna2gdlabo.genesdiffusion.com, dossier partagé : Labo\génotypages\Génotypages
SAM\SAM_MD_v...\ExportSampleSheet_XT, au format SAMAAMMNNN_MD_vN_XT_NN.

**PHASE II : Traitement des génotypages**

**1)** **Analyse Genome Studio**

**a)** **Création d’un projet Genome Studio (GS)**

Pré-requis : installation du logiciel Genome Studio ILLUMINA téléchargeable en ligne.

En entrée il est nécessaire d’avoir accès aux élément suivants :

   - export de samplesheet électronique (.csv),

   - données brutes de scan,

   - fichier Bead pool manifest (.bpm),

   - fichier de clustering approprié (.egt).

Ouvrir Genome studio et créer un projet « **genotyping** » :

4/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


Indiquer l’emplacement de destination du projet et son nom :

Localisation du projet sur le serveur
gna2gdlabo.genesdiffusion.com :
Labo\genotypages\Genotypages_SAM\SAM_M
D_v...\Indexations\aaaa\indexations_mois_aaaa
Il existe 1 emplacement de destination par mois
et par année.
_Note : le projet peut être créé en local dans un_
_premier temps afin d’écourter les temps de_
_chargements et de calculs. Il sera ensuite_
_déplacé à l’emplacement évoqué ci-dessus._

Par convention le projet est nommé comme suit
: **indexation_jjmmaa** .

Renseigner les champs demandés :

Samplesheet sur le serveur
gna2gdlabo.genesdiffusion.com :
Labo\genotypages\Genotypages_SAM\SAM_MD_v...\E
xportSampleSheet_XT.
Data Repository (données brutes) sur le serveur
gna2gdlabo.genesdiffusion.com :
Labo\genotypages\Genotypages_SAM\SAM_MD_v...\S

can.

Manifest Repository (fichier .bpm) sur le serveur
gna2gdlabo.genesdiffusion.com :
Labo\genotypages\Genotypages_SAM\SAM_MD_v...\C
lustering.

5/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


Sélectionner les paramètres d’analyse :

Cluster File (fichier .egt) sur le serveur
gna2gdlabo.genesdiffusion.com :
Labo\genotypages\Fichiers_Clustering
Veillez à utiliser la dernière version du cluster adapté au
format de puce et au type de projet.
Paramétrer Gen Call Treshold = 0,15.

Cliquer sur « Finish », la création du projet démarre :

Pour ajouter des échantillons supplémentaires (étape à répéter autant de fois qu’il y a de
samplesheets) :

   - cliquer sur file,

   - load additional samples,

   - renseigner la localisation de la samplesheet et des données brutes de scan
correspondantes sur le serveur gna2gdlabo.genesdiffusion.com.

A l’issue de l’ajout d'échantillons, il est nécessaire de recalculer les statistiques. Pour cela,
cliquer sur l’icône calculatrice dans la partie Samples Table (cadre en bas à gauche) une fois
tous les échantillons ajoutés. Exclure du projet les individus qui n’ont pas à s’y trouver et
relancer un calcul. En revanche, les outliers (échantillons dont le CallRate est inférieur à 0,95
et considérés en échec de génotypage) ne sont pas à exclure (traçabilité de l’ensemble des
génotypages).

6/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


**b)** **Vérification des résultats**

Vérifier ensuite les contrôles internes des puces, en cliquant sur Analysis → View Controls
Dashboard, ils permettent de valider le bon déroulement de chacune des étapes du run de
génotypage en se basant sur les intensités relatives :

   - Staining : permettent de valider l’efficacité de l’étape de staining (Red = DNP
(dinitrophénol), Green = Biotine) → bonne intensité de signal attendue pour le DNP
(High) sur le canal Red, et pour la Biotine (High) sur le canal Green, les autres points
de données doivent figurer dans le bas (faible intensité),

   - Extension : permettent de valider l’efficacité de l’étape d’extension simple base durant
le staining (Red = bases A et T, Green = bases G et C) → bonne intensité de signal
attendue pour les bases A et T sur le canal Red, et pour les bases G et C sur le canal
Green, les autres points de données doivent figurer dans le bas (faible intensité),

7/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|



- Target removal : permettent de valider l’efficacité de l’étape de déshybridation des
séquences cibles après l’extension simple base, ils ne sont présents que sur le canal
Red → faible intensité attendue sur les deux canaux, si significativement élevée sur le
canal Red = déshybridation inefficace,

- Hybridization : permettent de valider l’efficacité de l’étape d’hybridation à partir de
séquences cibles synthétiques présentes en 3 concentrations différentes (faible,
moyenne et haute), ils ne sont présents que sur le canal Green → faible intensité
attendue sur le canal Red, ainsi que pour le niveau de concentration Low du canal
Green, intensité moyenne attendue pour le niveau Medium, et haute pour le niveau
High,

- Non-specific binding : permettent de valider la qualité et la spécificité de l’essai de par
leur complémentarité à des séquences bactériennes → faible intensité attendue sur
les deux canaux.

8/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


Les contrôles Stringency, Non-polymorphic, applicables à l’ADN humain, et Restoration,
applicable à un protocole spécifique, ne sont pas à vérifier.

Classer les call rates dans l’ordre croissant afin de les visualiser.

➔ **Condition de libération d’une série de génotypage**

Une série de génotypages (génotypages réalisés concomitamment) ne peut être libérée que
si plus de 85 % des échantillons analysés ont un callrate supérieur à 0,95. En deçà de ce
seuil, le run est mis sous séquestre, l’incident est traité selon la GDB_PRO_08_Gestion des
incidents et non conformités, il est donc répertorié au sein du fichier GDB_ENR_72_Gestion
des incidents et des non conformités, et une fiche de non-conformité GDB_FORM_01_Fiche
de non-conformité est ouverte.

Un taux d’outliers compris entre [5 % - 15 %[ sur l’ensemble des génotypages ou au sein
d’une même plaque doit amener à réaliser des vérifications supplémentaires : intensités
p50/p95 (faibles en cas d’absence d’ADN : p50Grn < 200, p50Red < 500, p95Grn et p95Red
< 1000), position des outliers plaque/lame/run, remarques prélèvements/génotypage, etc…
afin de mettre en évidence un éventuel incident pouvant déboucher sur une non-conformité.

Vérifier ensuite la présence éventuelle d’ADN mitochondrial pour les outliers, au niveau des
SNP dédiés (« MT » dans la colonne Chr du Full Data Table, la classer dans l’ordre croissant
pour mieux les repérer). Les individus contaminés à l’ADN mitochondrial apparaissent avec
une intensité élevée, et se situent au-dessus des clusters. Vérifier si des échantillons sont
concernés : intensité Norm R supérieure à 10 pour au moins un des SNP dédiés. Le cas
échéant, la précision « MT » sera apportée dans la colonne Précisions (BE) du fichier de suivi
des échantillons.

Insérer une colonne Comment dans la partie Samples Table, juste après la colonne CallRate,
en cliquant sur l’onglet Column Chooser. Ajouter un code selon la convention suivante, sur
une sélection d’individus, par clic droit au niveau de la colonne Comment, puis « other » :

   - 1 pour les individus exclus, ne faisant pas partie du projet,

9/19

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|



   - 0 pour les autres individus (valides et outliers).

Enregistrer le Projet.

**c)** **Création des fichiers TYP et COM**

Les fichiers nécessaires à l’envoi en indexation sont :

   - fichier TYP,

   - fichier COM.

Ces fichiers sont générés à partir du projet Genome Studio. Ils sont enregistrés dans le dossier
d’indexation correspondant au Genome Studio en cours.

**i)** **Fichier TYP**

Le fichier TYP regroupe l’ensemble des résultats issus du génotypage. Pour le générer,
cliquer sur : Analysis > Reports > Reports Wizard.

Valider les différentes étapes :

a) type of report : Final Report > Next,
b) samples excluded : remove them from the report > Next,
c) SNPs to include :

`o` Zeroed SNPs : Include zeroed SNPs in the report,
`o` Intensity only SNPs : Include Intensity only SNPs > Next,
d) format final report :

`o` cocher la case Standard,
`o` Standard Format Options : inclure les informations suivantes, dans cet ordre,

dans la colonne Displayed Fields :

SNP Name,Sample ID,Allele1 - Top,Allele2 - Top,GC Score,Sample Name,Sample
Group,Sample Index,SNP Index,SNP Aux,Allele1 - Forward,Allele2 - Forward,Allele1 Design,Allele2 - Design,Allele1 - AB,Allele2 - AB,Allele1 - Plus,Allele2 - Plus,Chr,Position,GT

Score,Cluster Sep,SNP,ILMN Strand,Customer Strand,Top Genomic Sequence,Plus/Minus

Strand,Theta,R,X,Y,X Raw,Y Raw,B Allele Freq,Log R Ratio,CNV Value,CNV Confidence

`o` Group by : sample,
`o` cocher la case Comma,
`o` (sauvegarder ce formatage pour ne pas avoir à valider ces informations les

prochaines fois en cliquant sur Save Current… dans Favorite Formats, le
nommer TYP_GD, et cliquer sur Add To Favorites, puis OK. Il suffira alors de
le sélectionner dans le menu déroulant la prochaine fois)
`o`     - Next,
e) enregistrer dans le dossier d’indexation correspondant au Genome Studio en cours,

Report Name : **TYP_file**    - Finish.

**ii)** **Fichier COM**

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


Le fichier COM fournit l’information Call Rate, score global de l’échantillon, non fourni par le
TYP report. Pour générer ce fichier, tout se passe dans la partie Samples Table en bas à
gauche de l’écran Genome Studio. Dans la section Column Chooser sélectionner, dans cet
ordre : Sample name, Call Rate, Comment, puis valider.

Dans la partie Samples Table n’apparaissent plus que ces 3 colonnes, à exporter dans le
dossier d’indexation correspondant au Genome Studio en cours, en cliquant sur « Export
displayed data to a file » (icône document avec flèche sortante), sous le nom
**samples_table_COM** .

Fermer Genome Studio sans enregistrer.

Si le projet a été créé en local sur l’ordinateur, le déplacer sur le serveur
gna2gdlabo.genesdiffusion.com :
Labo\genotypages\Genotypages_SAM\SAM_MD_v...\Indexations\aaaa\indexations_mois_a

aaa.

**2)** **Enregistrement des résultats en base de données (étape 3)**

Dans l’interface GDBoard, dans le groupe de génotypage, dans « 3 : Insertion TYP », cliquer
sur « insérer un TYP », et ensuite remplir le chemin vers le fichier TYP, en faisant un
copier/coller du chemin du dossier dans la barre d’adresse de l’explorateur de fichier windows.

L’étape prend quelques minutes, les fichiers TYP et COM sont d’abord téléchargés, puis
vérifiés et découpés en génotypages individuels, ceux-ci sont comparés aux précédents de
l’animal déjà existants et rangés, et les QC sont générés.
Le callrate, le callrate iso, le scope iso ainsi que la date d’insertion et le délai sont calculés à
cette étape, et complétées dans le fichier de suivi des échantillons.

Une fois l’insertion terminée, le message « status : success » apparaît.

Il est possible de faire de multiples projets génome studio en cas de série comportant
beaucoup de plaques (pour des raisons de performance ou d’organisation), et donc de
multiples TYP/COM, et de réaliser ainsi plusieurs fois cette étape.

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


➔ A ce stade il est important de vérifier les contrôles qualités répétabilité et

reproductibilités (QC) :

Pour vérifier les QC, aller dans le menu vache (voir annexe 2) puis cliquer sur « fichiers
récapitulatifs », dans la fenêtre qui s’ouvre, déplier la partie « Fichiers Email & QC »
Ici seront listés les QC, avec leur état. Deux boutons à côté du titre permettent de télécharger
et de visualiser le fichier PDF du QC.

Dans le récapitulatif, en cliquant sur « Semaine en cours » de la partie « Monitoring », se
trouve sur la droite la partie Quality Check.
On y retrouve tous les QC par run de la semaine en cours, avec leur état.

Le détail complet des QC avec les SNP est disponible sur la page
[http://dashboardgenoprod.gspp2gdlab.genesdiffusion.com/main/quality-check.](http://dashboardgenoprod.gspp2gdlab.genesdiffusion.com/main/quality-check) C’est
également sur cette page que les rapports en .pdf sont à extraire.

Se référer au document GDB_PRO_05_Contrôle de répétabilité et de reproductibilité :
méthode de génotypage haut-débit par puces à ADN pour plus de précisions.

**3)** **Vérification des résultats (étape 4)**

Cette étape n’est débloquée que lorsque que toutes les plaques du groupe ont passé l’étape
d’insertion du TYP (étape 3).
Comme les vérifications se font en partie entre les plaques, une fois réalisée il ne sera donc
plus possible d’ajouter de nouvelles plaques, sans au préalable annuler cette vérification. Il
faudra alors ensuite la relancer.

Dans « 4 : Vérifications », cliquer sur “Vérifier le groupe” pour lancer la vérification. Celle-ci
prend quelques minutes.

Seront ainsi vérifiés :

   - la race,

   - le sexe,

   - la compatibilité génétique avec les parents déclarés,

   - la possibilité de doublon dans une plaque ou dans un lot,

   - les mutations déclenchant un blocage de diffusion des résultats à des tiers, selon la
demande du client.

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


Les fichiers générés par ces vérifications sont disponibles dans les « Fichiers récapitulatifs »
accessible depuis le menu vache (annexe 2).
Il convient alors de contrôler les fichiers suivants afin de visualiser et mettre en évidence un

éventuel problème de manipulation au laboratoire (ex : inversion de plaques, …).

Dans la catégorie « Fichiers Vérification » :
compatibilite_html_{groupe_génotypage}_{date_génération}.html
_Ce fichier représente graphiquement les problèmes d’incompatibilité par plaque_
doublon_html_{groupe_génotypage}_{date_génération}.html
_Ce fichier représente graphiquement les doublons par plaque_

Et dans la partie « Fichiers Email & QC », lorsque le cas se présente :
stop_mutation_{groupe_génotypage}_{date_génération}.csv
_Ce fichier contient les analyses bloquées à cause d’une mutation_
erreur_compatibilite_{groupe_génotypage}_{date_génération}.csv
_Ce fichier liste les problèmes d’incompatibilité_
erreur_race_{groupe_génotypage}_{date_génération}.csv
_Ce fichier liste les problèmes de race_
erreur_sexe_{groupe_génotypage}_{date_génération}.csv
_Ce fichier liste les problèmes de sexe_
doublon_{groupe_génotypage}_{date_génération}.csv
_Ce fichier liste les problèmes de doublons, les blocages et leur justification_
conflits_regenotypage_{groupe_génotypage}_{date_génération}.csv
_Ce fichier liste les conflits avec et les anciens génotypages des animaux_

Récupérer ensuite les fichiers de la partie « Fichiers Email & QC ».

**4)** **Génération des résultats (étape 5)**

Cette étape comprend la génération des comptes rendus et la diffusion de résultats à des tiers
sous mandat explicite du client.
Dans « 5 : Génération Résultats », cliquer sur « Génération Résultats » (le processus peut
prendre plusieurs minutes).
Les comptes rendus sont téléchargeables zippés depuis le sous menu « Fichiers
récapitulatifs » dans la partie « Fichiers Email & QC », item «
compte_rendu_iso_{groupe_génotypage}.zip »

Le détail de la diffusion des résultats est listé dans la partie « Fichier recap valogène ».

**5)** **Finalisation (étape 6)**

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


Cette étape est simplement la clôture du groupe de génotypage, aucune autre action ne
pourra être effectuée. Dans « 6 : Finalisation », cliquer sur Finalisation.

Archiver les fiches extraction sur le serveur gna2gdlabo.genesdiffusion.com, dossier partagé
archives_labo : déplacer les fiches extraction de la semaine correspondante (versions
d’origine et versions old/corrigées) de
partage_labo\Extractions\Fichiers_extraction\Listes\Semaine génotypage à
partage_labo\Extractions\Fichiers_extraction\Listes\A_archiver. Les fichiers sont
automatiquement basculés dans le dossier sécurisé archives_labo.

Archiver les fichiers SAM sur le serveur gna2gdlabo.genesdiffusion.com, dossier partagé
archives_labo : déplacer les fichiers SAM de la semaine correspondante (SAM et SAM
old/corrigées) de partage_labo\Extractions\Fichiers_SAM\Semaine génotypage à
partage_labo\Extractions\Fichiers_SAM\A_archiver. Les fichiers sont automatiquement
basculés dans le dossier sécurisé archives_labo.

**PHASE III :** **B** **ilan hebdomadaire**

**1)** **Mise à jour du fichier de suivi des échantillons**

a) Le fichier de suivi des échantillons est complété automatiquement avec la date

de vérification des résultats, ainsi que la validation ou non d’un résultat rendu
sous ISO 17025 (voir contrat de prestation établi avec le client).

b) Surligner les lignes outliers en jaune (ajouter l’action à réaliser en colonne BD,

ex : demande de réextraction, et les précisions en colonne BE, ex : présence
d’ADN mitochondrial, ...), les lignes des porteurs ataxie en orange (préciser le
génotype Ataxie en colonne BD), et les lignes des projets extérieurs à l’activité
de génotypage en prune (tests, recherche IPL, …).

c) ~~Lorsqu’un~~ ~~outlier~~ ~~concerne~~ ~~un~~ ~~projet~~ ~~qPCR~~, ~~vérifier~~ ~~le~~ c ~~al~~ l ~~rat~~ e :

`o` ~~s’il~~ ~~est~~ ~~inférieur~~ ~~à~~ ~~0~~, ~~80~~, ~~retraiter~~ ~~l’échantillon~~,

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


d) Lorsqu’un outlier concerne le projet IDENTIFICATION GENETIQUE, vérifier le

callrate :

`o` s’il est inférieur à 0,60, mettre l’échantillon en réextraction (incluant un

nouveau génotypage, col.BD),

`o` s’il est supérieur ou égal à 0,60, un dépôt sera automatiquement tenté

en Base Nationale (date « d’envoi en indexation » à renseigner dans le
fichier de suivi des échantillons malgré l’échec de génotypage, col. BB).
En effet, pour ce projet, seuls 200 marqueurs sont exploités. Il faudra
cependant prévoir l’action à effectuer (col. BD) si le génotypage ne
passe pas : Génotypage inexploitable - Nouvelle extraction, ou
Génotypage inexploitable - Nouveau prélèvement (voir ci-après).

e) Une demande de re-prélèvement sera effectuée (col. BD) dans les cas suivants

:

`o` cartilage : après le 1er échec, le prélèvement ayant été extrait dans son

intégralité,
`o` semence : après le 1er échec s’il ne reste pas de paillettes ou après 2

échecs d’extraction/génotypage,
`o` poil : après 2 échecs d’extraction/génotypage sur le même échantillon,

ou après le 1er échec si une seule extraction a pu être réalisée ou que
les poils sont sales (cf. remarques col. AN),
`o` sang : après le 1 [er] échec si le sang est coagulé, ou demander un

prélèvement autre que du sang après le 1er échec si l’animal possède
un jumeau (demander l’information au client au préalable et compléter
la colonne F du fichier de suivi des échantillons par **O** ou **N** ), ou après
2 échecs d’extraction/génotypage sur le même échantillon si l’animal
ne possède pas de jumeau.

f) Pour les autres génotypages outliers, s’il s’agit potentiellement d’un défaut de

puce ou de génotypage, les mettre en re-génotypage (col. BD), le labo laissera
les places nécessaires et ceux-ci seront re-génotypés la semaine suivante. Si
non, les mettre en réextraction (incluant un nouveau génotypage, (col. BD)).

**2)** **Bilan aux équipes**

Dans un mail adressé au client et à l’équipe du laboratoire de génotypage avec en copie les
personnes habilitées à l’émission de rapports de résultats ainsi que le responsable SI :

a) Transmettre les différents fichiers récupérés précédemment au format .csv,
b) Transmettre les rapports des QC répétabilité et reproductibilité au format .pdf,

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


c) y joindre également un récapitulatif des échantillons défectueux, à générer à

partir du document intitulé GDB_FORM_07_Echecs de génotypage, à exporter
sous Excel et à transformer en enregistrement.
Compléter le numéro de semaine ainsi que l’année sur le premier onglet (report
automatique sur les autres).
Ce fichier comprend 4 onglets :

`o` **Nouveau(x) prélèvement(s) :** insérer les informations correspondant

aux échantillons nécessitant un nouveau prélèvement. Le client
enclenchera une demande de re-prélèvement.
`o` **Nouvelle(s) Extraction(s) :** insérer les informations correspondant aux

échantillons nécessitant une nouvelle extraction (incluant un nouveau
génotypage).
`o` **Identification(s)** **Génétique(s)** **:** insérer les informations
correspondant aux échantillons « IDENTIFICATION GENETIQUE »
outliers nécessitant une vérification en Base Nationale. Le service

génétique se chargera de vérifier le résultat et de la suite à donner
(VCG OK, ou re-traitement de l’échantillon / re-prélèvement de l’animal
en fonction de ce qui a été précisé).
`o` **Nouveau(x) Genotypage(s) :** insérer les informations correspondant

aux échantillons à regénotyper, le labo laissera les places nécessaires
et ceux-ci seront uniquement re-génotypés la semaine suivante.
d) préciser toute information complémentaire.

**ANNEXES**

➔ Document récapitulatif des projets et des flags :
[http://dashboardgenoprod.gspp2gdlab.genesdiffusion.com/main/documentation](http://dashboardgenoprod.gspp2gdlab.genesdiffusion.com/main/documentation)

➔ ~~**Annexe**~~ ~~**1**~~ ~~**:**~~ ~~liste~~ ~~et~~ ~~liens~~ ~~projet/mutation/SNP~~

|Projet|Mutation|
|---|---|
|qPCR Ataxie|ataxia|
|qPCR Ataxie + Culard|ataxia<br>GDF8_Q204X|

|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|








|Kappa caseine|KCAS_AB<br>KCAS_E|
|---|---|
|qPCR Blind|BLIND|
|qPCR Beta caseine|MBCAS_A1-A2|
|qPCR Beta caseine +<br>Kappa caseine|MBCAS_A1-A2<br>KCAS_AB<br>KCAS_E|
|qPCR Culard|GDF8_Q204X|
|MH BEEF|GDF8_F94L|
|qPCR Culard + MH BEEF|GDF8_F94L<br>GDF8_Q204X|
|qPCR Ataxie + Culard + MH<br>BEEF|GDF8_F94L<br>GDF8_Q204X<br>ataxia|
|qPCR Ataxie + MH BEEF|GDF8_F94L<br>ataxia|


~~Liste~~ ~~mutation/SNP~~ ~~:~~

|Mutation|Nom_du_marqueur|
|---|---|
|BLIND|EGX_BLIND_RP1|
|BLIND|EGX_BLIND_RP1_r|
|BLIND|EuroGMD_BLIND_RP1|
|BLIND|EuroGMD_BLIND_RP1_r|
|BLIND|GD4014_MBLIND_rs475071736_PMID27510606|
|GDF8_F94L|EuroG10K_GDF8F94L_F|
|GDF8_F94L|EuroG10K_GDF8F94L_R|
|GDF8_F94L|EuroG10K_GDF8F94L_R_B|
|GDF8_F94L|GD55_GDF8_F94L_Lim|
|GDF8_Q204X|EuroG10K_SNP_AB076403_204|
|GDF8_Q204X|EuroG10K_SNP_AB076403_204_ilmndup2|
|GDF8_Q204X|EuroG10K_SNP_AB076403_204_r|
|GDF8_Q204X|EuroG10K_SNP_AB076403_204_r_ilmndup2|
|GDF8_Q204X|GD52_GDF8_Q204X_Cha_BA|


|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


|KCAS_AB|CSN3_AY380228_13104_1|
|---|---|
|KCAS_AB|EuroG10K_SNP_X14908_5345|
|KCAS_AB|EuroG10K_SNP_X14908_5345_ilmndup2|
|KCAS_AB|EuroG10K_SNP_X14908_5345_r|
|KCAS_AB|EuroG10K_SNP_X14908_5345_r_ilmndup2|
|KCAS_AB|EuroG10K_SNP_X14908_5345_r2|
|KCAS_AB|EuroG10K_SNP_X14908_5345_r2_ilmndup2|
|KCAS_AB|EuroG10K_SNP_X14908_5345_r3|
|KCAS_AB|EuroG10K_SNP_X14908_5345_r3_ilmndup2|
|KCAS_AB|GD20_KCSN_X14908_5345|
|KCAS_E|CSN3_AY380228_13124|
|KCAS_E|EuroG10K_SNP_AF041482_130|
|KCAS_E|EuroG10K_SNP_AF041482_130_ilmndup2|
|KCAS_E|EuroG10K_SNP_AF041482_130_r|
|KCAS_E|EuroG10K_SNP_AF041482_130_r_ilmndup1|
|KCAS_E|EuroG10K_SNP_X14908_5365|
|KCAS_E|EuroG10K_SNP_X14908_5365_ilmndup2|
|KCAS_E|EuroG10K_SNP_X14908_5365_r|
|KCAS_E|EuroG10K_SNP_X14908_5365_r_ilmndup1|
|KCAS_E|GD21_KCSN_X14908_5365|
|ataxia|EGX_CHA_ATAX|
|ataxia|EGX_CHA_ATAX_r|
|ataxia|EuroGMD_CHA_ATAX|
|ataxia|EuroGMD_CHA_ATAX_r|
|MBCAS_A1-A2|CSN2_7|
|MBCAS_A1-A2|EuroG10K_CSN_beta|
|MBCAS_A1-A2|EuroG10K_CSN_beta_r|
|MBCAS_A1-A2|EuroG10K_CSN_beta_r_ilmndup1|
|MBCAS_A1-A2|EuroG10K_SNP_M55158_8101|
|MBCAS_A1-A2|EuroG10K_SNP_M55158_8101_ilmndup2|


|Col1|Enregistrement et traitement des<br>données de génotypage|Version 3.0|
|---|---|---|
|GDB_MOP_10|Analyse|05/06/2024|
|Rédaction :<br>L. LIETAR, M. BARBET|Vérification :<br>P. BOUVELLE, S. MARTEL|Approbation :<br>L. LIETAR|


|MBCAS_A1-A2|EuroG10K_SNP_M55158_8101_r|
|---|---|
|MBCAS_A1-A2|EuroG10K_SNP_M55158_8101_r_ilmndup2|
|MBCAS_A1-A2|GD26_CSN2_M55158_8101|


➔ **Annexe 2 :** **Description Interface groupe génotypage GDBoard**

Légende :

1 : Bouton « Menu vache »

2 : Menu vache (déplié)

3 : Bouton action visualisation

4 : Bouton action correction

5 : Onglet étape
6 : Bouton action d’étape

**Documents associés :**

GDB_FI_02_Fiche suivi indexation
GDB_PRO_05_Contrôle de répétabilité et de reproductibilité : méthode de génotypage hautdébit par puces à ADN
GDB_FORM_07_Echecs de génotypage
GDB_FORM_16_Génotypage Infinium Illumina - Tracking form (ancienne version sous
Google Forms jusqu’au 09/06/2023 : GDB_ENR_20_Génotypage Infinium Illumina - Tracking
form – Réponses)
GDB_PRO_08_Gestion des incidents et non conformités
GDB_ENR_72_Gestion des incidents et des non conformités
GDB_FORM_01_Fiche de non-conformité

