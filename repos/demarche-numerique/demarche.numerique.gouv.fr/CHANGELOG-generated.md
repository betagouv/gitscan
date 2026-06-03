## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 2 juin 2026)

### Résumé
Cette période a été marquée par des améliorations de sécurité, notamment concernant l'authentification multi-facteurs (OTP) pour les super-admins et la gestion des liens utilisateurs. Des optimisations de performance ont été apportées, notamment au niveau des requêtes GraphQL et de l'indexation des données. Plusieurs corrections de bugs et des refactorings ont également été réalisés pour améliorer la stabilité et la maintenabilité de la plateforme. Enfin, des améliorations ont été apportées à l'expérience utilisateur, notamment au niveau des formulaires et des notifications.

### Évolutions fonctionnelles
- Ajout de la possibilité de restreindre l'édition OCR instructeur aux champs RIB.
- Amélioration de la gestion des répétitions dans les champs de formulaire, avec ajout d'options de limites minimales et maximales configurables en administration.
- Correction d'un problème d'affichage des messages d'erreur pour les champs FranceConnect.
- Amélioration de l'expérience utilisateur pour les administrateurs avec des messages plus clairs et des options de configuration plus intuitives.
- Correction d'un bug empêchant la restauration correcte des procédures et des dossiers associés.
- Ajout de la possibilité de filtrer les champs par adresse (commune, département, région).
- Amélioration de l'affichage des informations sur les avis.
- Ajout de la possibilité de restreindre l'accès aux dossiers aux utilisateurs ayant un rôle spécifique.
- Correction d'un problème d'affichage des notifications.

### Évolutions techniques
- Migration de plusieurs tâches de fond vers Sidekiq avec gestion des retries natives pour une meilleure fiabilité.
- Refactorisation du code pour améliorer la performance des requêtes GraphQL.
- Optimisation des requêtes de recherche de dossiers.
- Amélioration de la gestion des erreurs et des exceptions.
- Mise à jour de plusieurs dépendances.
- Refactorisation de composants HAML vers ERB pour une meilleure maintenabilité.
- Amélioration de la sécurité en corrigeant des vulnérabilités potentielles liées à l'authentification et à l'accès aux données.
- Ajout de tests unitaires et d'intégration pour améliorer la qualité du code.
- Amélioration de la gestion des cookies et des sessions.
- Ajout de la gestion des erreurs de scan antivirus pour les pièces jointes.
- Amélioration de la gestion des données géographiques (communes, départements, régions).
- Amélioration de la gestion des logs et du monitoring.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de configuration.
- Nettoyage du code.
- Amélioration de la couverture de code des tests.
- Correction de bugs mineurs.
- Mise à jour des fichiers de configuration.
- Amélioration de la gestion des traductions.
- Correction de problèmes de compatibilité avec différentes versions de navigateurs.
- Ajout de nouvelles métriques de monitoring.
- Amélioration de la gestion des secrets et des clés API.
