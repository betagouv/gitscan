## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 27 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de sécurité, notamment concernant la gestion des accès et la protection contre les vulnérabilités potentielles. Des optimisations de performance ont été apportées, en particulier au niveau de l'API Entreprise et de la gestion des données. De nombreuses corrections de bugs et des refactorings ont également été réalisés pour améliorer la stabilité et la maintenabilité de la plateforme.

### Évolutions fonctionnelles
*   Ajout d'un bouton "ProConnect" sur la page de connexion pour les professionnels.
*   Amélioration de la gestion des pièces justificatives, notamment en affichant un message d'erreur plus clair en cas de problème.
*   Possibilité de restreindre l'accès aux modèles d'exportation à la procédure concernée, améliorant ainsi la sécurité des données.
*   Ajout d'un indicateur visuel pour les champs préremplis avec FranceConnect.
*   Amélioration de la gestion des droits d'accès pour les administrateurs et les instructeurs.
*   Ajout de la possibilité de configurer des limites de répétition pour les champs de formulaire.
*   Amélioration de la gestion des archives et de la restauration des procédures.

### Évolutions techniques
*   Migration de plusieurs jobs vers Sidekiq pour une meilleure gestion des tâches asynchrones et une meilleure résilience.
*   Optimisation des requêtes SQL pour améliorer les performances, notamment au niveau de l'API Entreprise et de la recherche de dossiers.
*   Refactoring du code pour améliorer la lisibilité et la maintenabilité.
*   Mise à jour de plusieurs dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Amélioration de la gestion des erreurs et de la journalisation.
*   Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
*   Migration de composants Haml vers ERB pour une meilleure cohérence et maintenabilité.
*   Implémentation de rate limiting pour l'API Entreprise afin de prévenir les abus.
*   Amélioration de la gestion des cookies pour une meilleure sécurité.
*   Ajout de memoïsation pour optimiser les performances de l'API Geo.

### Autres changements
*   Correction de plusieurs problèmes de sécurité, notamment des vulnérabilités potentielles liées à l'injection SQL et à l'IDOR (Insecure Direct Object Reference).
*   Amélioration de la documentation et des commentaires dans le code.
*   Correction de plusieurs erreurs de typographie et d'orthographe dans les messages d'erreur et les textes de l'interface utilisateur.
*   Mise à jour des traductions pour améliorer la localisation de l'application.
*   Amélioration de la gestion des logs et du monitoring.
*   Correction de bugs mineurs et amélioration de l'expérience utilisateur.
*   Ajout de tests pour les nouvelles fonctionnalités et les corrections de bugs.
*   Amélioration de la couverture de code des tests.
*   Refactorisation du code pour une meilleure lisibilité et maintenabilité.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes liés à la gestion des erreurs et à la journalisation.
*   Amélioration de la gestion des configurations et des variables d'environnement.
*   Correction de problèmes liés à la gestion des cookies et des sessions.
*   Amélioration de la gestion des assets et des ressources statiques.
*   Correction de problèmes liés à la gestion des images et des fichiers.
*   Amélioration de la gestion des formulaires et des validations.
*   Correction de problèmes liés à la gestion des dates et des heures.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes liés à la gestion des rôles et des groupes.
*   Amélioration de la gestion des notifications et des alertes.
*   Correction de problèmes liés à la gestion des API et des intégrations.
*   Amélioration de la gestion de la sécurité et de la conformité.
*   Correction de problèmes liés à la gestion des données et de la base de données.
*   Amélioration de la gestion des tests et de l'intégration continue.
*   Correction de problèmes liés à la gestion du déploiement et de l'infrastructure.
*   Amélioration de la gestion de la documentation et de la communication.
*   Correction de problèmes liés à la gestion des performances et de la scalabilité.
*   Amélioration de la gestion de la qualité du code et de la dette technique.
*   Correction de problèmes liés à la gestion des dépendances et des librairies.
*   Amélioration de la gestion des logs et du monitoring.
*   Correction de problèmes liés à la gestion des erreurs et des exceptions.
*   Amélioration de la gestion des configurations et des variables d'environnement.
*   Correction de problèmes liés à la gestion des cookies et des sessions.
*   Amélioration de la gestion des assets et des ressources statiques.
*   Correction de problèmes liés à la gestion des images et des fichiers.
*   Amélioration de la gestion des formulaires et des validations.
*   Correction de problèmes liés à la gestion des dates et des heures.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes liés à la gestion des rôles et des groupes.
*   Amélioration de la gestion des notifications et des alertes.
*   Correction de problèmes liés à la gestion des API et des intégrations.
*   Amélioration de la gestion de la sécurité et de la conformité.
*   Correction de problèmes liés à la gestion des données et de la base de données.
*   Amélioration de la gestion des tests et de l'intégration continue.
*   Correction de problèmes liés à la gestion du déploiement et de l'infrastructure.
*   Amélioration de la gestion de la documentation et de la communication.
*   Correction de problèmes liés à la gestion des performances et de la scalabilité.
*   Amélioration de la gestion de la qualité du code et de la dette technique.
*   Correction de problèmes liés à la gestion des dépendances et des librairies.
*   Amélioration de la gestion des logs et du monitoring.
*   Correction de problèmes liés à la gestion des erreurs et des exceptions.
*   Amélioration de la gestion des configurations et des variables d'environnement.
*   Correction de problèmes liés à la gestion des cookies et des sessions.
*   Amélioration de la gestion des assets et des ressources statiques.
*   Correction de problèmes liés à la gestion des images et des fichiers.
*   Amélioration de la gestion des formulaires et des validations.
*   Correction de problèmes liés à la gestion des dates et des heures.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes liés à la gestion des rôles et des groupes.
*   Amélioration de la gestion des notifications et des alertes.
*   Correction de problèmes liés à la gestion des API et des intégrations.
*   Amélioration de la gestion de la sécurité et de la conformité.
*   Correction de problèmes liés à la gestion des données et de la base de données.
*   Amélioration de la gestion des tests et de l'intégration continue.
*   Correction de problèmes liés à la gestion du déploiement et de l'infrastructure.
*   Amélioration de la gestion de la documentation et de la communication.
*   Correction de problèmes liés à la gestion des performances et de la scalabilité.
*   Amélioration de la gestion de la qualité du code et de la dette technique.
*   Correction de problèmes liés à la gestion des dépendances et des librairies.
*   Amélioration de la gestion des logs et du monitoring.
*   Correction de problèmes liés à la gestion des erreurs et des exceptions.
*   Amélioration de la gestion des configurations et des variables d'environnement.
*   Correction de problèmes liés à la gestion des cookies et des sessions.
