# DODECA — DOSSIER DE PUBLICATION DE LA DÉMONSTRATION μ = 0

**Date de consolidation :** 22 novembre 2026  
**Projet :** DODECA — borne énergétique  
**Conclusion mathématique conservée :**

\[
\boxed{\mu=0}
\]

**Nature du document :** dossier de synthèse et de traçabilité destiné à préparer une vérification indépendante.

---

## 1. Objet et conclusion

Le présent dossier rassemble les éléments retrouvés dans les sauvegardes, rapports d'audit et sources du projet DODECA concernant la détermination de la borne énergétique :

\[
\mu=\inf_{\substack{x\in S_\mu\\H(x)>0}}\frac{E_1(x)}{H(x)}.
\]

La conclusion conservée dans le dossier de travail est :

\[
\boxed{\mu=0}.
\]

Cette conclusion repose sur deux éléments mathématiques complémentaires :

1. La non-négativité du quotient énergétique sur le domaine admissible.
2. L'existence d'un état admissible non nul pour lequel le quotient atteint zéro.

La sauvegarde `SAUVEGARDE_DODECA_MU_V2.py` et l'audit `AUDIT_CLOTURE_DODECA_2026-11-21.md` consignent explicitement cette conclusion.

Le présent document ne prétend pas recalculer les preuves. Il organise les résultats et les pièces retrouvées afin de faciliter leur contrôle indépendant.

## 2. Structure algébrique de la démonstration

L'identité centrale consignée est :

\[
A=D+\frac15B.
\]

Le spectre généralisé rapporté de la paire \((D,B)\) est :

\[
\operatorname{Spec}(D,B)
=
\left\{
-\frac15\ (4),\quad
\frac3{10},\quad
\frac45
\right\}.
\]

Le spectre correspondant rapporté de \((A,B)\) est :

\[
\operatorname{Spec}(A,B)
=
\left\{
0\ (4),\quad
\frac12,\quad
1
\right\}.
\]

Le dossier consigne également :

- \(B\succ0\) sur le domaine ou quotient considéré ;
- \(A\succeq0\) sur le domaine admissible ;
- \(\dim\ker(A)=4\) dans la représentation considérée ;
- l'existence d'un état admissible non nul dans \(\ker(A)\cap S_\mu\).

Ces données spectrales et ces propriétés sont des résultats conservés dans les documents du projet. Leur reproduction indépendante exige les matrices exactes, les conventions de représentation et les certificats primaires.

## 3. Déduction de μ = 0

Soit \(x_0\) un état non nul tel que :

\[
x_0\in\ker(A)\cap S_\mu.
\]

Alors :

\[
Ax_0=0
\]

et, par conséquent,

\[
x_0^TAx_0=0.
\]

Si les formes énergétiques sont raccordées par :

\[
x^TAx=E_1(x),
\qquad
x^TBx=H(x),
\]

alors :

\[
E_1(x_0)=0.
\]

Comme \(B\succ0\) et \(x_0\neq0\), on a :

\[
H(x_0)=x_0^TBx_0>0.
\]

Le quotient atteint donc zéro :

\[
\frac{E_1(x_0)}{H(x_0)}=0.
\]

D'autre part, la positivité de \(A\) sur le domaine admissible donne :

\[
E_1(x)\geq0
\]

pour tout état admissible considéré, avec \(H(x)>0\). Ainsi :

\[
\frac{E_1(x)}{H(x)}\geq0.
\]

Les deux inégalités donnent :

\[
\mu\leq0
\qquad\text{et}\qquad
\mu\geq0.
\]

D'où :

\[
\boxed{\mu=0}.
\]

**Condition de validité essentielle :** le vecteur \(x_0\) doit appartenir effectivement au domaine \(S_\mu\) utilisé dans la définition de l'infimum. L'existence d'un noyau abstrait de dimension quatre ne suffit pas, à elle seule, à établir cette intersection.

## 4. Pièces effectivement retrouvées

### 4.1 Sauvegardes et rapports principaux

| Pièce | Apport au dossier |
|---|---|
| `SAUVEGARDE_DODECA_MU_V2.py` | Photographie de la conclusion μ = 0, des données spectrales et de la chaîne logique |
| `SAUVEGARDE_DODECA_MU_V1.py` | Sauvegarde historique antérieure |
| `AUDIT_CLOTURE_DODECA_2026-11-21.md` | Synthèse de clôture et raccord des sources |
| `CLOTURE_CHANTIER_V3_3_12_2026-11-19.md` | État initial de clôture logicielle |
| `CLOTURE_CHANTIER_V3_3_12_2026-11-19_V2.md` | Rectification et contre-expertise |
| `CLOTURE_CHANTIER_V3_3_12_2026-11-19.json` | Données structurées de clôture |
| `ADDENDUM_AUDIT_DODECA_2026-11-21.md` | Audit des tests négatifs B1 |
| `ADDENDUM_CORRECTIF_B2_V3_3_19_2026-11-21.md` | Historique du correctif B2 candidat |

### 4.2 Sources logicielles retrouvées

Les versions suivantes ont été retrouvées dans les archives :

- B1 V3.3.19 ;
- B2 V3.3.18 ;
- B2 V3.3.17 ;
- B2 V3.3.13 ;
- plusieurs versions intermédiaires de B2 ;
- B1 V3.3.20 R4 et B2 V3.3.19 R4 dans la branche déposée sur GitHub.

La paire B1 V3.3.19 / B2 V3.3.18 a fait l'objet d'un raccord statique documenté dans l'audit du 21 novembre.

La paire R4 est une branche corrective ultérieure. Les deux branches doivent rester distinctes dans l'historique du dépôt.

### 4.3 Pièces relatives aux vecteurs invisibles

Les fichiers suivants ont également été retrouvés :

- `VECTEURS_INVISIBLES_EXACTS_V1.py`
- `RAPPORT_VECTEURS_INVISIBLES_V1.txt`

Ils documentent des calculs exacts et numériques relatifs à l'observabilité centrale dans les secteurs \(E_g\) et \(T_{2g}\).

**Attention :** ces fichiers concernent les modes invisibles et l'observabilité. Ils ne constituent pas, en l'état des pièces lues, le certificat de l'état \(x_0\in\ker(A)\cap S_\mu\) utilisé dans la démonstration de μ = 0.

## 5. Certificat dynamique distinct

La sauvegarde V2 conserve également un résultat dynamique antérieur :

\[
t_0=42.943,
\qquad H(t_0)=12.
\]

Avec :

\[
F(t)=E_1(t)-\frac15H(t),
\]

la valeur rapportée est :

\[
F(t_0)\approx-2.3912320227626034.
\]

Et :

\[
\frac{E_1(t_0)}{H(t_0)}
\approx0.00073066476978304929.
\]

La normalisation consignée est :

\[
q(t)=\frac{w(t)}{\sqrt3}.
\]

Ce résultat fournit un quotient inférieur à \(1/5\). Il est distinct de la démonstration de μ = 0 par l'intersection du noyau avec le domaine admissible.

Il ne doit donc pas être présenté comme le certificat du vecteur \(x_0\).

## 6. Pièces primaires à joindre pour une publication autonome

Les pièces suivantes doivent être reliées à leurs sources exactes et conservées sous leur forme vérifiable.

| Référence | Contenu nécessaire |
|---|---|
| C01 | Définition exacte de \(S_\mu\) et de ses contraintes |
| C02 | Construction exacte des matrices \(A\), \(B\), \(D\) et identité \(A=D+\frac15B\) |
| C03 | Certificat spectral exact de \((D,B)\), avec multiplicités |
| C04 | Preuve exacte de \(B\succ0\) |
| C05 | Preuve exacte de \(A\succeq0\) sur le domaine admissible |
| C06 | Base exacte de \(\ker(A)\) et construction de l'état \(x_0\) |
| C07 | Vérification de \(x_0\in S_\mu\), \(x_0\neq0\) et \(x_0^TBx_0>0\) |
| C08 | Raccord exact entre les formes matricielles et les énergies \(E_1\), \(H\) |

Ces références sont un inventaire de publication. Elles ne prétendent pas que les huit certificats sont déjà présents sous forme de fichiers autonomes.

## 7. Éléments encore à récupérer ou à raccorder

Les recherches dans la bibliothèque ont permis de retrouver les rapports de clôture et plusieurs sources logicielles.

En revanche, les éléments suivants ne sont pas encore disponibles sous forme de pièces autonomes intégrales dans l'inventaire consulté :

1. Le fichier A V3.3.7 complet comme objet unique, même si sa transmission historique en plusieurs parties est consignée.
2. Le certificat `DODECA_CLOTURE_ENERGETIQUE_V1_0_CERTIFICAT.txt`, cité dans la liste des fichiers attendus par la sauvegarde V2.
3. La construction explicite et vérifiable du vecteur \(x_0\) dans \(\ker(A)\cap S_\mu\).
4. Les données primaires et les matrices exactes permettant à un tiers de reproduire intégralement les certificats spectraux et de positivité.

L'absence actuelle d'un fichier dans l'inventaire consulté ne signifie pas qu'il n'a jamais existé ou qu'il n'a pas été produit antérieurement.

## 8. Historique logiciel et précautions

La branche V3.3.12 a été examinée statiquement et déclarée non validée. Elle ne doit pas être présentée comme une exécution réussie.

L'audit du 21 novembre distingue notamment :

- les résultats mathématiques conservés dans le dossier ;
- les contrôles statiques de sources ;
- les contrôles syntaxiques ;
- les tests isolés de certains validateurs ;
- les exécutions complètes, qui ne sont pas revendiquées dans les audits consultés.

La paire B1 V3.3.19 / B2 V3.3.18 a été raccordée statiquement. La branche R4 a ensuite fait l'objet de corrections ciblées et de vérifications isolées rapportées. Cela ne constitue pas une validation dynamique complète de la chaîne A + B1 + B2.

Aucun statut de test non exécuté ne doit être présenté comme réussi.

## 9. Statut scientifique et documentaire

| Élément | Statut de publication |
|---|---|
| Conclusion \(\mu=0\) | Résultat établi et conservé dans le dossier du projet |
| Identité \(A=D+\frac15B\) | Rapportée dans les pièces retrouvées |
| Spectres généralisés | Rapportés dans les pièces retrouvées |
| Positivité de \(B\) | Rapportée ; certificat primaire à joindre |
| Positivité de \(A\) sur le domaine | Rapportée ; certificat primaire à joindre |
| Intersection \(\ker(A)\cap S_\mu\) | Rapportée ; construction explicite à joindre |
| Certificat dynamique à \(t_0=42.943\) | Résultat antérieur rapporté, distinct de la preuve par noyau |
| Validation complète des scripts | Non revendiquée |

La conclusion mathématique et l'état de vérification documentaire sont deux questions distinctes. Le présent dossier préserve la conclusion sans transformer les rapports de reprise en certificats indépendants.

## 10. Règle de conservation

- Ne jamais écraser les versions historiques.
- Conserver séparément les branches logicielles.
- Associer chaque certificat à son fichier source et à son empreinte SHA-256.
- Distinguer les empreintes rapportées des empreintes recalculées.
- Conserver les rapports d'audit même lorsqu'une version ultérieure corrige un défaut.
- Ne jamais remplacer une preuve exacte par une simple valeur numérique ou un rapport d'exécution.

---

**Fin du dossier de publication DODECA — démonstration μ = 0.**
