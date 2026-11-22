# ADDENDUM — RÉCUPÉRATION DU CERTIFICAT DYNAMIQUE V1.0

**Projet :** DODECA  
**Date de consolidation :** 22 novembre 2026

## 1. Identification

Le chantier du 19 novembre 2026 fait référence aux fichiers suivants :

- `DODECA_CLOTURE_ENERGETIQUE_V1_0.py`
- `DODECA_CLOTURE_ENERGETIQUE_V1_0.json`
- `DODECA_CLOTURE_ENERGETIQUE_V1_0_CERTIFICAT.txt`

Ces fichiers sont référencés dans la sauvegarde `SAUVEGARDE_DODECA_MU_V2.py`.

Le script possède une empreinte SHA-256 historique dont le préfixe est `aea7df8479bbcb9c` et le suffixe `dd7289b0`. L'empreinte complète n'a pas été recalculée à partir du fichier source dans la présente consolidation.

Les références aux rapports JSON et aux journaux sont également conservées dans l'historique du chantier.

## 2. Résultat dynamique conservé

Le certificat porte sur :

\[
F(t)=E_1(t)-\frac15H(t).
\]

Au temps rationnel :

\[
t_0=\frac{42943}{1000}=42.943,
\]

les valeurs rapportées sont :

\[
H(t_0)=12,
\]

\[
F(t_0)\approx
-2.3912320227626034085196249205899702808821182553855,
\]

\[
E_1(t_0)\approx0.0087679772373966,
\]

\[
\frac{E_1(t_0)}{H(t_0)}
\approx0.00073066476978304929.
\]

Des intervalles certifiés à 50, 80 et 120 chiffres ont été annoncés dans le dossier historique.

La normalisation utilisée est :

\[
q(t)=\frac{w(t)}{\sqrt3}.
\]

Ce résultat donne un état dynamique pour lequel :

\[
\frac{E_1(t_0)}{H(t_0)}<\frac15.
\]

## 3. Portée mathématique

Ce certificat dynamique constitue un résultat distinct de la démonstration de :

\[
\mu=0.
\]

Il établit un quotient inférieur à \(1/5\) pour l'état considéré, sous réserve de son appartenance au domaine de la définition de \(\mu\).

Il ne démontre pas à lui seul l'existence d'un état admissible dans :

\[
\ker(A)\cap S_\mu.
\]

La preuve de \(\mu=0\) par le noyau exige toujours le raccord exact entre le domaine \(S_\mu\), les matrices énergétiques et le vecteur du noyau.

## 4. Suite V1.3 et réserves

La reprise V1.3 a consigné les éléments suivants :

- certificat dynamique V1.0 raccordé et réutilisable ;
- espace \(S_\mu\) non retrouvé dans les 84 fichiers examinés ;
- fichier de matrices utilisant une quantité \(G(t_0)\) jugée bugguée et invalide pour certifier \(F(t_0)\) ;
- borne \(\mu\geq1/5\) toujours ouverte.

Il faut donc conserver séparément le résultat dynamique et la preuve par noyau.

## 5. État de récupération

Les noms de fichiers, résultats, empreintes partielles et références historiques sont retrouvés.

Les trois fichiers sources V1.0 ne sont pas encore récupérés sous forme d'objets complets vérifiables dans la bibliothèque consultée.

Aucune reconstruction de leur contenu ne doit être présentée comme le fichier original.

**Décision : conserver le certificat V1.0 comme résultat historique rapporté, en attente de récupération de ses fichiers primaires.**
