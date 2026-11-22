# Certificats mathématiques primaires

Ce répertoire doit contenir les pièces exactes permettant de vérifier indépendamment la démonstration de μ = 0.

## Répertoires attendus

### `certificat_spectral/`
- Matrices exactes A, B et D.
- Vérification de \(A=D+\frac15B\).
- Polynôme caractéristique généralisé ou réduction exacte équivalente.
- Multiplicités et bases des espaces propres.
- Vérification du spectre annoncé.

### `positivite_B/`
- Certificat exact de \(B\succ0\).
- Méthode utilisée : factorisation exacte, mineurs principaux ou autre certificat rigoureux.

### `positivite_A/`
- Certificat exact de \(A\succeq0\).
- Domaine sur lequel cette propriété est établie.
- Vérification des éventuelles conditions aux frontières.

### `noyau_admissible/`
- Vecteur exact non nul \(x_0\).
- Vérification exacte de \(Ax_0=0\).
- Définition de \(S_\mu\).
- Vérification de \(x_0\in S_\mu\).
- Vérification de \(x_0^TBx_0>0\).

### `certificat_dynamique/`
- Certificats du calcul dynamique historique, s'ils sont retenus.
- Paramètres, précision, intervalles et script de génération.
- Distinction explicite entre ce résultat dynamique et la preuve par noyau admissible.

## Règle

Ne placer dans ces répertoires que des pièces effectivement disponibles et identifiées. Un fichier de description ou un résumé ne remplace pas un certificat mathématique primaire.
