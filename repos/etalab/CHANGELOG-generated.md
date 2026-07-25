# Synthèse d'activité : etalab (du 22 avril 2026 au 22 juillet 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et la maintenance de ses outils et schémas de données, particulièrement dans les domaines du transport, du covoiturage et des services publics numériques. Plusieurs dépôts ont bénéficié de corrections de bugs, d'optimisations de performance et d'ajouts de nouvelles fonctionnalités, notamment pour la gestion des données IRVE, des opérateurs de vélos en libre-service et des dispositifs d'aide. L'organisation a également continué à développer et à documenter ses schémas de données, comme NeTEx France et MAJIC, pour faciliter l'interopérabilité et l'échange de données.  [transport-site](/repos/etalab/transport-site) et [data_pass](/repos/etalab/data_pass) ont été particulièrement actifs.

## Sécurité
- Correction d'un bug dans [flask-storage](/repos/etalab/flask-storage) qui pouvait potentiellement permettre la suppression de fichiers non autorisés sur S3.
- Rotation annuelle du token webhook dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour renforcer la sécurité.

## Autres changements notables
- Refactorisation du processus de consolidation IRVE dans [transport-site](/repos/etalab/transport-site) pour optimiser les performances.
- Passage à l'allocateur mémoire `jemalloc` dans [transport-validator](/repos/etalab/transport-validator) pour réduire la consommation mémoire.
- Introduction de l'architecture des "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) pour permettre l'extension du schéma de données.
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion.

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Amélioration du traitement des données IRVE, ajout de nouveaux opérateurs de vélos en libre-service et corrections de bugs.
- [data_pass](/repos/etalab/data_pass) : Ajout de la gestion des définitions d'autorisations et implémentation de nouvelles APIs.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs (CNOUS, MSA, MEN) et amélioration de la gestion des tokens et de la sécurité.
- [transport-validator](/repos/etalab/transport-validator) : Optimisation de la performance et de la consommation mémoire.
- [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) : Introduction de l'architecture des "data packages" pour une plus grande flexibilité du schéma.
