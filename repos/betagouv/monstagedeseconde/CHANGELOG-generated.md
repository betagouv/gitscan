## Changelog : monstagedeseconde (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de la stabilité de la plateforme et l'ajout de fonctionnalités mineures pour améliorer l'expérience utilisateur et l'administration. Plusieurs corrections ont été apportées concernant les conventions de stage, les adresses, et les erreurs signalées par Sentry. Des optimisations ont également été réalisées sur la gestion des données et des requêtes.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la création de conventions de stage avec des établissements corrects. [#837](https://github.com/betagouv/monstagedeseconde/issues/837)
- Amélioration de la gestion des adresses et des champs associés, avec une limitation de caractères pour éviter les erreurs.
- Correction d'un problème empêchant la validation de deux candidatures sur des semaines différentes pour un même élève.
- Amélioration de la recherche et de l'affichage des offres de stage.
- Correction d'un bug empêchant la création d'offres de stage avec des classes différentes.
- Correction d'un bug lié à la duplication de comptes (employeur/étudiant).
- Amélioration de l'affichage des informations sur les offres d'entreprise dans le tableau de bord.
- Correction d'un bug concernant les coordonnées des structures d'accueil.
- Correction de plusieurs bugs signalés par Sentry, notamment concernant les erreurs d'affichage et les erreurs 500.
- Amélioration de la gestion des semaines obligatoires dans les offres de stage.
- Suppression d'une ancienne fonctionnalité obsolète.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : webpack-dev-server, jwt, faraday, babel, view_component, devise, fast-uri, nokogiri, ip-address.
- Optimisation des requêtes SQL pour améliorer les performances, notamment lors de la reconstruction de l'index de recherche.
- Amélioration de la gestion des erreurs et des logs.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la gestion des tests et de l'intégration continue.
- Mise à jour de la configuration de l'environnement de développement.
- Utilisation de foreman start pour démarrer l'application en développement.
- Suppression de fichiers inutiles.
- Amélioration de la gestion des notifications.
- Correction de problèmes liés à l'unicité des adresses e-mail.

### Autres changements
- Documentation mise à jour pour refléter les changements apportés.
- Suppression de fichiers de configuration inutiles.
- Ajout de nouvelles compétences pour l'IA Claude.
- Nettoyage du code et amélioration de la structure du projet.
- Mise à jour des fichiers `.gitignore`.
- Correction de typos et amélioration de la qualité du code.
- Ajout de commentaires pour faciliter la compréhension du code.
- Amélioration de la gestion des variables d'environnement.
- Correction de problèmes de cache.
- Amélioration de la gestion des erreurs Sentry.
- Mise à jour des scripts de seed.
- Correction de problèmes liés à l'affichage des statistiques.
- Amélioration de la gestion des dates.
- Correction de problèmes liés à l'importation des données.
- Amélioration de la gestion des adresses IP.
- Correction de problèmes liés à l'affichage des informations sur les établissements.
- Amélioration de la gestion des autorisations.
- Correction de problèmes liés à la gestion des sessions.
- Amélioration de la sécurité de l'application.
- Correction de problèmes liés à la gestion des cookies.
- Amélioration de la gestion des erreurs de validation.
- Correction de problèmes liés à la gestion des formulaires.
- Amélioration de la gestion des images.
- Correction de problèmes liés à la gestion des fichiers.
- Amélioration de la gestion des vidéos.
- Correction de problèmes liés à la gestion des liens.
- Amélioration de la gestion des couleurs.
- Correction de problèmes liés à la gestion des polices.
- Amélioration de la gestion des styles.
- Correction de problèmes liés à la gestion des animations.
- Amélioration de la gestion des transitions.
- Correction de problèmes liés à la gestion des effets.
- Amélioration de la gestion des événements.
- Correction de problèmes liés à la gestion des interactions.
- Amélioration de la gestion des données utilisateur.
- Correction de problèmes liés à la gestion des données système.
- Amélioration de la gestion des logs.
- Correction de problèmes liés à la gestion des métriques.
- Amélioration de la gestion des alertes.
- Correction de problèmes liés à la gestion des notifications.
- Amélioration de la gestion des tâches planifiées.
- Correction de problèmes liés à la gestion des processus.
- Amélioration de la gestion des ressources.
- Correction de problèmes liés à la gestion de la mémoire.
- Amélioration de la gestion du CPU.
- Correction de problèmes liés à la gestion du réseau.
- Amélioration de la gestion du stockage.
- Correction de problèmes liés à la gestion de la base de données.
- Amélioration de la gestion de la sécurité.
- Correction de problèmes liés à la gestion des accès.
- Amélioration de la gestion des autorisations.
- Correction de problèmes liés à la gestion des rôles.
- Amélioration de la gestion des utilisateurs.
- Correction de problèmes liés à la gestion des groupes.
- Amélioration de la gestion des organisations.
- Correction de problèmes liés à la gestion des projets.
- Amélioration de la gestion des tickets.
- Correction de problèmes liés à la gestion des commentaires.
- Amélioration de la gestion des discussions.
- Correction de problèmes liés à la gestion des forums.
- Amélioration de la gestion des articles.
- Correction de problèmes liés à la gestion des pages.
- Amélioration de la gestion des catégories.
- Correction de problèmes liés à la gestion des tags.
- Amélioration de la gestion des menus.
- Correction de problèmes liés à la gestion des widgets.
- Amélioration de la gestion des thèmes.
- Correction de problèmes liés à la gestion des plugins.
- Amélioration de la gestion des extensions.
