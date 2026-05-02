## Changelog : iterion (30 derniers jours, au 01 mai 2026)

### Résumé
Ce mois-ci, iterion a connu une évolution significative, axée sur l'amélioration de l'expérience utilisateur dans l'éditeur, le renforcement de l'intégration avec les modèles de langage (LLM) via une nouvelle approche SDK, et l'optimisation de la fiabilité et de la performance du moteur de workflow. Des efforts importants ont été consacrés à l'ajout de fonctionnalités de débogage, de test et de couverture, ainsi qu'à la correction de bugs et à l'amélioration de la documentation.

### Évolutions fonctionnelles
- Amélioration significative de l'éditeur :
    - Ajout d'une palette de nœuds avec glisser-déposer pour faciliter la création de workflows.
    - Ajout d'une vue de bibliothèque pour les modèles et primitives préconfigurés.
    - Amélioration du routage des arêtes et de la navigation dans les nœuds.
    - Ajout d'un panneau latéral pour l'édition des nœuds et une vue détaillée des sous-nœuds.
    - Ajout d'un support pour les icônes des LLM.
- Intégration améliorée avec les LLM :
    - Nouvelle approche basée sur un SDK pour l'intégration avec Claude Code et Codex.
    - Prise en charge de la persistance de la conversation avec `ask_user` pour une meilleure expérience utilisateur.
    - Amélioration de la gestion des coûts et de la consommation de ressources pour les LLM.
- Amélioration de la gestion des workflows :
    - Ajout de la possibilité de reprendre l'exécution d'un workflow à partir d'un point d'interruption.
    - Ajout de la gestion des erreurs et des reprises pour les workflows.
    - Ajout de la possibilité de définir des règles de validation et de filtrage pour les workflows.
- Ajout d'un système de revue et de correction itératif avec des workflows dédiés.
- Ajout d'un outil de simplification pour améliorer la lisibilité des workflows.

### Évolutions techniques
- Refactorisation importante de l'architecture du projet :
    - Migration vers le framework Cobra pour la CLI.
    - Remplacement de la structure monolithique des nœuds par une interface polymorphe.
    - Séparation claire des responsabilités entre les différents composants.
- Amélioration de la couverture des tests :
    - Ajout de tests unitaires, de tests d'intégration et de tests de fuzzing.
    - Ajout de tests de couverture pour les workflows et les outils.
    - Ajout de tests en direct pour valider le comportement du système dans des conditions réelles.
- Optimisation des performances :
    - Amélioration de la gestion de la mémoire et de la consommation de CPU.
    - Optimisation des requêtes à la base de données.
    - Mise en cache des données fréquemment utilisées.
- Amélioration de la sécurité :
    - Correction de failles de sécurité potentielles.
    - Renforcement des mesures de protection contre les attaques.
- Mise à jour des dépendances :
    - Synchronisation avec les dernières versions des bibliothèques tierces.
- Amélioration de la journalisation et de la surveillance.
- Utilisation de `pnpm` pour la gestion des dépendances frontend.
- Refonte de la gestion des erreurs et des exceptions.
- Amélioration de la gestion de la configuration et des variables d'environnement.

### Autres changements
- Documentation mise à jour et traduite en anglais.
- Nettoyage du code et suppression du code mort.
- Amélioration de la structure du projet et de l'organisation des fichiers.
- Ajout de commentaires et de documentation au code.
- Correction de bugs mineurs et amélioration de la stabilité du système.
- Ajout de nouvelles fonctionnalités de débogage et de diagnostic.
- Ajout de nouveaux exemples et de tutoriels.
- Suppression de configurations obsolètes.
- Amélioration de la gestion des logs.
- Ajout de tests de performance et de benchmarks.
- Refonte de l'intégration continue et du déploiement continu (CI/CD).
- Ajout de support pour les variables d'environnement.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de nouvelles métriques et de tableaux de bord de surveillance.
- Amélioration de la sécurité et de la conformité.
- Ajout de support pour l'authentification et l'autorisation.
- Amélioration de la gestion des utilisateurs et des permissions.
- Ajout de support pour les notifications et les alertes.
- Amélioration de la gestion des données et des schémas.
- Amélioration de l'administration et du backoffice.
- Amélioration de l'interface utilisateur et du design.
- Amélioration du suivi et de la traçabilité.
- Ajout de support pour l'intelligence artificielle et le NLP.
- Ajout de support pour les données et l'open data.
- Ajout de support pour les API et les intégrations.
- Ajout de support pour la sécurité et la conformité.
