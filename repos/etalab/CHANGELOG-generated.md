# Synthèse d'activité : etalab (du 28 avril 2026 au 01 juin 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et la maintenance de ses nombreux projets open-source. Plusieurs dépôts ont bénéficié de mises à jour de sécurité, notamment [transport-site](/repos/etalab/transport-site) et [formulaire-qf](/repos/etalab/formulaire-qf). Des améliorations fonctionnelles ont été apportées à [transport-site](/repos/etalab/transport-site) avec l'ajout de la prise en charge des données GBFS de Yégo, et à [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) avec l'introduction des "data packages" pour une plus grande flexibilité du schéma. Des mises à jour de données ont également été effectuées sur [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) et [majic](/repos/etalab/majic). L'API [admin_api_entreprise](/repos/etalab/admin_api_entreprise) a vu l'ajout de nouvelles API et l'amélioration de la gestion des tokens.

## Sécurité
Plusieurs mises à jour de dépendances JavaScript ont été appliquées dans [transport-site](/repos/etalab/transport-site) pour corriger des failles de sécurité. La rotation annuelle du token webhook a également été implémentée dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour renforcer la sécurité.

## Autres changements notables
- Migration du système de gestion des styles SCSS de `@import` vers `@use` dans [transport-site](/repos/etalab/transport-site) pour une meilleure performance.
- Introduction de l'architecture des "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) pour étendre le schéma de données.
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion.

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Maintenance technique, améliorations de la sécurité et ajout de la prise en charge de nouvelles données.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la gestion des tokens et de la sécurité.
- [transport-validator](/repos/etalab/transport-validator) : Optimisation des performances et de la consommation mémoire.
- [formulaire-qf](/repos/etalab/formulaire-qf) : Correction de bugs et mise à jour des dépendances.
- [data_pass](/repos/etalab/data_pass) : Ajout de formulaires pré-remplis et amélioration de la recherche d'utilisateurs.
