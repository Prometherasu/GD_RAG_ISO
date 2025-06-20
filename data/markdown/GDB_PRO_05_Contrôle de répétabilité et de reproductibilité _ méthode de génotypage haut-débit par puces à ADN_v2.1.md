|Col1|Contrôle de répétabilité et de<br>reproductibilité :<br>méthode de génotypage haut-débit par<br>puces à ADN|Version 2.1|
|---|---|---|
|GDB_PRO_05|SMQ|16/12/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>C. AUDEBERT|Approbation :<br>L. LIETAR|


**1.** **OBJECTIFS ET CHAMP D’APPLICATION**

Le document définit les modalités de contrôle de répétabilité et de reproductibilité mis en
place au sein de la plateforme de génotypage haut-débit GD Scan.

**2.** **DEFINITIONS / ABREVIATIONS**

Répétabilité : part de variabilité due au dispositif de mesure dans notre système de mesure.
La répétabilité est la variation due à l'instrument de mesure. Il s'agit de la variation observée
lorsque le même opérateur mesure la même pièce de nombreuses fois, à l'aide de la même
instrumentation, dans les mêmes conditions. Dans notre contexte il s’agit de mesurer la
variabilité des résultats de génotypages (formes AA, AB, BB) aux marqueurs génotypés (cf
GDB_FI_15_SNP ISO 580) d’un même échantillon génotypé sous les mêmes conditions
(même puce à ADN, même jour, même manipulateur)

Reproductibilité : part de variabilité due aux différences entre les opérateurs dans notre
système de mesure. La reproductibilité est la variation due au système de mesure. Il s'agit de
la variation observée lorsque différents opérateurs mesurent la même pièce de nombreuses
fois, à l'aide de la même instrumentation, dans les mêmes conditions. Dans notre contexte
plus précisément, il s’agit de comparer les résultats de génotypages (AA, AB, BB) entre deux
échantillons issus d’un même individu obtenus sur deux puces à ADN différentes. Ceci revient
pour nous à comparer les résultats de génotypage d’un bovin obtenus sur deux runs de
génotypage distincts.

**3.** **TEXTE DE RÉFÉRENCE**

La présente procédure tient compte des exigences de la norme NF EN ISO/IEC 17025.

**4.** **PERSONNEL CONCERNÉ**

L’ensemble du personnel impliqué dans la production de génotypage haut-débit.

**5.** **DESCRIPTION DES OPÉRATIONS EN SITUATION NORMALE DE**

**FONCTIONNEMENT**

Notre contexte analytique aboutit à la production de données de type AA, AB, BB
(homozygotes forme AA, hétérozygotes AB ou homozygotes BB) à un marqueur donné. En

1/6

|Col1|Contrôle de répétabilité et de<br>reproductibilité :<br>méthode de génotypage haut-débit par<br>puces à ADN|Version 2.1|
|---|---|---|
|GDB_PRO_05|SMQ|16/12/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>C. AUDEBERT|Approbation :<br>L. LIETAR|


parallèle, plusieurs dizaines de marqueurs (GDB_FI_15_SNP ISO 580) sont analysés pour
aboutir à n génotypes (nombre de marqueurs génotypés en parallèle) au format “AA”, “AB”,
“BB” ou ”--” dans le cas d’une absence de données sur chacun des marqueurs génotypés.

**5.1 Objectif**

Le contrôle de répétabilité, reproductibilité porte ici sur la méthode de génotypage haut-débit.
Les opérations en amont de cette phase de production de données biologiques ne sont (car
ne peuvent) pas directement concernées. Néanmoins, les dysfonctionnements possibles
concernant les parties amont telle que la phase d’extraction d’ADN par exemple ont un impact
direct sur les métriques ciblées ici. Un dysfonctionnement de ces phases en amont de la phase
de génotypage haut-débit pourra engendrer une détérioration de ces métriques.

**5.2 Mode opératoire pour la mise en application du contrôle**

**5.2.1 Synoptique organisationnel**
Un contrôle sera effectué chaque semaine d’indexation (dont les résultats seront pris en
compte dans l’analyse hebdomadaire), et concernera donc une seule plaque, si possible
génotypée à compter du lundi.
Conformément au diagramme organisationnel présenté ci-dessous, après une semaine n, dite
d’amorçage, les semaines n+1 et au-delà sont rigoureusement identiques en termes
d’organisation. Il convient pour la semaine n de dupliquer l’échantillon présent en position A08
sur la position laissée vacante B08. Ce même échantillon génétique (même extraction d’ADN)
sera conservé pour être reporté la semaine suivante n+1, en position C08 de la plaque QC
n+1 laissée vacante. En semaine n+1 de la même façon sera dupliqué l’échantillon génétique
présent en A08, pour être reporté au niveau de la position B08 laissée vacante.
Les positions concernées sont reprises dans le schéma de plaque 96 puits repris dans la
figure 2 ci-après.

~~Cette~~ ~~actuelle~~ ~~procédure~~ ~~peut~~ ~~en~~ ~~outre~~ ~~permettre~~ ~~de~~ ~~val~~ ider u ~~ne~~ n ~~ouvel~~ l ~~e~~ ~~mé~~ th ~~od~~ e ~~ou~~ ~~l~~ a mi ~~se~~
~~en~~ ~~service~~ ~~de~~ ~~tout~~ ~~nouveau~~ ~~matériel~~ .

2/6

|Col1|Contrôle de répétabilité et de<br>reproductibilité :<br>méthode de génotypage haut-débit par<br>puces à ADN|Version 2.1|
|---|---|---|
|GDB_PRO_05|SMQ|16/12/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>C. AUDEBERT|Approbation :<br>L. LIETAR|


Figure 1 : représentation schématique de l’organisation du test de répétabilité/reproductibilité
en termes de gestion d’échantillon (ADN extrait)

**5.2.2 Échantillons qualité**

Le principe général de cette procédure repose sur le fait qu’un échantillon considéré pour la
réalisation de contrôle de répétabilité et de reproductibilité l’est de manière aléatoire puisqu’il
s’agit de duplication d’échantillon d’ADN de routine.

3/6

|Col1|Contrôle de répétabilité et de<br>reproductibilité :<br>méthode de génotypage haut-débit par<br>puces à ADN|Version 2.1|
|---|---|---|
|GDB_PRO_05|SMQ|16/12/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>C. AUDEBERT|Approbation :<br>L. LIETAR|


Figure 2 : représentation schématique des positions clés sur plaque d’échantillons d’ADN

source

**5.3** **Métriques**

**5.3.1 Répétabilité**

Pour être considéré, tout échantillon devra atteindre un seuil de CallRate 580 minimal de 0,95.
Pour être considéré comme conforme, un test de répétabilité doit renvoyer à un minimum strict
de 95 % de génotypes identiques
Tout test < 95 % sera considéré comme non valide, ce qui déclenchera une procédure de
vérification.

**5.3.2 Reproductibilité**

Pour être considéré, tout échantillon devra atteindre un seuil de CallRate 580 minimal de 0,95.
Pour être considéré comme conforme, un test de reproductibilité doit renvoyer à un minimum
strict de 95 % de génotypes identiques.
Tout test < 95 % sera considéré comme non valide, ce qui déclenchera une procédure de
vérification.

4/6

|Col1|Contrôle de répétabilité et de<br>reproductibilité :<br>méthode de génotypage haut-débit par<br>puces à ADN|Version 2.1|
|---|---|---|
|GDB_PRO_05|SMQ|16/12/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>C. AUDEBERT|Approbation :<br>L. LIETAR|


**5.4 Reporting**



Les résultats de ce contrôle qualité seront rendus disponibles de façon hebdomadaire, le
vendredi, via l’interface “DashBoard Génomique” [1] . L’analyse de résultats de ce contrôle
qualité est commentée lors des revues de direction si des mesures correctives ont été mises

en œuvre.

**5.5 Mise en œuvre de la procédure de vérification suite à un**
**contrôle non valide**

**5.5.1 QC à usage de validation de méthode ou de mise en service de nouveau matériel**
Dans ce cadre, le QC est impérieusement nécessaire pour procéder à ces deux types de
validation. Ainsi, tout contrôle invalide pour ces deux usages entrainera l’invalidité de la
validation de méthode et la non mise en service du nouveau matériel.

**5.5.2 QC à usage de surveillance des performances**
Dans le cas d’un contrôle QC non valide, l’incident est répertorié au sein du fichier
GDB_ENR_72_Gestion des incidents et des non conformités, le risque étant évalué à risque
moyen en raison de la remise en question des compétences de l’opérateur, une fiche de nonconformité ~~GDB~~ _ ~~FORM~~ _ ~~01~~ _ ~~Fiche~~ ~~de~~ ~~non~~ - ~~conformité~~ est alors ouverte.
Un rappel de la présente procédure sera fait à l’opérateur en charge du run de génotypage
correspondant.
A l’issue de la revue du document, l’opérateur devra procéder à un nouveau run de
génotypage incluant un contrôle QC dès que possible.
Dans le cas où celui-ci serait de nouveau non valide, son habilitation à génotyper sera
temporairement suspendue, le temps de procéder à un run de génotypage sous la supervision
d’un opérateur habilité au génotypage, puis, après validation de celui-ci, à un nouveau run de
génotypage en autonomie incluant un contrôle QC qui permettra de rétablir son habilitation le
cas échéant.

Si malgré ces étapes, ce dernier contrôle QC n’est toujours pas valide, l’opérateur perdra son
habilitation et devra repasser par une phase de formation initiale au génotypage.

**6.** **DOCUMENTS ASSOCIÉS**

~~GDB~~ _ ~~PRO~~ _ ~~08~~ _ ~~Gestion~~ ~~des~~ ~~incidents~~ ~~et~~ ~~non~~ ~~conformi~~ t ~~és~~
GDB_ENR_72_Gestion des incidents et des non conformités

1 L’interface DashBoard génomique (soumise à restriction d’utilisation : login/mdp) est disponible sur
le lien suivant : [http://dashboardgenoprod.gspp2gdlab.genesdiffusion.com](http://dashboardgenoprod.gspp2gdlab.genesdiffusion.com/)

5/6

|Col1|Contrôle de répétabilité et de<br>reproductibilité :<br>méthode de génotypage haut-débit par<br>puces à ADN|Version 2.1|
|---|---|---|
|GDB_PRO_05|SMQ|16/12/2024|
|Rédaction :<br>L. LIETAR|Vérification :<br>C. AUDEBERT|Approbation :<br>L. LIETAR|


~~GDB~~ _ ~~FORM~~ _ ~~01~~ _ ~~Fiche~~ ~~de~~ ~~non~~ ~~conformité~~
GDB_FI_15_SNP ISO 580


6/6

