## Changelog : questions-ecrites (30 derniers jours, au 21/08/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante dans l'amélioration de la qualité des données extraites du Journal Officiel (JO). Les efforts se sont concentrés sur la modernisation de l'intelligence artificielle (passage au modèle Albert) et sur une extraction beaucoup plus précise des questions et de leur contexte. Parallèlement, une refonte majeure de la base de données a été effectuée pour stabiliser l'architecture et faciliter les évolutions futures.

### Évolutions fonctionnelles
- **Précision de l'extraction** : Amélioration significative de la capacité du système à isoler la question réelle et son contexte textuel au sein des documents du JO.
- **Fiabilité de l'attribution** : Optimisation de l'attribution des questions aux bureaux grâce à l'intégration de nouveaux algorithmes et une meilleure gestion des workflows.

### Évolutions techniques
- **Intelligence Artificielle & NLP** :
    - Migration des embeddings vers le modèle **Albert** pour améliorer la recherche sémantique.
    - Amélioration de la robustesse du processus d'embedding face aux refus des garde-fous (guardrails).
    - Ajout d'une fonction sigmoïde stable pour les calculs mathématiques.
- **Base de données** :
    - Refonte complète de l'historique des migrations via un "squash" d'Alembic pour simplifier la gestion du schéma.
    - Création de nouvelles vues SQL pour la gestion des attributions et des allotissements du JO.
    - Ajout de colonnes de cache et d'analyse (ex: `direction_algo_id`, colonnes d'analyse de questions) pour optimiser les performances.
- **Ingestion & Analyse** :
    - Amélioration du parsing des textes du JO (gestion des phrases uniques, élargissement des patterns de détection de questions).
    - Optimisation de la déduplication des réponses et amélioration de l'ingestion des données historiques de l'Assemblée Nationale.
    - Passage au streaming pour l'extraction des questions depuis PostgreSQL afin de réduire l'empreinte mémoire.
- **Infrastructure & CI/CD** :
    - Mise en conformité pour Kubernetes (gestion des UID/GID numériques).
    - Renforcement de la qualité du code avec l'intégration de tests de type (**mypy**) et de sécurité (**bandit**) dans la CI.
    - Mise à jour des pipelines de déploiement et des tâches planifiées (cronjobs).

### Autres changements
- **Nettoyage** : Suppression de la fonctionnalité `office-attribution` et de plusieurs scripts d'ingestion obsolètes.
- **Documentation** : Mise à jour de la documentation technique suite aux changements de schémas de base de données et aux nouvelles méthodes d'extraction.
