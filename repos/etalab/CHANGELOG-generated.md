# Synthèse d'activité : etalab (du 16 mai 2026 au 27 avril 2026)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur plusieurs fronts chez etalab.  Les efforts se sont concentrés sur l'amélioration et l'extension des services liés au transport (données GBFS, NeTEx, validation GTFS) avec [transport-site](/repos/etalab/transport-site) et [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr).  Des avancées significatives ont également été réalisées sur la plateforme d'autorisation d'accès aux données [data_pass](/repos/etalab/data_pass) avec de nouvelles fonctionnalités pour la gestion des droits et l'intégration de nouvelles API.  Enfin, des mises à jour régulières ont été apportées aux bases de données de covoiturage [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) et aux données des jours fériés [jours-feries-france-data](/repos/etalab/jours-feries-france-data).

## Sécurité
Aucun changement lié à la sécurité n'a été spécifiquement mentionné dans les changelogs fournis.

## Autres changements notables
- Migration de la stack JavaScript dans [transport-site](/repos/etalab/transport-site).
- Refactorisation du code et suppression de code obsolète dans [transport-site](/repos/etalab/transport-site).
- Introduction de l'architecture "data packages" pour étendre le schéma des dispositifs d'aide dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion de la sécurité.
- Rotation annuelle du token webhook pour renforcer la sécurité dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Ajout du support de nouvelles données (GBFS, NeTEx) et refactorisation importante de la stack JavaScript.
- [data_pass](/repos/etalab/data_pass) : Amélioration de la gestion des droits d'accès et intégration de nouvelles API.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version (v2.4.0) du profil France NeTEx avec des clarifications et améliorations.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles API et amélioration de la sécurité et des performances.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Mise à jour régulière de la base de données des lieux de covoiturage.
