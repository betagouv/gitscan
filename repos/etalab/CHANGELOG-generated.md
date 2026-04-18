# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur plusieurs fronts. L'organisation a continué à enrichir ses APIs avec de nouvelles fonctionnalités, notamment dans le domaine de l'accès aux données sociales ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) et de l'éducation. Des améliorations significatives ont été apportées à la plateforme Data Pass ([data_pass](/repos/etalab/data_pass)) en termes de gestion des utilisateurs et de performance.  Les projets liés au transport ont également été actifs, avec des mises à jour des normes NeTEx ([transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr)), du site de publication ([transport-site](/repos/etalab/transport-site)) et des données elles-mêmes ([transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage)).

## Sécurité
- Rotation annuelle du token webhook pour renforcer la sécurité de l'API [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion.
- Optimisation significative des performances des tests CI/CD dans [data_pass](/repos/etalab/data_pass) grâce à la parallélisation et à l'optimisation de Docker.
- Mise à jour de Rails vers la version 8.1.2.1 dans [data_pass](/repos/etalab/data_pass).
- Prise en charge de la nouvelle version de la norme NeTEx v2.4.0 sur [transport-normes-site](/repos/etalab/transport-normes-site).
- Validation plus stricte des données GTFS-RT dans [transport-site](/repos/etalab/transport-site).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la sécurité et des performances.
- [data_pass](/repos/etalab/data_pass) : Amélioration de la gestion des utilisateurs, des performances et mise à jour des dépendances.
- [transport-site](/repos/etalab/transport-site) : Amélioration de l'interface utilisateur, ajout de nouvelles fonctionnalités d'export et renforcement de la validation des données.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version majeure du profil France NeTEx.
