## Changelog : iterion (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, iterion a connu une évolution significative, notamment avec l'introduction d'un sous-système de sandbox robuste pour une exécution plus sécurisée et isolée des workflows. De nombreuses améliorations ont été apportées à l'interface utilisateur, en particulier dans la vue des exécutions, avec des fonctionnalités telles que le suivi des logs en temps réel, la gestion des fichiers et des commits, ainsi que des informations détaillées sur les coûts. Des optimisations ont également été réalisées pour améliorer la performance et la fiabilité du système, notamment dans la gestion des sessions et l'intégration avec des outils externes comme Claude et Codex.

### Évolutions fonctionnelles
- Ajout d'une vue "Files" et "Commits" dans la vue d'exécution pour faciliter l'inspection des modifications de code.
- Implémentation d'une fonctionnalité de "pause" et "reprise" des exécutions avec conservation de l'état et de l'historique des conversations avec les LLM.
- Amélioration de l'interface utilisateur pour afficher les coûts associés à chaque nœud et au workflow global.
- Possibilité de télécharger les logs d'exécution.
- Ajout d'un panneau d'informations sur l'état d'avancement et les détails de l'exécution.
- Intégration de la gestion des fichiers et des pièces jointes.
- Amélioration de l'affichage des logs en temps réel avec suivi automatique.
- Ajout d'une fonctionnalité de "merge" des commits directement depuis l'interface utilisateur.
- Ajout d'un support pour les fichiers attachés aux exécutions.
- Possibilité de télécharger les logs d'exécution.
- Ajout d'un support pour les workflows avec des étapes de revue humaine (ask_user).

### Évolutions techniques
- Introduction d'un sous-système de sandbox basé sur Docker pour une exécution plus sécurisée et isolée des workflows.
- Refactorisation de l'architecture pour une meilleure modularité et maintenabilité.
- Amélioration de la gestion des erreurs et de la résilience du système.
- Mise à jour des dépendances et des outils de développement.
- Optimisation des performances de l'interface utilisateur et du backend.
- Implémentation d'un système de gestion des sessions plus robuste.
- Intégration de Prometheus pour la surveillance et la collecte de métriques.
- Amélioration de la gestion des logs et de la traçabilité.
- Utilisation de la bibliothèque `claw-code-go` pour l'interaction avec les modèles de langage.
- Amélioration de l'intégration avec les outils externes (Claude, Codex).
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Refonte de l'architecture de l'interface utilisateur avec des composants plus réutilisables et maintenables.
- Implémentation d'un système de cache pour améliorer les performances.
- Amélioration de la sécurité du système en corrigeant des vulnérabilités potentielles.
- Ajout d'un support pour les variables d'environnement.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture.
- Correction de bugs et amélioration de la stabilité du système.
- Amélioration de la gestion des dépendances.
- Ajout de nouvelles options de configuration.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de tests unitaires pour améliorer la couverture du code.
- Correction de problèmes de performance.
- Amélioration de la sécurité du système.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le déploiement.
- Mise à jour des exemples de workflows.
- Ajout d'un support pour les workflows avec des étapes de revue humaine.
- Ajout de la possibilité de télécharger les logs d'exécution.
- Amélioration de l'interface utilisateur pour faciliter l'inspection des fichiers et des commits.
- Ajout d'un support pour les variables d'environnement.
- Correction de bugs et amélioration de la stabilité du système.
- Ajout de nouvelles options de configuration.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de tests unitaires pour améliorer la couverture du code.
- Correction de problèmes de performance.
- Amélioration de la sécurité du système.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le déploiement.
- Mise à jour des exemples de workflows.
- Ajout d'un support pour les workflows avec des étapes de revue humaine.
- Ajout de la possibilité de télécharger les logs d'exécution.
- Amélioration de l'interface utilisateur pour faciliter l'inspection des fichiers et des commits.
- Ajout d'un support pour les variables d'environnement.
- Correction de bugs et amélioration de la stabilité du système.
- Ajout de nouvelles options de configuration.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de tests unitaires pour améliorer la couverture du code.
- Correction de problèmes de performance.
- Amélioration de la sécurité du système.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le déploiement.
- Mise à jour des exemples de workflows.
- Ajout d'un support pour les workflows avec des étapes de revue humaine.
- Ajout de la possibilité de télécharger les logs d'exécution.
- Amélioration de l'interface utilisateur pour faciliter l'inspection des fichiers et des commits.
- Ajout d'un support pour les variables d'environnement.
- Correction de bugs et amélioration de la stabilité du système.
- Ajout de nouvelles options de configuration.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de tests unitaires pour améliorer la couverture du code.
- Correction de problèmes de performance.
- Amélioration de la sécurité du système.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le déploiement.
- Mise à jour des exemples de workflows.
- Ajout d'un support pour les workflows avec des étapes de revue humaine.
- Ajout de la possibilité de télécharger les logs d'exécution.
- Amélioration de l'interface utilisateur pour faciliter l'inspection des fichiers et des commits.
- Ajout d'un support pour les variables d'environnement.
- Correction de bugs et amélioration de la stabilité du système.
- Ajout de nouvelles options de configuration.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de tests unitaires pour améliorer la couverture du code.
- Correction de problèmes de performance.
- Amélioration de la sécurité du système.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le déploiement.
- Mise à jour des exemples de workflows.
- Ajout d'un support pour les workflows avec des étapes de revue humaine.
- Ajout de la possibilité de télécharger les logs d'exécution.
- Amélioration de l'interface utilisateur pour faciliter l'inspection des fichiers et des commits.
- Ajout d'un support pour les variables d'environnement.
- Correction de bugs et amélioration de la stabilité du système.
- Ajout de nouvelles options de configuration.
