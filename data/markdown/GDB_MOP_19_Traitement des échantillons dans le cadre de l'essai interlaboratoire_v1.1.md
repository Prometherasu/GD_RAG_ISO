|Col1|Traitement des échantillons dans le cadre<br>de l'essai interlaboratoire|Version 1.1|
|---|---|---|
|GDB_MOP_19|Génotypage|18/04/2023|
|Rédaction :<br>L. LIETAR<br>P. BOUVELLE|Vérification :<br>C. AUDEBERT<br>K. LE ROUX|Approbation :<br>L. LIETAR|


**Ce protocole s’adresse au responsable SI et au responsable de la plateforme de**
**génotypage haut-débit**

**Mode opératoire**

1) Déclaration informatique des échantillons

a) Télécharger une copie du fichier ci dessous au format XLSX, et

remplacer mm-aaaa par le mois et l’année de l’essai :
GDB_EXT_FORM_Enregistrement des échantillons dans le cadre de
l'essai interlaboratoire - mm-aaaa_220301,

b) Copier les identifiants des échantillons reçus dans le fichier téléchargé

en colonne A et X,

c) Choisir le type d' échantillon en colonnes AB,

d) Enregistrer le fichier et le transmettre au service génétique pour

enregistrement dans la base de données échantillons.

2) Traitement des échantillons

a) Créer une fiche extraction fictive dédiée (les échantillons reçus sont

déjà extraits), selon le mode opératoire habituel
GDB_MOP_07_Elaboration des fichiers d’extraction, et préciser qu’il
s’agit des échantillons de l’essai interlaboratoire,

b) Les transférer dans la plaque SAM finale prévue et formater le fichier

SAM correspondant selon le mode opératoire habituel
GDB_MOP_13_Elaboration des fichiers SAM,

c) Poursuivre sur l’étape de génotypage.

3) Récupération des résultats

1/3

|Col1|Traitement des échantillons dans le cadre<br>de l'essai interlaboratoire|Version 1.1|
|---|---|---|
|GDB_MOP_19|Génotypage|18/04/2023|
|Rédaction :<br>L. LIETAR<br>P. BOUVELLE|Vérification :<br>C. AUDEBERT<br>K. LE ROUX|Approbation :<br>L. LIETAR|


Une fois le processus de génotypage terminé :

a) Dans Galaxy, Outils Consultation, utiliser l’outil “ **Consult Bovin”** en

entrant les identifiants dans la “zone de texte” et en configurant le reste
selon l’exemple ci-dessous :

b) Ensuite, toujours dans Galaxy, Outils Extraction, utiliser l’outil “ **Extract**

**200 SNP”** sur le résultat “[Consult]”,

c) Télécharger le fichier de résultats avec les SNPs,

d) Créer une copie du formulaire GDB_FORM_19_Résultats bruts essai

interlaboratoire - Laboratoire - mm-aaaa, en remplaçant Laboratoire par
le nom du laboratoire organisateur de l'essai et mm-aaaa par le mois et
l’année de l’essai,

2/3

|Col1|Traitement des échantillons dans le cadre<br>de l'essai interlaboratoire|Version 1.1|
|---|---|---|
|GDB_MOP_19|Génotypage|18/04/2023|
|Rédaction :<br>L. LIETAR<br>P. BOUVELLE|Vérification :<br>C. AUDEBERT<br>K. LE ROUX|Approbation :<br>L. LIETAR|


e) Compléter les informations “Laboratoire organisateur de l'essai” et

“Date de l'essai (mm-aaaa)”, puis reporter les SNPs dans cet
enregistrement. Les calculs de reproductibilité sont faits
automatiquement via des formules.

4) Traitement des résultats

a) Reporter les résultats de l’essai dans le fichier de synthèse

GDB_ENR_17_Synthèse essais interlaboratoires,

b) Générer un rapport via le fichier GDB_FORM_20_Essai interlaboratoire

         - Laboratoire - mm-aaaa en créant une copie, en remplaçant
Laboratoire par le nom du laboratoire organisateur de l'essai et mmaaaa par le mois et l’année de l’essai (les tableaux et informations
nécessaires à l’édition sont présents dans les fichiers de résultats bruts
et de synthèse générés précédemment).

**Documents associés :**

GDB_MOP_07_Elaboration des fichiers d’extraction
GDB_MOP_13_Elaboration des fichiers SAM
GDB_EX_FORM_Enregistrement des échantillons dans le cadre de l'essai interlaboratoire mm-aaaa_220301
GDB_FORM_19_Résultats bruts essai interlaboratoire - Laboratoire - mm-aaaa
GDB_FORM_20_Essai interlaboratoire - Laboratoire - mm-aaaa
GDB_ENR_17_Synthèse essais interlaboratoires

3/3

