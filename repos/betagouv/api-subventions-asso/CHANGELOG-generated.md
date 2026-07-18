## Changelog : api-subventions-asso (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration des données des associations, notamment via l'API Sirene et Chorus, ainsi que sur des corrections de bugs pour assurer la stabilité et la fiabilité du service. Des optimisations techniques ont également été apportées, notamment concernant la gestion des erreurs et l'authentification.

### Évolutions fonctionnelles

- Intégration de l'API Sirene pour récupérer les informations sur les établissements : permet d'enrichir les données des associations et d'améliorer la qualité du service. ([#3986](https://github.com/betagouv/api-subventions-asso/issues/3986))
- Amélioration des notifications lors de l'importation de données des fournisseurs. ([#3933](https://github.com/betagouv/api-subventions-asso/issues/3933))
- Correction d'un problème d'affichage des alertes de doublons SIREN sur l'interface utilisateur. ([#3964](https://github.com/betagouv/api-subventions-asso/issues/3964))

### Évolutions techniques

- Mise à jour de l'URL de l'API Sirene pour utiliser un lien stable, améliorant ainsi la robustesse de l'intégration. ([#3982](https://github.com/betagouv/api-subventions-asso/issues/3982))
- Refactorisation du service de gestion des droits (grant service) pour une meilleure maintenabilité. ([#3527](https://github.com/betagouv/api-subventions-asso/issues/3527))
- Suppression des codes d'erreur HTTP personnalisés au profit de codes standardisés, simplifiant ainsi l'intégration avec d'autres systèmes. ([#3945](https://github.com/betagouv/api-subventions-asso/issues/3945))
- Utilisation de l'entité `UserEntity` pour supprimer l'utilisation de `_id`, améliorant la cohérence du code. ([#3971](https://github.com/betagouv/api-subventions-asso/issues/3971))
- Remplacement de l'identifiant unique Chorus par un index composite pour une meilleure performance. ([#3942](https://github.com/betagouv/api-subventions-asso/issues/3942))
- Mise à jour de pnpm vers la version 11. ([#3897](https://github.com/betagouv/api-subventions-asso/issues/3897))
- Suppression du JWT lors de la déconnexion pour renforcer la sécurité. ([#1288](https://github.com/betagouv/api-subventions-asso/issues/1288))

### Autres changements

- Mise à jour des scripts de publication pour inclure tous les packages.
- Correction de la génération du changelog.
- Suppression d'un ancien nom de connexion Pro Connect.
- Tests unitaires mis à jour.
