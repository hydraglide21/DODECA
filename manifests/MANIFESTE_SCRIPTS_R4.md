# MANIFESTE DES SCRIPTS DODECA — R4

**Date de constitution :** 22 novembre 2026  
**Dépôt :** `hydraglide21/DODECA`  
**Statut :** inventaire initial des scripts déposés

## 1. Objet

Ce manifeste identifie les trois scripts Python déposés dans le dépôt DODECA.

Il conserve leur rôle, leur version et les empreintes SHA-256 historiquement rapportées. Il distingue ces empreintes des empreintes recalculées directement à partir des fichiers présents sur GitHub.

## 2. Inventaire

| Fichier | Rôle | Statut |
|---|---|---|
| `SAUVEGARDE_DODECA_MU_V2.py` | Photographie de sauvegarde du projet et de l'état de la démonstration μ = 0 | Déposé |
| `DODECA_BORNE_ENERGETIQUE_EXACTE_V3_3_20_PARTIE_B1.py` | Branche B1 — R4 | Déposé |
| `DODECA_BORNE_ENERGETIQUE_EXACTE_V3_3_19_PARTIE_B2.py` | Branche B2 — R4, dépend de B1 V3.3.20 R4 | Déposé |

## 3. Empreintes SHA-256 historiques rapportées

Les empreintes suivantes ont été consignées antérieurement dans le suivi du projet.

| Fichier | SHA-256 rapporté |
|---|---|
| B1 V3.3.20 R4 | `8d38cfbbbceab786b7f7d5849b7f4ef60bc7882ce1f2f013e33eeffb863f7829` |
| B2 V3.3.19 R4 | `2ff522cdbb02b64cfc7172d3d8485e4bd52d5a80a408b90628cd816da3ca58e3` |

L'empreinte SHA-256 de `SAUVEGARDE_DODECA_MU_V2.py` reste à renseigner.

**Important :** ces valeurs sont des empreintes historiques rapportées. Elles ne constituent pas encore une vérification indépendante des fichiers actuellement hébergés sur GitHub.

## 4. Relations entre les scripts

- La sauvegarde V2 conserve une photographie de l'état du projet et des résultats rapportés.
- B1 V3.3.20 R4 constitue la branche B1 de référence.
- B2 V3.3.19 R4 constitue la branche B2 associée et dépend de B1 V3.3.20 R4.

Les versions historiques antérieures ne sont pas remplacées par cette branche R4.

## 5. Réserves de vérification

À effectuer ultérieurement :

1. Recalculer les trois empreintes SHA-256 à partir des fichiers récupérés depuis GitHub.
2. Comparer les empreintes recalculées aux empreintes historiques disponibles.
3. Conserver les résultats dans un rapport de vérification distinct.
4. Vérifier les certificats mathématiques primaires associés à la démonstration μ = 0.

Le dépôt des scripts ne vaut pas, à lui seul, certification de leur exécution complète ni validation indépendante de tous les résultats mathématiques.

## 6. Règle de conservation

Aucune version antérieure ne doit être écrasée.

Toute correction ou évolution doit être déposée sous un nouveau nom de version, avec son propre rapport et sa propre empreinte.

---

**Fin du manifeste initial R4.**
