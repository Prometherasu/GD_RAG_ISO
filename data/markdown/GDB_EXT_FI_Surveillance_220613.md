# VigiSurv 10.200 : Manuel d’utilisation de la surveillance

**I.** **PRESENTATION .................................................................................................................................................................. 3**

A ) L OGICIEL ................................................................................................................................................................................... 3

B ) M ATERIEL ................................................................................................................................................................................. 4

C ) L EXIQUE SUPPLEMENTAIRE ............................................................................................................................................................ 5

**II.** **VIGISURV – SURVEILLANCE : CONSULTATION, SUIVI ET ALARMES ..................................................................................... 6**

A ) O UVERTURE ET CONNEXION .......................................................................................................................................................... 6

B ) E CRAN PRINCIPAL : ...................................................................................................................................................................... 8

−
_Vue générale : .................................................................................................................................................................... 8_

− _Barre d’outils : ................................................................................................................................................................. 10_

−
_Zoom sur la fonction verrouillage : .................................................................................................................................. 11_

−
_Visualisation par groupe : ................................................................................................................................................ 12_

−
_Autres possibilités d’affichage : ....................................................................................................................................... 14_

−
_Sortie/Fermeture de l’application : .................................................................................................................................. 15_

C ) L ES DIFFERENTS ETATS POSSIBLES D ’ UN LIEU ................................................................................................................................... 16

D ) A LARMES ................................................................................................................................................................................ 19

−
_Moyens d’alerte : ............................................................................................................................................................. 19_

−
_Acquittement : ................................................................................................................................................................. 19_

− _Alarmes de service : ......................................................................................................................................................... 21_

**III.** **VIGISURV – SURVEILLANCE : OUTILS ET OPTIONS............................................................................................................. 22**

A ) D ETAILS ET HISTORIQUES : .......................................................................................................................................................... 22

B ) I NDICATEUR D ’ ETALONNAGE DE LA SONDE ..................................................................................................................................... 28

C ) A CTIVATION / D ESACTIVATION DE LA SURVEILLANCE ........................................................................................................................ 29

D ) G RAPHIQUE INSTANTANE ........................................................................................................................................................... 30

E ) V ISUALISATION SUR PLAN ........................................................................................................................................................... 31

F ) B ANDEAU BAS / R ESUME ............................................................................................................................................................ 32

G ) O UTIL SUPERPOSITION DE COURBES .............................................................................................................................................. 32

**IV.** **VIGISURV – SURVEILLANCE : GESTION ET PARAMETRAGES DU LIEU ............................................................................ 34**

A ) F ICHE LIEU / O NGLET GENERAL .................................................................................................................................................... 35

B ) F ICHE LIEU / O NGLET METROLOGIE ( PRESENTATION GENERALE ) ......................................................................................................... 37

C ) F ICHE LIEU / O NGLET T ELEPHONIE -P LANNING ................................................................................................................................ 38

D ) F ICHE LIEU / O NGLET METROLOGIE ( PRESENTATION DETAILLEE ) ......................................................................................................... 40

−
_Cas 1a : Les EMT obéissent à la règle du quart / sans correction de l'erreur de justesse ................................................ 40_

−
_Cas 1b : Les EMT obéissent à la règle du quart /avec correction de l'erreur de justesse................................................. 41_

−
_Cas 2a : EMT saisie manuellement /sans correction de l'erreur de justesse ................................................................... 42_

−
_Cas 2b : EMT saisie manuellement /Avec correction de l'erreur de justesse ................................................................... 43_

−
_Cas 3a : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse / sans prise en_

_compte de la dérive dans l'incertitude : ................................................................................................................................... 44_

−
_Cas 3b : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse / sans prise en_

_compte de la dérive dans l'incertitude : ................................................................................................................................... 45_

−
_Cas 3c : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse / avec prise en_

_compte de la dérive dans l'incertitude : ................................................................................................................................... 46_

−
_Cas 3d : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse / avec prise en_

_compte de la dérive dans l'incertitude : ................................................................................................................................... 47_

−
_Cas 4a : Sans objet / sans correction de l'erreur de justesse ........................................................................................... 48_

−
_Cas 4b : Sans objet / avec correction de l'erreur de justesse ........................................................................................... 49_

**V.** **HOTLINE ET DEPANNAGE ................................................................................................................................................. 50**

− _Généralités : .................................................................................................................................................................... 50_

−
_Vérifications et auto-dépannage : ................................................................................................................................... 50_

− _Zoom sur la télémaintenance : ........................................................................................................................................ 51_

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : I. Présentation VigiTemp
## I. Présentation VigiTemp

a) Logiciel

Le système VigiTemp 10 est une solution client / serveur. Son architecture repose sur une base de données MySQL.

La collecte et la gestion des alarmes sont gérées par la partie serveur, cette dernière se présentant sous la forme

d’un service Windows appelé VigiServ.

L’exploitation des mesures, leur interprétation et les différentes fonctions F.M.E (Fonctions de Métrologie Evoluées)

sont quant à elles gérées par la partie client du logiciel, c’est VigiSurv.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 3 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : I. Présentation VigiTemp

b) Matériel

Le système VigiTemp est composé de divers éléments physiques. Voici la présentation d’un système radio. Il existe

également des possibilités d’installations filaires (modules et sondes sont reliés par câbles).

|PC Serveur<br>Cœur du système VigiTemp comprenant les logiciels :<br>* MySQL (base de données)<br>* VigiServ (service gérant l'interrogation des sondes, les relevés et<br>l'inscription des données<br>* Pilote de gestion de ports COM virtuels pour les bornes ou<br>modules radio/réseau|Col2|
|---|---|
|Les bornes ou modules de réceptions<br>Boitier composé d'une partie radio (pour dialogue avec les sondes)<br>et une partie réseau Ethernet (pour dialogue avec le PC serveur).<br>1 module = 1 adresse IP = 1 port COM virtuel sur le PC serveur||
|Les sondes<br>Ensemble composé de : capteur (T°, C02…) + boitier électronique<br>(gestion des relevés, radiofréquence…) + alimentation électrique.<br>Chaque sonde a son propre numéro de série.<br>Une sonde ne dialogue qu'avec un seul module (association<br>généralement définie selon la proximité géographique des deux<br>éléments) par ondes radio (869.525MHZ).<br>Possibilité de modifier l'association module/sonde, en cas de<br>déplacement de la sonde par exemple.||



Table des matières **Dernière MAJ : 01/04/2020**  - **Page 4 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : I. Présentation VigiTemp

Enfin, les **PC clients** (hébergeant le logiciel de surveillance **VIGISURV** ) : se connectent par le réseau informatique à la

base de données située sur le PC serveur. VigiSurv permet la consultation et gestion en temps réel de la surveillance

du système VigiTemp.

Les deux possibilités d’architecture peuvent être rencontrées :

c) Lexique supplémentaire




|LIEU|Elément surveillé par une sonde (ex : réfrigérateur, congélateur, étuve, salle, …).<br>Un lieu en surveillance est rattaché à une sonde.|
|---|---|
|||
|GROUPE|Permet le classement des lieux : par laboratoires, services, pièces, etc …|
|||
|UTILISATEUR|Compte (login + mot de passe) de connexion à VigiTemp.<br>Un compte peut voir un ou plusieurs groupes en surveillance.<br>Accès au logiciel et droits définis par le profil.|
|||
|PROFIL|Droits d'accès dans le logiciel : Accès intégral ou uniquement à quelques parties du logiciel<br>(ex : Surveillance)|


Table des matières **Dernière MAJ : 01/04/2020** - **Page 5 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes
## II. VigiSurv – Surveillance : Consultation, suivi et alarmes

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

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 6 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

**Ce manuel se concentre sur la partie Surveillance.**

Table des matières **Dernière MAJ : 01/04/2020** - **Page 7 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

b) Ecran principal :

−
_Vue générale :_

La surveillance s’ouvre sur un écran de ce type. Les différentes parties sont détaillées dans les pages suivantes.

En approchant la souris sur le côté gauche de l’écran, un bandeau déroulant apparait automatiquement.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 8 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

L’affichage est modifié comme ceci :

**A savoir :**

Le classement des lieux dans la partie principale se fait dans l’ordre alphanumérique des noms attribués à chacun.

L’attribution des noms est effectuée dans la partie ‘Gestion et paramétrage’ (P34) pour chaque lieu.

S’il y a beaucoup de lieux en surveillance affichés à l’écran, il peut être intéressant d’insérer un préfixe à chaque nom

afin d’obtenir une lecture facilitée.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 9 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

− _Barre d’outils :_

|Col1|Permet d'afficher le numéro de téléphone de la hotline MC2 VigiTemp puis<br>lance un logiciel de prise en main à distance (Teamviewer).<br>Pour plus d'infos sur la hotline, voir la section dédiée de ce document (P50).|
|---|---|
||Bouton actif uniquement sur écran tactile : permet de faire apparaitre le<br>bandeau à gauche de l’écran.|
||Outil de superposition de courbes.<br>Voir P32 pour plus de détails sur cet outil.|
||Permet d'afficher la fenêtre de légende d'un lieu en surveillance.|
||Permet d'accéder au(x) plan(s) chargés dans VigiTemp.<br>Sur ce(s) plan(s) sont matérialisés les lieux pour lesquels un plan a été associé.<br>(Fonction disponible par l'administration)|
||Permet de couper temporairement l'alarme sonore<br>(Réactivation automatique au bout d'un temps prédéfini dans l'administration,<br>10 minutes par défaut).|
||Permet de forcer le verrouillage de l'écran et/ou de changer d'utilisateur.<br>Voir page suivante pour les détails de cette fonction.|
||Permet de réduire, redimensionner ou fermer le programme.|



Table des matières **Dernière MAJ : 01/04/2020** - **Page 10 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

−
_Zoom sur la fonction verrouillage :_

La fonction de verrouillage fonctionne de la manière suivante :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 11 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

−
_Visualisation par groupe :_

Chaque lieu paramétré dans VigiTemp est associé à un groupe de surveillance (ex : par service ou par laboratoire ou

par pièce, etc...).

Le paramétrage de chaque compte utilisateur (dans l'administration) permet de définir les groupes qui pourront être

vus et gérés dans la surveillance pour un utilisateur donné. Il est ainsi possible, dans la surveillance, d'activer une vue

partielle par groupe de lieux.

=> Pas de choix (par défaut) ou Tout voir = l'utilisateur visualise l'ensemble des groupes de sondes auxquels il a

accès.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 12 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

=> Choix d'un groupe pour lequel l'utilisateur a le droit de visualisation.

=> Choix d'un groupe pour lequel l'utilisateur n'a pas le droit de visualisation.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 13 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

−
_Autres possibilités d’affichage :_

|Col1|Permet de dérouler ou enrouler les sections 'Lieu(x) en alarme...'.<br>Quand un lieu est en alarme (en cours ou terminée non acquittée) il apparait à la fois dans les<br>lieux en surveillance et aussi dans une des sections mentionnées ci-dessus (selon son état<br>d'alarme).|
|---|---|
||Permet de changer l'affichage des lieux en surveillance en enlevant les graphiques.<br>L'affichage ci-dessous est obtenu :|
|||
||Rétablit l'affichage avec les graphiques apparents.|



Il existe enfin un mode d’affichage appelé ‘Vision simple’, paramétrable uniquement depuis la partie Administrateur

(Paramètres globaux) et qui s’applique pour l’ensemble des postes disposant de VigiSurv. Cela donne l’affichage

suivant :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 14 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

−
_Sortie/Fermeture de l’application :_

Pour fermer VigiSurv, il faut cliquer, à partir de l’écran principal de la surveillance sur la croix rouge (angle supérieur

droit ou angle inférieur gauche) :

ou

Puis valider la fenêtre de sortie qui apparait en cliquant sur la croix rouge centrale :

Enfin, sur le dernier écran, selon le paramétrage effectué par les référents administrateurs, la saisie du mot de passe

utilisateur ainsi qu’un commentaire de sortie peuvent être obligatoires :

La fermeture de VigiSurv sur le PC n’a pas d’incidence sur la prise de mesure, cette partie étant assurée par le

serveur via le réseau informatique. Cependant les utilisateurs ne seront pas alertés en temps réel des alarmes

éventuelles. Il est conseillé de garder VigiSurv ouvert et réduit dans la barre des tâches Windows.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 15 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

c) Les différents états possibles d’un lieu

En appuyant sur le bouton, en haut à droite de l’écran, la fenêtre de légende suivante apparait :

Les différents états possibles pour un lieu sont présentés en détail ci-dessous :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 16 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

|Col1|Etat normal/standard :<br>Relevé correct situé sous le seuil maxi et au-dessus du<br>seuil mini.|
|---|---|
||Etat Alarme en cours, type dépassement de consigne :<br>Sortie des limites pendant une durée égale ou supérieure<br>au temps de retard d’alarme défini.<br>Le problème est actuel. Une action doit être entreprise<br>pour le corriger.|
||Etat Alarme en cours, type problème technique :<br>Cet état concerne les problèmes sur les bornes de<br>réceptions, de non-réponses de sondes, de défauts<br>capteurs ou d’alimentation.|
||Etat Alarme terminée, non acquittée :<br>Le lieu a été dans l'état Alarme en cours (deux cas<br>précédents) mais le problème est terminé (retour des<br>relevés dans les tolérances définies ou résolution du<br>problème technique).<br>L’alarme n’a pas été acquittée dans le logiciel. Pour<br>repasser dans l'état normal (en bleu) il faut acquitter<br>l’alarme. (Voir P19)|



Table des matières **Dernière MAJ : 01/04/2020** - **Page 17 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

|Col1|Etat Pré-Alarme :<br>Il est possible de paramétrer des seuils de pré-alarme<br>afin d’être alerté avant la sortie des limites hautes et<br>basses de températures.<br>Il s'agit uniquement d'un avertissement visuel (passage<br>en couleur jaune) qui ne tient pas compte du retard<br>d'alarme (changement d'état immédiat).<br>Il n'y a pas d'action d'acquittement à faire.|
|---|---|
||Etat Surveillance désactivée :<br>La surveillance du lieu a été arrêtée, la sonde ne mesure<br>plus.<br>(Ex : Appareil éteint ou en maintenance, sonde<br>défectueuse, etc. …)|
||Etat Relevé manuel :<br>Il s'agit d'un lieu paramétré et surveillé avec une sonde<br>type mini/maxi à relevés manuels.<br>Le relevé et la saisie des valeurs doivent être effectués<br>par un utilisateur.|



Table des matières **Dernière MAJ : 01/04/2020** - **Page 18 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

d) Alarmes

−
_Moyens d’alerte :_

Quand un lieu surveillé passe en état d'alarme en cours, le logiciel VigiSurv prévient l’utilisateur de plusieurs

manières :

     Passage de l’encadré bleu (Etat Normal) en couleur rouge (Etat alarme en cours, sortie de consignes) ou

en couleur noire (Etat alarme en cours, problème technique). Le(s) lieu(x) en alarme sont recopiés sur le

haut de l’écran principal, ligne ‘Alarmes en cours’.

     Alerte sonore (si le PC utilisé est équipé de hauts parleurs et que le son est activé dans Windows). Cette

alerte revient de manière récurrente tant que le problème existe.

     Apparition d’un bandeau rouge récapitulatif, lorsque le logiciel a été réduit dans la barre des tâches

Windows

Ce bandeau apparait au premier plan par rapport à toutes les autres fenêtres et logiciels ouverts sur le PC. Il n’est

pas bloquant et peut être déplacé sur l’écran.

Pour revenir dans la surveillance il faut faire un double clic sur le bandeau.

−
_Acquittement :_

Une alarme en cours peut être acquittée. Cependant, après acquittement, si le problème est toujours présent au

prochain relevé (température non conforme ou incident technique) le lieu passe à nouveau en alarme en cours.

**Dans l’idéal, l’acquittement d’une alarme doit se faire lorsque le problème est terminé et que le lieu est en état**

**‘Alarme terminée, non acquittée’ (encadré violet).**

Pour ouvrir la fenêtre d’acquittement d’alarme, faire un clic sur le nom du lieu en question puis réaliser les étapes

suivantes (exemple ici pour une alarme terminée de dépassement de la tolérance inférieure) :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 19 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

|Col1|Col2|La fenêtre de gestion de l’alarme apparait :<br>(1) : Sélection/Descriptif de l’alarme (Nom du lieu, Date heure de début<br>et fin, Etat)<br>(2) : Possibilité de dessiner le graphique (dans le cas d’alarmes de<br>dépassement)<br>(3) : Acquittement de l’alarme<br>(4) : Choix du commentaire dans la liste ou saisie manuelle dans le champ<br>prévu<br>(5) : Validation|Col4|
|---|---|---|---|
|||||
|Après validation, l’alarme est marquée Acquittée, fermer la fenêtre pour revenir à l’écran de surveillance.|Après validation, l’alarme est marquée Acquittée, fermer la fenêtre pour revenir à l’écran de surveillance.|Après validation, l’alarme est marquée Acquittée, fermer la fenêtre pour revenir à l’écran de surveillance.|Après validation, l’alarme est marquée Acquittée, fermer la fenêtre pour revenir à l’écran de surveillance.|
|||||
|Table des matières|Dernière MAJ : 01/04/2020 - Page 20 / 52|Dernière MAJ : 01/04/2020 - Page 20 / 52||

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : II. VigiSurv – Surveillance : Consultation, suivi et alarmes

**A savoir :**

Les différents messages pouvant apparaitre dans la colonne ‘Etat’ sont les suivants :

     L'alarme a été déclenchée par un dépassement de la tolérance supérieure.

     L'alarme a été déclenchée par un dépassement de la tolérance inférieure.

     L'alarme a été déclenchée par un problème sur le capteur de la sonde.

     L'alarme a été déclenchée par une coupure secteur.

     L'alarme a été déclenchée par une non-réponse de la sonde.

     L'alarme a été déclenchée par un problème sur le module.

La liste déroulante de commentaires prédéfinis doit être créée et alimentée par les administrateurs du système

VigiTemp.

Au retour à l’écran général de surveillance, le lieu pour lequel on vient d’acquitter l’alarme repasse en encadré bleu

au bout de quelques secondes.

− _Alarmes de service :_

Sur le haut de l’écran principal de la surveillance deux types de message peuvent apparaitre :

     Le serveur VigiTemp est inactif cela signifie que le service VigiServ est inactif sur le serveur VigiTemp.

     L’alarme téléphonique VigiTel est inactive signifie que le service VigiTel est inactif (sur le serveur

VigiTemp ou le PC VigiTel).

Dans les deux cas, prendre contact avec votre référent VigiTemp en interne ou contacter le service hotline VigiTemp.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 21 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options
## III. VigiSurv – Surveillance : Outils et options

Pour chaque lieu, différents outils, indicateurs et options de paramétrages sont disponibles.

a) Détails et historiques :

Pour le lieu choisi, ce bouton permet d’afficher, pour une période donnée, un historique précis et détaillé des

mesures effectuées (graphique + tableau) ainsi qu’un tableau des évènements.

Par défaut, il s’ouvre sur la journée en cours.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 22 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

**(1)** : Choix de la période de recherche / Option mesure ou moyenne / Outils

**(2)** : Tableau des évènements sur la période choisie

**(3)** : Graphique et table des mesures sur la période choisie

**(4)** : Outils d’export

Pour effectuer une recherche sur une période précise, renseigner les différents champs date/heure disponibles puis

cliquer sur rechercher. **Attention, plus la période est étendue, plus les résultats seront longs à charger et afficher.**

Deux modes sont disponibles :

‘Mesure’ = recherche et affichage des différents relevés effectués pour ce lieu sur la période.

‘Moyenne’ = recherche et affichage des différentes moyennes glissantes calculées sur la période pour ce lieu.

A chaque relevé effectué, une moyenne glissante pour la dernière heure est réalisée et stockée dans la base de

données. Il y a donc autant de valeurs de moyenne que de mesures.

Ceci permet de dégager une tendance générale en lissant, notamment, des épisodes sporadiques ou relevés isolés

potentiellement négligeables. Le but est d’appréhender les vitesses de variations de température par exemple, afin

de juger si les éléments conservés ont subi un stress thermique (ou choc thermique) pouvant engendrer une

dégradation.

Les résultats sont graphiquement visibles sur la partie courbe de l’écran. **(3)**

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 23 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

Exemple pour la même période :

Il est possible d’effectuer un zoom sur une partie de la courbe en l’encadrant avec la souris.

Au-dessus des courbes, un onglet permet de basculer sur les tableaux de mesures ou moyennes glissantes (selon le

mode choisi dans la recherche initiale).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 24 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

A partir de ces tableaux, il est possible de sélectionner une valeur pour suppression. Une fois la valeur sélectionnée,

renseigner le mot de passe (défini par l’administrateur) puis appuyer sur le bouton correspondant.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 25 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

Le tableau des évènements **(2)** présente la liste de toutes les actions tracées automatiquement par le serveur (ex :

Démarrage de la surveillance) ou à la suite d’une saisie par un utilisateur (ex : acquittement d’alarme) sur la période

de recherche. Dans le cas de la saisie par un utilisateur, son identifiant apparait à la ligne correspondante :

Un évènement peut être ajouté manuellement : (la date et heure de l’événement peuvent être modifiées)

Les différents tableaux et écrans présentés dans ce paragraphe peuvent être exportés à l’aide des boutons disponibles

en bas de l’écran :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 26 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

Un clic sur l’un de ces boutons ne génère pas une impression papier immédiate mais ouvre un éditeur à l’écran avec

des outils de mise en page et/ou annotations, export vers différents format (PDF, tableur, pièce jointe…) ou impression

papier :

Fermer l’éditeur pour revenir à la page précédente.

Une fois le travail de recherche et consultation terminé, fermer la fenêtre pour revenir à l’écran principal de

surveillance.

**A savoir :** le bouton ‘Ajouter une mesure manuelle’ n’est pas détaillé ici car il concerne la fonction ‘Mini/Maxi’ de

VigiTemp pour laquelle une documentation lui est spécialement dédiée (disponible sur simple demande).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 27 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

b) Indicateur d’étalonnage de la sonde




|Etat du<br>voyant|Signification|Ecran d’info au simple clic|
|---|---|---|
|Présent<br>Vert|La sonde<br>associée au lieu<br>surveillé a été<br>étalonnée. Ses<br>données<br>d’étalonnage<br>ont été<br>chargées.<br>La période de<br>validité n’est pas<br>expirée.||
|Présent<br>Rouge|La sonde<br>associée au lieu<br>surveillé a été<br>étalonnée. Ses<br>données<br>d’étalonnage<br>ont été<br>chargées.<br>La période de<br>validité est<br>expirée.||
|Absent|Les données<br>d’étalonnage de<br>la sonde n’ont<br>pas été chargées<br>ou la sonde n’a<br>pas été<br>étalonnée.|Aucun|


Table des matières **Dernière MAJ : 01/04/2020** - **Page 28 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

**A savoir :**

     Une sonde VigiTemp étalonnée par le laboratoire MC2 est fournie avec un fichier au format XML

contenant ses informations d’étalonnage (date, incertitude, correction, etc…). Il faut charger ce fichier

(Section Metrologie) pour intégrer ces différentes informations dans le système VigiTemp et voir

apparaitre le voyant vert sur le lieu associé.

     Pour les utilisateurs qui réalisent eux-mêmes l’étalonnage de leurs sondes dans VigiTemp, la validation

de l’étalonnage permet l’intégration des données et l’apparition du voyant vert.

     Par défaut, la durée de validité d’un étalonnage dans VigiTemp est de 365 jours. Cette valeur est fixée

dans la base de données et n’est pas modifiable par les utilisateurs ou administrateurs.

     Le voyant rouge n’est pas bloquant dans le fonctionnement et la prise de mesures. Il est informatif et

alerte sur la non-conformité métrologique.

c) Activation / Désactivation de la surveillance

Pour diverses raisons (maintenance, panne, décongélation ou nettoyage...) et éviter ainsi des alarmes inutiles, il est

possible de désactiver la surveillance d’un lieu et de la réactiver ultérieurement.

Cliquer sur la croix rouge pour désactiver la surveillance. Commenter cette action dans la fenêtre suivante puis

valider. La couleur de l’encadré du lieu passe en grisé, celui-ci est positionné à la fin de la liste principale.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 29 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

Pour remettre le lieu sous surveillance, il suffit de cliquer au même endroit (croix rouge devenue coche verte) sur le

lieu désactivé. Commenter de la même manière la réactivation. Le lieu est remis à sa place initiale dans la liste.

**A savoir :**

Il n’est pas possible de désactiver la surveillance d’un lieu alors que ce dernier est en alarme.

Chaque activation/désactivation est répertoriée dans le journal des évènements, le commentaire inséré à chaque

demande de validation est visible.

Selon le profil d'utilisation de chaque utilisateur, cette fonction peut ne pas être disponible (croix rouge visible mais

inactive). Voir avec votre référent qualité ou métrologie pour plus de renseignements.

d) Graphique instantané

Le graphique affiché sur chaque lieu présente les 125 dernières mesures effectuées.

En cliquant sur le graphique, celui-ci apparait de

manière zoomée et détaillée à l’écran.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 30 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

La période affichée est dépendante de la fréquence de mesure paramétrée. Pour une fréquence à 15 minutes

(réglage par défaut de l’application), le graphique présente les relevés des 31 dernières heures.

Le graphique peut être imprimé avec le bouton correspondant.

**A savoir :**

L’icône suivante indique que le lieu est sous surveillance VigiTel et/ou VigiMail. Cela signifie qu’en cas

d’alarme, le(s) contact(s) paramétrés (téléphone ou mail) seront avertis. Il s’agit d’une licence optionnelle pouvant

être ajoutée à un système VigiTemp. Une formation est dispensée en cas d’acquisition de l'option. Une

documentation spécialement dédiée à cette fonction est disponible sur simple demande au 04.73.28.55.60 ou

vigitemp@mc2lab.fr

e) Visualisation sur plan

L’insertion de plans est possible dans VigiTemp. Un paramétrage est à effectuer dans un premier temps (dédié aux

Administrateurs) pour insérer le(s) plan(s) scanné(s) au format image et pour ensuite positionner la sonde dessus.

Une fois ce paramétrage effectué, on peut afficher le plan à l’écran et visualiser la position de la sonde :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 31 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

f) Bandeau bas / Résumé

Sur la partie basse de chaque lieu, les informations suivantes sont disponibles :

     Dernier relevé effectué par la sonde, date et heure (ex : +21.74°C – 23/03/2020 10:12)

     Fréquence de mesure paramétrée (ex : 1mn)

     Numéro de série de la sonde associée au lieu surveillé (ex : IEE5S7)

**A savoir :**

Si, à la place du relevé, la zone est vide, cela signifie que la sonde n’a pas répondu à la demande de mesure. La sonde

sera réinterrogée tant qu’elle n’aura pas renvoyé de mesure. Au bout d’une heure en non-réponse, le lieu passe en

alarme (couleur noire pour non-réponse de la sonde).

g) Outil superposition de courbes

Le bouton suivant, en haut de l’écran principal, permet d’effectuer une superposition des courbes de deux lieux :

Selon le profil et les droits d’accès de l’utilisateur connecté, ce bouton n’est pas accessible
(visible mais inactif).

Exemples d'utilisation de cet outil :

     Doute sur la fiabilité d'une sonde. Une seconde sonde est placée en parallèle, un lieu temporaire associé

à cette sonde est créé. Après une période de mesures, les courbes de ces deux sondes peuvent être

superposées pour comparaison et analyse.

     Vérifier l’influence de la variation de la température d’ambiance sur la température de fonctionnement

d'un équipement.

     Comparer les mesures de deux appareils en tous points identiques.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 32 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : III. VigiSurv – Surveillance : Outils et options

A l’ouverture différents champs doivent être choisis :

**(1)** Premier lieu de comparaison

**(2)** Second lieu de comparaison

**(3)** Choix des éléments à comparer pour chaque lieu (Consigne supérieure / Consigne / Consigne inférieure)

**(4)** Période de recherche (Date/Heure début et Date/Heure fin)

**(5)** Lancer la recherche

Le résultat apparait ensuite à l’écran (trait plein pour le premier lieu et pointillés pour le second). Le résultat peut

être exporté.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 33 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu
## IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

     La fenêtre de paramétrage est décomposée en trois onglets : Général / Métrologie / Téléphonie &

Planning.

     De nombreux paramètres d’un lieu peuvent être modifiés, ce qui aura une incidence directe sur la

manière de surveiller et d’alerter.

     Selon le profil d'utilisation de chaque utilisateur, cette fonction peut ne pas être disponible (voir avec vos

référents qualité ou métrologie pour plus de renseignements).

     Certaines des modifications font l’objet d’une écriture dans le journal des évènements du lieu (affichage

d’une fenêtre de commentaire après clic sur le bouton validation).

Table des matières **Dernière MAJ : 01/04/2020** - **Page 34 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

a) Fiche lieu / Onglet général

**1)** Nom du Lieu (20 caractères maximum).

**2)** Commentaires sur le Lieu (toute information éventuellement utile, visible uniquement sur cette fiche).

**3)** Sélection d’un site (si la structure se compose de plusieurs sites). Le bouton + permet d'accéder à la liste des

sites et d'en ajouter si besoin.

**4)** Sélection du ou des groupes auxquels appartient le Lieu. Le bouton + permet d'accéder à la liste des groupes

et d'en rajouter éventuellement.

**5)** Sélection d’un plan et d’une localisation via le bouton Plan et possibilité de supprimer une précédente

localisation.

**6)** Module d’alarme associé au lieu (il s'agit de boitiers type gyrophare ou sonore pouvant être ajoutés sur une

installation VigiTemp). En cas d’alarme sur le lieu, le boitier s’actionne.

**7)** Sélection d’un document (ex: rapport de cartographie de l’appareil surveillé) si l’on souhaite le stocker dans

VigiTemp et l'associer au lieu en cours de paramétrage.

Table des matières **Dernière MAJ : 01/04/2020** - **Page 35 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

**8)** Réglage des consignes de surveillance. Seule la consigne centrale (ou cible) est obligatoire. La consigne

supérieure et la consigne inférieure permettent de déterminer les seuils à partir desquels des alarmes
pourront se déclencher.
Concernant les réglages de pré-alarme, il s’agit d’une option facultative d’affichage en surveillance (couleur
jaune) qui se déclenche pour tout relevé au-delà des seuils fixés. Ce n’est pas une « vraie » alarme nécessitant
un acquittement mais plutôt un avertissement pour l’utilisateur.

**9)** Réglage du retard d’alarme haut pour le lieu concerné (temporisation avant déclenchement de l'alarme, 60

minutes par défaut). Dans l’exemple, le retard d’alarme a été fixé à 120 minutes. L’alarme de dépassement du
seuil supérieur se déclenchera s’il y a au moins 120 minutes de relevés consécutifs au-delà de +30°C.

**10)** Réglage du retard d’alarme bas pour le lieu concerné (temporisation avant déclenchement de l'alarme, 60

minutes par défaut). Dans l’exemple, le retard d’alarme a été fixé à 60 minutes. L’alarme de dépassement du
seuil inférieur se déclenchera s’il y a au moins 60 minutes de relevés consécutifs en-deçà de +15°C.

**11)** Réglage de la fréquence des mesures pour le lieu concerné (15 minutes par défaut).

**A savoir :**

     Cet onglet de paramétrage est l’un des plus importants dans VigiTemp car il conditionne, notamment, les
déclenchements d’alarmes par l’intermédiaire des critères consignes et retards d’alarme.

     Chaque lieu dispose de son propre paramétrage. On peut donc appliquer des conditions de surveillance

différentes selon la criticité de l’élément surveillé.

     A l’installation d’un système VigiTemp, un paramétrage par défaut est appliqué pour chacun des lieux. Il
conviendra aux référents administrateurs de l’application d’affiner et personnaliser les réglages en
fonction des besoins.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 36 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

b) Fiche lieu / Onglet métrologie (présentation générale)

**(1)** Choix de la sonde associée au lieu surveillé (par son numéro de série).

**(2)** Informations sur les données métrologiques de la sonde, issues de son étalonnage (Erreur de justesse,

Incertitude et Dérive).

**(3)** Rappel des consignes paramétrées dans l'onglet général.

**(4)** Choix des règles de calcul de l’EMT de surveillance. Selon le choix effectué, les tolérances seront adaptées **(5)** .

Dix possibilités de paramétrage sont possibles, voir à partir de P40 pour plus de détails (par défaut Sans objet).

**(6)** Choix de la prise en compte de l'erreur de justesse dans la mesure (en lien avec le choix des règles de calcul

de l'EMT, voir point suivant pour plus de détails).

**(7)** Choix de la prise en compte de la dérive dans l'incertitude (en lien avec le choix des règles de calcul de l'EMT,

voir point suivant pour plus de détails).

**(8)** Accès au suivi SAV de la sonde en lien direct avec la Gestion de Parc Matériel SMILE.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 37 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

c) Fiche lieu / Onglet Téléphonie-Planning

**(1)** : Lié à l’option VigiTel / VigiMail (formation dispensée en cas d’acquisition de l'option). Une documentation

spécialement dédiée à cette fonction est disponible sur simple demande au 04.73.28.55.60 ou vigitemp@mc2lab.fr

**(2)** : Mise en place d'un planning de changement de consignes pour le lieu actuel

Le planning des consignes permet d'effectuer de manière automatique un changement des consignes de surveillance

selon un planning hebdomadaire à définir. Dans notre exemple les consignes du lieu sont les suivantes :

20° +/- 5° du lundi 07:00 au vendredi 18:00

10° +/- 5° du vendredi 18:00 au lundi 07:00

Les consignes (et seuils d'alarme) changent donc automatiquement aux jours et horaires définis. L'échelle des

graphiques s'adapte au niveau de la surveillance.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 38 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

**(1)** : Activer le planning des consignes.

**(2) (3)** : Définir les jours et heures de changement (un seul changement possible par jour).

**(4** ) : Remplir, pour chaque jour, la consigne et limites mini et maxi. Les jours pour lesquels un horaire de changement

a été défini, remplir avec les données avant/après heure de changement.

**(5)** : Définir un retard d'alarme de changement de consigne = Temps laissé à la sonde pour obtenir une stabilisation

de relevé sans déclenchement d'alarme intempestive.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 39 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

d) Fiche lieu / Onglet métrologie (présentation détaillée)

Différents choix peuvent être effectués au niveau des règles de calcul de l'EMT de la sonde et des tolérances du lieu.

_Note : les captures d’écran présentées ci-après sont issues de la documentation VigiSurv – Surveillance version 10.122. Cette_

_fenêtre est en tout point identique à celle de la version VigiSurv 10.200 à la seule différence que le bouton SAV n’est pas présent_

_ici. Tous les cas possibles et règles de calcul sont identiques._

−
_Cas 1a : Les EMT obéissent à la règle du quart / sans correction de l'erreur de justesse_

L'EMT de la sonde est fixé au quart de l'EMT de l'équipement (5°C dans notre exemple, donc EMT sonde = 5/4 =

1.25). Ce calcul est appliqué automatiquement sur les seuils de tolérances.

L'erreur de justesse n'est pas appliquée sur la mesure de surveillance.

En cas de non-conformité (si |Erreur de Justesse|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur

l’écran principal de la section métrologie).

|Col1|Col2|
|---|---|
|Table des matières Dernière MAJ : 01/04/2020 - Page 40 / 52|Table des matières Dernière MAJ : 01/04/2020 - Page 40 / 52|
|Table des matières|Dernière MAJ : 01/04/2020 - Page 40 / 52|

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 1b : Les EMT obéissent à la règle du quart /avec correction de l'erreur de justesse_

L'EMT de la sonde est fixé au quart de l'EMT de l'équipement (5°C dans notre exemple, donc EMT sonde = 5/4 =

1.25). Ce calcul est appliqué automatiquement sur les seuils de tolérances.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée

directement sur la mesure effectuée.

En cas de non-conformité (|Dérive|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur l’écran

principal de la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 41 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 2a : EMT saisi manuellement /sans correction de l'erreur de justesse_

L'EMT de la sonde peut être saisi de manière manuelle (déduit par exemple selon des méthodes de calcul interne ou

basé sur les données issues de l'étalonnage, l'erreur de justesse devant être prise en compte dans ce calcul).

Dans notre exemple la saisie d'un EMT de la sonde à 0.55 corrige automatiquement les seuils de tolérances.

En cas de non-conformité (si |Erreur de Justesse|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur

l’écran principal de la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 42 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 2b : EMT saisi manuellement /Avec correction de l'erreur de justesse_

L'EMT de la sonde peut être saisi de manière manuelle (déduit par exemple selon des méthodes de calcul interne ou

basé sur les données issues de l'étalonnage).

Dans notre exemple la saisie d'un EMT de la sonde à 0.30 corrige automatiquement les seuils de tolérances.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée

directement sur la mesure effectuée.

En cas de non-conformité (|Dérive|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur l’écran

principal de la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 43 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 3a : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse /_

_sans prise en compte de la dérive dans l'incertitude :_

Dans cet exemple on choisit d'appliquer l'incertitude d'utilisation de la sonde (issue de son étalonnage) sans prise en

compte de l’erreur de justesse sur la mesure de surveillance et sans prise en compte de la dérive.

L'équation suivante est appliquée : 𝐼𝑚𝑒𝑠 =| 𝐸𝑗 |+ 𝐼𝑒𝑡 soit dans notre exemple 𝐼𝑚𝑒𝑠 = 0.29 + 0.20=0.49

Les seuils de tolérance sont adaptés automatiquement. Lors du prochain étalonnage, après insertion des nouvelles

données, l'EMT de la sonde sera mis à jour automatiquement (ainsi que les tolérances).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 44 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 3b : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse /_

_sans prise en compte de la dérive dans l'incertitude :_

Dans cet exemple on choisit d'appliquer l'incertitude d'utilisation de la sonde (issue de son étalonnage) avec prise en

compte de l’erreur de justesse sur la mesure de surveillance et sans prise en compte de la dérive.

L'équation suivante est appliquée : 𝐼𝑚𝑒𝑠 = 𝐼𝑒𝑡 soit dans notre exemple 𝐼𝑚𝑒𝑠 = 0.20

Les seuils de tolérance sont adaptés automatiquement.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée

directement sur la mesure effectuée.

Lors du prochain étalonnage, après insertion des nouvelles données, l'EMT de la sonde sera mis à jour

automatiquement (ainsi que les tolérances). Idem concernant l'erreur de justesse.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 45 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 3c : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse /_

_avec prise en compte de la dérive dans l'incertitude :_

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
(


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

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée

directement sur la mesure effectuée.

Lors du prochain étalonnage, après insertion des nouvelles données, l'EMT de la sonde sera mis à jour

automatiquement (ainsi que les tolérances). Idem concernant l'erreur de justesse. Une nouvelle valeur de dérive

sera appliquée au calcul.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 46 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 3d : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse /_

_avec prise en compte de la dérive dans l'incertitude :_

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


~~√~~ 3 [)]


2


𝐼𝑒𝑡


2


2


2


= 0.49


Lors du prochain étalonnage, après insertion des nouvelles données, l'EMT de la sonde sera mis à jour

automatiquement (ainsi que les tolérances). Idem concernant l'erreur de justesse. Une nouvelle valeur de dérive

sera appliquée au calcul.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 47 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 4a : Sans objet / sans correction de l'erreur de justesse_

Dans cet exemple aucun paramétrage n'a été sélectionné concernant l'EMT de la sonde.

Il n'y a au **c** une correction apportée sur la mesure et sur les tolérances. Le choix de ce paramétrage doit pouvoir se

justifier.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 48 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : IV. VigiSurv – Surveillance : Gestion et paramétrages du lieu

−
_Cas 4b : Sans objet / avec correction de l'erreur de justesse_

Dans cet exemple aucun paramétrage n'a été sélectionné concernant l'EMT de la sonde.

Il n'y a au **c** une correction apportée sur les tolérances. La valeur relative de l'erreur de justesse arrondie au centième

(-0.29 dans notre exemple) sera appliquée directement sur la mesure effectuée.

Le choix de ce paramétrage doit pouvoir se justifier.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 49 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : V. Hotline et dépannage
## V. Hotline et dépannage

− _Généralités :_

En cas de défaillance ou problèmes d’ordre matériel ou logiciel, une hotline est à disposition au numéro de

téléphone suivant :

**04-73-28-55-60** (8H30-12H30 / 13H30-17H du lundi au jeudi et 8H30-12H15 le vendredi).

Pour les clients sous contrat, possibilité de joindre la hotline le vendredi de 13h30 à 17H au numéro spécial fourni.

Voir avec votre référent VigiTemp interne ou responsable qualité/métrologie.

Il est également possible d'envoyer un mail à l'adresse **vigitemp@mc2lab.fr** en précisant les informations suivantes :

Nom du laboratoire et/ou du groupement, Ville, Nom et téléphone de la personne à contacter, Descriptif de la

demande. N’hésitez pas à joindre le maximum d’informations et, le cas échéant, une ou des captures d’écran si cela

peut aider dans la résolution du problème.

−
_Vérifications et auto-dépannage :_

Avant de contacter le service hotline, quelques petites vérifications et tests peuvent être effectués sur votre

installation :

- S’assurer qu’il n’y a pas de dysfonctionnements d’ordre général de type électrique ou sur le réseau

informatique pouvant entrainer un problème dans la surveillance VigiTemp mais également pour d’autres

applications ou matériel.

- Si toutes les sondes apparaissent en alarmes techniques dans la surveillance, réinitialiser la ou les bornes de

réception des sondes (retirer le petit connecteur d’alimentation électrique, attendre quelques secondes puis

rebrancher). Vérifier également le branchement correct de tous les câbles sur ce matériel. Si les erreurs persistent

après quelques minutes contacter la hotline.

- Si une seule sonde apparait en erreur alors que les autres fonctionnent bien, réaliser la même opération de

débranchement/rebranchement électrique sur le boitier de la sonde.

**A savoir :**

Bien connecter l’alimentation sur la sonde uniquement lorsque l’adaptateur secteur est déjà branché dans une prise.

De plus il convient d’utiliser le bon connecteur sur la sonde :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 50 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : V. Hotline et dépannage

− _Zoom sur la télémaintenance :_

Le bouton télémaintenance situé dans la barre d’outils en haut de l’écran principal de la surveillance permet

d’afficher le numéro de téléphone de la hotline :

Après avoir appuyé sur le bouton OK, le logiciel de prise en main à distance TeamViewer est lancé automatiquement

(soit la version MC2 Hotline, soit TeamViewer si ce dernier est déjà installé et exécuté sur le PC) :

|Version MC2 Hotline<br>(incluse avec VigiSurv)|Col2|
|---|---|
|Version TeamViewer<br>(si déjà sur le PC)||



Table des matières **Dernière MAJ : 01/04/2020**  - **Page 51 / 52**

## VigiSurv 10.200 : Manuel d’utilisation de la surveillance

En cours : V. Hotline et dépannage

Il suffit ensuite de communiquer les codes affichés à l’écran (ID et Mot de passe) au technicien hotline afin que celui
ci puisse prendre la main sur le PC et réaliser les vérifications nécessaires.

**A savoir :**

     Selon le profil et les droits d’accès de l’utilisateur connecté, le bouton télémaintenance n’est pas

accessible (visible mais inactif). Dans ce cas prendre contact avec le(s) référent(s) VigiTemp de votre

structure.

     Si le logiciel MC2 Hotline s’ouvre mais n’affiche aucun code (ID et mot de passe) cela peut signifier que

ce type de connexion n’est pas autorisé par votre service informatique.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 52 / 52**

