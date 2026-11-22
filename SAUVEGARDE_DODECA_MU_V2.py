#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DODECA — SAUVEGARDE DU POINT DE REPRISE μ = 0
Version 2.0 — photographie non destructive et horodatée.

À lancer depuis le dossier du projet DODECA.
Le script :
- crée un nouveau dossier de sauvegarde horodaté (sans écraser les précédents) ;
- copie les sources et données listées lorsqu'elles sont présentes ;
- calcule SHA-256 sur les copies réellement effectuées ;
- enregistre un état scientifique de reprise en Markdown et JSON ;
- distingue les résultats rapportés/établis dans le dossier des vérifications
  effectivement reproduites lors de cette exécution.

Aucun fichier source original n'est modifié.
Les fichiers non trouvés sont marqués ABSENT_NON_CAPTURE.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

VERSION = "2.0"

# Ajouter ici d'autres fichiers du projet si nécessaire.
PROJECT_FILES = [
    "DODECA_BORNE_ENERGETIQUE_EXACTE_V3_3_7_PARTIE_A.py",
    "DODECA_BORNE_ENERGETIQUE_EXACTE_V3_3_12_PARTIE_B1.py",
    "DODECA_BORNE_ENERGETIQUE_EXACTE_V3_3_12_PARTIE_B2.py",
    "DODECA_CLOTURE_ENERGETIQUE_V1_0.py",
    "DODECA_CLOTURE_ENERGETIQUE_V1_0.json",
    "DODECA_CLOTURE_ENERGETIQUE_V1_0_CERTIFICAT.txt",
    "SOMMETS_DODECAEDRE.csv",
    "CUBES_5.csv",
    "PERSISTANCE_MODALE_V1/ROTATIONS_EXACTES.json",
    "PERSISTANCE_MODALE_V1/R_K0.npz",
]

STATE = {
    "project": "DODECA — borne énergétique et détermination exacte de μ",
    "snapshot_date": "2026-11-21",
    "definition": "mu = inf_{x in S_mu, H(x)>0} E1(x)/H(x)",
    "final_conclusion": {
        "value": "mu = 0",
        "logical_basis": [
            "A = D + (1/5) B",
            "Spec(D,B) reported/established in the project: {-1/5 (multiplicity 4), 3/10, 4/5}",
            "Consequent generalized spectrum (A,B): {0 (multiplicity 4), 1/2, 1}",
            "B is positive definite on the considered quotient/domain",
            "A is positive semidefinite on the admissible domain",
            "The nonzero nullspace of A intersects S_mu: N=ker(A), N ∩ S_mu contains an admissible nonzero state",
            "For that state x0: A(x0)=0 and B(x0)=H(x0)>0, hence E1(x0)/H(x0)=0",
            "The lower bound E1/H >= 0 and the admissible zero-ratio state imply mu=0",
        ],
        "status": (
            "CONCLUSION DE REPRISE — l'utilisateur confirme que le calcul spectral, "
            "la positivité et l'admissibilité du noyau dans S_mu ont déjà été démontrés. "
            "Ce script archive cette conclusion mais ne réexécute pas les preuves."
        ),
    },
    "spectral_data": {
        "D": "D = A - (1/5) B",
        "A": "A = D + (1/5) B",
        "spectrum_D_B": ["-1/5 (multiplicity 4)", "3/10", "4/5"],
        "spectrum_A_B": ["0 (multiplicity 4)", "1/2", "1"],
        "nullity_A": 4,
        "kernel_condition": "N = ker(A), with N ∩ S_mu containing a nonzero admissible state",
        "status": "RESULTAT DU DOSSIER — non recalculé par ce script",
    },
    "dynamic_certificate": {
        "normalization": "q(t) = w(t)/sqrt(3), not w(t)/3",
        "omega2_squared": "2 - sqrt(6)/2",
        "omega5_squared": "2 + sqrt(6)/2",
        "third_frequency": "2",
        "t0": "42943/1000 = 42.943",
        "H_t0": "12",
        "F_definition": "F(t) = E1(t) - H(t)/5",
        "F_t0_approx": "-2.3912320227626034085196249205899702808821182553855",
        "E1_t0_approx": "0.0087679772373966",
        "ratio_t0_approx": "0.00073066476978304929",
        "meaning": (
            "Certificat dynamique antérieur : donne un état de quotient inférieur à 1/5. "
            "Il constitue un résultat distinct de la fermeture exacte mu=0 par le noyau admissible."
        ),
        "status": "CERTIFICAT RAPPORTÉ DANS LE DOSSIER — non réexécuté par ce script",
    },
    "modal_raccord": {
        "version": "Raccord modal V1.3",
        "identities": [
            "A_q, A_v, B_q, B_v et D_q, D_v identiques coefficient par coefficient entre les deux constructions, selon le rapport du projet",
            "q = w/sqrt(3)",
            "F = c^T D_q c + c'^T D_v c'",
            "F = E1 - H/5",
        ],
        "status": "RÉSULTAT RAPPORTÉ/ÉTABLI DANS LE DOSSIER — non recalculé par ce script",
    },
    "important_distinctions": [
        "La conclusion μ=0 repose sur l'admissibilité dans S_mu d'un état non nul du noyau de A, et pas seulement sur le spectre du quotient abstrait.",
        "Ne pas réduire la conclusion à la seule borne dynamique E1/H ≈ 0.00073066477.",
        "Ne pas confondre F(t0) ≈ -2.391232 avec une autre quantité G parfois rapportée.",
        "Conserver la normalisation q=w/sqrt(3).",
        "Ne pas prétendre que ce script a exécuté ou vérifié les démonstrations mathématiques.",
    ],
    "provenance": {
        "A_V3_3_7_reported_size": 42090,
        "A_V3_3_7_reported_sha256": "2da8e5140dafecd96ffab68c723abdf2d0d9a2b95352ccc113458276ee1f7fdb",
        "CLOTURE_V1_0_reported_sha256_prefix": "aea7df8479bbcb9c",
        "CLOTURE_V1_0_reported_sha256_suffix": "dd7289b0",
        "note": "Empreintes historiques rapportées ; le présent script recalcule les empreintes uniquement des fichiers effectivement copiés.",
    },
    "next_steps": [
        "Conserver cette photographie avec les versions sources et leurs rapports.",
        "Si les sources sont présentes, vérifier que leurs empreintes correspondent aux empreintes historiques consignées.",
        "Produire, dans une étape séparée, un certificat autonome lisible de la positivité de B, de A >= 0 et de l'intersection ker(A) ∩ S_mu.",
        "Ne pas rouvrir les étapes déjà établies sans raison mathématique précise.",
    ],
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def unique_snapshot_dir(parent: Path, timestamp: str) -> Path:
    candidate = parent / f"PHOTO_MU_{timestamp}"
    index = 1
    while candidate.exists():
        candidate = parent / f"PHOTO_MU_{timestamp}_{index:02d}"
        index += 1
    return candidate


def main() -> int:
    root = Path.cwd().resolve()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_root = root / "SAUVEGARDES_DODECA_MU"
    backup_root.mkdir(parents=True, exist_ok=True)
    output = unique_snapshot_dir(backup_root, timestamp)
    output.mkdir(parents=False, exist_ok=False)

    captured = []
    missing = []

    for relative_name in PROJECT_FILES:
        source = root / relative_name
        if source.is_file():
            destination = output / "sources" / relative_name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            captured.append({
                "source": relative_name,
                "backup_relative_path": str(destination.relative_to(output)),
                "size_bytes": destination.stat().st_size,
                "sha256": sha256(destination),
                "status": "COPIED_AND_HASHED",
            })
        else:
            missing.append({
                "source": relative_name,
                "status": "ABSENT_NON_CAPTURE",
            })

    manifest = {
        "backup_name": "DODECA_PHOTOGRAPHIE_MU",
        "script_version": VERSION,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "project_root": str(root),
        "backup_directory": str(output),
        "non_destructive": True,
        "captured_files": captured,
        "missing_files": missing,
        "scientific_checkpoint": STATE,
        "execution_scope": (
            "Copie de fichiers et calcul SHA-256 uniquement. "
            "Aucune preuve mathématique n'est recalculée ici."
        ),
    }

    (output / "MANIFESTE_MU.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# DODECA — Photographie de reprise : μ = 0",
        "",
        f"- Version du script : {VERSION}",
        f"- Date UTC : {manifest['created_utc']}",
        f"- Dossier source : `{root}`",
        "- Sauvegarde non destructive ; aucune source originale modifiée.",
        "- Chaque exécution crée un nouveau dossier, sans écraser les précédents.",
        "",
        "## Conclusion mathématique conservée",
        "",
        r"$$\boxed{\mu=0}$$",
        "",
        "Cette conclusion repose sur les résultats déjà établis/confirmés dans le dossier :",
        "",
        "1. `A = D + (1/5) B`.",
        "2. Spectre généralisé rapporté de `(D,B)` : `{-1/5 (×4), 3/10, 4/5}`.",
        "3. Spectre correspondant de `(A,B)` : `{0 (×4), 1/2, 1}`.",
        "4. `B` est définie positive sur le domaine considéré.",
        "5. `A` est positive ou nulle sur le domaine admissible.",
        "6. Le noyau `N=ker(A)` rencontre `S_mu` en un état admissible non nul.",
        "7. Cet état a `E1/H=0`, tandis que la positivité donne `E1/H>=0`.",
        "",
        "Donc `mu>=0` et `mu<=0`, d'où `mu=0`.",
        "",
        "## Certificat dynamique distinct",
        "",
        "- Normalisation : `q(t)=w(t)/sqrt(3)`.",
        "- `t0=42.943`, `H(t0)=12` (rapportés).",
        "- `F(t0)=E1(t0)-H(t0)/5 ≈ -2.3912320227626034`.",
        "- `E1(t0)/H(t0) ≈ 0.00073066476978304929`.",
        "- Ce certificat fournit un état sous `1/5`; il est distinct de la preuve `mu=0` par le noyau admissible.",
        "",
        "## Raccord modal V1.3",
        "",
        "Identités coefficient par coefficient de `A_q, A_v, B_q, B_v, D_q, D_v` rapportées dans le dossier. La normalisation `q=w/sqrt(3)` est conservée.",
        "",
        "## Fichiers copiés et empreintes recalculées",
        "",
    ]

    if captured:
        for item in captured:
            lines.append(
                f"- `{item['source']}` — {item['size_bytes']} octets — "
                f"SHA-256 `{item['sha256']}`."
            )
    else:
        lines.append("- Aucun fichier de la liste n'a été trouvé dans le dossier courant.")

    lines.extend(["", "## Fichiers non capturés", ""])
    if missing:
        lines.extend(f"- `{item['source']}` — ABSENT_NON_CAPTURE." for item in missing)
    else:
        lines.append("- Aucun.")

    lines.extend([
        "",
        "## Portée de cette sauvegarde",
        "",
        "Ce script copie les fichiers présents et archive le point de reprise. "
        "Il ne réexécute pas les preuves et ne transforme pas les résultats historiques "
        "en résultats recalculés. Les empreintes historiques consignées dans le manifeste "
        "sont distinctes des empreintes recalculées sur les copies.",
        "",
        "## Suite",
        "",
    ])
    lines.extend(f"{index}. {task}" for index, task in enumerate(STATE["next_steps"], 1))
    (output / "REPRISE_MU.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("SAUVEGARDE CRÉÉE")
    print(f"Dossier : {output}")
    print(f"Fichiers copiés : {len(captured)}")
    print(f"Fichiers non trouvés : {len(missing)}")
    print("Documents : MANIFESTE_MU.json, REPRISE_MU.md")
    print("Aucune source originale n'a été modifiée.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
