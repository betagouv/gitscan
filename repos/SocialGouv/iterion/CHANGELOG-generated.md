## Changelog : iterion (30 derniers jours, au 2026-06-28)

### Résumé
Ce mois-ci, iterion a connu une évolution significative, axée sur l'amélioration de la gestion des organisations, l'intégration de fonctionnalités de sécurité, l'optimisation de l'expérience utilisateur dans l'interface studio, et l'ajout de nouvelles capacités pour l'automatisation et l'orchestration des workflows.  Des améliorations importantes ont été apportées à l'authentification, à la gestion des équipes, et à la surveillance des performances.

### Évolutions fonctionnelles
*   **Gestion des organisations :** Ajout de la suppression d'organisations super-administrateur et de la gestion des entrées de navigation.
*   **Authentification :** Implémentation de l'authentification SSO (Single Sign-On) avec prise en charge de domaines spécifiques à l'organisation.
*   **Interface utilisateur (Studio) :**
    *   Amélioration de la navigation avec un sélecteur d'organisation dédié.
    *   Refonte de la page des paramètres d'organisation et des équipes.
    *   Ajout d'un éditeur de métadonnées pour les bots.
    *   Amélioration de l'accessibilité et de l'ergonomie générale.
    *   Ajout d'un éditeur de fichiers dans le worktree en cours d'exécution.
*   **Intégrations :**
    *   Prise en charge de l'intégration avec GitHub Apps pour une authentification simplifiée.
    *   Ajout de la prise en charge de Forgejo et GitLab pour les webhooks.
*   **Workflows :**
    *   Ajout de la possibilité de planifier des bots avec un cron.
    *   Amélioration de la gestion des webhooks pour déclencher des actions.
*   **Sécurité :**
    *   Implémentation de contrôles de sécurité pour empêcher les injections de code.
    *   Amélioration de la gestion des secrets avec un nouveau système de stockage et de résolution.
    *   Ajout d'un scanner de sécurité pour détecter les vulnérabilités dans les dépendances.
*   **Bots :**
    *   Ajout de nouveaux bots, dont Revi pour les revues de code et Bmady pour l'agilité.
    *   Amélioration des bots existants, notamment pour la gestion des erreurs et la performance.

### Évolutions techniques
*   **Architecture :**
    *   Refonte de l'architecture de l'authentification et de la gestion des organisations.
    *   Amélioration de la gestion des erreurs et de la journalisation.
    *   Optimisation des performances du serveur et de l'interface utilisateur.
*   **Infrastructure :**
    *   Mise à jour des dépendances et des outils de développement.
    *   Amélioration de la configuration et du déploiement.
*   **CI/CD :**
    *   Amélioration du pipeline CI/CD pour automatiser les tests et le déploiement.
    *   Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
*   **Refactoring :**
    *   Nombreux refactorings pour améliorer la lisibilité, la maintenabilité et la testabilité du code.
    *   Simplification de l'architecture et réduction de la complexité.
*   **Sandbox :**
    *   Amélioration de la sécurité et de l'isolation des sandboxes.
    *   Ajout de la prise en charge de volumes persistants pour les sandboxes.
*   **Divers :**
    *   Utilisation de Docker pour la construction et le déploiement des images.
    *   Utilisation de Kubernetes pour l'orchestration des conteneurs.

### Autres changements
*   **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés.
*   **Configuration :** Ajout de nouvelles options de configuration pour personnaliser le comportement d'iterion.
*   **Nettoyage de code :** Suppression de code obsolète et amélioration de la qualité du code.
*   **Tests :** Ajout de nouveaux tests pour améliorer la couverture et la fiabilité du code.
*   **Divers :** Corrections de bugs mineurs et améliorations de l'expérience utilisateur.
*   **Amélioration des logs et de la surveillance.**
*   **Ajout de métriques de performance.**
*   **Correction de plusieurs vulnérabilités de sécurité.**
*   **Amélioration de la gestion des erreurs et de la robustesse du système.**
*   **Refonte de l'interface utilisateur pour une meilleure expérience utilisateur.**
*   **Ajout de nouvelles fonctionnalités pour l'automatisation et l'orchestration des workflows.**
*   **Amélioration de la gestion des secrets et de la sécurité des données.**
*   **Optimisation des performances et de la scalabilité du système.**
*   **Ajout de nouvelles intégrations avec d'autres outils et services.**
*   **Amélioration de la documentation et de la facilité d'utilisation.**
*   **Correction de bugs et amélioration de la stabilité du système.**
