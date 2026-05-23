# Synthèse d'activité : etalab (du 28 avril 2026 au 16 mai 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et l'enrichissement de ses services liés aux données de transport, à l'aide sociale et aux données d'entreprises. Plusieurs dépôts ont bénéficié de mises à jour pour supporter de nouveaux formats de données (GBFS, NeTEx), étendre les schémas de données (dispositifs d'aide, lieux de covoiturage) et améliorer l'expérience utilisateur (transport-site, admin_api_entreprise). Des efforts importants ont également été déployés pour renforcer la sécurité (correction d'une vulnérabilité dans `admin_api_entreprise`, mises à jour de dépendances) et maintenir la stabilité des infrastructures.

## Sécurité
- Correction d'une vulnérabilité bloquant l'authentification sur un SIRET invalide dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).
- Mises à jour de dépendances dans [formulaire-qf](/repos/etalab/formulaire-qf) pour corriger des vulnérabilités.

## Autres changements notables
- Migration de la stack JavaScript dans [transport-site](/repos/etalab/transport-site).
- Passage du validateur IRVE à la demande au validateur intégré de transport.data.gouv dans [transport-site](/repos/etalab/transport-site).
- Ajout de la prise en charge des extensions de schéma via l'architecture des "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Ajout du support de nouveaux formats de données et améliorations de l'interface utilisateur.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles API et amélioration de la gestion des tokens et de la sécurité.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version du profil France NeTEx avec des clarifications et améliorations.
- [data_pass](/repos/etalab/data_pass) : Ajout d'une interface de gestion des droits utilisateurs et de nouveaux endpoints API.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Enrichissement de la base de données de covoiturage avec de nouveaux lieux.
