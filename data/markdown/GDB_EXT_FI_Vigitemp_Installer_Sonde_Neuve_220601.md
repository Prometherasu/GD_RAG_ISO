# Installation et mise en service d’une sonde [0514] INSTALLATION ET MISE EN SERVICE D’UNE SONDE
## **1 **

# Installation et mise en service d’une sonde [0514]

Pré-requis :

   Un PC équipé du logiciel Vigisurv

   Dans Vigisurv : un compte disposant des droits d’accès administrateur et métrologie (si votre

compte ne le permet pas, contactez votre référent Vigitemp interne)

   Le fichier de calibrage de la sonde (+ optionnel : le fichier d'étalonnage).

   La sonde et son chargeur d’alimentation

   Connaitre le n° de série de la sonde à installer (inscrit sur la sonde, sur une étiquette ou un

code barre, exemple : IN0DH9)
## **2 **

# Installation et mise en service d’une sonde [0514]
### Etape 1 : Installation physique de la sonde :

Brancher le bloc d’alimentation de la sonde sur une prise électrique à proximité de l’appareil qui sera

surveillé (ou dans la pièce dans le cas d’une température ambiante).

Insérer le connecteur d’alimentation dans le boitier de la sonde, exactement comme indiqué sur la

photo ci-dessous : (trou de connexion le plus éloigné du câble du capteur)

Le boitier sera posé, fixé ou scratché sur l’appareil ou au mur de la pièce.

Le capteur sera ensuite placé à l'endroit désiré pour une surveillance optimale.

La sonde illustrée ci-dessus est de type I. La procédure de mise en place et branchement est valide

pour tous les autres types de sonde.
## **3 **

# Installation et mise en service d’une sonde [0514]
### Etape 2 : Déclarer la sonde dans Vigitemp par son fichier de calibrage :

Ouvrir Vigitemp puis se connecter.

En premier lieu, aller dans le menu Administration puis Liste des modules.

Repérer dans la liste affichée à l’écran, le module auquel la sonde sera rattachée (il s’agit du boitier

principal de réception). Noter son numéro de série et port COM, ces informations seront

indispensables dans la prochaine phase.

Sortir de la liste des modules par le bouton Fermer en bas à gauche.

Approcher la souris sur le bord gauche de l’écran principal afin d’ouvrir le menu déroulant. Cliquer en

haut sur le bouton Métrologie.
## **4 **

# Installation et mise en service d’une sonde [0514]

Toujours en allant sur le côté gauche de l’écran, sélectionnez l’option Calibrer une sonde par fichier

externe dans le bandeau déroulant.

A l’écran suivant, cliquer sur la loupe afin d’aller chercher le fichier de calibrage de la sonde à

installer.

Parcourir jusqu’à l'emplacement de stockage du fichie. Sélectionner le fichier de calibrage voulu (il

contient le n° de série de la sonde dans son intitulé). Appuyer sur Ouvrir.
## **5 **

# Installation et mise en service d’une sonde [0514]

Le descriptif de la sonde apparait à l’écran. Dans la liste déroulante Module par défaut, en haut à

droite de l’écran, sélectionner le module de rattachement de la sonde (pour lequel le N° de série et

port COM ont été précédemment notés).

Appuyer enfin sur le bouton ‘Calibrer’ en bas à gauche.

La sonde est désormais déclarée dans le logiciel et affectée au module récepteur.
## **6 **

# Installation et mise en service d’une sonde [0514]
### Etape 3 : Création du lieu surveillé par la nouvelle sonde :

Dans Vigitemp, une sonde en surveillance est liée à un lieu (appareil, pièce, etc …).

La prochaine étape consiste donc à créer le lieu surveillé par la nouvelle sonde.

Dans la partie Administrateur, ouvrir la liste des lieux.

Cliquer sur le bouton en haut à droite ‘Nouveau’.

Remplir tous les champs avec les informations voulues (nom du lieu, consignes, etc …) :

Passer à l’onglet métrologie puis choisir, dans la liste déroulante, la sonde précédemment chargée.
## **7 **

# Installation et mise en service d’une sonde [0514]

Valider la création du lieu avec le bouton en bas à droite.

Répondre aux questions (Enregistrer les modifications ? Activer la surveillance ? Attribuer un plan ?)
## **8 **

# Installation et mise en service d’une sonde [0514]
### Etape 4 : Chargement du fichier d’étalonnage de la sonde :

Si la sonde a reçu un étalonnage MC2, un fichier correspondant est à charger pour, notamment,

pouvoir prendre en compte l’incertitude de mesure.

Retourner dans la partie ‘Métrologie’ du logiciel, puis dans le menu déroulant gauche, bouton

‘Etalonner une sonde’ par fichier externe.

A l’écran suivant, cliquer sur la loupe afin d’aller chercher le fichier d’étalonnage de la sonde.

Parcourir jusqu’à la l'emplacement de stockage du fichier. Sélectionner le fichier voulu (il contient le

n° de série de la sonde dans son intitulé). Appuyer sur Ouvrir.
## **9 **

# Installation et mise en service d’une sonde [0514]

Les caractéristiques d’étalonnage de la sonde apparaissent à l’écran. Valider avec le bouton

‘Enregistrer les étalonnages’ :

Cette manipulation permet, dans la fiche du lieu, onglet métrologie, de charger l’incertitude de la

sonde pour une prise en compte et correction des consignes de température.
## **10 **

# Installation et mise en service d’une sonde [0514]
### Etape 5 : Validation du fonctionnement de la sonde :

Dans la partie ‘Surveillance’ de Vigitemp, vérifier que le lieu créé affiche bien un relevé de

température (attention le relevé n’est pas immédiat. Patienter environ 10 minutes).

Il est également possible d’initier un test de connexion entre la sonde et son boitier récepteur à

partir de l’écran administrateur > bouton ‘Outils’.

Sur l’écran suivant chercher la sonde dans la liste, cocher la case devant son numéro de série puis

lancer le test. Les résultats apparaissent sur la partie droite de l’écran.

Selon la taille du système Vigitemp (nombre de sondes, de laboratoires connectés) et selon les

performances du réseau informatique, le délai d’apparition du résultat d’un test peut varier de

quelques secondes à plusieurs minutes.

Pour quitter le test, y compris avant l’apparition d’un résultat, appuyer sur le bouton stop puis

quitter.
### Etape 6 : Dépannage :

Si la sonde nouvellement installée ne renvoie pas de mesures, procéder à son redémarrage

électrique. Pour cela, sur le boitier gris de la sonde, retirer le petit connecteur noir d’alimentation,

patienter quelques secondes, puis le remettre en place.

Tester, si cela est possible, avec un autre bloc d’alimentation.

Si toutes les étapes d’installation ont été respectées et si la sonde ne fonctionne toujours pas,

prendre contact avec la hotline Vigitemp au 04.73.28.99.99
## **11 **

