## Changelog : iterion (30 derniers jours, au 2026-06-28)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, de la robustesse et de l'expérience utilisateur. Des fonctionnalités clés ont été ajoutées, notamment l'intégration de secrets, l'amélioration de la gestion des erreurs, et de nouvelles capacités pour les bots et les workflows. L'interface utilisateur a également été améliorée avec de nouvelles fonctionnalités et corrections de bugs. L'accent a été mis sur la préparation du projet pour un déploiement cloud plus stable et sécurisé.

### Évolutions fonctionnelles
*   **Authentification et Sécurité :** Ajout de la gestion des secrets avec des fonctionnalités de chiffrement et de rotation des clés. Implémentation de l'authentification à deux facteurs et de la gestion des accès basée sur les rôles.
*   **Intégrations :** Ajout de la prise en charge de GitHub Apps, GitLab et Forgejo pour l'intégration avec des dépôts de code.
*   **Bots :**
    *   Ajout de nouveaux bots pour l'analyse de sécurité du code (sec-audit-source).
    *   Amélioration des bots existants, notamment Revi pour la revue de code et Nexie pour l'assistance aux utilisateurs.
    *   Possibilité de définir des bots personnalisés avec des métadonnées et des workflows spécifiques.
*   **Interface Utilisateur :**
    *   Amélioration de l'interface utilisateur pour la gestion des runs et des logs.
    *   Ajout d'une vue pour la gestion des secrets.
    *   Amélioration de la navigation et de la recherche.
*   **Workflows :**
    *   Ajout de la possibilité de planifier des runs de bots avec un cron.
    *   Amélioration de la gestion des erreurs et des retries dans les workflows.
    *   Ajout de la possibilité de définir des dépendances entre les runs de bots.
*   **Fonctionnalités diverses :**
    *   Ajout d'un système d'alerte pour les runs qui échouent.
    *   Amélioration de la documentation et des exemples.
    *   Ajout de la possibilité de suivre l'utilisation des ressources (temps CPU, mémoire, etc.).

### Évolutions techniques
*   **Architecture :**
    *   Refactorisation de plusieurs composants pour améliorer la maintenabilité et la testabilité du code.
    *   Amélioration de la gestion des erreurs et des exceptions.
    *   Optimisation des performances de certains composants.
*   **Infrastructure :**
    *   Mise à jour des dépendances vers les dernières versions.
    *   Amélioration de la configuration et du déploiement.
    *   Ajout de tests d'intégration et de bout en bout.
*   **Sécurité :**
    *   Correction de plusieurs vulnérabilités de sécurité.
    *   Implémentation de mesures de sécurité supplémentaires pour protéger les données sensibles.
*   **Outils :**
    *   Ajout de nouveaux outils pour le développement et le test.
    *   Amélioration des outils existants.
*   **Divers :**
    *   Amélioration de la couverture de test.
    *   Correction de bugs et amélioration de la stabilité.
    *   Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    *   Utilisation de nouvelles bibliothèques et frameworks pour améliorer les performances et la sécurité.

### Autres changements
*   **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés au code.
*   **Configuration :** Ajout de nouvelles options de configuration pour personnaliser le comportement du projet.
*   **Nettoyage de code :** Suppression du code mort et des commentaires inutiles.
*   **Tests :** Ajout de nouveaux tests unitaires et d'intégration pour améliorer la couverture de test.
*   **Chore:** Mise à jour des dépendances et des outils de développement.
*   **CI/CD:** Amélioration du pipeline CI/CD pour automatiser le processus de construction, de test et de déploiement.
*   **Corrections de bugs:** Correction de nombreux bugs mineurs et amélioration de la stabilité du projet.
