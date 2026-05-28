## Changelog : monstagedeseconde (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la robustesse de la plateforme, notamment en corrigeant des erreurs et en améliorant la gestion des erreurs Sygne. Des améliorations ont également été apportées à la gestion des autorisations, à la validation des candidatures et à l'expérience utilisateur globale, avec l'ajout d'un chatbot Crisp et des corrections de textes. Plusieurs mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un chatbot Crisp pour l'assistance utilisateur.
- Amélioration de la validation des candidatures pour permettre à un élève de seconde de valider deux stages simultanément [#836](https://github.com/betagouv/monstagedeseconde/issues/836).
- Correction de l'affichage du message de validation de candidature pour les élèves de seconde [#819](https://github.com/betagouv/monstagedeseconde/issues/819).
- Amélioration de la gestion des offres d'entreprises, notamment pour l'affichage dans le tableau de bord des employeurs.
- Correction de l'affichage des statistiques pour les maisons d'accueil [#848](https://github.com/betagouv/monstagedeseconde/issues/848).
- Correction de l'affichage des informations relatives à la ville du SIRET dans Sentry [#845](https://github.com/betagouv/monstagedeseconde/issues/845).
- Amélioration de la gestion des autorisations pour les statisticiens [#874](https://github.com/betagouv/monstagedeseconde/issues/874).
- Correction de l'affichage des semaines dans la comparaison des offres [#1643](https://github.com/betagouv/monstagedeseconde/issues/1643).
- Amélioration de la validation de l'adresse et de la géolocalisation des entreprises [#817](https://github.com/betagouv/monstagedeseconde/issues/817).
- Ajout du préfixe téléphonique de la Guadeloupe [#859](https://github.com/betagouv/monstagedeseconde/issues/859).

### Évolutions techniques
- Mise à jour de Ruby à la version 3.4.9 [#884](https://github.com/betagouv/monstagedeseconde/issues/884).
- Amélioration de la gestion des erreurs Sygne avec la création d'une classe `SygneApiError` pour documenter les différents cas d'échec et l'ajout de mécanismes de retry [#888](https://github.com/betagouv/monstagedeseconde/issues/888).
- Refactorisation du modèle `InternshipApplication` pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la gestion des autorisations avec l'utilisation de CanCanCan.
- Correction de plusieurs tests et suppression de tests obsolètes.
- Mise à jour de plusieurs dépendances (webpack-dev-server, nokogiri, devise, babel, ip-address, etc.).
- Amélioration de la gestion des jobs asynchrones pour éviter les interruptions.
- Correction de problèmes de cache avec Sentry.
- Amélioration de la sécurité en corrigeant des potentielles failles XSS [#860](https://github.com/betagouv/monstagedeseconde/issues/860), [#869](https://github.com/betagouv/monstagedeseconde/issues/869).

### Autres changements
- Correction de typos et amélioration de la formulation de certains textes.
- Nettoyage du code et suppression de fichiers inutiles.
- Mise à jour de la documentation.
- Correction de problèmes liés à la configuration de l'environnement de développement.
- Suppression de code obsolète.
- Correction de problèmes liés à l'intégration continue.
