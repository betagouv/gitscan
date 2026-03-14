# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur plusieurs fronts chez etalab. L'API d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) s'est enrichie de nouvelles intégrations avec des services publics (CNOUS, DGFIP, MSA, CNAV) et de fonctionnalités de gestion des délégations et des tokens.  Des améliorations significatives ont également été apportées au site [transport-site](/repos/etalab/transport-site) avec une refonte de la recherche de jeux de données et l'ajout de rapports de validation NeTEx.  Plusieurs dépôts ont bénéficié de mises à jour de sécurité et de maintenance pour assurer la stabilité et la conformité des services.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :
- Rotation annuelle des tokens webhook dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) et [data_pass](/repos/etalab/data_pass) pour renforcer la sécurité.

## Autres changements notables
- Mise à jour de Postgres et TimescaleDB dans l'environnement CI de [transport-site](/repos/etalab/transport-site) pour bénéficier des dernières corrections de sécurité.
- Publication de la version 2.4.0 du profil France NeTEx ([transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr)) avec des clarifications et améliorations importantes.
- Mise en place de Rails Pulse pour le monitoring de la performance de l'application [data_pass](/repos/etalab/data_pass).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles intégrations API et amélioration de la gestion des autorisations.
- [transport-site](/repos/etalab/transport-site) : Refonte de la recherche de données et ajout de rapports de validation NeTEx.
- [data_pass](/repos/etalab/data_pass) : Amélioration de la gestion des habilitations FranceConnect et ajout de fonctionnalités de révocation d'habilitations.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la nouvelle version 2.4.0 du profil France NeTEx.
- [transport-validator](/repos/etalab/transport-validator) : Amélioration de la validation des données GTFS.
