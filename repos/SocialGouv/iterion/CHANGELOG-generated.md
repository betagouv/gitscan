## Changelog : iterion (30 derniers jours, au 2026-06-20)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur dans l'interface studio, avec un accent particulier sur la gestion des tâches, l'intégration avec des outils externes (Forge, GitHub), et l'amélioration de la robustesse et de la performance du système. Des efforts importants ont également été déployés pour améliorer la sécurité, notamment en matière d'authentification et de gestion des secrets. L'ajout de fonctionnalités comme le support de l'authentification OAuth pour Forge et GitHub, ainsi que l'amélioration de la gestion des erreurs et des alertes, contribuent à rendre iterion plus fiable et plus facile à utiliser.

### Évolutions fonctionnelles

*   **Intégrations Forge :** Ajout de la prise en charge de Forge (GitLab, Forgejo, GitHub) avec création automatique d'applications GitHub, gestion des identifiants et connexion aux dépôts.
*   **Interface Studio :**
    *   Amélioration de l'interface utilisateur pour la gestion des bots, avec des badges d'état et des informations plus claires.
    *   Ajout d'une vue "What's Next" pour faciliter la gestion des tâches et des propositions.
    *   Amélioration de la gestion des fichiers et des différences dans l'éditeur.
    *   Ajout d'un éditeur de métadonnées de bot et d'un gestionnaire de catalogue.
    *   Amélioration de la navigation et de la réactivité de l'interface.
    *   Possibilité de lancer des bots directement depuis la page d'accueil.
*   **Gestion des secrets :** Introduction d'un système de gestion des secrets plus robuste avec support de clés BYOK (Bring Your Own Key) et chiffrement.
*   **Alertes et notifications :** Ajout d'alertes pour les runs bloqués et intégration de webhooks pour les notifications.
*   **Amélioration de la gestion des runs :** Possibilité de finaliser et de commiter les changements d'un run, affichage des informations de coût et de temps d'exécution.
*   **Fonctionnalités CLI :** Ajout de la commande `iterion schedule` pour automatiser l'exécution des bots.
*   **Support de Claude Opus 4.8 et Ultracode.**

### Évolutions techniques

*   **Refactoring et optimisation :** Refactoring important du code pour améliorer la lisibilité, la maintenabilité et la performance.
*   **Amélioration de la sécurité :**
    *   Correction de plusieurs vulnérabilités de sécurité identifiées par des audits.
    *   Implémentation de l'authentification HMAC pour les webhooks.
    *   Amélioration de la gestion des autorisations et des accès.
*   **Gestion des dépendances :** Mise à jour des dépendances et correction de problèmes liés à la gestion des versions.
*   **Amélioration de la robustesse :**
    *   Gestion améliorée des erreurs et des exceptions.
    *   Implémentation de mécanismes de reprise après erreur.
    *   Amélioration de la gestion des ressources.
*   **Infrastructure :** Amélioration de l'infrastructure de build et de déploiement.
*   **Tests :** Ajout de nouveaux tests unitaires et d'intégration pour améliorer la couverture et la qualité du code.
*   **Docker :** Amélioration de l'image Docker, ajout d'outils de développement et de sécurité.
*   **Sandbox :** Amélioration de la sécurité et de la configuration du sandbox.
*   **Observabilité :** Ajout de métriques et de logs pour faciliter le monitoring et le débogage.
*   **Architecture :** Amélioration de l'architecture pour une meilleure scalabilité et flexibilité.

### Autres changements

*   **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés au code.
*   **Nettoyage du code :** Suppression de code obsolète et amélioration de la qualité du code.
*   **Corrections de bugs :** Correction de nombreux bugs et problèmes mineurs.
*   **Amélioration des messages d'erreur et des logs.**
*   **Refonte de l'organisation des fichiers et des répertoires.**
*   **Amélioration des performances des requêtes et des API.**
*   **Ajout de commentaires et de documentation au code.**
*   **Mise à jour des outils de développement et des bibliothèques.**
*   **Correction de problèmes de compatibilité avec différentes versions de Go.**
*   **Amélioration de la gestion des configurations.**
*   **Ajout de nouvelles variables d'environnement.**
*   **Correction de problèmes d'affichage dans l'interface utilisateur.**
*   **Amélioration de la gestion des sessions utilisateur.**
*   **Correction de problèmes de sécurité liés aux injections SQL.**
*   **Amélioration de la gestion des erreurs de réseau.**
*   **Correction de problèmes de performance liés aux requêtes de base de données.**
*   **Ajout de nouvelles fonctionnalités de débogage.**
*   **Amélioration de la gestion des logs.**
*   **Correction de problèmes de compatibilité avec différents navigateurs.**
*   **Ajout de nouvelles fonctionnalités d'accessibilité.**
*   **Amélioration de la gestion des autorisations.**
*   **Correction de problèmes de sécurité liés aux attaques XSS.**
*   **Amélioration de la gestion des erreurs de validation.**
*   **Ajout de nouvelles fonctionnalités de monitoring.**
*   **Correction de problèmes de performance liés à l'utilisation de la mémoire.**
*   **Amélioration de la gestion des erreurs de configuration.**
*   **Ajout de nouvelles fonctionnalités de reporting.**
*   **Correction de problèmes de sécurité liés aux attaques CSRF.**
*   **Amélioration de la gestion des erreurs de communication.**
*   **Ajout de nouvelles fonctionnalités de gestion des utilisateurs.**
*   **Correction de problèmes de performance liés à l'utilisation du CPU.**
*   **Amélioration de la gestion des erreurs de fichier.**
*   **Ajout de nouvelles fonctionnalités de gestion des rôles.**
*   **Correction de problèmes de sécurité liés aux attaques de type man-in-the-middle.**
*   **Amélioration de la gestion des erreurs de réseau.**
*   **Ajout de nouvelles fonctionnalités de gestion des groupes.**
*   **Correction de problèmes de performance liés à l'utilisation du disque.**
*   **Amélioration de la gestion des erreurs de base de données.**
*   **Ajout de nouvelles fonctionnalités de gestion des permissions.**
*   **Correction de problèmes de sécurité liés aux attaques de type brute force.**
*   **Amélioration de la gestion des erreurs de session.**
*   **Ajout de nouvelles fonctionnalités de gestion des audits.**
*   **Correction de problèmes de performance liés à l'utilisation de la bande passante.**
*   **Amélioration de la gestion des erreurs de cache.**
*   **Ajout de nouvelles fonctionnalités de gestion des logs.**
*   **Correction de problèmes de sécurité liés aux attaques de type phishing.**
*   **Amélioration de la gestion des erreurs de configuration.**
*   **Ajout de nouvelles fonctionnalités de gestion des notifications.**
*   **Correction de problèmes de performance liés à l'utilisation de la mémoire.**
*   **Amélioration de la gestion des erreurs de communication.**
*   **Ajout de nouvelles fonctionnalités de gestion des workflows.**
*   **Correction de problèmes de sécurité liés aux attaques de type SQL injection.**
*   **Amélioration de la gestion des erreurs de validation.**
*   **Ajout de nouvelles fonctionnalités de gestion des tâches.**
*   **Correction de problèmes de performance liés à l'utilisation du CPU.**
*   **Amélioration de la gestion des erreurs de fichier.**
*   **Ajout de nouvelles fonctionnalités de gestion des projets.**
*   **Correction de problèmes de sécurité liés aux attaques de type XSS.**
