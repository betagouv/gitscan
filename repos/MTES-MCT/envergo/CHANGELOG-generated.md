## Changelog : envergo (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la page de contact, la gestion des haies Natura 2000, et la correction de bugs liés à la validation et à l'affichage des données. Des optimisations de performance et des mises à jour de l'infrastructure ont également été réalisées. La FAQ a été migrée vers Gitbook.

### Évolutions fonctionnelles

*   **Page de contact :** Amélioration de l'interface utilisateur, ajout d'une barre de recherche et d'informations sur les moyens de contact.
*   **Haies Natura 2000 :**
    *   Ajout de la gestion du paramètre "concerne_aa" pour les haies Natura 2000.
    *   Amélioration de la validation de la longueur des haies.
    *   Affichage d'un message personnalisé pour la réglementation Natura 2000 dans la vue `confighaie_settings`.
*   **FAQ :** Migration de la FAQ vers Gitbook pour une meilleure accessibilité et maintenance.
*   **Affichage des résultats :** Amélioration de l'affichage des résultats de densité et ajout de détails sur les cartes.
*   **Gestion des contacts :** Amélioration de la gestion des contacts et ajout de liens vers les informations pertinentes.
*   **Analytique :** Ajout de suivi pour les informations de responsabilité sur les pages d'évaluation et de simulation.

### Évolutions techniques

*   **Optimisations de performance :**
    *   Optimisation des requêtes de densité.
    *   Réduction de la complexité de certaines opérations.
*   **Refactoring :**
    *   Simplification du code et suppression de code obsolète.
    *   Remplacement de `var` par `const` dans le code JavaScript.
    *   Amélioration de la structure du code pour une meilleure maintenabilité.
*   **Infrastructure :**
    *   Mise à jour de la configuration de déploiement pour résoudre les problèmes de mémoire.
    *   Ajout de variables d'environnement pour Sentry.
    *   Correction de problèmes liés à la gestion des erreurs et des timeouts.
*   **Tests :** Ajout et amélioration des tests unitaires et d'intégration.
*   **Migrations :** Ajout de nouvelles migrations pour la gestion des données et des configurations.
*   **Sécurité :** Correction d'une vulnérabilité XSS potentielle dans le message d'erreur de la messagerie.

### Autres changements

*   **Documentation :** Mise à jour de la documentation et ajout de commentaires.
*   **Configuration :** Ajout de nouvelles constantes de configuration pour faciliter la maintenance et la personnalisation.
*   **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
*   **Corrections de bugs :** Correction de divers bugs mineurs et amélioration de la stabilité de l'application.
*   **Mise à jour des dépendances :** (non listées individuellement)
