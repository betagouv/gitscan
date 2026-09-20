## Changelog : Muffin (30 derniers jours, au 20 septembre 2026)

### Résumé
Muffin a franchi une étape majeure en passant d'un outil de recherche à une plateforme de gestion de connaissances complète. Les évolutions récentes se concentrent sur la mesure de la qualité des réponses de l'IA (via un nouveau tableau de bord), l'ajout de capacités de recherche sur le web, et une gestion beaucoup plus fine des collections de documents. L'interface utilisateur a également été profondément modernisée pour offrir une expérience plus fluide et interactive.

### Évolutions fonctionnelles

**Expérience de Chat & Agent**
- **Recherche Web :** Intégration d'un outil de recherche sur internet via SearXNG, activable directement depuis l'interface.
- **Transparence de l'IA :** Affichage détaillé de l'exécution de l'agent étape par étape et distinction visuelle des types de sources dans le panneau latéral.
- **Gestion des sources :** Amélioration de la présentation des citations et des documents sources (cartes dédiées, modales de détails avec résumé et QA).
- **Interactivité :** Ajout d'animations de type "streaming" pour les titres de conversation et possibilité de fixer (pin) des collections spécifiques à une recherche.
- **Feedback utilisateur :** Mise en place d'un système de notation des réponses permettant de collecter et de persister les retours utilisateurs.

**Gestion des Connaissances & Qualité**
- **Tableau de bord Qualité :** Nouveau centre de pilotage pour suivre les métriques de performance de l'IA (coût, latence, longueur des discussions, etc.).
- **Gestion des Collections :** Contrôle accru sur les collections (visibilité publique/privée, partage sécurisé par hash, et paramètres de traitement personnalisés).
- **Gestion Documentaire :** Interface complète pour l'importation, la suppression et la réindexation des documents avec prévisualisation détaillée.
- **Suivi des tâches :** Refonte de la page de gestion des tâches avec un tableau dépliable et paginé.

### Évolutions techniques

**Architecture & Intelligence Artificielle**
- **Moteur de recherche :** Migration de Qdrant vers Meilisearch pour optimiser la recherche hybride.
- **Nouveaux Workers :** Introduction de workers Celery dédiés pour le traitement des documents et l'évaluation automatique de la qualité.
- **Agent de recherche :** Implémentation de LangGraph pour orchestrer les flux de l'agent et ajout d'un outil de contexte temporel pour l'IA ([#56](https://github.com/IA-Generative/Muffin/issues/56)).
- **Évaluation automatisée :** Développement d'un système de scoring pour évaluer la pertinence des discussions et la qualité de la récupération d'informations (retrieval).

**Infrastructure & Sécurité**
- **Authentification :** Intégration de Keycloak pour la gestion des accès et de la sécurité.
- **Déploiement :** Mise à jour des charts Helm (rebranding en "muffin") et ajout de SearXNG comme dépendance.
- **Fiabilité :** Ajout de mécanismes de `HEALTHCHECK` dans les Dockerfiles et amélioration des pipelines CI/CD pour les releases.

### Autres changements
- **Documentation :** Réécriture complète du README principal, création de documentations par service et documentation exhaustive de toutes les variables d'environnement.
- **Nettoyage :** Refactorisation du code frontend (linting, TypeScript) et correction de messages d'erreur pour éviter l'affichage de détails techniques bruts aux utilisateurs.
