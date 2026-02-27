# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur plusieurs dépôts d'etalab. L'accent a été mis sur l'amélioration des APIs (admin_api_entreprise, data_pass) avec de nouvelles fonctionnalités pour la gestion des requêtes, l'authentification et l'accès aux données.  Des efforts importants ont également été déployés pour améliorer la qualité des données de transport (transport-site, transport-validator, lieux-covoiturage, transport-base-nationale-covoiturage) et pour assurer la stabilité et la sécurité des applications (formulaire-qf, flask-storage). L'API calendrier.api.gouv.fr a bénéficié d'une surveillance accrue de sa disponibilité.

## Sécurité
- L'API [admin_api_entreprise](/repos/etalab/admin_api_entreprise) a bénéficié d'améliorations de la sécurité et de la gestion des paramètres de sécurité des requêtes d'autorisation.
- L'authentification multi-facteurs (MFA) a été forcée pour les utilisateurs MonComptePro via ProConnect dans [data_pass](/repos/etalab/data_pass).

## Autres changements notables
- L'implémentation de `rails_pulse` pour le monitoring de l'application dans [data_pass](/repos/etalab/data_pass).
- L'ajout d'un cache disque et la vérification de l'ETag pour le proxy Unlock S3 dans [transport-site](/repos/etalab/transport-site) pour améliorer les performances.
- La mise à jour du workflow de test dans [lieux-covoiturage](/repos/etalab/lieux-covoiturage) pour améliorer la gestion du cache.

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Amélioration de l'expérience utilisateur et ajout de fonctionnalités pour la gestion des requêtes API.
- [data_pass](/repos/etalab/data_pass) : Intégration de FranceConnect, renforcement de la sécurité avec l'authentification multi-facteurs et amélioration du monitoring.
- [transport-site](/repos/etalab/transport-site) : Amélioration de la recherche de jeux de données et de l'affichage des métadonnées NeTEx.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Enrichissement de la base de données avec de nouveaux lieux de covoiturage.
- [siade_staging_data](/repos/etalab/siade_staging_data) : Mise à jour des données de test pour les APIs Entreprise et Particulier.
