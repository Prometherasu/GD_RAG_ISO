# VigiSurv 10.200 : Manuel d’utilisation de l’administration

**I.** **PRESENTATION VIGITEMP .................................................................................................................................................. 3**

A ) L OGICIEL ................................................................................................................................................................................... 3

B ) M ATERIEL ................................................................................................................................................................................. 4

C ) L EXIQUE SUPPLEMENTAIRE ............................................................................................................................................................ 5

**II.** **VIGISURV – ADMINISTRATION : ACCES ET PRESENTATION ................................................................................................. 6**

A ) O UVERTURE ET CONNEXION .......................................................................................................................................................... 6

B ) E CRAN PRINCIPAL ........................................................................................................................................................................ 8

**III.** **VIGISURV – ADMINISTRATION : JOURNAUX ET TABLEAUX DE BORD ................................................................................. 9**

A ) J OURNAL DU SYSTEME .................................................................................................................................................................. 9

B ) J OURNAL DES ACQUITTEMENTS .................................................................................................................................................... 10

C ) L ISTE DES APPELS ...................................................................................................................................................................... 10

D ) U TILISATEURS CONNECTES .......................................................................................................................................................... 10

E ) L IEU ( X ) AFFECTE ( S ) A AUCUN UTILISATEUR ..................................................................................................................................... 11

F ) S AUVEGARDE DU SYSTEME .......................................................................................................................................................... 11

G ) A LARMES EN COURS .................................................................................................................................................................. 12

**IV.** **VIGISURV – ADMINISTRATION : BARRE D’OUTILS INFERIEURE ..................................................................................... 14**

A ) L ISTE DES SONDES ..................................................................................................................................................................... 14

B ) L ISTE DES MODULES ................................................................................................................................................................... 17

C ) L ISTE DES ETALONS .................................................................................................................................................................... 18

D ) L ISTE DES ACTIONNEURS ............................................................................................................................................................. 19

E ) G ROUPES ................................................................................................................................................................................ 19

F ) L IEUX – E CRAN PRINCIPAL ........................................................................................................................................................... 21

G ) F ICHE LIEU / O NGLET GENERAL .................................................................................................................................................... 22

H ) F ICHE LIEU / O NGLET METROLOGIE ( PRESENTATION GENERALE ) ......................................................................................................... 24

I ) F ICHE LIEU / O NGLET T ELEPHONIE -P LANNING ................................................................................................................................ 25

J ) F ICHE LIEU / O NGLET METROLOGIE ( PRESENTATION DETAILLEE ) ......................................................................................................... 27

K ) P LANS .................................................................................................................................................................................... 38

L ) S ITES ...................................................................................................................................................................................... 40

M ) D ATALOGGER ........................................................................................................................................................................... 40

N ) O UTILS ................................................................................................................................................................................... 40

O ) S TATISTIQUES ........................................................................................................................................................................... 47

**V.** **VIGISURV – ADMINISTRATION : INDICATEURS D’ETAT / DIVERS ...................................................................................... 48**

**VI.** **VIGISURV – ADMINISTRATION : BANDEAU DEROULANT .............................................................................................. 49**

A ) G ESTION DES PROFILS ................................................................................................................................................................ 50

B ) G ESTION DES UTILISATEURS ......................................................................................................................................................... 53

C ) G ESTION DES ALARMES .............................................................................................................................................................. 55

D ) S CHEMA DE L ’ IMPLANTATION ...................................................................................................................................................... 56

E ) M ESURES ARCHIVEES ................................................................................................................................................................. 57

F ) P ARAMETRES GLOBAUX .............................................................................................................................................................. 58

G ) G ESTION DES LICENCES ............................................................................................................................................................... 60

H ) G ESTION DES SAUVEGARDES ........................................................................................................................................................ 61

I ) G ESTION DE LA TELEPHONIE ........................................................................................................................................................ 61

**VII.** **HOTLINE ET DEPANNAGE ............................................................................................................................................. 63**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : I. Présentation VigiTemp
## I. Présentation VigiTemp

a) Logiciel

Le système VigiTemp 10 est une solution client / serveur. Son architecture repose sur une base de données MySQL.

La collecte et la gestion des alarmes sont gérées par la partie serveur, cette dernière se présentant sous la forme

d’un service Windows appelé VigiServ.

L’exploitation des mesures, leur interprétation et les différentes fonctions F.M.E (Fonctions de Métrologie Evoluées)

sont quant à elles gérées par la partie client du logiciel, c’est VigiSurv.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 3 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : I. Présentation VigiTemp

b) Matériel

Le système VigiTemp est composé de divers éléments physiques. Voici la présentation d’un système radio. Il existe

également des possibilités d’installation filaires (modules et sondes sont reliés par câbles).

|PC Serveur<br>Cœur du système Vigitemp comprenant les logiciels :<br>* MySQL (base de données)<br>* VigiServ (service gérant l'interrogation des sondes, les relevés et<br>l'inscription des données<br>* Pilote de gestion de ports COM virtuels pour les bornes ou<br>modules radio/réseau|Col2|
|---|---|
|Les bornes ou modules de réceptions<br>Boitier composé d'une partie radio (pour dialogue avec les sondes)<br>et une partie réseau Ethernet (pour dialogue avec le PC serveur).<br>1 module = 1 adresse IP = 1 port COM virtuel sur le PC serveur||
|Les sondes<br>Ensemble composé de : capteur (T°, C02…) + boitier électronique<br>(gestion des relevés, radiofréquence…) + alimentation électrique.<br>Chaque sonde a son propre numéro de série.<br>Une sonde ne dialogue qu'avec un seul module (association<br>généralement définie selon la proximité géographique des deux<br>éléments) par ondes radio (869.525MHZ).<br>Possibilité de modifier l'association module/sonde, en cas de<br>déplacement de la sonde par exemple.||



Table des matières **Dernière MAJ : 01/04/2020**  - **Page 4 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

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
|PROFIL|Droits d'accès dans le logiciel : Accès intégral ou uniquement à quelques parties du logiciel<br>(Ex : Surveillance)|


Table des matières **Dernière MAJ : 01/04/2020** - **Page 5 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : II. VigiSurv – Administration : Accès et présentation
## II. VigiSurv – Administration : Accès et présentation

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

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 6 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : II. VigiSurv – Administration : Accès et présentation

Ce manuel se concentre sur la partie **Administration** .

**A savoir :**

De nombreux tableaux de données sont présentés dans ce document. La plupart sont exportables ou imprimables en

réalisant un clic-droit sur le coin supérieur droit :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 7 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : II. VigiSurv – Administration : Accès et présentation

b) Ecran principal

**(1)** : Journaux de fonctionnement et tableaux de bord

**(2)** : Gestion et paramétrage du matériel / Organisation de la surveillance / Outils

**(3)** : Différents outils de paramétrages (ex : utilisateurs et profils) / Accès aux autres parties du logiciel

**(4)** : Indicateurs d’état

Les différentes zones sont détaillées dans les chapitres suivants.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 8 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : III. VigiSurv – Administration : Journaux et tableaux de bord
## III. VigiSurv – Administration : Journaux et tableaux de bord

a) Journal du système

Le journal du système affiche la liste, pour la journée en cours, de tous les évènements tracés par le système

VigiTemp : connexion/déconnexion d’utilisateurs, activation/désactivation de la surveillance d’un lieu, Acquittement

d’alarme, etc…

Le bouton en forme de loupe permet d’effectuer une recherche pour une période donnée en sélectionnant la date

de début de recherche et celle de fin. Les commentaires saisis par les utilisateurs dans les différentes fenêtres de

confirmation d’action apparaissent dans la colonne correspondante.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 9 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : III. VigiSurv – Administration : Journaux et tableaux de bord

b) Journal des acquittements

Le journal des acquittements affiche la liste, pour la journée en cours, de tous les acquittements d’alarme effectués

par les utilisateurs.

Le bouton en forme de loupe permet d’effectuer une recherche pour une période donnée en sélectionnant la date

de début de recherche et celle de fin. Les commentaires saisis par les utilisateurs lors des acquittements

apparaissent dans la colonne correspondante.

c) Liste des appels

La liste des appels se concentre sur les appels et envoi d’emails par l’option VigiTel (sous condition que cette licence

soit installée et fonctionnelle sur le système VigiTemp en cours). De la même manière que les journaux précédents, il

est possible d’effectuer une recherche par période.

d) Utilisateurs connectés

Ce tableau présente la liste des utilisateurs actuellement connectés dans le système VigiTemp. Il s’agit donc des

utilisateurs qui ont lancé VigiSurv sur un PC et qui se sont connectés avec un login et mot de passe.

Les informations présentes dans ce tableau sont :

Login + Nom & prénom de l’utilisateur

Nom et adresse IP du PC sur lequel l’utilisateur s’est connecté

Version du logiciel VigiSurv utilisé (fonction disponible à partir de VigiSurv 10.200 uniquement)

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 10 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : III. VigiSurv – Administration : Journaux et tableaux de bord

e) Lieu(x) affecté(s) à aucun utilisateur

Ce tableau est une sécurité présentant, s’il y en a, la liste des lieux auxquels aucun groupe n’a été affecté (donc

potentiellement visible par aucun utilisateur). Cette sécurité permet aux administrateurs d’intervenir sur ces lieux

éventuels afin de corriger cette erreur de paramétrage. Comme indiqué sous le tableau, celui-ci doit être vide.

Si un lieu apparait dans la liste il suffit de double-cliquer dessus afin d’accéder à sa fiche de paramétrage et lui

attribuer un groupe (voir P22).

f) Sauvegarde du système

Comme vu dans le chapitre I, VigiTemp fonctionne avec un système de base de données MySQL. Deux bases sont

présentes : VigiTemp pour la partie paramétrage et VigiTemp mesure pour les mesures et journaux.

Ces bases de données sont stockées sur le serveur VigiTemp et sont essentielles au fonctionnement, il est donc

indispensable qu’elles soient sauvegardées.

A l’installation du système VigiTemp un processus de sauvegarde automatique est mis en place selon le plan suivant :

Sauvegarde complète des bases VigiTemp et VigiTemp mesure tous les jours à heure fixe (généralement 23H) soit

deux fichiers de sauvegarde par jour. Un historique de 7 jours de sauvegarde est conservé avec effacement

automatique des fichiers les plus anciens afin de ne pas saturer l’espace du disque qui accueille les sauvegardes.

Exemple d’une arborescence de sauvegarde (sur le serveur) :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 11 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : III. VigiSurv – Administration : Journaux et tableaux de bord

Le tableau « Sauvegarde du système » présente une liste de fichiers :

Les informations de date et heure de création des fichiers de sauvegarde sont incluses dans leurs noms (ici

06/03/2020).

Si ce tableau est vide ou si l’horodatage ne se met pas à jour, prendre contact avec le service hotline VigiTemp (voir

P63).

g) Alarmes en cours

Ce tableau regroupe toutes les alarmes (en cours et terminées/non acquittées) du système VigiTemp. Il est possible

de les visualiser en double-cliquant sur la ligne correspondante et en effectuer, si besoin, l’acquittement.

L’exemple ci-dessous ne montre qu’une alarme mais il peut y avoir plusieurs lignes remplies.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 12 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : III. VigiSurv – Administration : Journaux et tableaux de bord

**A savoir :**

Les différents messages pouvant apparaitre dans la colonne ‘Etat’ sont les suivants :

     L'alarme a été déclenchée par un dépassement de la tolérance supérieure.

     L'alarme a été déclenchée par un dépassement de la tolérance inférieure.

     L'alarme a été déclenchée par un problème sur le capteur de la sonde.

     L'alarme a été déclenchée par une coupure secteur.

     L'alarme a été déclenchée par une non-réponse de la sonde.

     L'alarme a été déclenchée par un problème sur le module.

La liste déroulante de commentaires prédéfinis doit être créée et alimentée par les administrateurs du système

VigiTemp. Voir P43.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 13 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure
## IV. VigiSurv – Administration : Barre d’outils inférieure

Les outils présentés ci-après permettent principalement de gérer la surveillance d’un point de vue matériel (surligné

vert) et organisationnel (surligné rouge).

a) Liste des sondes

Toutes les sondes du système VigiTemp sont regroupées ici dans un tableau synthétique. Pour qu’une sonde

apparaisse dans ce tableau, il faut au préalable avoir chargé son fichier de calibrage (fourni par le laboratoire MC2) à

partir de la section ‘Métrologie’ ou bien l’avoir créé manuellement avec le bouton ‘Nouveau’ (ce qui implique

ensuite d’en réaliser son calibrage avec le matériel adéquat, toujours dans la section ‘Métrologie’). Ces

manipulations sont décrites dans le manuel utilisateur dédié.

**(1)** Adresse et N° de série : identifiants uniques pour chaque sonde permettant au serveur de les interroger

individuellement et d’organiser les relevés de manière cohérente. Ces identifiants sont reportés

physiquement sur chaque sonde (stickers et code-barre d’identification).

**(2)** Port série et module : module/récepteur de communication paramétré pour chaque sonde. Modification de

cette association possible, voir point **(6)** .

**(3)** Etat de la sonde : Utilisée en surveillance (donc associée à un lieu qui est en surveillance) ou Surveillance

désactivée (associée à un lieu qui n’est pas en surveillance ou non associée à un lieu, donc disponible pour

un nouveau).

**(4)** Lieu associé à chaque sonde (‘Aucun’ si pas de lieu associé à une sonde).

**(5)** Sélection d’une sonde permettant d’accéder à ses données de calibrage et d’étalonnage (si disponibles).

Concernant les étalonnages, il est possible d’en supprimer (à la suite d’erreur ou les plus anciens par

exemple). Pour cela il faut disposer du mot de passe « super-admin » (voir P59).

**(6)** Modification d’une sonde concernant, notamment, le paramétrage de son association avec un module de

réception.

**(7)** Impression de la liste des sondes.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 14 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

Le point **(6)**, fiche d’une sonde est détaillé ci-après :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 15 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

**(A)** Modification de l’association sonde/module de réception. Choisir le module souhaité dans la liste (si sonde

déplacée ou erreur de paramétrage initial).

**(B)** Visuel d’une sonde de même type (ici sonde type IN).

**(C)** Liste des différents calibrages et étalonnages (si disponibles).

**(D)** Accès à la fiche SAV de la sonde en lien direct avec la Gestion de Parc Matériel SMILE. Si la sonde est en

cours d’intervention au SAV MC2, la fiche apparait avec ses informations de suivi.

**(E)** Valider si un changement de module récepteur a été effectué = retour à la fenêtre précédente.

**(F)** Fermer la fenêtre sans valider les changements éventuels ou pour terminer la consultation = retour à la

fenêtre précédente.

Table des matières **Dernière MAJ : 01/04/2020** - **Page 16 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

b) Liste des modules

Les modules récepteurs ou bornes de réception constituent, au même titre que le serveur, un point essentiel du

système de surveillance VigiTemp. A ce titre, toute intervention dans ce menu doit être réalisée en priorité par un

technicien MC2. Un mauvais paramétrage peut en effet entrainer un arrêt complet de la surveillance.

En voici, pour information, le descriptif :

**(1)** Type de module selon la technologie de matériel en place. Le système VigiTemp 10 est en effet rétro

compatible avec les générations de matériel plus anciennes. A ce titre les modules utilisés seront de type

BTR ou MRH (radio) et BIN (filaire). Les dernières gammes en date sont IETH et IUSB (radio) et BINX (filaire).

Les différentes générations de matériel peuvent cohabiter.

**(2)** N° de série (= identifiant unique du module) et emplacement (= toutes informations utiles pouvant aider à la

localisation rapide du matériel).

**(3)** Port série : il s’agit du numéro du port série virtuel paramétré sur le serveur VigiTemp pour chaque module.

Un module = un port.

**(4)** Nombre de sondes associées au module

**(5)** ID serveur : dans le cas d’un serveur type multicœur, un module est interrogé par un cœur de surveillance.

Le principe du multicœur consiste à faire fonctionner plusieurs serveurs VigiTemp sur la même machine,

chacun s’occupant d’une partie des sondes à interroger.

**(6)** Liste des sondes associées à un module quand celui-ci est sélectionné dans la liste principale.

**(7)** Outils pour créer, modifier ou archiver un module.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 17 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

Détail d’une fiche module lors de son édition :

Pour toute intervention ou question sur cette partie, contacter le service hotline VigiTemp, voir P63.

c) Liste des étalons

Il est possible de s’équiper d’une sonde étalon afin de réaliser soi-même le contrôle métrologique des sondes en

surveillance. Ce menu permet de créer et déclarer la ou les sondes étalon pour une utilisation future. Cette

fonctionnalité est également présente dans la section ‘Métrologie’. Voir le manuel dédié à cette partie pour tous les

détails et fonctionnalités.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 18 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

d) Liste des actionneurs

Les actionneurs sont des boitiers qui alertent les utilisateurs en cas d’alarmes. Ils peuvent avoir plusieurs

caractéristiques : alerte lumineuse type gyrophare, alerte sonore type buzzer, relais par contact sec vers un système

d’alarme externe.

De la même manière que pour les modules, l’intervention et le paramétrage dans cette partie sont réservés aux

techniciens MC2. Une fois un actionneur paramétré, il est disponible pour être associé aux lieux voulus (voir point f,

fiche lieu).

e) Groupes

La fonctionnalité groupe permet d’organiser et de répartir la surveillance :

     Géographiquement : par secteur, site, service, étage, etc…

     Par utilisateur : pour chaque utilisateur on peut donner accès à un ou plusieurs groupes selon les besoins

(voir P53 pour la gestion des utilisateurs).

L’écran principal présente les groupes paramétrés dans le système. A la sélection d’un groupe dans le tableau, les

listes ‘Lieu(x) associé(s)’ et ‘Utilisateur(s) associé(s)’ se mettent à jour afin d’avoir une vue synthétique et rapide du

paramétrage.

Il est possible de créer, modifier ou archiver un groupe. La liste principale peut être imprimée.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 19 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

Voici l’édition d’une fiche groupe :

**A savoir :**

     Lorsque l’on crée un nouveau groupe sur un système VigiTemp disposant déjà de comptes utilisateurs, il

faudra penser à aller sur chaque compte utilisateur devant avoir accès à ce nouveau groupe afin de

cocher la case correspondante.

     Un groupe peut être de niveau 1 ou 2. Le niveau 1 est le niveau par défaut, le plus utilisé, et permet

principalement la répartition géographique des lieux en surveillance.

Le niveau 2 permettra davantage un classement par type de lieu surveillé, par exemple pour regrouper

tous les points de surveillance en température ambiante.

Ensuite, sur le paramétrage d’un lieu (voir point suivant), celui-ci pourra être associé à deux groupes

différents (niveau 1 & 2).

Cela peut permettre de donner accès, à un utilisateur, aux lieux appartenant à un groupe de niveau 2

sans visualisation du reste des lieux. Selon l’illustration suivante, USER X voit tous les lieux FRIGO A,

CONGEL A, AMBIANTE A, FRIGO B, CONGEL B et AMBIANTE B. USER Y voit AMBIANTE A et AMBIANTE B

sans voir le reste.

|LIEUX|FRIGO A|CONGEL A|AMBIANTE A|FRIGO B|CONGEL B|AMBIANTE B|
|---|---|---|---|---|---|---|
|GROUPES<br>NIVEAU 1|A1|A1|A1|B1|B1|B1|
|GROUPES<br>NIVEAU 2|N/A|N/A|A2|N/A|N/A|B2|
|USER X /<br>GROUPES 1|A1|A1|A1|B1|B1|B1|
|USER Y /<br>GROUPES 2|N/A|N/A|A2|N/A|N/A|B2|



Table des matières **Dernière MAJ : 01/04/2020**  - **Page 20 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

f) Lieux – Ecran principal

Point central de la surveillance, le lieu détermine l’élément surveillé par une sonde. Son paramétrage est donc très

important et essentiel dans le fonctionnement de la surveillance et détermine, notamment, les conditions de

déclenchement des alarmes.

L’écran principal des lieux s’ouvre sur la liste des lieux en surveillance (sous réserve que l’utilisateur actuellement

connecté dispose du droit d’accès aux groupes correspondants). La liste déroulante en haut de l’écran permet

d’avoir accès aux lieux existants mais désactivés en surveillance ainsi qu’aux lieux ayant été archivés.

Le tableau synthétise le paramétrage effectué pour chaque fiche lieu, éditable par les boutons de création ou

modification à droite de l’écran.

**A savoir :**

     Pour créer un nouveau lieu, il faut disposer d’au moins une sonde disponible dans le système VigiTemp.

     Sur un lieu désactivé, si une sonde lui est associée il est possible de désactiver ce paramétrage afin de

rendre la sonde disponible pour un autre lieu (existant ou à créer).

     Un lieu désactivé peut être archivé (ex : appareil mis au rebut), cela aura pour effet de le retirer de

l’écran de surveillance. Son historique reste accessible dans la section ‘Métrologie’ (Historique des

mesures).

Les pages suivantes reprennent en détail les différents points de paramétrage disponibles dans la fiche lieu.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 21 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

g) Fiche lieu / Onglet général

**1)** Nom du Lieu (20 caractères maximum).

**2)** Commentaires sur le Lieu (toute information éventuellement utile, visible uniquement sur cette fiche).

**3)** Sélection d’un site (si la structure se compose de plusieurs sites). Le bouton + permet d'accéder à la liste des

sites et d'en ajouter si besoin. Cette notion est ici purement informative et n’a pas d’influence sur la

surveillance.

**4)** Sélection du ou des groupes auxquels appartient le Lieu. Le bouton + permet d'accéder à la liste des groupes

et d'en rajouter éventuellement. Voir point précédent (P19) pour l’explication groupe 1 & 2.

**5)** Sélection d’un plan et d’une localisation via le bouton Plan et possibilité de supprimer une précédente

localisation. Voir P38 pour plus de détails.

**6)** Module d’alarme associé au lieu (il s'agit de boitiers type gyrophare ou sonore pouvant être ajoutés sur une

installation VigiTemp). En cas d’alarme sur le lieu, le boitier s’actionne.

Table des matières **Dernière MAJ : 01/04/2020** - **Page 22 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

**7)** Sélection d’un document (ex: rapport de cartographie de l’appareil surveillé) si l’on souhaite le stocker dans

VigiTemp et l'associer au lieu en cours de paramétrage.

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

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 23 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

h) Fiche lieu / Onglet métrologie (présentation générale)

**(1)** Choix de la sonde associée au lieu surveillé (par son numéro de série).

**(2)** Informations sur les données métrologiques de la sonde, issues de son étalonnage (Erreur de justesse,

Incertitude et Dérive).

**(3)** Rappel des consignes paramétrées dans l'onglet général.

**(4)** Choix des règles de calcul de l’EMT de surveillance. Selon le choix effectué, les tolérances seront adaptées **(5)** .

Dix possibilités de paramétrage sont possibles, voir à partir de P27 pour plus de détails (par défaut Sans objet).

**(6)** Choix de la prise en compte de l'erreur de justesse dans la mesure (en lien avec le choix des règles de calcul

de l'EMT).

**(7)** Choix de la prise en compte de la dérive dans l'incertitude (en lien avec le choix des règles de calcul de

l'EMT).

**(8)** Accès au suivi SAV de la sonde en lien direct avec la Gestion de Parc Matériel SMILE.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 24 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

i) Fiche lieu / Onglet Téléphonie-Planning

**(1)** : Lié à l’option VigiTel / VigiMail (formation dispensée en cas d’acquisition de l'option). Une documentation

spécialement dédiée à cette fonction est disponible sur simple demande au 04.73.28.55.60 ou vigitemp@mc2lab.fr

**(2)** : Mise en place d'un planning de changement de consignes pour le lieu actuel

Le planning des consignes permet d'effectuer de manière automatique un changement des consignes de surveillance

selon un planning hebdomadaire à définir. Dans notre exemple les consignes du lieu sont les suivantes :

20° +/- 5° du lundi 07:00 au vendredi 18:00

10° +/- 5° du vendredi 18:00 au lundi 07:00

Les consignes (et seuils d'alarme) changent donc automatiquement aux jours et horaires définis. L'échelle des

graphiques s'adapte au niveau de la surveillance.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 25 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

**(1)** : Activer le planning des consignes.

**(2) (3)** : Définir les jours et heures de changement (un seul changement possible par jour).

**(4** ) : Remplir, pour chaque jour, la consigne et limites mini et maxi. Les jours pour lesquels un horaire de changement

a été défini, remplir avec les données avant/après heure de changement.

**(5)** : Définir un retard d'alarme de changement de consigne = Temps laissé à la sonde pour obtenir une stabilisation

de relevé sans déclenchement d'alarme intempestive.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 26 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

j) Fiche lieu / Onglet métrologie (présentation détaillée)

Différents choix peuvent être effectués au niveau des règles de calcul de l'EMT sonde et des tolérances du lieu.

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

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 27 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

Table des matières **Dernière MAJ : 01/04/2020** - **Page 28 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

−
_Cas 1b : Les EMT obéissent à la règle du quart /avec correction de l'erreur de justesse_

L'EMT de la sonde est fixé au quart de l'EMT de l'équipement (5°C dans notre exemple, donc EMT sonde = 5/4 =

1.25). Ce calcul est appliqué automatiquement sur les seuils de tolérances.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée

directement sur la mesure effectuée.

En cas de non-conformité (|Dérive|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur l’écran

principal de la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 29 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

−
_Cas 2a : EMT saisie manuellement /sans correction de l'erreur de justesse_

L'EMT de la sonde peut être saisi de manière manuelle (déduit par exemple selon des méthodes de calcul interne ou

basé sur les données issues de l'étalonnage, l'erreur de justesse devant être prise en compte dans ce calcul).

Dans notre exemple la saisie d'un EMT de la sonde à 0.55 corrige automatiquement les seuils de tolérances.

En cas de non-conformité (si |Erreur de Justesse|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur

l’écran principal de la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 30 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

−
_Cas 2b : EMT saisi manuellement /Avec correction de l'erreur de justesse_

L'EMT de la sonde peut être saisi de manière manuelle (déduit par exemple selon des méthodes de calcul interne ou

basé sur les données issues de l'étalonnage).

Dans notre exemple la saisie d'un EMT sonde à 0.30 corrige automatiquement les seuils de tolérances.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée

directement sur la mesure effectuée.

En cas de non-conformité (|Dérive|+Incertitude étalonnage > EMT), un message d'alerte apparait (sur l’écran

principal de la section métrologie).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 31 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

−
_Cas 3a : Avec prise en compte des incertitudes d'utilisation / sans correction de l'erreur de justesse /_

_sans prise en compte de la dérive dans l'incertitude :_

Dans cet exemple on choisit d'appliquer l'incertitude d'utilisation de la sonde (issue de son étalonnage) sans prise en

compte de l’erreur de justesse sur la mesure de surveillance et sans prise en compte de la dérive.

L'équation suivante est appliquée : 𝐼𝑚𝑒𝑠 =| 𝐸𝑗 |+ 𝐼𝑒𝑡 soit dans notre exemple 𝐼𝑚𝑒𝑠 = 0.29 + 0.20=0.49

Les seuils de tolérance sont adaptés automatiquement. Lors du prochain étalonnage, après insertion des nouvelles

données, l'EMT de la sonde sera mis à jour automatiquement (ainsi que les tolérances).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 32 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

−
_Cas 3b : Avec prise en compte des incertitudes d'utilisation / avec correction de l'erreur de justesse /_

_sans prise en compte de la dérive dans l'incertitude :_

Dans cet exemple on choisit d'appliquer l'incertitude d'utilisation de la sonde (issue de son étalonnage) avec prise en

compte de l’erreur de justesse sur la mesure de surveillance et sans prise en compte de la dérive.

L'équation suivante est appliquée : 𝐼𝑚𝑒𝑠 = 𝐼𝑒𝑡 soit dans notre exemple 𝐼𝑚𝑒𝑠 = 0.20

Les seuils de tolérance sont adaptés automatiquement.

La valeur relative de l'erreur de justesse arrondie au centième (-0.29 dans notre exemple) sera appliquée

directement sur la mesure effectuée.

Lors du prochain étalonnage, après insertion des nouvelles données, l'EMT sonde sera mis à jour automatiquement

(ainsi que les tolérances). Idem concernant l'erreur de justesse.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 33 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

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

|Col1|Col2|Col3|
|---|---|---|
|Table des matières|Dernière MAJ : 01/04/2020 - Page 34 / 65||

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

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

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 35 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

−
_Cas 4a : Sans objet / sans correction de l'erreur de justesse_

Dans cet exemple aucun paramétrage n'a été sélectionné concernant l'EMT de la sonde.

Il n'y a au **c** une correction apportée sur la mesure et sur les tolérances. Le choix de ce paramétrage doit pouvoir se

justifier.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 36 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

−
_Cas 4b : Sans objet / avec correction de l'erreur de justesse_

Dans cet exemple aucun paramétrage n'a été sélectionné concernant l'EMT de la sonde.

Il n'y a au **c** une correction apportée sur les tolérances. La valeur relative de l'erreur de justesse arrondie au centième

(-0.29 dans notre exemple) sera appliquée directement sur la mesure effectuée.

Le choix de ce paramétrage doit pouvoir se justifier.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 37 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

k) Plans

Comme vu précédemment dans la description de l’onglet général de la fiche lieu, il est possible de positionner

visuellement la sonde associée à un lieu sur une image (Ex : plan d’un laboratoire scanné au format image).

Voici comment ajouter un plan :

Avec le bouton ‘Image’ sélectionner le fichier voulu sur le PC puis faire ouvrir après sélection :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 38 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

Le plan sélectionné apparait dans la fiche. Il faut lui mettre un titre puis valider si tout est correct. Sinon il est

possible de supprimer l’image choisie pour en sélectionner une autre ou annuler la manipulation en cours (bouton

‘Fermer’.

A savoir :

     L’ajout d’un plan peut se faire directement depuis la fiche d’un lieu, onglet général, bouton ‘Plans’ à la

ligne Localisation.

Cela permet de placer la sonde du lieu paramétré sur le plan

     - La visualisation du plan se fait dans la partie surveillance ( ou ). Sur le plan affiché, au survol

d’une sonde avec la souris, les détails suivants apparaissent : Nom du lieu, N° de série de la sonde,

Dernier relevé). Si le lieu est en alarme il apparait en rouge.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 39 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

l) Sites

Les sites sont utiles pour créer des tournées dans la partie Datalogger (voir manuel dédié à cette partie). Pour un

système VigiTemp n’utilisant pas la partie Datalogger, cette partie n’a pas d’incidence sur l’organisation de la

surveillance. On peut toutefois créer un ou des sites ici. On les retrouvera dans les fiches lieux et utilisateurs à titre

d’information.

m) Datalogger

Cette partie concerne le paramétrage d’une surveillance par Dataloggers (sondes mobiles). Voir le manuel

spécialement dédié pour cette fonction.

n) Outils

La partie ‘Outils’ est détaillée ci-après selon les différents choix qu’elle regroupe :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 40 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

− _Outils – Test de connexion_

La fonction ‘Outils’ s’ouvre directement sur le test de connexion. Il s’agit ici d’un tableau permettant de tester la

connexion entre une sonde et le module de réception qui lui est associée.

Rechercher dans la liste la sonde à tester par son numéro de série, cocher la case juste devant celui-ci puis appuyer

sur le bouton ‘Lancer’.

La durée du test et l’apparition du résultat dépendent du nombre de sondes en service sur le système VigiTemp, la

puissance du serveur, la qualité du réseau informatique, etc …).

Exemple d’un résultat de test positif :

**(1)** Signal lu = réponse du capteur.

**(2)** Taux de réussite du test en % par rapport au nombre de mesures effectuées **(3)** . Ici 100%.

**(3)** Le nombre de mesures demandées augmente tant que le test n’est pas stoppé.

**(4)** Arrêt du test.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 41 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

Exemple d’un résultat de test négatif :

**(1)** Signal lu = réponse du capteur. Ici rien.

**(2)** Taux de réussite du test en % par rapport au nombre de mesures effectuées **(3)** . Ici 0%.

**(3)** Le nombre de mesures demandées augmente tant que le test n’est pas stoppé.

**(4)** Arrêt du test.

**A savoir :**

     Lorsqu’un test est lancé, cela prend le pas sur la surveillance normale et stoppe les relevés de l’ensemble

des sondes (sauf configuration serveur multicœur). Le test ne doit donc pas durer trop longtemps et il

doit impérativement être stoppé. Si l’on essaie de sortir du test alors que celui-ci est en cours, un

message d’avertissement apparait.

     Le test de connexion s’avère utile lorsque l’on a un doute sur le choix de l’association d’une sonde et

d’un module (dans le cas où plusieurs modules se trouvent à peu près à la même distance de la sonde).

     Dans le cas d’une installation en radiofréquence, un résultat de test en dessous de 50% de réussite peut

refléter un problème de couverture. Refaire le test une seconde fois, déplacer le matériel si possible.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 42 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

− _Outils – Commentaires :_

Cet outil permet de gérer les listes de commentaires prédéfinis qui apparaissent en liste déroulante de choix lors de

la validation d’une action. Exemple ici lors de l’acquittement d’une alarme :

Il faut donc dans un premier temps rédiger les commentaires pour chaque type d’action concernée.

**(1)** Sélection du type d’action (ici Acquittement des alarmes)

**(2)** Rédaction du commentaire

**(3)** Enregistrement du nouveau commentaire

**(4)** Commentaire ajouté à la liste existante

**(5)** Possibilité de suppression d’un commentaire existant (à sélectionner dans la liste)

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 43 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

− _Gestion des PDF :_

Il est possible de créer une base documentaire dans VigiTemp afin d’avoir un accès rapide et centralisé aux différents

documents en lien avec la surveillance paramétrée. Il peut s’agir, par exemple, des rapports d’étalonnage des

sondes, rapports de cartographie des appareils surveillés, notices et mode d’emploi divers, export PDF des

différentes listes présentes dans l’application, etc.

**(1)** Ajouter un nouveau document

**(2)** Modifier un document existant (son titre ou son contenu en prenant un autre fichier)

**(3)** Supprimer un fichier

**(4)** Visualiser un fichier dans le lecteur intégré

En appuyant sur ajouter **(1)**, l’explorateur du PC apparait. Il suffit d’aller chercher le fichier voulu, le sélectionner et

appuyer sur ouvrir.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 44 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

Le fichier apparait ensuite à l’écran. Son nom peut être modifié en haut de l’écran. Il faut ensuite appuyer sur le

bouton ‘Ajouter’ pour terminer le chargement.

Le chargement est terminé, le fichier a été ajouté dans la base documentaire. Il est consultable dans cette partie du

logiciel mais peut également être ajouté en lien dans la fiche de paramétrage d’un lieu (voir P23).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 45 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

−
_Config :_

Il s’agit ici de tableaux synthétiques et récapitulatifs de l’organisation et la configuration du système VigiTemp. Ils

peuvent être exportés sous tableur.

− _Surveillance_

Outils de tests utilisés notamment par les techniciens MC2 en cas de hotline. Cela permet de vérifier que les

dialogues avec le PC serveur sont opérationnels. Exemple :

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 46 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : IV. VigiSurv – Administration : Barre d’outils inférieure

o) Statistiques

Le dernier bouton de la barre d’outils présente un tableau statistique permettant d’afficher pour une période choisie

les données calculées suivantes :

     - Relevé mini

     - Relevé maxi

     Moyenne des relevés

     - Durée des alarmes hautes

     - Durée des alarmes basses

     Durée des dépassements hauts et bas sans alarme

Ce qui donne le tableau suivant (pour les lieux auxquels l’utilisateur connecté a accès) :

Les lieux désactivés apparaissent en gris, les lieux ayant eu des dépassements de tolérances sans alarme sont en

rouge pastel et les lieux ayant eu des alarmes sont en rouge vif.

Les résultats peuvent être exportés sous tableur ou imprimés.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 47 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : V. VigiSurv – Administration : Indicateurs d’état / Divers
## V. VigiSurv – Administration : Indicateurs d’état / Divers

     Le bouton Aide ouvre ce document dans le lecteur PDF par défaut du PC.

     Voyant sauvegarde vert : paramétrage des sauvegardes correct.

     Voyant sauvegarde rouge : problème sur le paramétrage des sauvegardes. Voir P11 pour plus de détails.

     Voyant étalonnages vert : les lieux en surveillance, pour lesquels les données d’étalonnage de leur sonde

ont été chargées, sont dans la période de validité (365 jours par défaut)

     Voyant étalonnages rouge : certains lieux en surveillance, pour lesquels les données d’étalonnage de leur

sonde ont été chargées, ne sont pas dans la période de validité (365 jours par défaut)

En cliquant sur le voyant la liste de(s) lieu(x) concerné(s) apparait :

     Haut-parleur apparent : le son est actif pour les alarmes en cours (dépend des paramètres audios du PC

et de la présence de haut-parleurs).

     Haut-parleur barré : son désactivé pour une durée définie dans les paramètres globaux de l’application

(voir P59)

     Boutons de réduction de l’application ou de fermeture

Table des matières **Dernière MAJ : 01/04/2020** - **Page 48 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant
## VI. VigiSurv – Administration : Bandeau déroulant

En approchant la souris sur le côté gauche de l’écran, un bandeau déroulant apparait automatiquement, permettant

d’accéder aux autres parties du logiciel mais également d’accéder à des outils supplémentaires.

Accès à :

Surveillance

Métrologie

Datalogger

Outils supplémentaires (détaillées dans les chapitres suivants)

A propos affiche la version VigiSurv Fermer pour quitter VigiSurv

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 49 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

a) Gestion des profils

Les profils permettent de déterminer les droits d’accès des utilisateurs dans l’application. Un profil peut être attribué

à plusieurs utilisateurs. Il faut donc paramétrer en premier lieu le ou les différents profils avant de créer les comptes

utilisateurs (chapitre suivant). Cela va permettre de limiter ou interdire l’accès à certaines parties du logiciel.

La page principale présente :

**(1)** Les profils déjà existants et le nombre d’utilisateurs associés pour chacun

**(2)** Les différents boutons permettant de créer un nouveau profil, modifier un profil existant, dupliquer un profil

existant, imprimer la liste et gérer les droits d’un profil.

**A savoir :**

     Les profils Administrateurs MC2 et Administrateurs existent par défaut dans l’application et donnent un

accès complet aux utilisateurs associés.

     La sélection d’un profil dans la liste permet de voir les différents utilisateurs associés.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 50 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

L’écran suivant présente la création d’un profil (bouton Nouveau) :

**(1)** : Donner un nom au profil (+ commentaires informatifs éventuels)

**(2)** : Valider (Bouton en bas à droite de l’écran)

**(3)** : Confirmer l’enregistrement puis le paramétrage des droits

Le paramétrage des droits et autorisations d’un profil se présente sous la forme de cases à cocher selon les accès

que l’on souhaite donner ou non aux utilisateurs qui auront ce profil.

Dans l’exemple ci-dessous, le profil donne accès à la partie surveillance uniquement. Dans cette partie le droit ‘Gérer

les lieux’ a été retiré, les utilisateurs disposant de ce profil ne pourront pas avoir accès à la fiche de paramétrage des

lieux. Ils pourront réaliser le reste des actions possibles dans cette partie (consultation, acquittement,

activation/désactivation de la surveillance, ouverture de la télémaintenance, superposition de courbes et fermeture

de l’application).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 51 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

Valider l’écran une fois le paramétrage voulu terminé.

Il est toujours possible de revenir sur un profil existant par la suite afin d’en modifier les autorisations (Boutons

Modifier ou Droits sur l’écran général des profils).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 52 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

b) Gestion des utilisateurs

VigiTemp permet la gestion d’une base d’utilisateurs. Chaque utilisateur créé dispose d’un login et mot de passe de

connexion, hérite d’un profil d’utilisation et de droits de visualisation à un ou plusieurs groupes de lieux en

surveillance.

La page principale présente :

**(1)** : Les comptes utilisateurs déjà existants

**(2)** : Les différents boutons permettant de créer un nouveau compte, modifier un compte existant, archiver un

compte ou imprimer la liste.

**A savoir :**

Un compte utilisateur ne peut pas être connecté en même temps sur deux postes. Il est donc possible pour un

administrateur de déconnecter un utilisateur afin que celui-ci puisse ouvrir une session sur un poste différent. Pour

l’utilisateur déjà connecté, un pictogramme indiquant cet état est présent dans le tableau (colonne gauche).

L’administrateur sélectionne le compte et appuie sur le bouton ‘Déconnexion’ qui apparait à droite.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 53 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

L’écran suivant présente la création d’un compte utilisateur (Bouton Nouveau) :

**(1)** : Login de l’utilisateur (Identifiant de connexion)

**(2)** : Nom de l’utilisateur

**(3)** : Prénom de l’utilisateur

**(4)** : Téléphone et email : informations facultatives mais à renseigner dans le cas d’alarmes VigiTel (licence

supplémentaire pour être contacté par téléphone ou mail en cas d’alarme)

**(5)** : Mot de passe de l’utilisateur

**(6)** : Profil de l’utilisateur (voir chapitre précédent)

**(7)** : Site (renseignement facultatif, peut être laissé par défaut à Tous)

**(8)** : Groupes à visualiser en surveillance = système de cases à cocher. Aucune case cochée = visualisation de

tous les groupes

‘Valider’ pour terminer la création du compte ou ‘Fermer’ pour annuler.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 54 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

**A savoir :**

     Il est possible de créer des comptes nominatifs ou des comptes génériques (un compte par laboratoire

ou service par exemple). Un même utilisateur peut disposer de plusieurs comptes (login différent par

compte).

     Le choix des groupes visualisés est important car il conditionne la vue obtenue en surveillance.

     Quand on crée un nouveau groupe et qu’il doit être vu par des utilisateurs déjà existants, il faut venir sur

chaque compte concerné pour cocher la case correspondante. Voir P19 pour la gestion des groupes.

c) Gestion des alarmes

Comme à l’écran principal de l’administration, un tableau regroupant toutes les alarmes (en cours et terminées/non

acquittées) du système VigiTemp est présent ici. Il est possible de les visualiser en double-cliquant sur la ligne

correspondante et en effectuer, si besoin, l’acquittement (Voir P13 pour la procédure).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 55 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

d) Schéma de l’implantation

Le schéma de l’implantation est un résumé visuel de l’installation VigiTemp. Il présente sous forme graphique les

différents composants paramétrés en surveillance et leurs liens et l’arborescence obtenue.

**A savoir :**

     Le schéma est utile et pratique dans le cas de problèmes de non-réponses de sondes. Il permet en effet

de voir rapidement si une sonde est connectée au bon module de réception par exemple.

     Une zone du schéma est spécialement dédiée à la fonction serveur multicœurs. Il s’agit d’une nouvelle

option permettant de garantir un niveau de disponibilité de l’application nécessaire à un usage à grande

échelle, grâce à la gestion d’une interrogation multicœurs. Le principe du multicœur consiste à faire

fonctionner plusieurs serveurs VigiTemp sur la même machine, chacun s’occupant d’une partie des

sondes à interroger. Cela permet donc de diminuer le temps de traitement et donc de rendre la solution

bien plus réactive.

Les renseignements nécessaires sur cette fonction sont disponibles sur simple demande.

La mise en œuvre est assurée, sur le serveur VigiTemp, par le service hotline.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 56 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

e) Mesures archivées

Sur une installation VigiTemp en fonction depuis plusieurs années, les temps de chargement et d’affichage des

résultats lors des recherches peuvent parfois être longs. Afin d’améliorer cela il est possible d’archiver une partie des

mesures et journaux (les données les plus anciennes, date butoir à définir avant intervention). Il s’agit d’une

opération réalisée sur le serveur VigiTemp par le service hotline dans le cadre d’un contrat de maintenance VigiTemp

ou à la demande (voir avec le commercial MC2 de votre secteur ou directement auprès du service hotline, détails

P63).

Les données archivées sont donc retirées de la base de production et accessibles ici en lecture.

**(1)** Choix du lieu pour lequel on effectue la recherche

**(2)** Choix de la période de recherche (doit être antérieure à la date butoir définie avant archivage)

**(3)** Effectuer la recherche selon les critères choisis

**(4)** Fermer et revenir à l’administration

Les résultats apparaissent sous forme de trois tableaux : évènements, mesures et graphique. Chaque tableau est

exportable et imprimable.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 57 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

f) Paramètres globaux

Les différentes options et paramétrages présentés ici ont une incidence sur l’ensemble du système VigiTemp (sauf

point 3 expliqué ci-après).

**(1)** Définition d’une politique concernant les mots de passe utilisateur : Norme CFR21 Part11 (= demande de

changement du mot de passe tous les 90 jours et impossibilité de réutiliser un ancien mot de passe) ou choix

libre des différents paramètres (durée de validité, réutilisation d’un ancien mot de passe ou mot de passe

permanent sans demande de changement).

**(2)** Durée en minutes avant verrouillage de l’application, voir Manuel Surveillance (II – B) pour les détails de

cette fonction. Aucune durée par défaut.

**(3)** Connexion automatique d’un utilisateur au lancement de VigiSurv. Il s’agit du seul paramètre de cette page

qui ne concerne que le PC sur lequel on l’applique. Si un compte est sélectionné ici, il sera donc connecté

directement au lancement de VigiSurv qui s’ouvrira sur la fenêtre de surveillance. A la première action d’un

utilisateur sur la fenêtre, le mot de passe ou le changement d’utilisateur seront demandés.

**(4)** Choix de rendre obligatoire ou facultatif le commentaire sur chaque écran de validation d’une action. En

paramétrant obligatoire, les utilisateurs devront impérativement saisir ou choisir un commentaire pour

valider une action. Pour quitter le logiciel, il faudra, en plus du commentaire, saisir le mot de passe

utilisateur.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 58 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

**(5)** Deux options, ici, concernant la sonnerie d’alarme sur les PC ayant VigiSurv ouvert et connecté : la durée

avant réactivation automatique quand le bouton haut-parleur a été cliqué (10 minutes par défaut) et la

sonnerie pour les alarmes terminées non acquittées (par défaut la sonnerie ne concerne que les alarmes en

cours).

10 minutes

(ou durée
modifiée)

**(6)** Gestion des sondes :

   Activer/Désactiver la mémoire des sondes de type IE (utile par exemple en cas de dépannage)

   Enregistrer ou omettre les non-réponses de sondes dans les graphiques et tableaux des mesures, selon si

l’on veut voir les périodes de non-réponses apparaitre visuellement (zones vides dans les tableaux et

trous dans les graphiques).

**(7)** Activation de la présentation graphique « Vision simple » pour la surveillance


Vision

normale,

par

défaut


Vision simple

activée


**(8)** Définition d’un mot de passe « super-admin » qui sera demandé lors de la suppression d’un étalonnage ou

d’une mesure. (MC2LAB par défaut).

**(9)** Valider les changements éventuels apportés dans cette fenêtre.

**(10)** Fermer la fenêtre sans valider les changements éventuels ou pour terminer la consultation.

Table des matières **Dernière MAJ : 01/04/2020** - **Page 59 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

g) Gestion des licences

Dans cette partie il est possible de :

     Visualiser les licences en cours d’utilisation (VigiTemp & VigiTel)

     Modifier une licence (VigiTemp & VigiTel)

     Ajouter une licence VigiTel à un système existant

Pour fonctionner, un système VigiTemp doit disposer au minimum d’une licence 5 utilisateurs :

Explication de la licence VigiTemp 5 utilisateurs :

Permet d’ouvrir VigiSurv sur 5 PC différents en simultané (un compte utilisateur connecté par poste). Pas de
possibilité pour une 6 [ème] connexion à moins d’attendre une déconnexion.

Une licence VigiTemp peut être augmentée par « paquets » de 5 connexions supplémentaires (jusqu'à 255).

Voir avec votre responsable commercial MC2 pour plus de détails.

Explication de la licence VigiTel :

Permet d’ajouter, sur un système VigiTemp, une option de relai des alarmes par téléphone et/ou mail.

Après acquisition de la licence, un numéro doit être renseigné dans l’onglet correspondant.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 60 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

h) Gestion des sauvegardes

Permet d’avoir, dans un tableau un peu moins réduit que celui présent sur l’écran principal de l’administration, la

liste des différents fichiers de sauvegarde actuellement présents sur le serveur VigiTemp. Voir P11 pour plus de

détails sur le système de sauvegarde.

i) Gestion de la téléphonie

Entendre par téléphonie la fonction VigiTel, et plus précisément VigiMail puisqu’ici les différents paramètres liés à

cette fonction peuvent être insérés. L’insertion ou modification de ces paramètres sont réservés au personnel

technique compétent (techniciens MC2 ou personnel informatique de la structure).

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 61 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VI. VigiSurv – Administration : Bandeau déroulant

Table des matières **Dernière MAJ : 01/04/2020** - **Page 62 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VII. Hotline et dépannage
## VII. Hotline et dépannage

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

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 63 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VII. Hotline et dépannage

−
_Zoom sur la télémaintenance (Surveillance) :_

Le bouton télémaintenance situé dans la barre d’outils en haut de l’écran principal de la surveillance permet

d’afficher le numéro de téléphone de la hotline :

Après avoir appuyé sur le bouton OK, le logiciel de prise en main à distance TeamViewer est lancé automatiquement

(soit la version MC2 Hotline, soit TeamViewer si ce dernier est déjà installé et exécuté sur le PC) :

Version MC2 Hotline

(incluse avec VigiSurv)

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 64 / 65**

## VigiSurv 10.200 : Manuel d’utilisation de l’administration

En cours : VII. Hotline et dépannage

Version TeamViewer

(si déjà sur le PC)

Il suffit ensuite de communiquer les codes affichés à l’écran (ID et Mot de passe) au technicien hotline afin que celui
ci puisse prendre la main sur le PC et réaliser les vérifications nécessaires.

**A savoir :**

     Selon le profil et les droits d’accès de l’utilisateur connecté, le bouton télémaintenance n’est pas

accessible (visible mais inactif). Dans ce cas prendre contact avec le(s) référent(s) VigiTemp de votre

structure.

     Si le logiciel MC2 Hotline s’ouvre mais n’affiche aucun code (ID et mot de passe) cela peut signifier que

ce type de connexion n’est pas autorisé par votre service informatique.

Table des matières **Dernière MAJ : 01/04/2020**  - **Page 65 / 65**

