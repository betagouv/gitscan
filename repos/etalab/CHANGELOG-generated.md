# Synthèse d'activité : etalab (du 27 avril 2026 au 16 mai 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et l'extension de ses services liés aux données de transport, aux données d'aides sociales et à la gestion des API. Plusieurs dépôts ont bénéficié de mises à jour significatives, notamment [transport-site](/repos/etalab/transport-site) avec l'ajout du support de nouveaux formats de données (GBFS, NeTEx) et une refonte technique majeure, et [data_pass](/repos/etalab/data_pass) avec l'ajout de fonctionnalités de gestion des utilisateurs et d'amélioration de la sécurité.  Des efforts ont également été déployés pour améliorer la qualité des données, comme le montrent les mises à jour de la base de données de covoiturage [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) et du profil France NeTEx [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr).

## Sécurité
Plusieurs dépôts ont reçu des mises à jour de dépendances pour corriger des vulnérabilités et améliorer la sécurité :
- Mise à jour de dépendances de sécurité dans [formulaire-qf](/repos/etalab/formulaire-qf).
- Rotation annuelle du token webhook pour renforcer la sécurité dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Refonte majeure de la stack JavaScript dans [transport-site](/repos/etalab/transport-site).
- Ajout de la prise en charge des extensions de schéma via "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).
- Passage du validateur IRVE à la demande au validateur intégré de transport.data.gouv dans [transport-site](/repos/etalab/transport-site).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Ajout de support pour de nouveaux formats de données de transport et refonte technique importante.
- [data_pass](/repos/etalab/data_pass) : Amélioration de la gestion des utilisateurs, ajout de fonctionnalités de bannissement et amélioration de la sécurité.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la gestion des tokens et des performances.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version du profil France NeTEx avec des clarifications et des améliorations.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Enrichissement de la base de données de covoiturage avec de nouveaux lieux.
