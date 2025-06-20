# VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

**I.** **PRESENTATION VIGITEMP.......................................................................................................................................................... 3**

A ) L OGICIEL .................................................................................................................................................................................... 3

B ) M ATERIEL .................................................................................................................................................................................. 4

C ) L EXIQUE SUPPLEMENTAIRE ............................................................................................................................................................ 5

**II.** **VIGISURV – METROLOGIE : ACCES – PAGE PRINCIPALE – FICHE LIEU .......................................................................................... 6**

A ) O UVERTURE ET CONNEXION ........................................................................................................................................................... 6

B ) E CRAN PRINCIPAL ........................................................................................................................................................................ 8

C ) F ICHE LIEU / O NGLET GENERAL ..................................................................................................................................................... 10

D ) F ICHE LIEU / O NGLET METROLOGIE ( PRESENTATION GENERALE ) .......................................................................................................... 12

E ) F ICHE LIEU / O NGLET T ELEPHONIE -P LANNING ................................................................................................................................. 13

F ) F ICHE LIEU / O NGLET METROLOGIE ( PRESENTATION DETAILLEE ) .......................................................................................................... 15

−
_Cas 1a : Les EMT obéissent à la règle du quart / sans correction de l'erreur de justesse ........................................................ 15_

−
_Cas 1b : Les EMT obéissent à la règle du quart /avec correction de l'erreur de justesse ......................................................... 16_

−
_Cas 2a : EMT saisie manuellement /sans correction de l'erreur de justesse ............................................................................ 17_

−
_Cas 2b : EMT saisie manuellement /Avec correction de l'erreur de justesse ........................................................................... 18_

−
_Cas 3a : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse / sans prise en compte_

_de la dérive dans l'incertitude : ........................................................................................................................................................ 19_

−
_Cas 3b : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse / sans prise en compte_

_de la dérive dans l'incertitude : ........................................................................................................................................................ 20_

−
_Cas 3c : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse / avec prise en compte_

_de la dérive dans l'incertitude : ........................................................................................................................................................ 21_

−
_Cas 3d : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse / avec prise en compte_

_de la dérive dans l'incertitude : ........................................................................................................................................................ 22_

−
_Cas 4a : Sans objet / sans correction de l'erreur de justesse ................................................................................................... 23_

−
_Cas 4b : Sans objet / avec correction de l'erreur de justesse ................................................................................................... 24_

G ) R ECAPITULATIF DES DIFFERENTS CAS POSSIBLES DE CONFORMITE SELON LE CHOIX EMT SELECTIONNE : ....................................................... 25

**III.** **VIGISURV – METROLOGIE : BANDEAU DEROULANT – OUTILS ................................................................................................... 26**

A ) G ESTION DES ALARMES ............................................................................................................................................................... 27

B ) G ESTION DES ETALONS ............................................................................................................................................................... 29

−
_Déclarer une nouvelle sonde étalon dans le système : ............................................................................................................. 29_

−
_Modifier une sonde étalon existante : ...................................................................................................................................... 30_

− _Archiver une sonde étalon existante : ...................................................................................................................................... 30_

−
_Tester une sonde étalon type VigiTemp SEF : ........................................................................................................................... 31_

C ) G ESTION DES MILIEUX ................................................................................................................................................................ 33

−
_Ajouter un nouveau bain / milieu ............................................................................................................................................. 34_

−
_Modifier un bain/milieu existant .............................................................................................................................................. 34_

D ) G ESTION DES SONDES ................................................................................................................................................................. 35

E ) C ALIBRER UNE SONDE ................................................................................................................................................................. 36

F ) C ALIBRAGE PAR FICHIER EXTERNE .................................................................................................................................................. 42

G ) E TALONNER UNE SONDE ............................................................................................................................................................. 44

H ) E TALONNER UNE SONDE PAR FICHIER EXTERNE ................................................................................................................................ 49

I ) H ISTORIQUE DES MESURES .......................................................................................................................................................... 51

J ) A NALYSE D ’ IMPACT .................................................................................................................................................................... 57

K ) E XPORT CONFIG ........................................................................................................................................................................ 60

**IV.** **HOTLINE ET DEPANNAGE ...................................................................................................................................................... 61**

− _Généralités : ............................................................................................................................................................................. 61_

−
_Vérifications et auto-dépannage : ............................................................................................................................................ 61_

−
_Zoom sur la télémaintenance (Surveillance) :........................................................................................................................... 62_

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : I. Présentation VigiTemp
## I. Présentation VigiTemp

a) Logiciel

Le système VigiTemp 10 est une solution client / serveur. Son architecture repose sur une base de données MySQL. La

collecte et la gestion des alarmes sont gérées par la partie serveur, cette dernière se présentant sous la forme d’un

service Windows appelé VigiServ.

L’exploitation des mesures, leur interprétation et les différentes fonctions F.M.E (Fonctions de Métrologie Evoluées) sont

quant à elles gérées par la partie client du logiciel, c’est VigiSurv.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 3 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : I. Présentation VigiTemp

b) Matériel

Le système VigiTemp est composé de divers éléments physiques. Voici la présentation d’un système radio. Il existe

également des possibilités d’installations filaires (modules et sondes sont reliés par câbles).

|PC Serveur<br>Cœur du système VigiTemp comprenant les logiciels :<br>* MySQL (base de données)<br>* VigiServ (service gérant l'interrogation des sondes, les relevés et<br>l'inscription des données)<br>* Pilote de gestion de ports COM virtuels pour les bornes ou<br>modules radio/réseau|Col2|
|---|---|
|Les bornes ou modules de réceptions<br>Boitier composé d'une partie radio (pour dialogue avec les sondes)<br>et une partie réseau Ethernet (pour dialogue avec le PC serveur).<br>1 module = 1 adresse IP = 1 port COM virtuel sur le PC serveur||
|Les sondes<br>Ensemble composé de : capteur (T°, C02…) + boitier électronique<br>(gestion des relevés, radiofréquence…) + alimentation électrique.<br>Chaque sonde a son propre numéro de série.<br>Une sonde ne dialogue qu'avec un seul module (association<br>généralement définie selon la proximité géographique des deux<br>éléments) par ondes radio (869.525MHZ).<br>Possibilité de modifier l'association module/sonde, en cas de<br>déplacement de la sonde par exemple.||



Table des matières **Dernière MAJ : 01/04/2020**  - **Page 4 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : I. Présentation VigiTemp

Enfin, les **PC clients** (hébergeant le logiciel de surveillance **VIGISURV** ) : se connectent par le réseau informatique à la base

de données située sur le PC serveur. VigiSurv permet la consultation et la gestion en temps réel de la surveillance du

système VigiTemp.

Les deux possibilités d’architecture peuvent être rencontrées :

c) Lexique supplémentaire




|LIEU|Elément surveillé par une sonde (ex : réfrigérateur, congélateur, étuve, salle, …).<br>Un lieu en surveillance est rattaché à une sonde.|
|---|---|
|||
|GROUPE|Permet le classement des lieux : par laboratoires, services, pièces, etc …|
|||
|UTILISATEUR|Compte (login + mot de passe) de connexion à VigiTemp.<br>Un compte peut voir un ou plusieurs groupes en surveillance.<br>Accès au logiciel et droits définis par le profil.|
|||
|PROFIL|Droits d'accès dans le logiciel : Accès intégral ou uniquement à quelques parties du logiciel<br>(Ex : Surveillance)|


Table des matières **Dernière MAJ : 01/04/2020** - **Page 5 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu
## II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

a) Ouverture et connexion

L’accès au logiciel VigiSurv se fait à partir du raccourci bureau suivant :

La fenêtre d’identification suivante apparait :

Les quatre sections du logiciel VigiTemp apparaissent ensuite à l’écran :

     - **Administration** : réglages et paramétrages du logiciel, journaux système, gestion du matériel.

     **Métrologie** : calibrage, étalonnage, conformité, détails et gestion des sondes.

     - **Surveillance** : courbes et suivi des relevés, gestion des alarmes.

     **Datalogger** : section dédiée à l’utilisation des sondes de transport.

Selon le profil de l’utilisateur connecté, l’accès à certains modules du logiciel peut être bloqué ou restreint. Ce

paramétrage est défini par les personnes disposant d’un compte administrateur (référents métrologie, responsables

qualités, etc…).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 6 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

Ce manuel se concentre sur le module Métrologie et présente un système VigiTemp existant et paramétré (sondes

calibrées et étalonnées, lieux créés et surveillés, etc.…).

Sauf mention contraire (pour les nouvelles fonctions), il s’agit ici du manuel VigiTemp Métrologie Version 10.122.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 7 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

b) Ecran principal

A l'ouverture de l'écran de métrologie, les tableaux récapitulatifs du système de surveillance apparaissent :

Il s’agit, notamment, d’un résumé des différents critères et choix métrologiques appliqués à la surveillance en cours.

Il est possible, à partir du tableau principal, d'accéder à la fiche de paramétrage d'un lieu (gestion du lieu accessible

également depuis la partie Administration ou depuis la partie Surveillance).

Pour cela il suffit de double cliquer sur la ligne correspondante au lieu voulu. Voir P10 pour plus de détails.

Chaque partie de cet écran est détaillée ci-après :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 8 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

**(1)** : Lieu affecté : Il s'agit du lieu paramétré (dans VigiTemp, le lieu est l'élément surveillé).

Son statut **(14)** peut être en surveillance ou désactivé.

Si le lieu est en surveillance, une sonde lui est forcément affectée **(2)** .

Si la surveillance est désactivée, une sonde n'est pas forcément liée au lieu (ex : Lieu réformé).

**(2)** : Sonde : Il s'agit de l'élément physique et actif de surveillance du lieu.

Les sondes sont identifiées dans VigiTemp par un numéro de série unique.

Par exemple le n° de série IEE3FL signifie : sonde de type IE dont l'adresse est E3FL.

Une sonde est forcément liée à un lieu dont la surveillance est active. Si une sonde n'est associée à aucun lieu, cela

signifie qu'elle est disponible pour surveiller un nouveau lieu ou un lieu existant dont la sonde initiale serait en panne par

exemple.

**(3)** : Conformité : Cette colonne indique les différentes décisions de conformité selon le choix des règles de calcul de

l'EMT de la sonde en rapport avec l'EMT de l'équipement surveillé (voir à partir de P15 & P25 plus de détails).

Les différentes conformités sont les suivantes : **Non applicable**, **Alerte**, **Non Conforme**, **Conforme**, **Conforme** .

**(4) (5) (6)** : Paramétrage actuel de : consigne de surveillance du lieu, tolérance inférieure et supérieure

(Valeurs adaptées selon les choix d'EMT de la sonde effectués, voir P15 pour plus de détails).

**(7)** : Date d'étalonnage de la sonde affectée au lieu (en rouge si la date est supérieure à 365 jours, sinon en vert).

**(8)** : Erreur de justesse de la sonde, calculée lors de son étalonnage.

**(9)** : Incertitude d'étalonnage de la sonde, calculée lors de son étalonnage.

**(10)** : Correction de l'erreur de justesse sur la mesure de surveillance :

Case cochée ou non selon les choix d'EMT de la sonde effectués (Voir P15 pour plus de détails).

**(11)** : Prise en compte de la dérive dans l'incertitude de la sonde.

**(12)** : Valeur de la dérive de la sonde

**(13)** : Incertitude de mesure de la sonde. Cette valeur est la résultante des choix d'EMT de la sonde effectués, voir P15

pour plus de détails.

**(14)** : Statut : Détail de l'état de surveillance (en surveillance ou désactivé) et détail de la conformité selon les choix d'EMT

de la sonde effectués (voir P25 plus de détails).

**(15)** : Tableau général des alarmes : Liste de tous les lieux pour lesquels au moins une alarme n'est pas acquittée. Le

double-clic sur une ligne permet d'ouvrir le tableau de gestion des alarmes du lieu concerné avec possibilité

d'acquittement.

**(16)** : Tableau des sondes dont l'étalonnage initial est dépassé d'au moins 365 jours. Le double-clic sur une ligne du

tableau permet de lancer le processus d'étalonnage de la sonde concernée (Voir P44 pour plus de détails).

**(17)** : En approchant la souris du côté gauche de l'écran, un bandeau déroulant permet d'accéder à différentes

fonctionnalités (voir à partir de la P26 plus de détails).

**(18)** : Bouton permettant de couper temporairement l'alarme sonore sur le PC

(Réactivation automatique au bout de 10 minutes par défaut).

**(19)** : Options classiques de réduction, agrandissement et fermeture de la fenêtre.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 9 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

c) Fiche lieu / Onglet général

**1)** Nom du Lieu (20 caractères maximum).

**2)** Commentaires sur le Lieu (toute information éventuellement utile, visible uniquement sur cette fiche).

**3)** Sélection d’un site (si la structure se compose de plusieurs sites). Le bouton + permet d'accéder à la liste des sites

et d'en ajouter si besoin. Cette notion est ici purement informative et n’a pas d’influence sur la surveillance.

**4)** Sélection du ou des groupes auxquels appartient le Lieu. Le bouton + permet d'accéder à la liste des groupes et

d'en rajouter éventuellement.

**5)** Sélection d’un plan et d’une localisation via le bouton Plan et possibilité de supprimer une précédente localisation.

**6)** Module d’alarme associé au lieu (il s'agit de boitiers type gyrophare ou sonore pouvant être ajoutés sur une

installation VigiTemp). En cas d’alarme sur le lieu, le boitier s’actionne.

Table des matières **Dernière MAJ : 01/04/2020** - **Page 10 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

**7)** Sélection d’un document (ex : rapport de cartographie de l’appareil surveillé) si l’on souhaite le stocker dans

VigiTemp et l'associer au lieu en cours de paramétrage.

**8)** Réglage des consignes de surveillance. Seule la consigne centrale (ou cible) est obligatoire. La consigne supérieure

et la consigne inférieure permettent de déterminer les seuils à partir desquels des alarmes pourront se déclencher.
Concernant les réglages de pré-alarme, il s’agit d’une option facultative d’affichage en surveillance (couleur jaune)
qui se déclenche pour tout relevé au-delà des seuils fixés. Ce n’est pas une « vraie » alarme nécessitant un
acquittement mais plutôt un avertissement pour l’utilisateur.

**9)** Réglage du retard d’alarme haut pour le lieu concerné (temporisation avant déclenchement de l'alarme, 60 minutes

par défaut). Dans l’exemple, le retard d’alarme a été fixé à 120 minutes. L’alarme de dépassement du seuil
supérieur se déclenchera s’il y a au moins 120 minutes de relevés consécutifs au-delà de +30°C.

**10)** Réglage du retard d’alarme bas pour le lieu concerné (temporisation avant déclenchement de l'alarme, 60 minutes

par défaut). Dans l’exemple, le retard d’alarme a été fixé à 60 minutes. L’alarme de dépassement du seuil inférieur
se déclenchera s’il y a au moins 60 minutes de relevés consécutifs en-deçà de +15°C.

**11)** Réglage de la fréquence des mesures pour le lieu concerné (15 minutes par défaut).

**A savoir :**

     Cet onglet de paramétrage est l’un des plus importants dans VigiTemp car il conditionne, notamment, les
déclenchements d’alarmes par l’intermédiaire des critères consignes et retards d’alarme.

     Chaque lieu dispose de son propre paramétrage. On peut donc appliquer des conditions de surveillance

différentes selon la criticité de l’élément surveillé.

     A l’installation d’un système VigiTemp, un paramétrage par défaut est appliqué pour chacun des lieux. Il
conviendra aux référents administrateurs de l’application d’affiner et personnaliser les réglages en fonction

des besoins.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 11 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

d) Fiche lieu / Onglet métrologie (présentation générale)

_(Capture d’écran VigiSurv 10.200, présence du bouton SAV)_

**(1)** Choix de la sonde associée au lieu surveillé (par son numéro de série).

**(2)** Informations sur les données métrologiques de la sonde, issues de son étalonnage (Erreur de justesse, Incertitude

et Dérive).

**(3)** Rappel des consignes paramétrées dans l'onglet général.

**(4)** Choix des règles de calcul de l’EMT de surveillance. Selon le choix effectué, les tolérances seront adaptées **(5)** .

Dix possibilités de paramétrage sont possibles, voir à partir de P15 pour plus de détails (par défaut Sans objet).

**(6)** Choix de la prise en compte de l'erreur de justesse dans la mesure (en lien avec le choix des règles de calcul de

l'EMT).

**(7)** Choix de la prise en compte de la dérive dans l'incertitude (en lien avec le choix des règles de calcul de l'EMT).

**(8)** Accès au suivi SAV de la sonde en lien direct avec la Gestion de Parc Matériel SMILE.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 12 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

e) Fiche lieu / Onglet Téléphonie-Planning

**(1)** : Lié à l’option VigiTel / VigiMail (formation dispensée en cas d’acquisition de l'option). Une documentation

spécialement dédiée à cette fonction est disponible sur simple demande au 04.73.28.55.60 ou vigitemp@mc2lab.fr

**(2)** : Mise en place d'un planning de changement de consignes pour le lieu actuel

Le planning des consignes permet d'effectuer de manière automatique un changement des consignes de surveillance

selon un planning hebdomadaire à définir. Dans notre exemple les consignes du lieu sont les suivantes :

20° +/- 5° du lundi 07:00 au vendredi 18:00

10° +/- 5° du vendredi 18:00 au lundi 07:00

Les consignes (et seuils d'alarme) changent donc automatiquement aux jours et horaires définis. L'échelle des graphiques

s'adapte au niveau de la surveillance.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 13 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

**(1)** : Activer le planning des consignes.

**(2) (3)** : Définir les jours et heures de changement (un seul changement possible par jour).

**(4** ) : Remplir, pour chaque jour, la consigne et limites mini et maxi. Les jours pour lesquels un horaire de changement a

été défini, remplir avec les données avant/après heure de changement.

**(5)** : Définir un retard d'alarme de changement de consigne = Temps laissé à la sonde pour obtenir une stabilisation de

relevé sans déclenchement d'alarme intempestive.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 14 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

f) Fiche lieu / Onglet métrologie (présentation détaillée)

Différents choix peuvent être effectués au niveau des règles de calcul de l'EMT de la sonde et des tolérances du lieu.

−
_Cas 1a : Les EMT obéissent à la règle du quart / sans correction de l'erreur de justesse_

L'EMT de la sonde est fixé au quart de l'EMT de l'équipement (5°C dans notre exemple, donc EMT sonde = 5/4 = 1.25). Ce

calcul est appliqué automatiquement sur les seuils de tolérances.

L'erreur de justesse n'est pas appliquée sur la mesure de surveillance.

En cas de non-conformité (si |Erreur de Justesse|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur

l’écran principal de la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 15 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 1b : Les EMT obéissent à la règle du quart /avec correction de l'erreur de justesse_

L'EMT de la sonde est fixé au quart de l'EMT de l'équipement (5°C dans notre exemple, donc EMT sonde = 5/4 = 1.25). Ce

calcul est appliqué automatiquement sur les seuils de tolérances.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée directement sur

la mesure effectuée.

En cas de non-conformité (|Dérive|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur l’écran principal de

la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 16 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 2a : EMT saisi manuellement /sans correction de l'erreur de justesse_

L'EMT de la sonde peut être saisi de manière manuelle (déduit par exemple selon des méthodes de calcul interne ou basé

sur les données issues de l'étalonnage, l'erreur de justesse devant être prise en compte dans ce calcul).

Dans notre exemple la saisie d'un EMT de la sonde à 0.55 corrige automatiquement les seuils de tolérances.

En cas de non-conformité (si |Erreur de Justesse|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur

l’écran principal de la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 17 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 2b : EMT saisi manuellement /Avec correction de l'erreur de justesse_

L'EMT de la sonde peut être saisi de manière manuelle (déduit par exemple selon des méthodes de calcul interne ou basé

sur les données issues de l'étalonnage).

Dans notre exemple la saisie d'un EMT de la sonde à 0.30 corrige automatiquement les seuils de tolérances.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée directement sur

la mesure effectuée.

En cas de non-conformité (|Dérive|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur l’écran principal de

la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 18 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 3a : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse / sans_

_prise en compte de la dérive dans l'incertitude :_

Dans cet exemple on choisit d'appliquer l'incertitude d'utilisation de la sonde (issue de son étalonnage) sans prise en

compte de l’erreur de justesse sur la mesure de surveillance et sans prise en compte de la dérive.

L'équation suivante est appliquée : 𝐼𝑚𝑒𝑠 =| 𝐸𝑗 |+ 𝐼𝑒𝑡 soit dans notre exemple 𝐼𝑚𝑒𝑠 = 0.29 + 0.20=0.49

Les seuils de tolérance sont adaptés automatiquement. Lors du prochain étalonnage, après insertion des nouvelles

données, l'EMT de la sonde sera mis à jour automatiquement (ainsi que les tolérances).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 19 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 3b : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse / sans_

_prise en compte de la dérive dans l'incertitude :_

Dans cet exemple on choisit d'appliquer l'incertitude d'utilisation de la sonde (issue de son étalonnage) avec prise en

compte de l’erreur de justesse sur la mesure de surveillance et sans prise en compte de la dérive.

L'équation suivante est appliquée : 𝐼𝑚𝑒𝑠 = 𝐼𝑒𝑡 soit dans notre exemple 𝐼𝑚𝑒𝑠 = 0.20

Les seuils de tolérance sont adaptés automatiquement.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée directement sur

la mesure effectuée.

Lors du prochain étalonnage, après insertion des nouvelles données, l'EMT de la sonde sera mis à jour automatiquement

(ainsi que les tolérances). Idem concernant l'erreur de justesse.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 20 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 3c : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse / avec_

_prise en compte de la dérive dans l'incertitude :_

Dans cet exemple on choisit d'appliquer l'incertitude d'utilisation de la sonde (issue de son étalonnage) avec prise en

compte de l’erreur de justesse sur la mesure de surveillance et avec prise en compte de la dérive dans le calcul

d'incertitude.

L'équation suivante est appliquée :


𝐼𝑚𝑒𝑠= 2 [√]
~~(~~


+
~~(~~


𝐷𝑒𝑟𝑖𝑣𝑒


soit dans notre exemple 2 [√]
~~(~~


0.20


2 [)]


+
~~(~~


−0.04


2 [)]


~~√~~ 3 [)]


~~√~~ 3 [)]


2


𝐼𝑒𝑡


2


2


2


= 0.21


Les seuils de tolérance sont adaptés automatiquement.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée directement sur

la mesure effectuée.

Lors du prochain étalonnage, après insertion des nouvelles données, l'EMT de la sonde sera mis à jour automatiquement

(ainsi que les tolérances). Idem concernant l'erreur de justesse. Une nouvelle valeur de dérive sera appliquée au calcul.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 21 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 3d : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse / avec_

_prise en compte de la dérive dans l'incertitude :_

Dans cet exemple on choisit d'appliquer l'incertitude d'utilisation de la sonde (issue de son étalonnage) sans prise en

compte de l’erreur de justesse sur la mesure de surveillance et avec prise en compte de la dérive dans le calcul

d'incertitude.

L'équation suivante est appliquée :


𝐼𝑚𝑒𝑠= |𝐸𝑗| + 2 [√]
~~(~~


+
~~(~~


𝐷𝑒𝑟𝑖𝑣𝑒


soit dans notre exemple |0.29| + 2 [√]
~~(~~


0.20


2 [)]


+
~~(~~


−0.04


2 [)]


~~√~~ 3 [)]


2


~~√~~ 3 [)]


2


𝐼𝑒𝑡


2


2


= 0.49


Lors du prochain étalonnage, après insertion des nouvelles données, l'EMT dela sonde sera mis à jour automatiquement

(ainsi que les tolérances). Idem concernant l'erreur de justesse. Une nouvelle valeur de dérive sera appliquée au calcul.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 22 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 4a : Sans objet / sans correction de l'erreur de justesse_

Dans cet exemple aucun paramétrage n'a été sélectionné concernant l'EMT de la sonde.

Il n'y a au **c** une correction apportée sur la mesure et sur les tolérances. Le choix de ce paramétrage doit pouvoir se

justifier.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 23 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

−
_Cas 4b : Sans objet / avec correction de l'erreur de justesse_

Dans cet exemple aucun paramétrage n'a été sélectionné concernant l'EMT de la sonde.

Il n'y a au **c** une correction apportée sur les tolérances. La valeur relative de l'erreur de justesse arrondie au centième (
0.29 dans notre exemple) sera appliquée directement sur la mesure effectuée.

Le choix de ce paramétrage doit pouvoir se justifier.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 24 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : II. VigiSurv – Métrologie : Accès – Page principale – Fiche Lieu

g) Récapitulatif des différents cas possibles de conformité selon le choix EMT sélectionné :




|CAS|CHOIX|Correction Ej|Prise en compte dérive|Conformité|
|---|---|---|---|---|
|1A|1|Non|Oui (imposé)|Non conforme si |Ej| + Iet > EMT sonde|
|1A|1|Non|Oui (imposé)|Conforme si |Ej| + Iet < EMT sonde|
|1B|1|Oui|Oui (imposé)|Non conforme si |dérive| + Iet > EMT sonde|
|1B|1|Oui|Oui (imposé)|Conforme si |dérive| + Iet < EMT sonde|
|2A|2|Non|Oui (imposé)|Non conforme si |Ej| + Iet > EMT sonde|
|2A|2|Non|Oui (imposé)|Conforme si |Ej| + Iet < EMT sonde|
|2A|2|Non|Oui (imposé)|Conforme : EMT choisie > 1/4 EMT équipement|
|2B|2|Oui|Oui (imposé)|Non conforme si |dérive| + Iet > EMT sonde|
|2B|2|Oui|Oui (imposé)|Conforme si |dérive| + Iet < EMT sonde|
|2B|2|Oui|Oui (imposé)|Conforme : EMT choisie > 1/4 EMT équipement|
|3A|3|Non|Non|Alerte si Incertitude de mesure > 1/4 équipement<br>Sinon Non applicable (Le choix de la prise en compte<br>de l'incertitude de mesure n'entraine pas de décision<br>de conformité)|
|3B|3|Oui|Non|Non|
|3C|3|Oui|Oui|Oui|
|3D|3|Non|Oui|Oui|
|4A|4|Non|Non applicable|Non applicable|
|4B|4|Oui|Non applicable|Non applicable|


Table des matières **Dernière MAJ : 01/04/2020** - **Page 25 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils
## III. VigiSurv – Métrologie : Bandeau déroulant – Outils

En approchant la souris sur le côté gauche de l'écran, un bandeau déroulant apparait.

|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(1) : Accès à la section Administration (Sous condition d'avoir<br>les droits d'accès). Voir manuel correspondant.|
|---|---|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(2) : Accès à la section Surveillance (Sous condition d'avoir les<br>droits d'accès). Voir manuel correspondant.|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(3) : Accès à la section Datalogger (Sous condition d'avoir les<br>droits d'accès). Voir manuel correspondant.|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(4) : Accès au tableau général des alarmes (en cours ou non<br>acquittées).|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(5) : Accès à la gestion des étalons.|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(6) : Accès à la gestion des milieux d'étalonnage.|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(7) : Accès au tableau général de la gestion des sondes.|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(8) : Accès au module de calibrage des sondes<br>(À l'aide d'une sonde étalon).|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(9) : Accès au calibrage des sondes par fichiers externes<br>(Fournis par le laboratoire MC2).|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(10) : Accès au module d'étalonnage des sondes<br>(À l'aide d'une sonde étalon).|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(11) : Accès à l'étalonnage des sondes par fichiers externes<br>(fournis par le laboratoire MC2)|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(12) : Accès à l'historique des mesures des lieux.|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(13) : Accès à l’outil d’analyse d’impact.|
|(Capture d’écran VigiSurv 10.200, présence du bouton Analyse d’impact)|(14) : Accès aux tableaux récapitulatifs des configurations<br>VigiTemp (avec possibilités d'exports Excel).|



Table des matières **Dernière MAJ : 01/04/2020**  - **Page 26 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

a) Gestion des alarmes

Le tableau liste toutes les alarmes non acquittées actuellement présentes dans le système (alarmes en cours et alarmes

terminées non acquittées). Pour acquitter une alarme, il faut sélectionner la ligne voulue **(1)** puis cliquer sur le bouton

d'acquittement **(2)** .

En cochant la case **(3)** (avant acquittement), on fait apparaitre le graphique correspondant à l'alarme.

Après avoir appuyé sur le bouton d'acquittement, une dernière fenêtre apparait. Il s'agit de la fenêtre de traçabilité de

l'alarme en cours d'acquittement.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 27 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

L'alarme sélectionnée a bien été acquittée :

Fermer la fenêtre de gestion des alarmes pour revenir à l'écran principal de la Métrologie.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 28 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

b) Gestion des étalons

Ce tableau permet :

- De déclarer une sonde étalon dans le système VigiTemp

- De modifier une sonde étalon existante (en la sélectionnant préalablement dans la liste)

- D'archiver une sonde étalon existante (en la sélectionnant préalablement dans la liste)

- De tester le fonctionnement d'une sonde étalon (en la sélectionnant préalablement dans la liste, type VigiTemp SEF

uniquement)

−
_Déclarer une nouvelle sonde étalon dans le système :_

Exemple pour une sonde de type Externe (sonde étalon non fournie par MC2, permettant de calibrer des sondes dans

VigiTemp mais ne permettant pas leur étalonnage) :

Remplir tous les champs avec les spécificités délivrées par le fournisseur de la sonde puis valider la fiche.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 29 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Exemple pour une sonde de type VigiTemp SEF (sonde étalon fournie par MC2, permettant de calibrer et étalonner des

sondes dans VigiTemp) :

Remplir tous les champs avec les informations fournies sur le certificat d'étalonnage de la sonde étalon.

Le champ module par défaut correspond au module de communication qui sera utilisé par la sonde étalon. Ce choix peut

être modifié par la suite.

Le champ résolution est fixé par défaut. Le champ incertitude reprend l'incertitude maxi des différents points saisis.

Valider la fiche pour terminer la déclaration de la sonde étalon VigiTemp SEF.

−
_Modifier une sonde étalon existante :_

Modifier les informations de la sonde (suite à son nouvel étalonnage par exemple).

− _Archiver une sonde étalon existante :_

Supprimer une sonde étalon du système lorsque celle-ci n'est plus utilisée.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 30 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

−
_Tester une sonde étalon type VigiTemp SEF :_

Le test se déroule de la façon suivante :

Choix de la désactivation de la surveillance générale pendant la durée du test :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 31 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Déroulement du test :

Il s'agit d'un test de lecture de la sonde étalon, les valeurs lues s'inscrivent au fur et à mesure dans le tableau.

Le test doit être arrêté avec le bouton STOP.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 32 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

c) Gestion des milieux

Cette partie permet de gérer les milieux d'inter-comparaison utilisés pour la réalisation de calibrage ou étalonnage.

A l'ouverture, un rappel métrologique sur les milieux d'inter-comparaison apparait. Appuyer sur la flèche > pour passer à

l'étape suivante.

Il est ensuite possible :

- D'ajouter un nouveau bain/milieu

- Modifier un bain/milieu existant

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 33 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

−
_Ajouter un nouveau bain / milieu_

Il s'agit de remplir une fiche avec les spécificités du bain/milieu que l'on souhaite ajouter (voir avec spécificités

fournisseur).

Puis valider.

−
_Modifier un bain/milieu existant_

Sélectionner le bain dans la liste puis modifier les informations voulues.

Valider.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 34 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

d) Gestion des sondes

La gestion des sondes permet d'accéder à un tableau récapitulatif de l'ensemble des sondes présentes dans le système.

Il est possible d'effectuer un classement de ce tableau en cliquant sur la colonne voulue (classement par Adresse, N° de

série, Port série et module, Etat et Lieu associé). **(1)**

A la sélection d'une sonde dans la liste il est possible :

- D'effectuer une modification au niveau de l'association sonde/module de dialogue. **(2)**

- De réformer une sonde qui ne serait plus présente dans l'installation. **(3)**

- D'accéder aux rapports de calibrage et étalonnage de la sonde (avec possibilité de supprimer des anciens étalonnages).

**(4), (5), (6)**

Il est également possible d'exporter ou imprimer la liste complète des sondes. **(7)**

_Voir manuel dédié à l’Administration pour plus de détails sur ce tableau._

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 35 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

e) Calibrer une sonde

Cette fonction permet de réaliser le calibrage d'une ou plusieurs sondes à l'aide d'une sonde étalon.

Par exemple, pour une sonde de température, le calibrage consiste à faire la relation entre la température indiquée par

un étalon (voir sonde étalon) et le signal numérique mesuré de la sonde calibrée (sonde fille).

Cette relation est linéaire dans le cas de sondes linéaires ou polynomiales dans le cas des sondes platines.

Dans tous les cas, une relation linéaire est déterminée et les coefficients sont exploités soit sous la forme d’une droite,

soit au travers de la relation de Callendar Van Dusen (cas des sondes platine).

Le principe du calibrage consiste à mesurer le signal numérique en deux points de températures encadrant la plage

d’utilisation.

Dans le cas de l’utilisation des sondes pour des températures négatives, il est fortement conseillé de calibrer la sonde en

au moins un point négatif.

Exemples :

- Pour une utilisation à +40°C, le calibrage peut se faire à +10°C et +60°C.

- Pour une utilisation à +5°C, le calibrage peut se faire à 0°C et +20°C.

- Pour une utilisation à -10°C, le calibrage peut se faire à -20°C et +40°C.

- Pour une utilisation à -80°C, le calibrage peut se faire à -80°C et +40°C.

- Pour une utilisation entre +5°C et +100°C, le calibrage peut se faire à 0°C et +110°C.

Lors de ce calibrage, le logiciel détermine la nouvelle relation entre le signal mesuré et la température indiquée. On

retrouvera sur le rapport de calibrage les températures obtenues avec la relation T=f(signal) avant calibrage et T=f(signal)

après calibrage excepté lors du premier calibrage de la sonde.

Le calibrage permet également de minimiser l’erreur de justesse de la sonde. L’erreur résiduelle sera intégrée à

l’incertitude d’étalonnage et donc d’utilisation de la sonde.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 36 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

A l'entrée dans la fonction calibrage, la fenêtre suivante apparaît :

Cette fenêtre permet de sélectionner les sondes que l'on souhaite calibrer (plusieurs sondes peuvent être sélectionnées

en gardant la touche ctrl appuyée).

Cliquer sur lorsque la sélection est terminée, valider le message de confirmation.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 37 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

**Attention :**

     Certains types de sonde ne peuvent être calibrés en même temps (Exemple : sonde de type EN et GN...), le

logiciel préviendra dans tous les cas.

     S'assurer que les sondes sélectionnées sont toutes de même type de mesure : uniquement température, ou

uniquement CO2, ....

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 38 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

L'écran de traitement apparait :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 39 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

En haut de cet écran, on retrouve :

     Date du calibrage (remplie automatiquement)

     Opérateur (saisie obligatoire)

     Nombre de décimal d'affichage : 1 par défaut

     Sélectionner l'étalon (liste préremplie, tous les champs seront renseignés automatiquement après sélection).

     Sélection du milieu de comparaison (liste préremplie, tous les champs seront renseignés automatiquement

après sélection).

Lorsque tous les champs sont renseignés, il faut lancer la lecture :

Le plateau de stabilité apparait uniquement si l'on utilise un étalon VigiTemp, cela permet de s'assurer de la stabilité du

contexte de mesure. Une barre de progression permet de visualiser le plateau.

Lorsque le plateau de stabilité est atteint (stabilité respectée pendant la durée définie), le point de calibrage est pris, la

mesure des sondes est alors égale à la mesure lue par l’étalon et le signal numérique est égal au signal lu par la ou les

sondes à calibrer.

Une fois terminé, les points peuvent être enregistrés. Si un étalon externe est utilisé, il convient de s'assurer de sa

stabilité.

Le second point peut alors être lancé, en réitérant les mêmes opérations.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 40 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

: Affiche la mesure de l'étalon. Si un étalon externe est utilisé, il faut saisir cette valeur.

: Affiche la mesure obtenue avec l'ancien calibrage s'il existe.

: Affiche le signal numérique renvoyé par la sonde (ou non réponse si pb de

communication).

: la sonde répond

: problème de lecture

Lorsque tout est correct, valider le premier point .

La valeur du premier point s'affiche :

Effectuer les mêmes opérations pour le second point.

Une fois les 2 points enregistrés, le bouton d'enregistrement des calibrages apparaît :

Cliquer dessus pour enregistrer les calibrages obtenus pour les sondes sélectionnées, un rapport pourra être édité.

**Attention :**

     Un écart de mesure de l'étalon d'au moins 10% est nécessaire entre les 2 points

     Aucun calibrage ne sera enregistré pour les sondes ne répondant pas.

     Le calibrage enregistré sera dorénavant le calibrage en cours utilisé dans la surveillance d’une sonde active.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 41 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

f) Calibrage par fichier externe

Cette fonction permet d'intégrer les valeurs de calibrage de sondes à l'aide de fichiers informatiques préformatés.

Lors de l'installation initiale d'un système VigiTemp, ou en cas d’ajout de sondes sur un système existant, les fichiers de

calibrage à intégrer permettent de déclarer les sondes dans le système.

La manipulation est assez simple. Il suffit, avec le bouton loupe, de parcourir l'ordinateur jusqu'à l'emplacement des

fichiers de calibrage. Il est possible de sélectionner et charger plusieurs fichiers à la fois.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 42 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Une fois les fichiers sélectionnés, il faut choisir dans la liste déroulante qui apparait le module de réception qui servira au

dialogue avec les sondes puis terminer avec le bouton calibrer.

Note : l'association sonde/module peut être modifiée à partir de la section Gestion des sondes (voir P35).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 43 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

g) Etalonner une sonde

L’étalonnage d’une sonde VigiTemp se fait en un seul point. L’utilisateur peut effectuer autant d’étalonnage en un point

qu’il le désire afin de connaître les incertitudes des sondes étalonnées en chaque point d’utilisation.

L’objectif de cet étalonnage est d’effectuer le raccordement aux étalons nationaux et de déterminer l’incertitude

d’étalonnage de la sonde VigiTemp.

L’étalonnage se fait uniquement à l’aide d’un étalon VIGITEMP (fourni en option).

Cet étalon a fait l’objet d’un étalonnage et son certificat est enregistré dans le logiciel (voir P29 Gestion des étalons).

**Attention :**

     Seule une sonde calibrée peut être étalonnée.

     Au moins un milieu d’inter-comparaison (ou bain d’étalonnage) doit avoir été créé (voir P33).

A l'entrée dans la fonction étalonnage, la fenêtre suivante apparaît :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 44 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Sélectionner 1 ou plusieurs sondes à étalonner (en gardant la touche ctrl enfoncée) puis cliquer sur :

Valider le message de confirmation.

**Attention** : il n'est pas possible d'étalonner simultanément des sondes de type différent.

A l’apparition de l’écran suivant, il faut sélectionner l’étalon VigiTemp et le milieu d’étalonnage utilisé. Les différents

champs concernant ces éléments seront renseignés automatiquement.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 45 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Lancer la lecture

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 46 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

L’étalon fait des mesures régulières, dès que ces mesures sont stables, l’étalonnage peut être lancé :

.

10 mesures espacées de 30 secondes au minimum seront enregistrées pour chaque sonde.

Une barre de progression indique l'état d'avancement de l'étalonnage :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 47 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Lorsqu'un étalonnage est terminé, le résultat s'affiche présentant l’incertitude obtenue :

Cliquer sur le bouton pour les enregistrer et valider l'étalonnage ou sinon le bouton

Fermer pour annuler l’étalonnage si celui-ci n’est pas conforme.

À la suite de la réalisation de l’étalonnage, les données métrologiques de la ou des sondes sont mises à jour.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 48 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

h) Etalonner une sonde par fichier externe

Cette fonction permet d'intégrer les valeurs d'étalonnage de sondes à l'aide de fichiers informatiques préformatés.

Ces fichiers sont mis à disposition lors de l'installation de sondes étalonnées par MC2 (en atelier ou sur site par un

technicien).

La manipulation est assez simple. Il suffit, avec le bouton loupe, de parcourir l'ordinateur jusqu'à l'emplacement des

fichiers d'étalonnage. Il est possible de sélectionner et charger plusieurs fichiers à la fois.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 49 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

A savoir :

     Si, au moment du chargement des fichiers d’étalonnage, les sondes concernées sont affectées à des lieux, les

données métrologiques affichées dans la fiche de ces lieux (onglet métrologie) seront mises à jour (voir P12).

Il conviendra cependant, à l’utilisateur, de vérifier l’application correcte des nouvelles valeurs sur chaque

fiche.

     Le lien entre les fichiers et les sondes concernées se fait à l’aide du numéro de série unique pour chaque

sonde, contenu à l’intérieur de chaque fichier.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 50 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

i) Historique des mesures

_(Captures d’écran VigiSurv 10.200)_

**(1)** : Choix du lieu et de la période de recherche / Option mesure ou moyenne / Outils

**(2)** : Tableau des évènements sur la période choisie

**(3)** : Graphique et table des mesures sur la période choisie

**(4)** : Outils d’export

Table des matières **Dernière MAJ : 01/04/2020** - **Page 51 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Pour effectuer une recherche sur une période précise, après choix du lieu, renseigner les différents champs date/heure

disponibles puis appuyer sur rechercher. **Attention, plus la période est étendue, plus les résultats seront longs à charger**

**et afficher.**

Deux modes sont disponibles :

‘Mesure’ = recherche et affichage des différents relevés effectués pour ce lieu sur la période.

‘Moyenne’ = recherche et affichage des différentes moyennes glissantes calculées sur la période pour ce lieu.

A chaque relevé effectué, une moyenne glissante pour la dernière heure est réalisée et stockée dans la base de données.

Il y a donc autant de valeurs de moyenne que de mesures.

Ceci permet de dégager une tendance générale en lissant, notamment, des épisodes sporadiques ou relevés isolés

potentiellement négligeables. Le but est d’appréhender les vitesses de variations de température par exemple, afin de

juger si les éléments conservés ont subi un stress thermique (ou choc thermique) pouvant engendrer une dégradation.

Les résultats sont graphiquement visibles sur la partie courbe de l’écran. **(3)**

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 52 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Exemple pour la même période :

Il est possible d’effectuer un zoom sur une partie de la courbe en l’encadrant avec la souris.

Au-dessus des courbes, un onglet permet de basculer sur les tableaux de mesures ou moyennes glissantes (selon le mode

choisi dans la recherche initiale).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 53 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

A partir de ces tableaux, il est possible de sélectionner une valeur pour suppression. Une fois la valeur sélectionnée,

renseigner le mot de passe (défini par l’administrateur) puis appuyer sur le bouton correspondant.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 54 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Le tableau des événements **(2)** présente la liste de toutes les actions tracées automatiquement par le serveur (ex :

Démarrage de la surveillance) ou à la suite d’une saisie par un utilisateur (ex : acquittement d’alarme) sur la période de

recherche. Dans le cas de la saisie par un utilisateur, son identifiant apparait à la ligne correspondante :

Un évènement peut être ajouté manuellement : (la date et heure de l’événement peuvent être modifiées)

Les différents tableaux et écrans présentés dans ce paragraphe peuvent être exportés à l’aide des boutons disponibles en

bas de l’écran :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 55 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Le clic sur l’un de ces boutons ne génère pas une impression papier immédiate mais ouvre un éditeur à l’écran avec des

outils de mise en page et/ou annotations, export vers différents format (PDF, tableur, pièce jointe…) ou impression papier.

Fermer l’éditeur pour revenir à la page précédente.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 56 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

j) Analyse d’impact

_(Capture d’écran VigiSurv 10.200, fonction Analyse d’impact)_

Depuis VigiSurv 10.200 il est possible à l’utilisateur métrologue de réaliser l’analyse d’impact sur des mesures antérieures

en intervenant sur les valeurs de tolérances paramétrées.

Cela permet :

     De visualiser, a posteriori, les mesures et temps d’alarme en prenant en compte les nouvelles valeurs

d’étalonnage (pour une sonde donnée, l’étalonnage réalisé à un instant T est applicable pour les relevés

effectués par cette sonde depuis l’étalonnage précédent et jusqu’à cet instant).

     - De voir si une enceinte est utilisable avec des tolérances de surveillance différente

Présentation de l’outil :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 57 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Haut du tableau :

**(1)** Sélection du lieu surveillé par la sonde concernée

**(2)** Sélection de la période de recherche

**(3)** Lancer la recherche, le tableau en-dessous affiche les relevés effectués sur la période. Les mesures en alarmes sur

cette période apparaissent en rouge **(6)** .

**(4)** Lors de cette 1 [ère] recherche, les valeurs de tolérances actuellement paramétrées pour le lieu concerné ont été

renseignées automatiquement (il s’agit des valeurs pondérées par l’application d’un réglage EMT, voir P15).

**(5)** Saisir les valeurs de tolérances voulues afin de réaliser la comparaison (Ex : suite à un nouvel étalonnage de

sonde par exemple). Dans l’exemple ci-dessus : tolérance haute actuelle à -10 vs tolérance haute de comparaison

à -11.

**(7)** Actualiser le tableau des relevés pour prise en compte des nouvelles valeurs de tolérance.

**(8)** Le tableau est actualisé, les valeurs en alarme selon le nouveau critère défini, apparaissent en orangé. Cela

permet d’identifier les alarmes ou dépassements qui n’avaient pas été signalés avec les seuils de tolérance

d’origine. Les durées et impacts peuvent être pris en compte.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 58 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

Le bouton **(9)** permet d’ajouter les commentaires issus de cette analyse. Ils seront visibles sous la forme d’un évènement

apparaissant dans le journal du lieu concerné (voir P55).

**A savoir :**

Le tableau des valeurs peut être exporté en faisant un clic droit en haut à droite.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 59 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : III. VigiSurv – Métrologie : Bandeau déroulant – Outils

k) Export config

Cette partie affiche deux tableaux récapitulatifs du système VigiTemp.

**(1)** Liste des lieux par groupes de surveillance avec sondes associées et modules de réception

**(2)** Configuration VigiTel du système (si licence)

**(3)** Export des deux tableaux au format Excel

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 60 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : IV. Hotline et dépannage
## IV. Hotline et dépannage

− _Généralités :_

En cas de défaillance ou problèmes d’ordre matériel ou logiciel, une hotline est à disposition au numéro de téléphone

suivant :

**04-73-28-55-60** (8H30-12H30 / 13H30-17H du lundi au jeudi et 8H30-12H15 le vendredi).

Pour les clients sous contrat, possibilité de joindre la hotline le vendredi de 13h30 à 17H au numéro spécial fourni. Voir

avec votre référent VigiTemp interne ou responsable qualité/métrologie.

Il est également possible d'envoyer un mail à l'adresse **vigitemp@mc2lab.fr** en précisant les informations suivantes :

Nom du laboratoire et/ou du groupement, Ville, Nom et téléphone de la personne à contacter, Descriptif de la demande.

N’hésitez pas à joindre le maximum d’informations et, le cas échéant, une ou des captures d’écran si cela peut aider dans

la résolution du problème.

−
_Vérifications et auto-dépannage :_

Avant de contacter le service hotline, quelques petites vérifications et tests peuvent être effectués sur votre installation :

- S’assurer qu’il n’y a pas de dysfonctionnements d’ordre général de type électrique ou sur le réseau informatique

pouvant entrainer un problème dans la surveillance VigiTemp mais également pour d’autres applications ou matériel.

- Si toutes les sondes apparaissent en alarmes techniques dans la surveillance, réinitialiser la ou les bornes de

réception des sondes (retirer le petit connecteur d’alimentation électrique, attendre quelques secondes puis rebrancher).

Vérifier également le branchement correct de tous les câbles sur ce matériel. Si les erreurs persistent après quelques

minutes contacter la hotline.

- Si une seule sonde apparait en erreur alors que les autres fonctionnent bien, réaliser la même opération de

débranchement/rebranchement électrique sur le boitier de la sonde.

**A savoir :**

Bien connecter l’alimentation sur la sonde uniquement lorsque l’adaptateur secteur est déjà branché dans une prise. De

plus il convient d’utiliser le bon connecteur sur la sonde :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 61 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : IV. Hotline et dépannage

−
_Zoom sur la télémaintenance (Surveillance) :_

Le bouton télémaintenance situé dans la barre d’outils en haut de l’écran principal de la surveillance permet d’afficher le

numéro de téléphone de la hotline :

Après avoir appuyé sur le bouton OK, le logiciel de prise en main à distance TeamViewer est lancé automatiquement (soit

la version MC2 Hotline, soit TeamViewer si ce dernier est déjà installé et exécuté sur le PC) :

Version MC2 Hotline

(incluse avec VigiSurv)

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 62 / 63**

## VigiSurv 10.200 : Manuel d’utilisation – Partie METROLOGIE

En cours : IV. Hotline et dépannage

Version TeamViewer

(si déjà sur le PC)

Il suffit ensuite de communiquer les codes affichés à l’écran (ID et Mot de passe) au technicien hotline afin que celui-ci

puisse prendre la main sur le PC et réaliser les vérifications nécessaires.

**A savoir :**

     Selon le profil et les droits d’accès de l’utilisateur connecté, le bouton télémaintenance n’est pas accessible

(visible mais inactif). Dans ce cas prendre contact avec le(s) référent(s) VigiTemp de votre structure.

     Si le logiciel MC2 Hotline s’ouvre mais n’affiche aucun code (ID et mot de passe) cela peut signifier que ce

type de connexion n’est pas autorisé par votre service informatique.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 63 / 63**

