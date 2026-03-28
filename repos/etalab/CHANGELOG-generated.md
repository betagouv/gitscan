# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur les APIs d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) avec l'ajout de nouvelles fonctionnalités et l'amélioration de la sécurité.  L'écosystème de données de transport a également connu des évolutions significatives, notamment avec la mise à jour du profil France NeTEx ([transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr)) et l'amélioration de la recherche et de la validation de données sur [transport-site](/repos/etalab/transport-site).  De nouvelles intégrations d'APIs ont été réalisées sur [data_pass](/repos/etalab/data_pass) et des améliorations apportées à l'interface utilisateur.

## Sécurité
- Rotation annuelle du token webhook pour renforcer la sécurité sur [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Migration des scopes des tokens vers les demandes d'autorisation pour une meilleure gestion sur [admin_api_entreprise](/repos/etalab/admin_api_entreprise).
- Mise à jour de Postgres et TimescaleDB dans l'environnement CI sur [transport-site](/repos/etalab/transport-site).
- Prise en charge de la nouvelle version de la norme NeTEx v2.4.0 sur [transport-normes-site](/repos/etalab/transport-normes-site).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la sécurité des tokens.
- [data_pass](/repos/etalab/data_pass) : Intégration de nouvelles APIs et amélioration de l'interface d'administration.
- [transport-site](/repos/etalab/transport-site) : Amélioration significative de la recherche de données et ajout de rapports de validation NeTEx.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 du profil France NeTEx avec des clarifications et améliorations.
