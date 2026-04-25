# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur plusieurs fronts chez etalab. On observe des avancées significatives dans l'enrichissement des APIs de l'administration (ajout d'APIs CNOUS, MSA, et mise à jour de l'API MEN), améliorant ainsi l'accès aux données publiques pour les services numériques.  Des efforts importants ont également été consacrés à l'amélioration de la plateforme Data Pass avec de nouvelles fonctionnalités de gestion des demandes et des utilisateurs, ainsi qu'à la modernisation de l'infrastructure et des schémas de données, notamment dans le domaine du transport. L'accent a été mis sur la qualité des données et la conformité aux normes (NeTEx, GTFS).

## Sécurité
- Rotation annuelle du token webhook pour renforcer la sécurité de l'API [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion des accès.
- Mise à jour de Rails vers la version 8.1.2.1 dans [data_pass](/repos/etalab/data_pass).
- Prise en charge de la norme NeTEx v2.4.0 sur [transport-normes-site](/repos/etalab/transport-normes-site).
- Introduction de l'architecture des "data packages" pour étendre le schéma des dispositifs d'aide dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la gestion des tokens et de l'interface d'administration.
- [data_pass](/repos/etalab/data_pass) : Ajout de fonctionnalités de gestion des demandes, des utilisateurs et correction de bugs.
- [transport-site](/repos/etalab/transport-site) : Intégration de données NeTEx, amélioration de l'accessibilité et de l'export des données.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 du profil France NeTEx avec des clarifications et améliorations.
- [transport-normes-site](/repos/etalab/transport-normes-site) : Mise à jour pour supporter la dernière version de la norme NeTEx.
