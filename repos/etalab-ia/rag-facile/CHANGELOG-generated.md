## Changelog : rag-facile (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par une amélioration significative du projet, avec l'ajout de nouvelles fonctionnalités comme un système d'expansion de requêtes pour améliorer la pertinence des résultats, une meilleure intégration avec l'API Albert, et une refonte de l'architecture pour faciliter la distribution et l'utilisation du projet. De plus, de nombreuses corrections de bugs et améliorations de la documentation ont été apportées.

### Évolutions fonctionnelles
*   Ajout d'un système d'expansion de requêtes avec stratégies multi-requêtes et HyDE pour améliorer la pertinence des résultats de recherche.
*   Amélioration de l'intégration avec l'API Albert, notamment en gérant mieux les erreurs et en fournissant des informations de débogage plus claires.
*   Possibilité d'utiliser des collections publiques Albert comme sources de données pour le RAG.
*   Ajout d'un nouveau mode "standalone" pour une installation et une utilisation simplifiées du projet.
*   Ajout de la prise en charge de l'upload de fichiers PDF pour le contexte.
*   Ajout d'une interface utilisateur pour afficher les fichiers attachés dans l'application de chat.
*   Ajout de commandes CLI pour la gestion de la configuration du RAG.
*   Ajout d'un nouveau CLI `rag-facile` avec une bannière et une commande version.
*   Ajout d'une fonctionnalité pour télécharger des jeux de données avec des filtres par tâche et par langue.

### Évolutions techniques
*   Refonte de l'architecture du projet pour une meilleure modularité et maintenabilité.
*   Extraction de packages pour l'ingestion, le contexte, le reranking et la configuration.
*   Utilisation de Moon pour la génération de templates de projets.
*   Intégration de `just` pour la gestion des tâches de développement.
*   Amélioration du système de configuration avec un fichier `ragfacile.toml`.
*   Mise à jour des dépendances (pypdf, cryptography, protobuf).
*   Ajout de tests unitaires et d'intégration.
*   Amélioration de la gestion des erreurs et des logs.
*   Utilisation de release-please pour la gestion des versions et la génération du changelog.
*   Ajout de workflows CI/CD pour l'automatisation des tests et du déploiement.
*   Correction de problèmes de compatibilité avec Python 3.13.
*   Ajout de support pour Windows.

### Autres changements
*   Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture.
*   Ajout d'un guide pour les contributeurs.
*   Correction de problèmes de style et de formatage du code.
*   Ajout de commentaires et de docstrings pour améliorer la lisibilité du code.
*   Amélioration de la gestion des erreurs et des exceptions.
*   Ajout d'un fichier `.env.example` pour la configuration des variables d'environnement.
*   Ajout d'un fichier `.gitignore` pour ignorer les fichiers inutiles.
*   Ajout d'un fichier `CONTRIBUTING.md` pour guider les contributeurs.
*   Ajout d'un fichier `AGENTS.md` avec des informations sur le projet.
*   Correction de problèmes de typage avec `ty`.
*   Suppression de fichiers et de dépendances inutiles.
*   Amélioration des messages d'erreur et des logs.
*   Correction de bugs mineurs et amélioration de la stabilité du projet.
