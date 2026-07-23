## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 2026-07-23)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la performance, de la sécurité et de l'expérience utilisateur. Des corrections de bugs ont été apportées, notamment concernant l'affichage des informations et la gestion des pièces jointes. Des refactorings importants ont été réalisés pour préparer la plateforme à de futures évolutions, notamment en vue de l'intégration de nouvelles fonctionnalités et de l'amélioration de la gestion des données. L'accessibilité a également été améliorée.

### Évolutions fonctionnelles
*   **Gestion des pièces jointes :** Amélioration de la gestion des pièces jointes, notamment pour l'avis d'imposition avec extraction OCR.
*   **Interface utilisateur :**
    *   Amélioration de l'interface pour la gestion des dossiers, notamment avec l'ajout d'un panneau de filtre et d'une recherche.
    *   Refonte de l'affichage des informations sur les procédures.
    *   Amélioration de l'affichage des informations relatives à l'expiration des dossiers.
    *   Amélioration de l'affichage des informations sur les transferts de dossiers.
*   **Notifications :** Ajout d'une notification pour les dossiers soumis via ProConnect.
*   **Sécurité :** Renforcement de la sécurité avec l'ajout d'une validation de la présence d'un token API.
*   **API :** Ajout de la possibilité de cloner une démarche via l'API.
*   **Gestion des utilisateurs :** Possibilité pour un administrateur de réinitialiser le mot de passe d'un autre super-administrateur.
*   **Amélioration de l'accessibilité :** Amélioration de l'accessibilité pour les champs et les formulaires.

### Évolutions techniques
*   **Refactoring :**
    *   Migration de nombreux composants HAML vers ERB pour une meilleure maintenabilité.
    *   Refactorisation du code pour améliorer la performance et la lisibilité.
    *   Refactorisation de la gestion des champs et des types de champs.
*   **Performance :** Optimisation des requêtes SQL pour améliorer la performance de l'application.
*   **Tests :** Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
*   **Déploiement :** Amélioration du processus de déploiement.
*   **Dépendances :** Mise à jour des dépendances pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
*   **Infrastructure :** Amélioration de l'infrastructure pour garantir la disponibilité et la scalabilité de l'application.
*   **Oaken Seeds:** Utilisation de Oaken seeds pour les données de test, améliorant la cohérence et la reproductibilité des tests.
*   **GraphQL:** Utilisation de dataloader pour optimiser les requêtes GraphQL.
*   **S3:** Ajout d'un feature flag pour l'utilisation de S3.

### Autres changements
*   **Documentation :** Mise à jour de la documentation pour refléter les dernières modifications.
*   **i18n :** Ajout de traductions pour les nouvelles fonctionnalités.
*   **Nettoyage du code :** Suppression du code obsolète et amélioration de la qualité du code.
*   **Skylight:** Instrumentation de la liste des dossiers pour le suivi des performances avec Skylight.
*   **Suppression de fonctionnalités obsolètes:** Suppression de fonctionnalités et de code inutilisés.
*   **Amélioration des logs:** Ajout de logs plus informatifs pour faciliter le débogage.
*   **Correction de bugs mineurs:** Correction de divers bugs mineurs.
