# Synthèse d'activité : etalab (du 27 avril 2026 au 8 juin 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et la maintenance de ses outils et données, notamment dans les domaines du transport, du covoiturage, des données d'aide sociale et des API d'administration. Plusieurs dépôts ont bénéficié de corrections de bugs, d'optimisations de performance et de mises à jour de données. L'ajout de nouvelles fonctionnalités, comme l'extension du schéma des dispositifs d'aide via des "data packages" ([schema-dispositif-aide](/repos/etalab/schema-dispositif-aide)) et l'intégration de nouvelles API (CNOUS, MSA) dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise), témoignent d'une volonté d'enrichir l'offre de services.  Des améliorations significatives ont également été apportées à [data_pass](/repos/etalab/data_pass) pour la gestion des droits et l'expérience utilisateur.

## Sécurité
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion des accès.
- Rotation annuelle du token webhook dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour renforcer la sécurité.

## Autres changements notables
- Passage à l'allocateur mémoire `jemalloc` dans [transport-validator](/repos/etalab/transport-validator) pour optimiser la consommation mémoire en production.
- Refactoring important dans [transport-site](/repos/etalab/transport-site) avec suppression de code obsolète et simplification de l'architecture.
- Mise à jour de Ruby à la dernière version dans [data_pass](/repos/etalab/data_pass).
- Migration du scope TVA d'API Entreprise de VIES vers la DGFIP dans [data_pass](/repos/etalab/data_pass).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Consolidation et gestion des données IRVE, améliorations de la précision des coordonnées et optimisations de l'architecture.
- [data_pass](/repos/etalab/data_pass) : Amélioration de la gestion des droits d'accès, ajout de nouvelles API et maintenance technique.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Intégration de nouvelles API (CNOUS, MSA), amélioration de l'interface d'administration et renforcement de la sécurité.
- [transport-validator](/repos/etalab/transport-validator) : Optimisation de la performance et de la consommation mémoire.
- [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) : Ajout de la prise en charge des extensions de schéma via l'architecture des "data packages".
