# Synthèse d'activité : demarche-numerique (du 15/08 au 21/08/2026)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur l'amélioration de la précision de l'extraction de données et la flexibilité des infrastructures. [la_taupe](/repos/demarche-numerique/la_taupe) renforce ses capacités d'analyse automatique de documents grâce à un nouveau moteur d'OCR et l'introduction du traitement par lots, rendant l'extraction d'informations bancaires plus robuste. 

Parallèlement, [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) enrichit l'expérience utilisateur avec des outils de recherche avancés et des exports PDF améliorés, tandis que [ds_proxy](/repos/demarche-numerique/ds_proxy) gagne en polyvalence en intégrant le support de nouveaux systèmes de stockage comme S3 et Swift.

## Sécurité
- Renforcement de la sécurité sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) via la protection contre les attaques par *path traversal* et la sécurisation du traitement d'images avec `libvips`.

## Autres changements notables
- **Optimisation de l'OCR et de la performance :** Migration vers un nouveau moteur d'OCR (PP-OCR v6) et mise en place d'outils de benchmarking pour mesurer la précision et la latence sur [la_taupe](/repos/demarche-numerique/la_taupe).
- **Évolutions d'infrastructure et de stockage :** Extension du support des protocoles S3 et Swift et simplification des dépendances pour [ds_proxy](/repos/demarche-numerique/ds_proxy).
- **Refonte technique et recherche :** Optimisation des performances de recherche (via `tsvectors` et GraphQL) et refonte de l'architecture des champs sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration majeure de l'OCR et ajout du traitement par lots via CLI.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Extension du support de stockage et optimisation de la configuration.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Évolutions de l'interface utilisateur, de la recherche et renforcement de la sécurité.
