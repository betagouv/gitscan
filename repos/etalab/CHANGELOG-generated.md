# Synthèse d'activité : etalab (derniers 30 jours)

## Résumé de l'activité
Le mois dernier, l'activité d'etalab s'est concentrée sur l'amélioration de la sécurité et de la qualité des données, ainsi que sur l'ajout de nouvelles fonctionnalités à ses outils. L'admin API entreprise [admin_api_entreprise](/repos/etalab/admin_api_entreprise) a bénéficié de renforcements de sécurité et de nouvelles capacités de recherche d'API et d'intégration de données INSEE. Les données de la base nationale de covoiturage [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) ont été affinées avec l'ajout de nouveaux départements et la correction de doublons. Enfin, le validateur de données GTFS [transport-validator](/repos/etalab/transport-validator) a vu ses règles de validation renforcées pour garantir une meilleure qualité des données de transport en commun.

## Sécurité
L'admin API entreprise [admin_api_entreprise](/repos/etalab/admin_api_entreprise) a reçu des améliorations significatives en matière de sécurité :
- Implémentation de la réauthentification MFA pour les utilisateurs MonComptePro.
- Renforcement de la sécurité des tokens d'administration.
- Possibilité de bannir un token d'administrateur avec une date de fin personnalisée.

## Autres changements notables
- Suppression des identifiants Algolia de l'admin API entreprise [admin_api_entreprise](/repos/etalab/admin_api_entreprise).
- Ajout de la configuration optionnelle du nom du bucket S3 dans flask-storage [flask-storage](/repos/etalab/flask-storage).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Amélioration de la sécurité, ajout de fonctionnalités de recherche et intégration de données INSEE.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Mise à jour et correction de la base de données des lieux de covoiturage.
- [transport-validator](/repos/etalab/transport-validator) : Renforcement des règles de validation des données GTFS.
