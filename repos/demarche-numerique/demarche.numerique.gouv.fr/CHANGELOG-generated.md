## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 26 avril 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment concernant la gestion des URL et la prévention d'attaques potentielles. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant la gestion des pièces justificatives, les liens entre les dossiers et les notifications. Des optimisations de performance et des refactorings ont été réalisés pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- Amélioration de la gestion des pièces justificatives : ajout de la prise en charge du format Markdown (.md) et des fichiers .xlsm.
- Gestion des dossiers liés :
    - Affichage de l'état d'un dossier lié (supprimé, expiré) pour les utilisateurs et les instructeurs.
    - Possibilité de lier un dossier en cours de traitement (brouillon) à un dossier existant.
    - Affichage des informations sur les dossiers liés dans l'interface utilisateur.
- Amélioration de la gestion des erreurs et des notifications :
    - Correction d'un problème d'affichage des erreurs lors du téléchargement de fichiers.
    - Amélioration des messages d'erreur pour une meilleure clarté.
- Amélioration de l'interface utilisateur :
    - Correction de l'affichage du menu de navigation pour les préférences de notification.
    - Amélioration de l'accessibilité de certains composants.
- Ajout de la possibilité de personnaliser la présentation des procédures par les administrateurs.
- Ajout d'une option pour activer la saisie de la date de naissance.

### Évolutions techniques
- **Sécurité :**
    - Correction de vulnérabilités potentielles liées à la manipulation des URL et à l'injection de code.
    - Amélioration de la validation des données pour prévenir les attaques par cross-site scripting (XSS).
    - Renforcement de la sécurité de l'authentification FranceConnect.
- **Architecture et Refactoring :**
    - Refactorisation de plusieurs composants pour améliorer la lisibilité et la maintenabilité du code.
    - Migration de composants HAML vers ERB.
    - Simplification de la logique de certains contrôleurs et services.
    - Utilisation de nouvelles bibliothèques et frameworks pour améliorer les performances et la sécurité.
- **Performance :**
    - Optimisation des requêtes SQL pour améliorer les temps de réponse.
    - Amélioration de la gestion de la mémoire pour réduire la consommation de ressources.
    - Mise en cache de certaines données pour réduire la charge sur la base de données.
- **Infrastructure :**
    - Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performances.
    - Amélioration du processus de déploiement pour réduire les temps d'arrêt.
- Utilisation de WeasyPrint pour la génération d'attestations de dépôt en PDF.
- Amélioration de la gestion des erreurs et des logs.

### Autres changements
- Documentation mise à jour pour refléter les dernières modifications.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Ajout de tests unitaires et d'intégration pour garantir la stabilité du code.
- Mise à jour des outils de développement et de l'environnement de test.
- Ajout de la clé publique pour les paquets debian.
- Suppression de fonctionnalités obsolètes.
- Amélioration de la gestion des variables d'environnement.
- Correction de problèmes de compatibilité avec certaines versions de logiciels.
- Ajout de nouvelles métriques de surveillance pour suivre les performances de l'application.
- Suppression de code mort.
- Amélioration de la gestion des emails.
- Ajout de tests pour la gestion des pièces justificatives.
- Amélioration de la gestion des logs.
- Correction de problèmes d'affichage.
- Amélioration de la gestion des erreurs.
- Ajout de nouvelles fonctionnalités pour les administrateurs.
- Correction de bugs mineurs.
- Amélioration de la documentation.
- Mise à jour des dépendances.
- Amélioration de la sécurité.
- Amélioration de la performance.
- Amélioration de la maintenabilité du code.
- Ajout de nouvelles métriques de surveillance.
- Suppression de code mort.
- Amélioration de la gestion des emails.
- Ajout de tests pour la gestion des pièces justificatives.
- Amélioration de la gestion des logs.
- Correction de problèmes d'affichage.
- Amélioration de la gestion des erreurs.
- Ajout de nouvelles fonctionnalités pour les administrateurs.
- Correction de bugs mineurs.
- Amélioration de la documentation.
- Mise à jour des dépendances.
- Amélioration de la sécurité.
- Amélioration de la performance.
- Amélioration de la maintenabilité du code.
- Ajout de nouvelles métriques de surveillance.
- Suppression de code mort.
- Amélioration de la gestion des emails.
- Ajout de tests pour la gestion des pièces justificatives.
- Amélioration de la gestion des logs.
- Correction de problèmes d'affichage.
- Amélioration de la gestion des erreurs.
- Ajout de nouvelles fonctionnalités pour les administrateurs.
- Correction de bugs mineurs.
- Amélioration de la documentation.
- Mise à jour des dépendances.
- Amélioration de la sécurité.
- Amélioration de la performance.
- Amélioration de la maintenabilité du code.
- Ajout de nouvelles métriques de surveillance.
- Suppression de code mort.
- Amélioration de la gestion des emails.
- Ajout de tests pour la gestion des pièces justificatives.
- Amélioration de la gestion des logs.
- Correction de problèmes d'affichage.
- Amélioration de la gestion des erreurs.
- Ajout de nouvelles fonctionnalités pour les administrateurs.
- Correction de bugs mineurs.
