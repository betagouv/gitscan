# Synthèse d'activité : demarche-numerique (du 24/10 au 31/10)

## Résumé de l'activité
L'activité de cette période est marquée par une amélioration significative des capacités d'extraction de données et des outils d'instruction. [la_taupe](/repos/demarche-numerique/la_taupe) franchit un cap technique avec l'intégration d'un nouveau moteur OCR plus performant pour l'analyse des RIB et l'ajout du traitement par lots. Parallèlement, [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) enrichit son offre fonctionnelle pour les instructeurs (pré-remplissage, traçabilité) et renforce la résilience de ses services.

L'écosystème se structure également avec le lancement de nouveaux espaces de collaboration via [commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr) et [commun-demarche-numerique](/repos/demarche-numerique/commun-demarche-numerique), tandis que [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr) entame une refonte majeure de sa documentation pour mieux accompagner les usagers et les instructeurs.

## Sécurité
- Renforcement de la sécurité des jetons API grâce à l'adoption du hachage SHA-256 dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Optimisations techniques et résilience :**
    - Mise en place d'un mécanisme de "parking" des tâches pour gérer les pannes de services tiers dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
    - Migration vers Ruby 4.0.9 et refactorisation de l'authentification ProConnect dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
    - Passage au moteur OCR PP-OCR v6 tiny pour une meilleure efficacité d'extraction dans [la_taupe](/repos/demarche-numerique/la_taupe).
    - Extension des capacités de stockage avec la prise en charge de S3 et Swift dans [ds_proxy](/repos/demarche-numerique/ds_proxy).
    - Mise à jour du système de routage pour [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr).
- **Maintenance et infrastructure :**
    - Simplification et allègement des dépendances AWS dans [ds_proxy](/repos/demarche-numerique/ds_proxy).
    - Intégration de l'outil Clippy pour garantir la qualité du code Rust dans [la_taupe](/repos/demarche-numerique/la_taupe).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration de la précision de l'OCR et ajout du traitement par lots (batch).
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Évolutions majeures des outils d'instruction et renforcement de la résilience système.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Ajout du support pour les stockages S3/Swift et optimisation des dépendances.
- [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr) : Structuration de la documentation et lancement du guide usager.
