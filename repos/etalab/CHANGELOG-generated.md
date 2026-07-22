# Synthèse d'activité : etalab (du 20 avril 2026 au 20 juillet 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et la maintenance de ses outils et données liés à la mobilité, aux normes de transport, et aux services publics numériques. Plusieurs dépôts ont bénéficié d'optimisations de performance, notamment [transport-validator](/repos/etalab/transport-validator) et [transport-site](/repos/etalab/transport-site), avec des améliorations de la gestion de la mémoire et du traitement des données IRVE. Des mises à jour importantes ont également été apportées aux schémas de données (Netex, Dispositif d'aide, lieux de covoiturage) pour une meilleure interopérabilité et flexibilité. Enfin, des efforts ont été déployés pour améliorer l'accès aux données (MAJIC 2024) et la sécurité des API (rotation de tokens, gestion des scopes).

## Sécurité
- Correction d'un bug dans [formulaire-qf](/repos/etalab/formulaire-qf) pour garantir que seules les notifications créées par l'application soient supprimées.
- Rotation annuelle du token webhook dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour renforcer la sécurité.
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion.

## Autres changements notables
- Refactorisation de la consolidation IRVE dans [transport-site](/repos/etalab/transport-site) pour optimiser le traitement des données.
- Suppression de dépendances obsolètes (TimescaleDB, exvcr, proxy_request) dans [transport-site](/repos/etalab/transport-site).
- Introduction de l'architecture "data packages" pour étendre le schéma de données dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).
- Migration de l'API TVA d'API Entreprise de VIES vers la DGFIP dans [data_pass](/repos/etalab/data_pass).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Amélioration du traitement des données IRVE et de l'expérience utilisateur.
- [transport-validator](/repos/etalab/transport-validator) : Optimisation des performances et de la consommation mémoire.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la gestion des autorisations.
- [data_pass](/repos/etalab/data_pass) : Développement de nouvelles fonctionnalités pour la gestion des autorisations et des APIs.
- [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) : Introduction d'une nouvelle architecture pour l'extension du schéma de données.
