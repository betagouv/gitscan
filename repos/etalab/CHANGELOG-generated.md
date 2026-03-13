# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur plusieurs fronts chez etalab. L'API d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) a connu des évolutions majeures avec l'intégration de nouvelles API gouvernementales (CNOUS, DGFIP, MSA, CNAV) et l'amélioration de la gestion des tokens et des autorisations.  L'accent a également été mis sur l'amélioration de l'expérience utilisateur avec l'ajout de tableaux de bord et d'interfaces plus conviviales.  Dans le domaine du transport, des améliorations significatives ont été apportées à la recherche de données et à la validation des données NeTEx et GTFS, renforçant la qualité et l'accessibilité des informations pour les acteurs du secteur.

## Sécurité
- Rotation annuelle du token webhook pour renforcer la sécurité dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) et [data_pass](/repos/etalab/data_pass).
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Mise à jour de Postgres et TimescaleDB dans l'environnement CI de [transport-site](/repos/etalab/transport-site).
- Publication de la v2.4.0 du profil France NeTEx dans [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) avec des modifications structurelles et des clarifications importantes.
- Amélioration de la gestion des erreurs XSD dans le traitement NeTEx dans [transport-site](/repos/etalab/transport-site).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nombreuses intégrations d'API et amélioration de la gestion des autorisations.
- [data_pass](/repos/etalab/data_pass) : Amélioration de la gestion des habilitations FranceConnect et ajout de fonctionnalités de révocation.
- [transport-site](/repos/etalab/transport-site) : Amélioration significative de la recherche de données et ajout de rapports de validation NeTEx.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version majeure du profil France NeTEx.
- [transport-validator](/repos/etalab/transport-validator) : Amélioration de la validation des données GTFS, notamment pour le calendrier et la langue.
