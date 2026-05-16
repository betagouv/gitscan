## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 14 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de sécurité, notamment concernant la gestion des accès, la validation des données et la protection contre les attaques potentielles (IDOR, spoofing). Des corrections ont également été apportées pour améliorer la robustesse de la plateforme, notamment au niveau de la gestion des fichiers et des tâches asynchrones. Enfin, des améliorations ont été apportées à l'expérience utilisateur, notamment en termes de préremplissage des formulaires avec les données FranceConnect et de la gestion des groupes d'instructeurs.

### Évolutions fonctionnelles
- Amélioration du préremplissage des champs avec les données FranceConnect, notamment pour la date de naissance.
- Possibilité de préremplir la date de naissance avec FranceConnect pour les usagers et les instructeurs.
- Ajout d'un badge FranceConnect sur les champs de date de naissance préremplis.
- Amélioration de la gestion des groupes d'instructeurs, avec des restrictions d'accès plus précises.
- Ajout de limites de répétition pour les blocs répétables dans les formulaires.
- Amélioration de la gestion des pièces justificatives, notamment en termes de sécurité et de performance.
- Ajout de notifications aux administrateurs avant l'expiration des tokens API Entreprise.
- Amélioration de l'interface utilisateur pour la gestion des préférences de notification.
- Possibilité de lier des dossiers entre eux.

### Évolutions techniques
- Migration de nombreux composants HAML vers ERB pour une meilleure maintenabilité.
- Refactorisation de l'architecture de gestion des fichiers pour améliorer la performance et la sécurité.
- Amélioration de la gestion des tâches asynchrones avec Sidekiq, notamment pour les tâches de longue durée.
- Optimisation des requêtes SQL pour améliorer la performance de l'application.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité et améliorer la stabilité de la plateforme.
- Amélioration de la gestion des erreurs et des logs pour faciliter le débogage et la résolution des problèmes.
- Utilisation de Vips pour le traitement des images, améliorant ainsi la performance et la qualité.
- Amélioration de la sécurité en validant les données d'entrée et en protégeant contre les attaques potentielles (IDOR, spoofing).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la documentation pour faciliter la compréhension et l'utilisation de la plateforme.

### Autres changements
- Correction de plusieurs bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour de la documentation pour refléter les changements apportés à la plateforme.
- Nettoyage du code et suppression du code obsolète.
- Amélioration des messages d'erreur pour faciliter le diagnostic des problèmes.
- Ajout de commentaires au code pour améliorer la compréhension.
- Correction de problèmes de performance liés à la gestion des fichiers.
- Amélioration de la gestion des erreurs dans les tâches asynchrones.
- Correction de problèmes de sécurité liés à la gestion des accès.
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité.
- Amélioration de la gestion des logs pour faciliter le débogage.
- Ajout de tests unitaires pour garantir la qualité du code.
- Amélioration de la documentation pour faciliter la compréhension de la plateforme.
