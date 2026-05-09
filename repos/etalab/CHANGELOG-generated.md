# Synthèse d'activité : etalab (du 23 avril 2026 au 27 mai 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et l'enrichissement des données et des services existants, ainsi que sur l'ajout de nouvelles fonctionnalités pour répondre aux besoins des utilisateurs. On observe une forte activité sur les schémas de données (IRVE, dispositifs d'aide, covoiturage) avec des évolutions majeures comme l'introduction de l'architecture "data packages" pour le schéma des dispositifs d'aide. Plusieurs dépôts ont bénéficié d'améliorations de l'API et de l'interface utilisateur, notamment [data_pass](/repos/etalab/data_pass) et [admin_api_entreprise](/repos/etalab/admin_api_entreprise). L'intégration de nouvelles données (MAJIC 2024, lieux de covoiturage) et l'amélioration de la couverture géographique sont également notables.

## Sécurité
- Rotation annuelle du token webhook pour renforcer la sécurité sur [admin_api_entreprise](/repos/etalab/admin_api_entreprise).
- Migration des scopes des tokens vers les demandes d'autorisation pour une meilleure gestion sur [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Migration majeure de la stack JavaScript (tooling, build, dépendances) sur [transport-site](/repos/etalab/transport-site).
- Modernisation du tooling de test pour améliorer la robustesse sur [schema-irve](/repos/etalab/schema-irve).
- Ajout de la prise en charge des extensions de schéma via l'architecture des "data packages" sur [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Ajout de nouvelles fonctionnalités d'affichage de données NeTEx et d'une page de suivi des jobs dans le back-office, ainsi qu'une mise à jour majeure de la stack JavaScript.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs (CNOUS, MSA) et améliorations de l'interface d'administration et de la gestion des tokens.
- [data_pass](/repos/etalab/data_pass) : Ajout de la possibilité de bannir des utilisateurs, amélioration de l'affichage du statut des demandes et création de demandes via l'API.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version (v2.4.0) du profil France NeTEx avec des clarifications et améliorations.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Enrichissement de la base de données avec de nouveaux lieux de covoiturage.
