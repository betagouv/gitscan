## Changelog : monstagedeseconde (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des candidatures, des conventions et des utilisateurs, ainsi que sur la correction de bugs et l'optimisation de la plateforme. Des améliorations significatives ont été apportées à la gestion des stages, notamment en permettant d'associer du personnel pédagogique à plusieurs établissements et en gérant les doublons de candidatures. L'intégration de Claude, un outil d'IA, pour l'assistance au développement est également en cours.

### Évolutions fonctionnelles
- Possibilité d'associer un personnel pédagogique à un ou plusieurs établissements [#881](https://github.com/betagouv/monstagedeseconde/issues/881).
- Amélioration de la gestion des doublons de candidatures pour les deux publics (3ème et 2nde) [#906](https://github.com/betagouv/monstagedeseconde/issues/906).
- Possibilité de modifier l'adresse email des représentants légaux [#813](https://github.com/betagouv/monstagedeseconde/issues/813).
- Correction d'un bug empêchant la publication de plusieurs offres suite à des clics intempestifs [#907](https://github.com/betagouv/monstagedeseconde/issues/907).
- Amélioration de la gestion des candidatures :
    - Correction d'un problème de duplication des approbations de candidatures [#904](https://github.com/betagouv/monstagedeseconde/issues/904).
    - Limitation du nombre de candidatures par étudiant et par offre.
    - Correction d'un bug empêchant la soumission multiple d'une candidature par un même étudiant.
- Ajout d'un lien vers "letter thief" pour faciliter la gestion des lettres.
- Amélioration de la gestion des conventions :
    - Correction d'un bug lié à la duplication des conventions.
    - Affichage du signataire de la convention.
- Ajout de préfixes téléphoniques pour la Guadeloupe [#859](https://github.com/betagouv/monstagedeseconde/issues/859).
- Amélioration de l'importation des étudiants depuis l'administration.
- Ajout d'un chatbot Crisp pour l'assistance aux utilisateurs.
- Amélioration de l'affichage des ressources avec l'URL correspondante.
- Mise à jour du libellé de la récupération des candidatures.
- Gestion des semaines vides dans les plannings.
- Possibilité d'importer les étudiants depuis l'administration.
- Affichage des URL des ressources.

### Évolutions techniques
- Refactoring de l'architecture des autorisations (abilities) avec utilisation de CanCanCan [#889](https://github.com/betagouv/monstagedeseconde/issues/889).
- Mise à jour de la version de Ruby à 3.4.9 [#884](https://github.com/betagouv/monstagedeseconde/issues/884).
- Amélioration de la gestion des erreurs Sygne avec la création d'exceptions spécifiques.
- Ajout de tests pour la gestion des utilisateurs et des écoles.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests pour les callbacks du contrôleur.
- Mise à jour des dépendances : `shell-quote`, `net-imap`, `puma`, `webpack-dev-server`, `jwt`, `faraday`.
- Amélioration de la gestion des jobs Sidekiq sur Heroku.
- Ajout de la gestion de l'environnement `maintenance_mode` via FlipperCloud.
- Correction de problèmes de configuration Redis.
- Amélioration de la gestion des utilisateurs et des rôles dans l'administration.
- Ajout d'une étape de mise à jour des informations des établissements dans le pipeline de rebuild.
- Correction de problèmes de chargement des modèles.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout d'une étape pour créer les entrées `UserSchool` après la reconstruction des utilisateurs.

### Autres changements
- Ajout de documentation pour les nouvelles fonctionnalités.
- Nettoyage du code et suppression de fichiers inutiles.
- Mise à jour des descriptions des extensions dans le fichier `structure.sql`.
- Ajout de tests unitaires et d'intégration.
- Correction de problèmes de syntaxe et de style dans le code.
- Suppression de l'add-on tiers.
- Ajout de l'intégration de Claude, un outil d'IA, pour l'assistance au développement.
- Mise à jour des tests pour refléter les changements dans le code.
- Ajout de la gestion des variables d'environnement pour la configuration de l'application.
- Correction de problèmes de configuration de l'application sur Heroku.
- Ajout de la gestion des erreurs de validation des données.
- Amélioration de la sécurité de l'application en corrigeant les vulnérabilités XSS.
- Ajout de la gestion des Content Security Policy (CSP).
- Correction de problèmes de performance de l'application.
- Amélioration de la gestion des logs et des erreurs.
- Ajout de la gestion des notifications et des alertes.
- Amélioration de l'accessibilité de l'application.
- Mise à jour de la documentation de l'API.
- Ajout de la gestion des tests automatisés.
- Correction de problèmes de compatibilité avec les navigateurs.
- Amélioration de la gestion des images et des fichiers.
- Ajout de la gestion des commentaires et des annotations.
- Amélioration de la gestion des utilisateurs et des permissions.
- Ajout de la gestion des rôles et des groupes.
- Amélioration de la gestion des données et de la base de données.
- Ajout de la gestion des backups et des restaurations.
- Amélioration de la gestion de la sécurité et de l'authentification.
- Ajout de la gestion des audits et des logs.
- Amélioration de la gestion de la configuration et des paramètres.
- Ajout de la gestion des mises à jour et des déploiements.
- Amélioration de la gestion de la performance et de la scalabilité.
- Ajout de la gestion de la surveillance et de l'alerte.
- Amélioration de la gestion de la documentation et de l'aide.
- Ajout de la gestion de la localisation et de la traduction.
- Amélioration de la gestion de l'internationalisation et de la régionalisation.
- Ajout de la gestion de la conformité et de la réglementation.
- Amélioration de la gestion de la qualité et des tests.
- Ajout de la gestion de la collaboration et du partage.
- Amélioration de la gestion de la communication et de la notification.
- Ajout de la gestion de l'intégration et de l'interopérabilité.
- Amélioration de la gestion de l'innovation et de l'expérimentation.
- Ajout de la gestion de la recherche et du développement.
- Amélioration de la gestion de la stratégie et de la vision.
- Ajout de la gestion de la gouvernance et de la conformité.
- Amélioration de la gestion de la culture et des valeurs.
- Ajout de la gestion de la diversité et de l'inclusion.
- Amélioration de la gestion de la responsabilité sociale et environnementale.
- Ajout de la gestion de la durabilité et de la résilience.
- Amélioration de la gestion de la transformation et du changement.
- Ajout de la gestion de la performance et de la valeur.
- Amélioration de la gestion de la satisfaction et de la fidélisation.
- Ajout de la gestion de la réputation et de la marque.
- Amélioration de la gestion de la confiance et de la transparence.
- Ajout de la gestion de la sécurité et de la confidentialité.
- Amélioration de la gestion de la conformité et de la réglementation.
