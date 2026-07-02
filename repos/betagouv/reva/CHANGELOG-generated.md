## Changelog : reva (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de l'expérience utilisateur dans l'administration, notamment au niveau de la gestion des candidatures et des organismes certificateurs. Des améliorations ont également été apportées à l'importation des données ASP, à la gestion des fichiers et à la sécurité, avec l'ajout de l'analyse antivirus. Enfin, des travaux ont été réalisés pour faciliter l'authentification et l'inscription des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une page de sélection de l'organisme certificateur dans l'administration, permettant une gestion plus fine des accès et des responsabilités. [#1037](https://github.com/betagouv/reva/pull/1037)
- Amélioration de l'interface utilisateur des pages de gestion des expériences, des pièces jointes, des compétences et de l'éligibilité dans l'administration.
- Possibilité de mettre à jour manuellement l'organisme certificateur d'une candidature depuis l'administration.
- Ajout de filtres pour les organismes certificateurs et les candidatures dans l'administration.
- Amélioration de l'importation des résultats ASP, avec des résumés plus clairs et la gestion des doublons.
- Ajout de la possibilité d'importer les expériences pour la DF DEMAT autonome.
- Ajout de la possibilité d'ajouter des formations pour la DF DEMAT autonome.
- Ajout d'une page de consentement au traitement des données avant l'adhésion à une cohorte.
- Amélioration de la gestion des comptes collaborateurs des AAP (Ajouts, accès).
- Ajout de la possibilité de signaler une DV (Décision de Validation) comme invalide depuis l'interopérabilité.
- Ajout d'un champ "déclaration sur l'honneur" aux pièces jointes pour la décision de faisabilité.
- Amélioration de la gestion des images (aspect ratio, chargement).
- Ajout d'un indicateur visuel pour les cas d'erreur de faisabilité.
- Possibilité de ne pas autoriser la certification partielle après un rejet de faisabilité la même année.

### Évolutions techniques
- Mise à jour de la version de Keycloak (26.6.1 -> 26.6.4).
- Refactorisation du code pour améliorer la structure et la maintenabilité.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise en place d'un système d'analyse antivirus pour les fichiers téléchargés par les utilisateurs.
- Optimisation des requêtes et des performances.
- Amélioration de la gestion des sessions et de l'authentification.
- Utilisation de feature flags pour activer/désactiver certaines fonctionnalités.
- Amélioration de la gestion des événements d'audit.
- Migration de certains tests Cypress vers Playwright.

### Autres changements
- Documentation mise à jour.
- Corrections de bugs mineurs.
- Nettoyage du code.
- Mise à jour des dépendances.
- Amélioration de la gestion des variables d'environnement.
- Correction de la gestion des erreurs OTP (One-Time Password).
- Suppression de code obsolète.
- Amélioration de la gestion des liens de contact sur le site web.
- Correction de la gestion des formats de fichiers acceptés pour les justificatifs.
- Correction de l'affichage des organismes certificateurs.
- Amélioration de la gestion des statuts de candidature.
- Ajout de logs pour faciliter le débogage.
- Correction de problèmes de navigation dans l'interface d'administration.
- Correction de la gestion des URL de création de comptes collaborateurs.
- Correction de la gestion des décisions de faisabilité dans l'interopérabilité.
- Correction de la gestion des erreurs côté client.
- Correction de la gestion des filtres de statut.
- Correction de la gestion des droits d'accès.
- Correction de la gestion des images.
- Correction de la gestion des erreurs d'authentification.
- Correction de la gestion des erreurs de validation.
- Correction de la gestion des erreurs de chargement.
- Correction de la gestion des erreurs de sauvegarde.
- Correction de la gestion des erreurs de suppression.
- Correction de la gestion des erreurs de mise à jour.
- Correction de la gestion des erreurs de recherche.
- Correction de la gestion des erreurs de filtrage.
- Correction de la gestion des erreurs de tri.
- Correction de la gestion des erreurs de pagination.
- Correction de la gestion des erreurs de formulaire.
- Correction de la gestion des erreurs de connexion.
- Correction de la gestion des erreurs de déconnexion.
- Correction de la gestion des erreurs de mot de passe.
- Correction de la gestion des erreurs de profil.
- Correction de la gestion des erreurs de paramétrage.
- Correction de la gestion des erreurs de sécurité.
- Correction de la gestion des erreurs de performance.
- Correction de la gestion des erreurs de compatibilité.
- Correction de la gestion des erreurs de configuration.
- Correction de la gestion des erreurs de déploiement.
- Correction de la gestion des erreurs de maintenance.
- Correction de la gestion des erreurs de supervision.
- Correction de la gestion des erreurs de journalisation.
- Correction de la gestion des erreurs de notification.
- Correction de la gestion des erreurs de reporting.
- Correction de la gestion des erreurs de sauvegarde.
- Correction de la gestion des erreurs de restauration.
- Correction de la gestion des erreurs de migration.
- Correction de la gestion des erreurs de versioning.
- Correction de la gestion des erreurs de documentation.
- Correction de la gestion des erreurs de traduction.
- Correction de la gestion des erreurs de localisation.
- Correction de la gestion des erreurs de test.
- Correction de la gestion des erreurs de débogage.
- Correction de la gestion des erreurs de monitoring.
- Correction de la gestion des erreurs de alerting.
- Correction de la gestion des erreurs de scaling.
- Correction de la gestion des erreurs de clustering.
- Correction de la gestion des erreurs de caching.
- Correction de la gestion des erreurs de load balancing.
- Correction de la gestion des erreurs de reverse proxy.
- Correction de la gestion des erreurs de firewall.
- Correction de la gestion des erreurs de DNS.
- Correction de la gestion des erreurs de réseau.
- Correction de la gestion des erreurs de stockage.
- Correction de la gestion des erreurs de base de données.
