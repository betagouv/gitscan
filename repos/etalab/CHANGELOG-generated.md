# Synthèse d'activité : etalab (du 28 avril 2026 au 11 juin 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration de la sécurité, l'enrichissement des données et l'ajout de nouvelles fonctionnalités à ses différents services.  Plusieurs dépôts ont bénéficié de mises à jour pour faciliter l'accès aux données (MAJIC, covoiturage) ou pour renforcer la sécurité des API (DataPass, admin_api_entreprise). Des améliorations significatives ont été apportées à l'API `admin_api_entreprise` avec l'ajout de nouvelles sources de données et une gestion plus fine des autorisations. Le profil France NeTEx a également été mis à jour pour clarifier et améliorer la structuration des données.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de failles de sécurité JavaScript dans [transport-site](/repos/etalab/transport-site).
- Renforcement de la sécurité des sessions DataPass (durée réduite) et gestion des clés API dans [data_pass](/repos/etalab/data_pass).
- Rotation annuelle du token webhook dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Passage à l'allocateur mémoire `jemalloc` dans [transport-validator](/repos/etalab/transport-validator) pour optimiser la consommation mémoire.
- Refactoring de l'API et ajout de la possibilité de trier les résultats dans [data_pass](/repos/etalab/data_pass).
- Introduction de l'architecture des "data packages" pour étendre le schéma de données des dispositifs d'aide dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Améliorations du module IRVE, corrections de sécurité et refactoring technique.
- [data_pass](/repos/etalab/data_pass) : Renforcement de la sécurité, ajout de nouvelles fonctionnalités et optimisations des performances.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles API, amélioration de la gestion des autorisations et optimisations des performances.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version (v2.4.0) avec des clarifications et améliorations du profil France NeTEx.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Mises à jour régulières de la base de données des lieux de covoiturage.
