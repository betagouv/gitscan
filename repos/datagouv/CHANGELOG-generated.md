# Synthèse d'activité : datagouv (derniers 7 jours)

## Résumé de l'activité
L'organisation datagouv a connu une semaine riche en activités, avec des améliorations significatives apportées à plusieurs de ses outils et pipelines de données. On note des avancées majeures dans l'amélioration de la qualité des données (normalisation des noms de lieux avec [api-geo](/repos/datagouv/api-geo), correction des formats de dates avec [csv-detective](/repos/datagouv/csv-detective)), la robustesse des pipelines (gestion des erreurs et migration vers OVH S3 avec [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines)), et la mise à jour des données de référence (découpage administratif avec [decoupage-administratif](/repos/datagouv/decoupage-administratif) et schéma de métadonnées avec [schema.data.gouv.fr](/repos/datagouv/schema.data.gouv.fr)). L'API [api-tabular](/repos/datagouv/api-tabular) a également été renforcée en termes de sécurité et de flexibilité.

## Sécurité
L'API [api-tabular](/repos/datagouv/api-tabular) a bénéficié d'une correction des en-têtes CORS pour améliorer la compatibilité et la sécurité.

## Autres changements notables
- Migration du système de documentation vers GitBook pour [guides.data.gouv.fr](/repos/datagouv/guides.data.gouv.fr).
- Refactorisation des interactions avec S3 dans [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) pour une meilleure gestion et performance.
- Modernisation de la bibliothèque `fr-format` ([fr-format](/repos/datagouv/fr-format)) pour supporter Python 3.10 et supérieur.
- Ajout d'un champ `uptime_since` à l'API de santé de [hydra](/repos/datagouv/hydra) pour une information plus précise sur la durée de fonctionnement.

## Dépôts les plus actifs
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Amélioration de la robustesse des pipelines de données et ajout de nouvelles fonctionnalités pour la gestion des pétitions du Sénat.
- [csv-detective](/repos/datagouv/csv-detective) : Ajout de nouveaux formats de détection et amélioration de la précision de la détection des nombres et des dates.
- [fr-format](/repos/datagouv/fr-format) : Modernisation de la bibliothèque et ajout de nouveaux formats de validation.
- [hydra](/repos/datagouv/hydra) : Amélioration de la gestion des données WFS et correction de l'insertion de données dans la table `tables_index`.
- [schema.data.gouv.fr](/repos/datagouv/schema.data.gouv.fr) : Mises à jour régulières des recommandations du schéma de métadonnées.
