## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 07 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, des optimisations de performance, et des évolutions fonctionnelles concernant la gestion des pièces justificatives, des procédures et des utilisateurs. Des corrections de bugs et des refactorings importants ont également été réalisés pour améliorer la stabilité et la maintenabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de la gestion des pièces justificatives avec l'ajout de la prise en charge du format `.md` et `.xlsm`.
- Possibilité pour les administrateurs de personnaliser les tableaux de dossiers pour les instructeurs.
- Ajout de filtres "Authentification FranceConnect" pour les instructeurs.
- Amélioration de l'affichage des informations de lien de dossier (état supprimé, expiration).
- Amélioration de la gestion des erreurs d'upload avec des messages plus clairs et accessibles.
- Ajout d'une notification aux administrateurs avant l'expiration des tokens API Entreprise.
- Amélioration de la gestion des pièces justificatives avec la possibilité de lier des dossiers existants.
- Amélioration de la gestion des utilisateurs et de leurs droits.

### Évolutions techniques
- Migration de nombreux jobs vers Sidekiq pour une meilleure gestion des tâches asynchrones et une meilleure résilience.
- Optimisation des requêtes GraphQL pour améliorer les performances.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de plusieurs dépendances.
- Amélioration de la sécurité en corrigeant des vulnérabilités potentielles (injection, IDOR, CSRF).
- Utilisation de Vips pour le traitement des images, améliorant les performances et la robustesse.
- Migration de composants Haml vers ERB.
- Amélioration de la gestion des erreurs et des logs.
- Amélioration de la gestion des caches.
- Ajout d'instrumentation pour le suivi des performances.
- Amélioration de la gestion des tests.
- Remplacement de l'authentification SAML.

### Autres changements
- Documentation mise à jour.
- Corrections de bugs mineurs.
- Amélioration de la qualité du code.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des messages de traduction.
- Nettoyage du code et suppression de code obsolète.
- Amélioration de la configuration de l'environnement de développement.
- Ajout de vérifications de sécurité supplémentaires.
- Correction de problèmes de performance.
- Amélioration de l'expérience utilisateur.
- Correction de problèmes d'accessibilité.
- Ajout de tests pour les nouvelles fonctionnalités.
- Mise à jour des dépendances.
- Amélioration de la documentation.
- Correction de bugs mineurs.
- Amélioration de la qualité du code.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des messages de traduction.
- Nettoyage du code et suppression de code obsolète.
- Amélioration de la configuration de l'environnement de développement.
- Ajout de vérifications de sécurité supplémentaires.
- Correction de problèmes de performance.
- Amélioration de l'expérience utilisateur.
- Correction de problèmes d'accessibilité.
- Ajout de tests pour les nouvelles fonctionnalités.
