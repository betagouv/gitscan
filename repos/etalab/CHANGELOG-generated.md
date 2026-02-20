# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par des améliorations significatives en matière de sécurité et d'expérience utilisateur sur plusieurs projets d'etalab. L'admin API entreprise ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) a renforcé sa sécurité avec l'authentification MFA et la gestion des tokens, tout en améliorant les fonctionnalités de recherche d'API et l'intégration de données INSEE.  Data Pass ([data_pass](/repos/etalab/data_pass)) a progressé dans l'intégration de FranceConnect et l'amélioration de la gestion des habilitations, facilitant l'accès aux données pour les utilisateurs. Des améliorations de la qualité des données ont également été apportées à la base nationale des lieux de covoiturage ([transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage)) et au validateur GTFS ([transport-validator](/repos/etalab/transport-validator)).

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :

- Implémentation de la réauthentification MFA pour les utilisateurs MonComptePro via ProConnect dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).
- Ajout de l'authentification multi-facteurs (MFA) pour les utilisateurs ProConnect dans [data_pass](/repos/etalab/data_pass).
- Renforcement de la sécurité en utilisant le namespace au lieu d'une valeur codée en dur pour les tokens d'administration dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Mise en place de feature flags pour l'APIFC dans [data_pass](/repos/etalab/data_pass) pour une meilleure gestion des déploiements.
- Implémentation de rails_pulse pour le monitoring de la performance dans [data_pass](/repos/etalab/data_pass).
- La validation de l'absence de calendrier est maintenant signalée comme une erreur critique dans [transport-validator](/repos/etalab/transport-validator).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Amélioration de la sécurité, ajout de nouvelles fonctionnalités de recherche d'API et intégration de données INSEE.
- [data_pass](/repos/etalab/data_pass) : Intégration et amélioration de FranceConnect, ajout de l'authentification MFA et amélioration de la gestion des habilitations.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Mise à jour de la base de données des lieux de covoiturage avec l'ajout du département du Loir-et-Cher et la suppression de doublons.
- [transport-validator](/repos/etalab/transport-validator) : Amélioration de la validation des informations de calendrier et de langue pour les données GTFS.
