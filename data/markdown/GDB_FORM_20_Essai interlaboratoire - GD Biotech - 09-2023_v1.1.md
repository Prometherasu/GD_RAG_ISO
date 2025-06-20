|Col1|Essai interlaboratoire<br>Laboratoire - mm-aaaa|Version 1.1|
|---|---|---|
|GDB_FORM_20|SMQ|12/05/2023|
|Rédaction :<br>L. LIETAR|Vérification :<br>P. BOUVELLE, K. LE ROUX|Approbation :<br>C. AUDEBERT|


**Essai interlaboratoire – GD Biotech – 09-2023**

Préambule : conformément à la procédure GDB_PRO_16_Contrôle des performances du
génotypage réalisé par méthode des puces à ADN : essai interlaboratoire, deux fois par an
un essai interlaboratoire est prévu entre le laboratoire d’Agranis (Agreelia au 01/09/2023, 141
Bd des Loges, 53940 Saint-Berthevin) et GD Biotech (3595 Route de Tournai, 59501 Douai).

Ce test a été organisé sur la période du 26/09/2023 au 04/10/2023.
GD Biotech a procédé à l’envoi d’un panel de 12 échantillons à destination du laboratoire
d’Agreelia.

Avant toute chose, il est à signaler qu’une erreur de prélèvement a été faite, ce n’est pas
l’échantillon GD534921 qui a été envoyé dans le tube n°6 mais GD534920 (également
génotypé le 21/09/23, avec un callrate de 0,9995077 au lieu de 0,9993585 mentionné dans le
courrier accompagnant les échantillons).
La référence a été corrigée dans ce document ainsi que dans celui répertoriant les données
brutes (en rouge).

**1) Validité de niveau 1 (marqueur / marqueur)**

L’objectif de cette analyse consiste à identifier les marqueurs qui présenteraient des résultats
discordants entre les deux plateformes de génotypage haut-débit.

1/3

|Col1|Essai interlaboratoire<br>Laboratoire - mm-aaaa|Version 1.1|
|---|---|---|
|GDB_FORM_20|SMQ|12/05/2023|
|Rédaction :<br>L. LIETAR|Vérification :<br>P. BOUVELLE, K. LE ROUX|Approbation :<br>C. AUDEBERT|


En premier lieu, il apparaît que 3 marqueurs ne sont pas génotypés de la part du laboratoire
Agreelia, et 1 marqueur par le laboratoire GD Biotech, ces marqueurs sont considérés comme
manquants, ce qui induit une chute du CallRate et donc du taux de concordances entre les
résultats d’analyse des deux laboratoires (en effet un résultat manquant comparé à un résultat
présent est considéré de la même manière qu’une discordance de génotypage).

Marqueurs manquants :
AGREELIA

ARS-BFGL-NGS-112094

ARS-BFGL-NGS-117319

ARS-USMARC-Parent-DQ837643-rs29018818

GD Biotech

ARS-USMARC-Parent-AY863214-rs17871744

Outre ces marqueurs absents, deux autres renvoient à des discordances de génotypage
(résultat manquant chez Agreelia contre résultat présent chez GD Biotech) :

   - pour 3 échantillons sur les 12 testés (GD532965 inclus) : BTB-01285245

   - pour 4 échantillons sur les 12 testés : ARS-USMARC-Parent-AY851163-rs17871661
Le clustering de ces SNP est à optimiser.

Concernant l’échantillon GD532965 non conforme, le CallRate obtenu au laboratoire
d’Agreelia est de 0,95, et de 0,999463 au laboratoire de GD Biotech.
Au-delà des marqueurs manquants et discordances évoqués ci-dessus, on note :

   - 3 discordances -> résultats différents

   - 3 discordances -> résultat manquant chez Agreelia

2/3

|Col1|Essai interlaboratoire<br>Laboratoire - mm-aaaa|Version 1.1|
|---|---|---|
|GDB_FORM_20|SMQ|12/05/2023|
|Rédaction :<br>L. LIETAR|Vérification :<br>P. BOUVELLE, K. LE ROUX|Approbation :<br>C. AUDEBERT|


Ce dernier point permet d’observer que 91,7 % des échantillons génotypés bénéficient de
résultats concordants et valides au-dessus du seuil de 95 % de concordance et de CallRate

individuel.

**2) Validité de niveau 2 (synthèse)**

Le taux de concordance moyen est de 97,46 % entendu qu’un échantillon présente un taux
de concordance inférieur à 95 %. Le résultat retenu est un échec de l’essai interlaboratoire.

L’analyse des résultats met en évidence un effet important des 4 marqueurs manquants entre
les deux plateformes (2% de discordance) mais qui n’impacte à ce jour pas la qualité du
génotypage réalisé.









|Laboratoire<br>organisateur<br>de l'essai|Date de<br>l'essai|VALIDITE<br>niveau 1<br>(nombre<br>d'échantillons<br>/12)|Résultat<br>attendu|VALIDITE<br>niveau 2<br>(%<br>concordance)|Résultat<br>attendu|Résultat<br>retenu|
|---|---|---|---|---|---|---|
|GD Biotech|26/09/2023|11|> 95 % de<br>résultats<br>concordant entre<br>les deux<br>laboratoires pour<br>chacun des<br>échantillons|97,46|> 95 % de<br>résultats<br>concordant<br>entre les deux<br>laboratoires<br>pour l'ensemble<br>des échantillons|ECHEC|


**Note :** nous recommandons au laboratoire d’Agreelia de génotyper à nouveau l’échantillon
GD532965 afin d’expertiser l’échec de génotypage.
(Un retour du laboratoire d’Agreelia en date du 17/11/2023 confirme le succès du
regénotypage de l’échantillon GD532965 avec une concordance à 98 %, dont les résultats
bruts ont été ajoutés au fichier de données brutes GDB_FORM_19_Résultats bruts essai
interlaboratoire - GD Biotech - 09-2023_v1.1)

Signature Agreelia Signature GDBiotech,
Florent Perrin, Responsable Technique Génomique et Santé Animale Christophe Audebert, directeur R&D

23/01/2024

31/01/2024

3/3

