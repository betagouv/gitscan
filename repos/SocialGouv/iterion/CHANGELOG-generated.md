## Changelog : iterion (30 derniers jours, au 2026-07-30)

### Résumé
Ce mois-ci, iterion a connu des améliorations significatives en termes de fonctionnalités, de stabilité et d'expérience utilisateur. Les efforts se sont concentrés sur l'amélioration de l'interface studio, l'ajout de nouvelles capacités aux bots (notamment en matière de gestion des dépendances et de sécurité), et l'optimisation des performances et de la fiabilité de la plateforme. Des améliorations ont également été apportées à la gestion des plugins et à l'intégration avec des outils externes.

### Évolutions fonctionnelles
- **Plugins:** Ajout d'une interface pour installer des plugins depuis l'UI, avec filtrage par type. Possibilité de configurer les plugins via une interface dédiée.
- **Studio:** Amélioration significative de l'interface utilisateur avec une navigation regroupée, des états plus clairs, et une meilleure harmonisation visuelle.
- **Bots:**
    - Ajout de la gestion des dépendances avec `supply-shield` pour la sécurité des dépendances.
    - Possibilité de définir des topologies de revue (mono/dual) pour les bots.
    - Ajout de la possibilité de lancer des bots avec des configurations spécifiques (modèle, backend) par nœud.
    - Prise en charge de l'exécution de bots imbriqués (subbots).
- **Intégrations:** Amélioration de l'intégration avec GitHub Apps, notamment pour la gestion des permissions.
- **API:** Ajout d'une API pour supprimer des runs.
- **Logs:** Amélioration de l'affichage des logs, avec la possibilité d'afficher les entrées et sorties des outils.
- **Webhooks:** Amélioration de la gestion des webhooks, notamment pour la création automatique de PRs.

### Évolutions techniques
- **Architecture:** Refactorisation importante du code, notamment pour la gestion des événements et des logs.
- **Performance:** Optimisation des performances de l'interface utilisateur et des requêtes API.
- **Sécurité:** Amélioration de la sécurité de la plateforme, notamment en matière de gestion des permissions et de protection contre les attaques.
- **Infrastructure:** Mise à jour des dépendances et amélioration de la configuration de l'infrastructure.
- **Tests:** Ajout de nouveaux tests unitaires et d'intégration pour améliorer la couverture et la fiabilité du code.
- **CI/CD:** Amélioration du pipeline CI/CD pour automatiser les tests et le déploiement.
- **Runtime:** Amélioration de la gestion des ressources et de la scalabilité du runtime.
- **DSL:** Ajout de nouvelles fonctionnalités au DSL pour la définition des workflows.
- **Observabilité:** Amélioration de la surveillance et de la journalisation de la plateforme.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés à la plateforme.
- Correction de nombreux bugs et améliorations de la stabilité.
- Amélioration de la gestion des erreurs et des messages d'erreur.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de nouvelles métriques pour surveiller les performances de la plateforme.
- Amélioration de la gestion des secrets.
- Correction de problèmes de sécurité.
- Amélioration de la gestion des dépendances.
- Ajout de nouvelles fonctionnalités pour la gestion des utilisateurs et des permissions.
- Amélioration de la gestion des workflows.
- Ajout de nouvelles fonctionnalités pour l'intelligence artificielle et le NLP.
- Amélioration de la surveillance et de la journalisation.
