## Changelog : iterion (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse, la sécurité et les capacités d'observabilité d'Iterion. Des améliorations significatives ont été apportées au système de sandbox, permettant une exécution plus sécurisée et isolée des workflows. L'intégration de nouvelles fonctionnalités, comme la gestion des pièces jointes et l'amélioration du support de Claude Code, renforcent la flexibilité et les performances de la plateforme. De plus, des efforts considérables ont été déployés pour améliorer la journalisation, le débogage et la surveillance, facilitant ainsi la maintenance et l'optimisation du système.

### Évolutions fonctionnelles
- Ajout de la possibilité de charger un fichier d'environnement (`.iterion/env`) au démarrage du bureau.
- Intégration de la gestion des pièces jointes aux workflows, permettant de joindre des fichiers et des images.
- Amélioration de l'interface utilisateur du bureau avec un panneau de fichiers, un panneau de commits et une vue des logs.
- Ajout d'un bouton pour copier le log dans l'interface utilisateur.
- Implémentation d'un système de sandbox plus robuste pour une exécution plus sécurisée des workflows.
- Possibilité de lancer des exécutions de bureau à partir d'une session Claude.
- Ajout de la détection automatique des informations d'identification LLM et configuration par défaut.
- Amélioration de la gestion des erreurs et des messages d'information dans l'interface utilisateur.
- Ajout d'une fonctionnalité de "pause" et de "reprise" des exécutions, avec conservation de l'état et de l'historique.
- Ajout d'une vue "Workflow" dans la console d'exécution, offrant une représentation visuelle de l'exécution.

### Évolutions techniques
- Refactorisation du système de sandbox pour une meilleure isolation et sécurité.
- Amélioration de la gestion des erreurs et de la journalisation.
- Mise à jour des dépendances et correction de vulnérabilités de sécurité.
- Amélioration des performances du système, notamment en matière de gestion de la mémoire et de l'utilisation du CPU.
- Intégration de Prometheus et OpenTelemetry pour la surveillance et la collecte de métriques.
- Utilisation de Docker pour l'exécution des workflows dans un environnement conteneurisé.
- Amélioration de l'intégration avec Kubernetes pour le déploiement et la gestion des workflows.
- Ajout de tests unitaires, d'intégration et E2E avec Playwright pour garantir la qualité du code.
- Refactorisation de l'architecture pour une meilleure modularité et maintenabilité.
- Amélioration de la gestion des secrets et des informations d'identification.
- Implémentation d'un système de cache pour améliorer les performances.
- Ajout d'un système de gestion des versions pour faciliter le déploiement et la restauration des workflows.

### Autres changements
- Ajout d'une documentation plus complète et à jour.
- Amélioration de la configuration et de la personnalisation du système.
- Nettoyage du code et suppression du code obsolète.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de bugs mineurs et amélioration de la stabilité du système.
- Ajout d'un logo et d'un favicon pour améliorer l'identité visuelle du projet.
- Mise à jour des dépendances et correction de vulnérabilités de sécurité.
- Ajout d'un workflow CI/CD pour automatiser le processus de construction, de test et de déploiement.
- Amélioration de la gestion des fichiers de configuration.
- Ajout d'un système de gestion des logs pour faciliter le débogage et la surveillance.
- Ajout d'un système de gestion des utilisateurs et des permissions.
- Amélioration de la sécurité du système en implémentant des mesures de protection contre les attaques courantes.
- Ajout d'un système de gestion des notifications et des alertes.
- Amélioration de la performance du système en optimisant le code et en utilisant des algorithmes plus efficaces.
- Ajout d'un système de gestion des données et des schémas.
- Amélioration de l'interface utilisateur et du design.
- Ajout d'un système de collaboration et de workflow.
- Amélioration de l'intégration avec les outils d'intelligence artificielle et de NLP.
