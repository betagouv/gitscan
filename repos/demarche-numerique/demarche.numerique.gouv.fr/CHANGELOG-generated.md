## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 22 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de performance, notamment au niveau des requêtes en base de données et de l'adaptation de l'API Entreprise. De nombreuses migrations de composants Haml vers ERB ont été réalisées. Des corrections de sécurité ont également été implémentées, ainsi que des améliorations de l'expérience utilisateur, notamment concernant la gestion des pièces justificatives et des champs FranceConnect.

### Évolutions fonctionnelles
- Ajout d'un bouton ProConnect sur la page de connexion pour les professionnels.
- Amélioration de l'affichage des informations sur les procédures dans l'interface d'administration.
- Amélioration de la gestion des pièces justificatives, avec des indications plus claires sur les fichiers acceptés.
- Amélioration de la gestion des champs FranceConnect, notamment pour le préremplissage des données.
- Ajout d'une fonctionnalité permettant de restaurer des dossiers archivés.
- Amélioration de la recherche de dossiers dans l'interface d'administration.
- Ajout d'une bannière d'information dans l'interface d'administration concernant le tableau des champs.
- Possibilité de restreindre l'accès à certaines fonctionnalités aux administrateurs ayant une authentification multi-facteurs (MFA) activée.
- Amélioration de la gestion des erreurs et des messages d'information pour les utilisateurs.

### Évolutions techniques
- Migration de nombreux composants Haml vers ERB pour améliorer la maintenabilité et la performance.
- Optimisation des requêtes en base de données pour améliorer les performances, notamment au niveau des procédures et des avis.
- Adaptation de l'API Entreprise à la version 4, avec extraction des données d'unité légale.
- Refactorisation du code pour améliorer la lisibilité et la modularité.
- Mise en place de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Utilisation de Sidekiq pour la gestion des tâches asynchrones, notamment pour les traitements longs.
- Amélioration de la sécurité, notamment en corrigeant des vulnérabilités potentielles.
- Mise à jour des dépendances.
- Amélioration de la gestion des cookies pour l'export.
- Utilisation de memoization pour optimiser les performances de l'API Geo.
- Migration des jobs longs vers Sidekiq avec retry natif.

### Autres changements
- Ajout de traductions en anglais pour certains composants.
- Amélioration de la documentation.
- Correction de bugs mineurs.
- Nettoyage du code.
- Mise à jour des fichiers de configuration.
- Amélioration des tests.
- Ajout d'instrumentation pour le suivi des performances.
- Correction de problèmes de performance liés à la gestion des fichiers.
- Correction de problèmes de sécurité liés à la gestion des données utilisateur.
- Correction de problèmes d'affichage dans l'interface utilisateur.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Amélioration de l'accessibilité de l'application.
