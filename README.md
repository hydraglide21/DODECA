# DODECA — Démonstration énergétique de μ = 0

## Objet du dépôt

Ce dépôt rassemble les éléments mathématiques et informatiques du programme DODECA consacré à l'étude énergétique d'une structure géométrique tridimensionnelle construite à partir de cinq cubes couplés.

Le modèle étudié comporte notamment :
- une géométrie de dodécaèdre rhombique ;
- 20 sommets et 60 barres dans la description géométrique considérée ;
- 60 degrés de liberté dans le modèle mécanique suivi ;
- une formulation énergétique faisant intervenir des formes quadratiques et des matrices symétriques.

## Résultat central publié

La conclusion consignée dans la sauvegarde DODECA du 21 novembre 2026 est :

\[
\boxed{\mu=0}
\]

La démonstration rapportée repose sur l'existence d'un état admissible non nul appartenant à l'intersection :

\[
\ker(A)\cap S_\mu.
\]

Cet état possède une énergie quadratique nulle. Sous les conditions de positivité et de non-annulation du dénominateur énergétique, il permet d'obtenir la valeur minimale annoncée.

## Organisation du dépôt

- `docs/` : démonstration, état des preuves et chronologie.
- `certificates/` : certificats mathématiques primaires.
- `sources/` : scripts sources authentifiés.
- `reports/` : rapports d'audit et d'exécution.
- `manifests/` : empreintes et inventaires des fichiers.

## Principe de traçabilité

Les versions historiques ne sont pas écrasées. Chaque fichier publié doit être identifié par son nom, sa version et son empreinte SHA-256 lorsque celle-ci est disponible.

Le dépôt distingue :
1. un résultat mathématique consigné ;
2. un certificat exact fourni ;
3. un contrôle statique du code ;
4. une exécution effective ;
5. une reproduction indépendante.

Ces statuts ne sont pas interchangeables.

## État documentaire initial

La sauvegarde `SAUVEGARDE_DODECA_MU_V2.py` consigne le raisonnement aboutissant à μ = 0. Elle constitue une photographie de l'état du travail, et non un remplacement des certificats primaires.

Les certificats exacts relatifs au spectre, aux positivités, au noyau admissible et à l'admissibilité de l'état doivent être joints pour rendre la démonstration entièrement vérifiable à partir du dépôt seul.

Aucun script n'est réputé exécuté du seul fait de sa présence dans ce dépôt.

## Historique

Les versions et branches sont conservées séparément. Les branches R4 et les versions historiques antérieures ne doivent pas être fusionnées sans justification explicite.

## Statut

Dépôt de préparation documentaire. La complétude de la preuve indépendante dépend de la présence effective des certificats primaires mentionnés dans `certificates/`.
