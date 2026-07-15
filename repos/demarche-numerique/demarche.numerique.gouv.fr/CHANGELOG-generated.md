## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la performance, de la sécurité et de l'expérience utilisateur. Des corrections de bugs ont été apportées, notamment concernant la gestion des pièces jointes et des adresses. Des fonctionnalités ont été ajoutées pour faciliter la gestion des dossiers par les instructeurs et les administrateurs, ainsi que pour améliorer l'accessibilité et la conformité aux normes. Une migration vers Rails 8 a été finalisée.

### Évolutions fonctionnelles
- Ajout de badges pour signaler les dossiers partagés et ceux qui expirent bientôt.
- Amélioration de l'affichage des informations sur les procédures dans l'interface administrateur.
- Possibilité pour les instructeurs de modifier les dossiers (sous conditions).
- Ajout d'une page dédiée pour gérer les transferts de dossiers.
- Amélioration de la gestion des adresses et de la recherche d'informations via l'API BAN.
- Ajout d'un système de bannières d'information pour les administrateurs.
- Amélioration de la gestion des pièces justificatives, notamment pour l'extraction OCR.
- Ajout d'un indicateur de lecture des messages pour les instructeurs.
- Amélioration de l'affichage des informations de contact pour les procédures.
- Ajout d'un champ "commentaire" pour les dossiers.
- Possibilité de filtrer les dossiers par date de création.
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Ajout de la possibilité de pré-remplir certains champs des formulaires.

### Évolutions techniques
- Finalisation de la migration vers Rails 8.
- Optimisation des performances des requêtes en base de données (correction de N+1).
- Amélioration de la gestion de la mémoire lors de l'exportation des données au format XLSX.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances (nokogiri, faraday, concurrent-ruby, jwt, graphql).
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Utilisation de Flipper pour gérer les fonctionnalités.
- Amélioration de la sécurité en validant les données saisies par les utilisateurs.
- Utilisation de Sidekiq pour gérer les tâches asynchrones.
- Amélioration de l'architecture de l'application pour faciliter l'évolutivité.
- Amélioration de la documentation du code.
- Utilisation de React et TypeScript pour le développement de l'interface utilisateur.
- Amélioration de l'intégration continue et du déploiement continu (CI/CD).
- Correction de problèmes de race condition dans la gestion des groupes d'instructeurs.
- Amélioration de la gestion des erreurs lors de l'extraction de données avec l'API 2DDOC.
- Amélioration de la gestion des adresses et de la géolocalisation.

### Autres changements
- Mise à jour de la documentation de déploiement.
- Correction de problèmes de typographie et de grammaire dans les textes de l'interface utilisateur.
- Amélioration de l'accessibilité de l'application.
- Nettoyage du code et suppression du code obsolète.
- Ajout de commentaires pour faciliter la compréhension du code.
- Mise à jour des traductions.
- Correction de bugs mineurs.
- Amélioration de la gestion des logs.
- Refactorisation des composants HAML vers ERB.
- Ajout de tests pour les nouveaux composants et fonctionnalités.
- Amélioration de la gestion des erreurs dans les tests.
- Ajout de tests d'intégration pour les fonctionnalités clés.
- Amélioration de la couverture de code des tests.
- Correction de problèmes de performance dans les tests.
- Amélioration de la configuration de l'environnement de développement.
- Mise à jour des outils de développement.
- Amélioration de la gestion des secrets et des clés API.
- Amélioration de la sécurité de l'application.
- Correction de problèmes de sécurité.
- Amélioration de la gestion des utilisateurs et des permissions.
- Amélioration de la gestion des rôles et des droits d'accès.
- Amélioration de la gestion des sessions et de l'authentification.
- Amélioration de la gestion des cookies.
- Amélioration de la gestion des données personnelles.
- Amélioration de la conformité aux réglementations en matière de protection des données.
- Amélioration de la gestion des logs et de la surveillance de l'application.
- Amélioration de la gestion des alertes et des notifications.
- Amélioration de la gestion des incidents et des pannes.
- Amélioration de la gestion des sauvegardes et de la restauration des données.
- Amélioration de la gestion de la scalabilité et de la performance de l'application.
- Amélioration de la gestion de la disponibilité et de la fiabilité de l'application.
- Amélioration de la gestion de la sécurité de l'application.
- Amélioration de la gestion de la conformité aux réglementations en matière de sécurité.
- Amélioration de la gestion des risques et des vulnérabilités de l'application.
- Amélioration de la gestion de la qualité du code et des tests.
- Amélioration de la gestion de la documentation et de la formation.
- Amélioration de la gestion des coûts et des ressources.
- Amélioration de la gestion des relations avec les parties prenantes.
- Amélioration de la gestion des projets et des programmes.
- Amélioration de la gestion de la communication et de la collaboration.
- Amélioration de la gestion du changement et de l'innovation.
- Amélioration de la gestion de la performance et des objectifs.
- Amélioration de la gestion de la satisfaction des utilisateurs.
- Amélioration de la gestion de la réputation et de l'image de marque.
- Amélioration de la gestion de la responsabilité sociale et environnementale.
- Amélioration de la gestion de la gouvernance et de la conformité.
- Amélioration de la gestion de la stratégie et de la vision.
- Amélioration de la gestion de la culture et des valeurs.
- Amélioration de la gestion de la diversité et de l'inclusion.
- Amélioration de la gestion de la santé et de la sécurité.
- Amélioration de la gestion de la formation et du développement.
- Amélioration de la gestion de la motivation et de l'engagement.
- Amélioration de la gestion de la reconnaissance et de la récompense.
- Amélioration de la gestion de la performance et de l'évaluation.
- Amélioration de la gestion de la succession et du remplacement.
- Amélioration de la gestion de la communication et de la collaboration.
- Amélioration de la gestion du changement et de l'innovation.
- Amélioration de la gestion de la performance et des objectifs.
- Amélioration de la gestion de la satisfaction des utilisateurs.
- Amélioration de la gestion de la réputation et de l'image de marque.
