## Changelog : iterion (30 derniers jours, au 2026-07-05)

### Résumé
Ce mois-ci, iterion a connu des améliorations significatives en termes de gestion des secrets, d'intégration de l'écosystème de développement (Forge, GitHub), d'expérience utilisateur dans l'interface studio, et de robustesse générale du système. Des efforts importants ont été consacrés à l'amélioration de la sécurité, notamment avec l'introduction de nouvelles fonctionnalités de gestion des secrets et d'audit de sécurité. L'interface utilisateur a été modernisée et rendue plus intuitive, et des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité.

### Évolutions fonctionnelles
*   **Gestion des secrets:** Introduction d'une gestion des secrets locale scellée pour l'environnement de bureau/CLI, améliorant la sécurité et la gestion des informations sensibles.
*   **Intégration Forge:** Amélioration de l'intégration avec GitHub et Forgejo, incluant la gestion des applications OAuth, la connexion aux dépôts et la possibilité de créer des applications GitHub directement depuis l'interface.
*   **Interface Studio:**
    *   Refonte de l'interface utilisateur avec de nouveaux composants (boutons, champs de formulaire, etc.) pour une expérience plus cohérente et moderne.
    *   Amélioration de la navigation et de l'organisation des menus.
    *   Ajout d'un éditeur de métadonnées pour les bots, permettant de gérer plus facilement les informations associées à chaque bot.
    *   Affichage amélioré des journaux de run et des informations de débogage.
    *   Possibilité de filtrer et de trier les runs par bot et par dépôt.
*   **Webhooks:** Ajout de la prise en charge des webhooks pour déclencher des actions en réponse à des événements sur les plateformes Forge (GitHub, GitLab, Forgejo).
*   **Board:** Amélioration du tableau de bord avec la possibilité de créer des vues personnalisées et de regrouper les tâches par différents critères.
*   **Amélioration de l'exécution des bots:** Possibilité de configurer des budgets et des limites de temps pour l'exécution des bots.
*   **Nouvelles fonctionnalités de débogage:** Ajout d'outils de débogage pour faciliter l'identification et la résolution des problèmes.
*   **Amélioration de la sécurité:** Ajout de mesures de sécurité pour protéger contre les attaques potentielles, telles que l'injection de code et les vulnérabilités de sécurité.

### Évolutions techniques
*   **Refactoring:** Refactorisation importante du code pour améliorer la lisibilité, la maintenabilité et la performance.
*   **Amélioration de la gestion des erreurs:** Amélioration de la gestion des erreurs pour fournir des messages d'erreur plus informatifs et faciliter le débogage.
*   **Optimisation des performances:** Optimisation des performances pour réduire la consommation de ressources et améliorer la réactivité de l'application.
*   **Mise à jour des dépendances:** Mise à jour des dépendances pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
*   **Infrastructure:** Amélioration de l'infrastructure pour améliorer la scalabilité et la fiabilité de l'application.
*   **Tests:** Ajout de nouveaux tests unitaires et d'intégration pour améliorer la couverture des tests et garantir la qualité du code.
*   **Sécurité:**
    *   Implémentation d'un système de gestion des secrets plus robuste.
    *   Amélioration de la sécurité des webhooks.
    *   Correction de plusieurs vulnérabilités de sécurité.
*   **Architecture:**
    *   Refonte de l'architecture de certains composants pour améliorer la modularité et la flexibilité.
    *   Utilisation de nouvelles technologies et de nouveaux frameworks pour améliorer la performance et la scalabilité.
*   **CI/CD:** Amélioration du pipeline CI/CD pour automatiser le processus de construction, de test et de déploiement.

### Autres changements
*   **Documentation:** Mise à jour de la documentation pour refléter les dernières modifications et améliorations.
*   **Configuration:** Ajout de nouvelles options de configuration pour personnaliser le comportement de l'application.
*   **Nettoyage du code:** Nettoyage du code pour supprimer le code obsolète et améliorer la lisibilité.
*   **Corrections de bugs:** Correction de nombreux bugs pour améliorer la stabilité et la fiabilité de l'application.
*   **Amélioration des logs:** Amélioration des logs pour faciliter le débogage et le suivi des événements.
*   **Ajout de nouvelles métriques:** Ajout de nouvelles métriques pour surveiller les performances et l'utilisation de l'application.
*   **Amélioration de l'accessibilité:** Amélioration de l'accessibilité de l'application pour les utilisateurs handicapés.

[#49](https://github.com/SocialGouv/iterion/issues/49)
[#64](https://github.com/SocialGouv/iterion/issues/64)
[#78](https://github.com/SocialGouv/iterion/issues/78)
