|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


**Ce protocole s’adresse à l’ensemble du personnel intervenant dans la production de**
**génotypage GD Scan.**

**DESCRIPTIF DE L’APPLICATION**

**Objectifs**

1. Création d’un système de gestion des stocks sur le site de Douai
2. Gérer les historiques de commande et d’entrées/sorties
3. Création d’un système d’alerte en cas de stock faible

**Caractéristiques**

L’interface est basée sur Angular 2+ NodeJS
La base de données est une base MySQL
L’API est basé sur FLASK (python)

**Lien**

http://stocklabo.gspp2gdlab.genesdiffusion.com/

**Connection compte et utilisateur**

L’interface de connexion utilise les identifiants @genesdiffusion.com

**MODE D’EMPLOI DE L’APPLICATION**

**Vue dashboard**

Vue sur :

   la liste des produits en cours de réapprovisionnement

   la liste des produits à surveiller (stock faible)

   l’historique des réapprovisionnements

   l’historique des sorties

   les chiffres du mois (sorties par mois)

   le récapitulatif des stocks

1/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


Coté Laboratoire, la gestion des stock est assurée par le Responsable achats et ses
suppléants. La routine de gestion est la suivante :

   La mise à jour des stocks se fait de façon hebdomadaire

   Un tableau blanc est mis à disposition dans la salle de stockage de façon à
renseigner les sorties et les entrées des consommables

2/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


**Sortir un produit**




Dans le menu à gauche, cliquez sur “Sortir un produit”

Rechercher votre produit dans la barre de recherche

Cliquer sur le bouton “Sortir le produit” (icône stylo)

Sélectionner le client (#labo Douai)

Sélectionner le lot du produit à sortir

Sélectionner la quantité à sortir de ce lot

Cliquer sur “Valider”


3/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


**Demande de commande**

Il y a deux catégories de commande :

   - Les commandes manuelles pour les produits ne nécessitant pas un

réapprovisionnement permanent

   Les commandes avec seuil et alerte pour les produits à usages fréquent

1- Commande manuelle

   Dans le menu à gauche, cliquer sur “Sortir un produit”

   Rechercher votre produit dans la barre de recherche

   Cliquer sur le bouton cloche pour déclencher la commande

   Indiquer la quantité souhaitée

   Valider en tapant sur entrée

2- Commande avec seuil et alerte

Une alerte est lancée lorsque le seuil limite du produit est atteint. Le message “Stock faible 
Alerte lancée” est affiché en rouge sur la ligne du produit ce qui permet de déclencher la

commande. Lorsqu’un produit passe en dessous du seuil limite, une case “quantité à

commander” avec un minimum de 1 apparaît dans la colonne “Quantité à commander” de

l’onglet “Sortir un produit”:

   Dans le menu à gauche, cliquer sur “Sortir un produit”

   Rechercher votre produit dans la barre de recherche

   Indiquer la quantité souhaitée

   Valider en tapant sur entrée

4/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


**Valider la réception d’une commande**

   Dans le menu à gauche, cliquer sur “REAPPROVISIONNEMENT”

   Sélectionner le produit à restocker en cliquant sur le stylo

   - Sélectionner le fournisseur

   Renseigner le(s) numéro(s) de(s) bon(s) de livraison

   Renseigner le nombre de lots reçus

   Renseigner le(s) lot(s) et la quantité reçue

   - Valider


5/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


**Ajouter un certificat de conformité correspondant à un lot**

   Dans le menu à gauche, cliquer sur “AJOUT DE CERTIFICATS”

   Sélectionner le produit associé au lot (une barre de recherche est à votre disposition

la recherche peut être effectuée par produit ou par numéro de lot)

   Sélectionner le lot correspondant en cliquant sur le logo +

   Ajouter votre certificat au format .pdf dans l’épingle

   Cliquer sur Upload

Une fois le fichier chargé, le logo + devient un logo pdf qui vous permet de le télécharger.

6/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


**Commande**




Cet accès est réservé au Responsable achats. Un mail récapitulatif des alertes stocks
faibles ainsi que des demandes de commandes lui est envoyé tous les samedi :

La validation des commandes permet de changer le statut des stocks faibles en stocks en
cours de réapprovisionnement.

   Dans le menu à gauche, cliquer sur “Shopping”

   Rechercher votre produit

   Cliquer sur le chariot

   - Sélectionner le fournisseur

   Renseigner le numéro de commande

   Sélectionner la référence du produit

   Renseigner la quantité à commander

   Renseigner le prix s’il est différent de celui pré-enregistré

7/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


**Récapitulatif de commande et ajout de facture**

Cet accès est réservé au Responsable achats. Cette page permet de visualiser l’état des

commandes et d’y ajouter le(s) numéro(s) de facture(s) associé(s) au(x) bon(s) de livraison.

Les commandes sont rangées par fournisseur et par date.

Par défaut, la liste des commandes reprend les deux derniers mois mais un choix de date

est possible.

Ajouter une facture :

   Cliquer sur ajouter la facture au bon de livraison associé

   - Entrer le numéro de facture et valider

8/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


**Créer un produit/Ajouter une référence**

Cet accès est réservé au Responsable achats et/ou au Responsable S.I.

   Dans le menu à gauche, cliquer sur “Produit”

   Sélectionner la catégorie du produit

   Renseigner le nom du produit

   Ajouter une description si besoin

   Indiquer le stock

   Indiquer le seuil d’alerte

   Renseigner la référence du produit par défaut

   Renseigner le fournisseur par défaut

   Cliquer sur “Créer le produit”

   Rafraîchir la page

Une fois le produit créé, il est possible d’ajouter d’autres références (autres fournisseurs ou

équivalentes) correspondant à ce même produit en renseignant la partie “ajouter une

référence”

9/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


   Renseigner la référence

   Renseigner le fournisseur

   Sélectionner le produit préalablement créé dans la liste de choix déroulant

   Renseigner le nombre d’unités contenues dans cette référence

   Renseigner le tarif

   Cliquer sur “Créer le produit”

**Export de récapitulatifs**

Il est possible de générer des rapports récapitulatifs annuels (bilan annuel des achats,
inventaire de fin d’année). Ceux-ci permettent d’accéder aux informations de consommation
et achats de l’année. Il est possible de générer ces rapports selon les procédures suivantes :

   - Inventaire des stocks :

        Dans le menu à gauche, cliquer sur “Dashboard Stock Labo”

        Cliquer sur le bouton “Exporter le récap”

   - Bilan des achats annuels :

        Dans le menu à gauche, cliquer sur “Factures & suivi”

        Cliquer sur le bouton “Export récap”

Inventaire :

10/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


Bilan Achat :




11/12

|Col1|Application GDStock<br>Descriptif et Mode d'emploi|Version 1.0|
|---|---|---|
|GDB_FI_45|SMQ|07/06/2023|
|Rédaction :<br>S. MERLIN|Vérification :<br>K. LE ROUX; M. MERBAH|Approbation :<br>L. LIETAR|


Inventaire par lot :




12/12

