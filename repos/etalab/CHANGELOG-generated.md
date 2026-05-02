# Synthèse d'activité : etalab (du 16/04 au 16/05)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et l'extension de ses services liés aux données de transport et à l'administration publique.  Plusieurs dépôts ont bénéficié de mises à jour pour supporter de nouveaux formats de données (NeTEx), enrichir les données disponibles (lieux de covoiturage, MAJIC 2024, API CNOUS), et améliorer la sécurité et la gestion des accès (data_pass, admin_api_entreprise). L'accent a également été mis sur la maintenance technique et l'amélioration de l'infrastructure de plusieurs projets.

## Sécurité
- L'API `admin_api_entreprise` ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) a mis en place une rotation annuelle du token webhook pour renforcer la sécurité.
- Migration des scopes des tokens vers les demandes d'autorisation dans `admin_api_entreprise` ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) pour une meilleure gestion des accès.

## Autres changements notables
- Le projet `schema-dispositif-aide` ([schema-dispositif-aide](/repos/etalab/schema-dispositif-aide)) a introduit une nouvelle architecture basée sur les "data packages" pour permettre l'extension du schéma de données.
- `transport-site` ([transport-site](/repos/etalab/transport-site)) a intégré le validateur IRVE de transport.data.gouv et a effectué une mise à jour majeure de sa stack JavaScript (ESLint 10 et Prettier).
- `data_pass` ([data_pass](/repos/etalab/data_pass)) a vu l'ajout de fonctionnalités de gestion des utilisateurs (bannissement, révocation des droits) et l'ajout de webhooks pour les événements liés aux organisations.

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Ajout de nouvelles fonctionnalités d'affichage et de suivi des données de transport, notamment avec la prise en charge du format NeTEx.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Intégration de nouvelles APIs (CNOUS, MSA) et amélioration de la gestion des tokens et des autorisations.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version (v2.4.0) du profil France NeTEx avec des clarifications et des améliorations.
- [data_pass](/repos/etalab/data_pass) : Amélioration de la gestion des utilisateurs et ajout de webhooks pour une meilleure intégration avec d'autres services.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Enrichissement de la base de données des lieux de covoiturage avec de nouvelles localisations.
