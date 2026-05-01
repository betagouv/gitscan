## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 30 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives en matière de sécurité, notamment la correction de vulnérabilités potentielles liées à l'injection de code, au contournement d'authentification et à la divulgation d'informations sensibles. De nombreuses optimisations ont également été apportées à la plateforme, notamment au niveau du traitement des images, des performances des requêtes et de la gestion des fichiers. Des améliorations fonctionnelles ont été implémentées pour faciliter l'administration et la configuration des démarches, ainsi que pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une notification aux administrateurs avant l'expiration des tokens d'API Entreprise.
- Amélioration de la gestion des pièces justificatives, notamment en autorisant les fichiers `.md` et `.xlsm`.
- Possibilité pour les administrateurs de personnaliser la présentation des dossiers pour les instructeurs.
- Amélioration de l'interface utilisateur pour la gestion des champs et des référentiels.
- Ajout d'un indicateur visuel pour les dossiers liés qui ont été supprimés ou sont expirés.
- Amélioration de la gestion des erreurs et des messages d'information pour les utilisateurs.
- Possibilité de lier un dossier existant lors de la création d'une nouvelle demande.
- Amélioration de la gestion des champs de date de naissance dans l'interface d'administration.

### Évolutions techniques
- Refactorisation importante du code lié au traitement des images, avec l'utilisation de Vips pour optimiser les performances.
- Amélioration de la sécurité en corrigeant des vulnérabilités potentielles liées à l'injection de code SQL, à la manipulation de l'URL et au contournement de l'authentification.
- Optimisation des requêtes SQL pour améliorer les performances de la plateforme.
- Migration de composants HAML vers ERB pour une meilleure maintenabilité.
- Amélioration de la gestion des erreurs et des exceptions.
- Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performances.
- Amélioration de la gestion des tâches asynchrones avec Sidekiq.
- Ajout d'instrumentation pour le suivi des performances de l'API GraphQL.
- Amélioration de la gestion des cookies et des sessions.
- Correction de problèmes de concurrence lors de la gestion des pièces justificatives.
- Amélioration de la gestion des URLs et des redirections.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les modifications apportées à la plateforme.
- Corrections de bugs mineurs et améliorations de l'expérience utilisateur.
- Nettoyage du code et suppression de code obsolète.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la configuration de l'environnement de développement et de production.
- Mise à jour des outils de développement et des bibliothèques utilisées.
- Correction de problèmes de compatibilité avec certaines versions de Ruby et de Rails.
- Amélioration de la gestion des logs et du monitoring.
- Correction de problèmes de performance liés à la recherche et à la pagination.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de problèmes de typographie et de grammaire dans les messages d'erreur et les textes de l'interface utilisateur.
