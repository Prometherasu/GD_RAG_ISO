|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|


**1.** **OBJECTIFS ET CHAMP D’APPLICATION**

L’objectif du projet vise à rédiger un dossier de validation de méthode dans le cadre d’une
demande d’accréditation par la plateforme de génotypages de GD Biotech (société GÈNES
DIFFUSION) selon la norme ISO 17025 des laboratoires d’analyse et d’essai. Ce dossier
concerne plus particulièrement la méthode d’extraction d’ADN sur colonne de silice par
méthode manuelle. Il s’agit d’une méthode non reconnue pour laquelle aucun référentiel
n’est disponible. C’est pourquoi le présent dossier rassemble les éléments en permettant sa
validation en portée FLEX 3.

**2.** **DEFINITIONS / ABREVIATIONS**

ADN : Acide Désoxy ~~ribo~~ ~~Nucléique~~

**3.** **TEXTE DE RÉFÉRENCE**

La présente procédure tient compte des exigences de la norme NF EN ISO/IEC 17025.

**4.** **PERSONNEL CONCERNÉ**

Pilote du projet : Christophe AUDEBERT, Directeur Recherche & Développement.
L’ensemble du personnel de la plateforme de génotypage haut-débit.

**5.** **DESCRIPTION ET DÉROULEMENT DES OPÉRATIONS**

**5.1 Intitulé de méthode**

Extraction d’ADN manuelle sur colonne de silice _ méthode interne

**5.2 Elaboration du développement**

**5.2.1 Type de validation**
Adoption : oui ▣ non ▢
Adaptation : oui ▣ non ▢
Développement : oui ▣ non ▢

**5.2.2 Revue de méthodes**

Référentiel(s) : oui ▢ non ▣

1/9

|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|


**5.3 Contraintes du projet**
La qualité et la quantité de prélèvement à extraire. La méthode d’extraction est destructive
pour certaines catégories de prélèvements, les tests de répétabilité et de reproductibilité
sont limités pour un même échantillon.

**5.4 Caractéristiques de la méthode et performances attendues**

**5.4.1 Matrices**

Les extractions sont réalisées à partir de 4 types de prélèvements bovin (au choix du client) :



|Nature du prélèvement|Conditionnement|Conservation pré-traitement|
|---|---|---|
|sang total|tube EDTA|température ambiante|
|bulbes de poils|pochette Kit GDScan|température ambiante|
|biopsie auriculaire = cartilage|tube humide|température ambiante|
|semence|paillette de conservation de<br>sperme dilué|température ambiante|


**5.4.2 Paramètres**

Le paramètre analysé est la concentration d’ADN. La qualité de l’ADN n’est pas un
paramètre mesuré dans le présent dossier, la méthode de génotypage Illumina n’y faisant
pas référence.

**5.4.3 Principe de l’analyse**
Les prélèvements et leur conservation préalable à l’envoi pour génotypage sont sous la
responsabilité du client du laboratoire. Les échantillons sont réceptionnés au laboratoire
avec un code à barres (CAB) unique (composé des lettres GD suivies de 6 chiffres),
identifiant clé du prélèvement jusqu’au rendu de résultat.
L’ensemble des informations liées aux prélèvements (enregistrement et traçabilité) tout au
long de la méthode d’extraction d’ADN est enregistré au niveau du serveur commun
partage_labo, en base de données et dans Google Drive.
Les prélèvements sont traités, lysés puis déposés sur colonne de silice. Des étapes
successives de précipitation, adsorption sur colonne de silice, de lavage puis d’élution sont
réalisées manuellement pour purifier l’ADN. La quantité d’ADN obtenue suite à l’extraction
est dosée par mesure de fluorescence au PicoGreen. Une gamme étalon est réalisée à
chaque série de quantification et sert de référence pour déterminer la concentration en ADN

2/9

|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|


des échantillons.

_Remarque : Pour certains projets, notamment de recherche, il existe des conditions_
_spécifiques de traitement (ex : stockage du prélèvement brut dans un premier temps, puis_
_déstockage d’une sélection d’entre eux ultérieurement pour extraction/génotypage). Ainsi,_
_chaque fois qu’un nouveau projet est créé, une fiche projet doit être complétée par le_
_référent du projet, qui la diffuse par mail à l’ensemble de l’équipe de la plateforme de_
_génotypage haut-débit_ (GDB/FORM/11/Fiche projet_v1.0) _._

**5.4.4 Domaine d’application**
Le domaine d’application de la présente méthode s’applique à l’ensemble des prélèvements
reçus au laboratoire de génotypage haut débit.

**5.4.5 Critères de performance attendus**
Le critère de performance concernant la phase d’extraction de l’ADN est la quantité d’ADN
extraite, l’objectif étant l’obtention d’une quantité supérieure à 15 ng/µL, pour envoi de
l’échantillon d’ADN en phase de génotypage.

**5.5 Analyse**

**5.5.1 Modes opératoires**
Les modes opératoires d’extraction d’ADN des différents types de prélèvements sont listés
au niveau du point 6.DOCUMENTS ASSOCIÉS du présent document.

**5.5.2 Points à développer**

➢ _**Matériel**_




|Description|Raccordement<br>Métrologique|Commentaires|
|---|---|---|
|Micropipettes|Micropipettes|Micropipettes|
|P1200 Multi électronique|Oui|Métrologie sous-traitée|
|P200 Multi|Oui|Métrologie sous-traitée|
|P100 Multi|Oui|Métrologie sous-traitée|
|P10 Multi|Oui|Métrologie sous-traitée|
|P1000 mono|Oui|Métrologie sous-traitée|


3/9

|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|









|P200 mono|Oui|Métrologie sous-traitée|
|---|---|---|
|P10 mono|Oui|Métrologie sous-traitée|
|Centrifugeuses|Centrifugeuses|Centrifugeuses|
|Centrifugeuse rotor 2 plaques|Oui|Métrologie sous-traitée|
|Centrifugeuse de paillasse 12 tubes|Oui|Métrologie réalisée en interne|
|Incubateurs|Incubateurs|Incubateurs|
|Agitateurs chauffants (tubes/2<br>plaques)|Oui|Métrologie réalisée en interne|
|Agitateurs|Agitateurs|Agitateurs|
|Vortex (1 tube)|Non|Vortex de paillasse pour tube sang total|
|Enceintes de stockage froid|Enceintes de stockage froid|Enceintes de stockage froid|
|Description|Raccordement<br>Métrologique|Commentaires|
|Réfrigérateur (+ 4°C)|Oui|Métrologie réalisée en interne +<br>cartographie 1 x tous les 2 ans|
|Fluorimètre|Fluorimètre|Fluorimètre|
|Lecteur de plaques SPARK|Oui|Métrologie réalisée en interne|
|PC SPARK|Non||
|Bureautique - Informatique|Bureautique - Informatique|Bureautique - Informatique|
|PC|Non||
|Scanner (lecteur CAB)|Non||
|Imprimante|Non||


Le type de raccordement et la fréquence métrologique de l’ensemble du matériel est
consultable dans le document GDB/PRO/13/Métrologie_v1.0 _**.**_

4/9

|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|


➢ _**Kits et réactifs**_










|Kits d’extraction et autres réactifs|Col2|Col3|
|---|---|---|
|Produits / Consommables|Spécifications<br>attendues|Stockages|
|Kit Blood Macherey Nagel (core)|Réception à température<br>ambiante, pas de<br>spécification particulière|Protéinase K diluée -21°C +/- 3°C<br>Colonnes à 5°C +/- 3°C<br>Autres réactifs à 21°C +/- 3°C|
|Kit Blood tubes|Kit Blood tubes|Kit Blood tubes|
|Kit Tissue Macherey Nagel|Kit Tissue Macherey Nagel|Protéinase K diluée -21°C +/- 3°C<br>Réactifs à 21°C +/- 3°C|
|MiniKit Qiagen|MiniKit Qiagen|20°C +/- 5°C|
|Protéinase K Qiagen<br>additionnelle|Protéinase K Qiagen<br>additionnelle|20°C +/- 5°C|
|TE 1X|TE 1X|Température ambiante|
|TE 100X|TE 100X|Température ambiante|
|DTT|DTT|Flacon source à 5°C +/- 3°C<br>Aliquots de 100µl à -21°C +/- 3°C|
|Ethanol absolu|Ethanol absolu|Température ambiante|
|Picogreen|A l’obscurité|5°C +/- 3°C, à l’obscurité|
|ADN témoin|100 ng/µL|à 5°C +/- 3°C|


➢ _**Matrices**_









|Type de matrice|Spécifications attendues|Stockages|
|---|---|---|
|Sang|quantité minimale 200µl<br>non coagulé|5°C +/- 3°C<br>pendant minimum 21 jours<br>après extraction|
|Poil|quantité > 30 bulbes|Température ambiante pendant<br>21 jours après extraction|
|Biopsie auriculaire = cartilage|tube Allflex avec liquide<br>conservation|Température ambiante|


5/9

|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|


|Semence|2 paillettes décongelées|Température ambiante|
|---|---|---|
|Semence sexée|4 paillettes décongelées|Température ambiante|
|ADN||5°C +/- 3°C jusqu’au<br>génotypage, puis -21°C +/- 3°C<br>pendant 2 ans|


➢ _**Milieu**_

Pas de spécification

**5.5.3 Main d’oeuvre**

Les fonctions concernées par ce poste sont les Techniciens scientifiques et Responsable
activité de génotypage haut-débit. La description des fonctions et de la (ou des) formation(s)
est définie dans la fiche de poste et fiches de fonctions relatives. Les critères d’habilitation et
de maintien de compétences sont définis dans ces mêmes fiches.




|Poste Extraction d’ADN|Critères d’habilitation|Critères de maintien de<br>compétence|
|---|---|---|
|Responsable activité de<br>génotypage haut-débit|ANALYSE :<br>- seuil > 3 ans<br>d'ancienneté en<br>réalisation<br>d’extractions d’ADN<br>ou<br>- Réaliser en autonomie :<br>32 extractions ADN de<br>matrice sang, 32<br>extractions ADN de<br>matrice poils, 10<br>extractions ADN de<br>matrice semence<br>Objectifs : [ADN] > 15<br>ng/µL|Être en poste au moins une<br>fois tous les 6 mois.|
|Technicien scientifique|Technicien scientifique|Technicien scientifique|


➢ _**Fiche de poste - Fiche de fonction**_
La fiche de poste correspondante est consultable via le GDB/FI/08/Fiche de poste Extraction
ADN_v1.0.La fiche de fonction correspondante est consultable via GDB/FI/12/Fiche de
fonction Responsable activité génotypage haut-débit_v1.0.

6/9

|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|


**5.6 Critères de performance**

Dans le présent dossier, répétabilité et reproductibilité sont traitées au niveau de la phase
d’extraction et de dosage de l’ADN, et la méthodologie reprise dans la procédure
GDB/PRO/06/Contrôle de répétabilité et de reproductibilité de la phase d'extraction_v1.0. Le
contrôle de répétabilité, reproductibilité porte sur la méthode d’extraction d’ADN issus de
plusieurs matrices biologiques : sang, semence, poils ( concernant la matrice biologique
“cartilage”, le protocole d’extraction aboutit à la destruction de l’échantillon. Pour des
principes évidents de bien-être animal il est inconcevable de posséder plusieurs
prélèvements issus d’un même animal, et les tests de répétabilité et reproductibilité ne
seront donc pas effectués à partir de cette matrice).

Les résultats reproductibilité consisteront à la comparaison inter-opérateur (taux
d’échantillons conformes (concentration de l’ADN extrait est > 15 ng/ µL) d’une part, et
comparaison des dosages d’un même échantillon évalué par deux opérateurs différents
d’autre part. Pour simplifier, les deux opérateurs pratiquent une extraction sur les mêmes
matrices biologiques de départ.
Les résultats de ce contrôle répétabilité/reproductibilité et l'interprétation de l’analyse de ces
échantillons contrôles sont rendus de manière annuelle à l’occasion du reporting de suivi de
production. Seront privilégiées les métriques synthétiques :

   synthèse des métriques de répétabilité/reproductibilité

   - dans le cas de non conformité il conviendra de commenter les mesures correctives

mises en oeuvre

**5.7 Facteurs de risques**

~~L’ensemble~~ ~~des~~ ~~facteurs~~ ~~de~~ ~~risques~~ ~~identifiés~~ ~~sont~~ ~~analysés~~ ~~et~~ ~~consultables~~ ~~via~~ ~~le~~ ~~document~~
~~GDB/PRO/08/Actions~~ ~~à~~ ~~mettre~~ ~~en~~ ~~oeuvre~~ ~~suite~~ ~~à~~ ~~non~~ ~~conformités~~ _ ~~v1~~ . ~~0~~ .

**5.8 Incertitudes**

La notion d’incertitude ne s’applique qu’à la seule méthode de dosage de la concentration
d’ADN. A l’issue de la mesure de concentration (dont l’incertitude de mesure dépend
directement du coefficient directeur de la droite de régression linéaire associée à la
réalisation de la gamme étalon), l’extraction est qualifiée ou non. Ainsi l’aboutissement de la
phase d’extraction d’ADN n’est pas une concentration en tant que telle mais une
qualification de l’extrait qui satisfera ou non un seuil minimal exigé.

7/9

|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|


**5.9.Surveillance de la qualité des résultats**



|Contrôle Qualité<br>interne|Oui / non|Carte de contrôle|Commentaires|
|---|---|---|---|
|Gamme étalons à<br>partir d’ADN témoin|Oui|Non|Gamme étalon<br>réalisée pour chaque<br>série de quantification<br>R² > 0,99|


**5.10 Confirmation et vérification**

**5.10.1 Validation**

Validation des critères de performance par Christophe AUDEBERT, Directeur Recherche et
Développement.
Méthode validée dans son domaine d’application décrit en 5.4.4 du présent document.

Date :    26/11/2021

**6.** **DOCUMENTS ASSOCIÉS**

~~GDB/PRS/01/Schéma~~ ~~traçabilité~~ ~~échantillon~~ _ ~~v1~~ . ~~0~~
~~GDB/PRS/02/Processus~~ ~~global~~ ~~de~~ ~~la~~ ~~matrice~~ ~~biologique~~ ~~au~~ ~~rendu~~ ~~analytique~~ _ ~~v1~~ . ~~0~~
~~GDB/PRS/05/Extraction~~ ~~d'ADN~~ _ ~~v1~~ . ~~0~~
~~GDB/PRO/06/Contrôle~~ ~~de~~ ~~répétabilité~~ ~~et~~ ~~de~~ ~~reproductibilité~~ ~~de~~ ~~la~~ ~~phase~~ ~~d'extraction~~ _ ~~v1~~ . ~~0~~
~~GDB/PRO/08/Actions~~ ~~à~~ ~~mettre~~ ~~en~~ ~~oeuvre~~ ~~suite~~ ~~à~~ ~~non~~ ~~conformités~~ _ ~~v1~~ . ~~0~~
~~GDB/PRO/13/Métrologie~~ _ ~~v1~~ . ~~0~~
~~GDB/MOP/01/Préparation~~ ~~des~~ ~~matrices~~ ~~pour~~ ~~extraction~~ ~~d'ADN~~ ~~à~~ ~~partir~~ ~~de~~ ~~prélèvements~~ ~~de~~
~~sang~~ _ ~~v1~~ . ~~0~~
~~GDB/MOP/02/Préparation~~ ~~des~~ ~~matrices~~ ~~pour~~ ~~extraction~~ ~~d'ADN~~ ~~à~~ ~~partir~~ ~~de~~ ~~prélèvements~~ ~~de~~
~~poils~~ ~~et~~ ~~cartilage~~ _ ~~v1~~ . ~~0~~
~~GDB/MOP/03/Extraction~~ ~~d'ADN~~ ~~en~~ ~~plaque~~ ~~à~~ ~~partir~~ ~~de~~ ~~cartilage/poil~~ _ ~~v1~~ . ~~0~~
~~GDB/MOP/04/Extraction~~ ~~d'ADN~~ ~~en~~ ~~tube~~ ~~à~~ ~~partir~~ ~~de~~ ~~semence~~ _ ~~v1~~ . ~~0~~
~~GDB/MOP/05/Extraction~~ ~~d'ADN~~ ~~en~~ ~~plaque~~ ~~à~~ ~~partir~~ ~~de~~ ~~sang~~ _ ~~v1~~ . ~~0~~
~~GDB/MOP/06/Extraction~~ ~~d'ADN~~ ~~en~~ ~~tube~~ ~~à~~ ~~partir~~ ~~de~~ ~~sang~~ _ ~~v1~~ . ~~0~~
~~GDB/MOP/07/Elaboration~~ ~~des~~ ~~fichiers~~ ~~d’extraction~~ _ ~~v1~~ . ~~0~~
~~GDB/MOP/08/Dosage~~ ~~ADN~~ _ ~~v1~~ . ~~0~~
~~GDB/FI/08/Fiche~~ ~~de~~ ~~poste~~ ~~Extraction~~ ~~ADN~~ _ ~~v1~~ . ~~0~~
~~GDB/FI/12/Fiche~~ ~~de~~ ~~fonction~~ ~~Responsable~~ ~~activité~~ ~~génotypage~~ ~~haut~~ - ~~débit~~ _ ~~v1~~ . ~~0~~

8/9

|Col1|Synthèse de la validation de méthode<br>extraction|Version 1.0|
|---|---|---|
|GDB_ENR_58|SMQ|26/11/2021|
|Rédaction :<br>K. LE ROUX|Vérification :<br>C. AUDEBERT, L. LIETAR|Approbation :<br>C. AUDEBERT|


~~GDB/FORM/02/Contrôle~~ ~~de~~ ~~répétabilité~~ ~~et~~ ~~de~~ ~~reproductibilité~~ ~~de~~ ~~la~~ ~~phase~~ ~~d'extraction~~ _ ~~v1~~ . ~~0~~
~~GDB/FORM/03/Habilitation~~ ~~extraction~~ ~~ADN~~ _ ~~v1~~ . ~~0~~
~~GDB/FORM/11/Fiche~~ ~~projet~~ _ ~~v1~~ . ~~0~~
~~GDB/ENR/06/Etude~~ ~~de~~ ~~la~~ ~~conservation~~ ~~des~~ ~~extractions~~ ~~ADN~~ ~~au~~ ~~cours~~ ~~du~~ ~~temps~~ _ ~~v1~~ . ~~0~~

**7.** **ANNEXE(S)**

9/9

