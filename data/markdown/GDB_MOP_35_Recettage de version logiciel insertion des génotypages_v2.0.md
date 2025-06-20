|Col1|Recettage de version logiciel<br>insertion des génotypages|Version 1.0|
|---|---|---|
|GDB_MOP_35|SI|26/01/2024|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G.EVEN|Approbation :<br>P. BOUVELLE|


**Ce protocole s’adresse aux personnes habilitées Responsable SI**

**Objectif :**

L’objectif est de s’assurer qu’une nouvelle version de l’application de suivi, déclaration, et
insertion, des génotypages, n’introduit pas de problème (inversion de données) et répond aux
besoins pour laquelle elle a été développée.

**Architecture :**

La nouvelle version est déployée dans un environnement de recettage (réplication identique
et isolé de l’environnement de production).

Cette application est désignée “GDBoard Recette”.

Un jeu de données factice a été créé afin de tester les fonctionnalités de l’application.

Celui-ci se trouve sur le serveur NAS gna2gdlabo :

/labo/genotypages/dataset_test

Les paramètres à compléter dans les formulaires se trouvent dans le fichier
**recettage_labo_readme.txt**

Le dossier **sam** contient les fichiers sam à déclarer lors de l’étape 1

Le dossier **typ_com** contient les fichiers pour l’étape 3

Le dossier **valogene** contient les fichiers générés à l’étape 5

Le dossier **comptes_rendus** contient les fichiers comptes rendus de référence.

**Déroulement :**

Se connecter sur le GDBoard Recette de la même manière que dans l’environnement de
production.

En suivant le GDB_MOP_10_Enregistrement et traitement des données, réaliser les étapes
suivantes, en remplissant dans le GDB_ENR_75_Suivi de version d’application la colonne
correspondante par valide ou invalide en fonction des critères de validation d’étape.

**1. Initialiser le recettage**

Dans le Suivi de génotypage, ouvrir le menu “Vache” et cliquer sur **(Ré)Initialiser le**
**recettage**

1/3

|Col1|Recettage de version logiciel<br>insertion des génotypages|Version 1.0|
|---|---|---|
|GDB_MOP_35|SI|26/01/2024|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G.EVEN|Approbation :<br>P. BOUVELLE|


2. **Créer un groupe de génotypage**

Critères de validation :

    Groupe correctement généré

3. **Déclarer les fichiers SAM de test**

Critères de validation :

    Insertion, sans rejet, des SAM

    Présence des lignes dans le fichier de suivi de recette

    Affichage des plaques dans l’interface après insertion

4. **Déclarer les samplesheets**

Critères de validation :

    Mise à jour des plaques dans l’interface

    Téléchargement des samplesheets et formatage des samplesheets corrects

5. **Insérer le TYP et le COM de test**

Critères de validation :

    Insertion sans rejet du TYP et du COM

    Mise à jour des plaques dans l’interface

    - Génération des QC

    Mise à jour des lignes dans le fichier de suivi de recette

    Mise à jour des flags dans la visualisation des plaques

6. **Lancer la vérification**

Critères de validation :

    Mise à jour des plaques dans l’interface

    - Présence des fichiers de vérification

7. **Générer les résultats**

Critères de validation :

    Mise à jour des plaques dans l’interface

    Téléchargement et vérification des comptes rendus

    - Présences des fichiers TYP LABO COM sur le FTP de recette

2/3

|Col1|Recettage de version logiciel<br>insertion des génotypages|Version 1.0|
|---|---|---|
|GDB_MOP_35|SI|26/01/2024|
|Rédaction :<br>P. BOUVELLE|Vérification :<br>G.EVEN|Approbation :<br>P. BOUVELLE|


8. **Finaliser le groupe de génotypage**

Critères de validation :

      Groupe correctement finalisé

      Suppression groupe indisponible

Contrôle humain :

Récupérer les comptes rendus d’analyse pour celles précisées dans le fichier
**recettage_labo_readme.txt.**

Et vérifier que les résultats et les informations d’analyse soient identiques aux références
placées dans le dossier **comptes_rendus**

Une fois toutes ces étapes terminées, si celles-ci sont toutes valides, la nouvelle version est
considérée comme valide et peut être mise en production par le responsable SI.

~~**Documents**~~ ~~**associés**~~ ~~**:**~~

GDB_MOP_10_Enregistrement et traitement des données

GDB_ENR_75_Suivi de version d’application

3/3

