|Col1|Process Commande|Version 1.0|
|---|---|---|
|GDB_MOP_34|SMQ|31/07/2024|
|Rédaction :<br>S.MARTEL|Vérification :<br>L. LIETAR|Approbation :<br>S.MERLIN|


**Ce protocole s’adresse aux personnes habilitées à passer des commandes**
**consommables pour le laboratoire de génotypage haut-débit.**

**GD Stock : application pour la gestion des stocks**
La gestion des stocks des consommables et kits du laboratoire se fait sur l’application “GD
Stock” suivant le lien GD stocklabo (http://stocklabo.gspp2gdlab.genesdiffusion.com/) (login
et mdp identiques à ceux utilisés sur GD Board).

Pour plus d’information sur l’utilisation de l’application, lire le document
GDB_FI_45_Application GDStock - Descriptif et Mode d'emploi

**Passer une commande**

Chaque lundi, un mail de gdscan-production, [STOCK_LABO_ALERTE], est envoyé au
responsable achat ainsi qu’aux suppléants. Il contient la liste des produits “stock faible” avec
le nombre de produits encore en stock, la quantité à commander si besoin, et l’information
fournisseur/référence.

1) Vérifier le nombre de commandes à passer pour l’ensemble des produits de la liste

envoyée.
2) Ouvrir le fichier de mise en concurrence GDB_ENR_60_Mise en concurrence

fournisseurs consommables sur le Dashboard. Ce document répertorie l’ensemble des
produits pouvant être commandés ainsi que les tarifs annuels et références pour
chacun des 3 fournisseurs référencés.

3) Rechercher la(es) référence(s) pour la(es)quelle(s) une commande doit être passée
4) Pour réaliser la commande, se connecter sur le site du fournisseur de la référence

concernée. Pour les personnes habilitées, l'accès aux informations de connexion des
fournisseurs est disponible dans le coffre-fort Bitwarden
(https://bitwarden.gspp2gdlab.genesdiffusion.com/#/). Le login est le suivant :
fournisseurs_labo@genesdiffusion.com. En cas de besoin, le mot de passe est
disponible auprès du responsable achat ou du responsable SI.
5) Une fois connecté, copier le login et le mot de passe du fournisseur concerné par la

commande.

_Remarque : le tarif du produit est le critère N°1 pour passer une commande. Néanmoins, avant_
_toute commande, il est nécessaire de vérifier la disponibilité des produits. La faveur pourra_
_être donnée à une référence plus couteuse mais disponible plus rapidement selon l'urgence_
_du besoin._

6) Les fournisseurs :

a) Fischer Scientific : [https://www.fishersci.fr/fr/fr/home.html](https://www.fishersci.fr/fr/fr/home.html)

1/3

|Col1|Process Commande|Version 1.0|
|---|---|---|
|GDB_MOP_34|SMQ|31/07/2024|
|Rédaction :<br>S.MARTEL|Vérification :<br>L. LIETAR|Approbation :<br>S.MERLIN|


i) Se connecter, onglet “Votre compte”
ii) Rechercher la référence et sélectionner la quantité à commander
iii) Une fois la commande terminée, cliquer sur “Aller au panier” puis sur

“Démarrer la validation des achats”

iv) Sélectionner la bonne adresse de livraison et de facturation avant toute

validation de commande

v) Compléter la case “Votre référence au choix” : GDDaaaammjj_X (X

étant le nombre de la commande passée sur la journée/fournisseur,
_exemple : GDD20230809_1_ )
vi) Cliquer sur “Vérifier et valider”

b) [Dominique Dutscher : https://www.dutscher.com/](https://www.dutscher.com/)

i) Se connecter, ici :
ii) Rechercher la référence et sélectionner la quantité à commander
iii) Cliquer sur le panier une fois la commande terminée et cliquer sur

“Finaliser la commande”

iv) Sélectionner l’adresse de livraison et de facturation

v) Donner un nom de commande : GDDaaaammjj_X (X étant le nombre

de la commande passée sur la journée/fournisseur, _exemple :_
_GDD20230809_1_ )
vi) Mettre un tiret dans la case “N° de projet / Ligne budgétaire / Code

service Chorus”

vii) Cliquer sur “Commander” (le paiement se fait directement par

facturation)
viii) Une fenêtre s’affiche : accepter toutes les conditions générales avant

de cliquer sur “continuer”

[c) Macherey-Nagel : https://www.mn-net.com/fr/](https://www.mn-net.com/fr/)

i) Se connecter, onglet “Mon compte”
ii) Pour chaque chaque référence utilisée en routine, il y a une liste de

favoris, cliquer sur “memo”, la liste des produits favoris s’affiche
iii) Cliquer sur le(s) produit(s) à commander et indiquer la quantité

nécessaire et cliquer sur “ajouter au panier”
iv) Cliquer sur “passer en caisse”, cocher la mention “Confirmation de

lecture”

v) Sélectionner l’adresse de livraison et de facturation
vi) Donner un nom de commande : GDDaaaammjj_X (X étant le nombre

de la commande passée sur la journée/fournisseur, _exemple :_
_GDD20230809_1_ )

2/3

|Col1|Process Commande|Version 1.0|
|---|---|---|
|GDB_MOP_34|SMQ|31/07/2024|
|Rédaction :<br>S.MARTEL|Vérification :<br>L. LIETAR|Approbation :<br>S.MERLIN|


Remarque : s’il y a un besoin de MB2, qui n’est pas dans la liste de favoris, dans la case
“commentaires” de l’onglet “Remarques”, indiquer “ajouter XU (X correspondant au nombre
d’unité souhaitées), la référence du produit et préciser l'offre de prix annuelle indiquée en note
dans GDB_ENR_60_Mise en concurrence fournisseurs consommables”

vii) Cliquer sur “Commander avec obligation de paiement” (le paiement

sera effectué via une facture après réception de la marchandise)

Remarque : concernant le paiement des commandes, celui-ci est automatiquement effectué
par facturation. Celle-ci est mise en paiement après validation de la réception des
marchandises.

GD Stock : renseigner les commandes passées dans l’application

1) Dans GD Stock, onglet “SHOPPING”, cliquer sur le “chariot +” du produit commandé

précédemment
2) Sélectionner le fournisseur de la commande, indiquer le numéro de la commande

(GDDaaaammjj_X), la quantité commandée, le prix annuel est renseigné par défaut.
Si toutefois le tarif devait être différent à celui pré-enregistré, il est possible de l’editer.
3) Sur l'onglet principal “DASHBOARD STOCK LABO”, la liste des commandes passées

apparaît dans la partie “Liste des produits en cours de réapprovisionnement”. Cela
permet à la personne responsable de la gestion des stocks de voir les prochaines
commandes à réceptionner au laboratoire.

Besoins particuliers
Dans le cas d’un besoin urgent ou d’une commande d’une référence en particulier (non
référencée), et de l’absence du responsable achat, il convient de contacter le représentant
commercial du fournisseur directement via l’adresse mail qui se trouve sur le compte client ou
sur le document GDB_FI_54_Référentiel Fournisseurs_v1.0.

**Documents associés :**

GDB_FI_45_Application GDStock - Descriptif et Mode d'emploi

GDB_ENR_60_Mise en concurrence fournisseurs consommables

GDB_PRO_31_Gestion des produits et services fournis par des prestataires externes

3/3

