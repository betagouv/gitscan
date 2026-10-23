## Changelog : mycollections (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois a été marqué par une évolution majeure du projet avec l'introduction des **Assistants de recherche**, permettant de créer, tester et piloter des agents intelligents. L'expérience utilisateur a été profondément modernisée avec une nouvelle interface (accueil compact, catalogue amélioré) et l'ajout d'un réseau d'entraide entre utilisateurs. Parallèlement, la robustesse technique a été renforcée par une meilleure gestion de l'indexation et une sécurité accrue.

### Évolutions fonctionnelles
- **Nouveaux Assistants de recherche** :
    - Mise en place d'un assistant de création complet (wizard en 5 étapes) pour configurer les sources et les consignes.
    - Introduction d'un mode "bac à sable" pour tester les réponses et visualiser le raisonnement de l'assistant.
    - Ajout de fonctionnalités de pilotage : archivage, restauration et évaluation de la qualité/fiabilité des réponses.
- **Réseau d'entraide** : Nouveau système permettant de publier des appels, de proposer des solutions et de répondre aux besoins de la communauté.
- **Refonte de l'interface utilisateur** :
    - Nouvel accueil compact et menu optimisé.
    - Catalogue de collections amélioré avec tri par satisfaction/fraîcheur et gestion des avis utilisateurs.
    - Fiches de collections et d'assistants enrichies (onglets historique, consignes, qualité et accès).
    - Amélioration de l'ergonomie mobile et intégration renforcée du Design System (DSFR).
- **Amélioration de la recherche** : Affichage de titres plus lisibles pour les sections et gestion plus précise des résultats (bornes basses).

### Évolutions techniques
- **Architecture et Intelligence Artificielle** :
    - Implémentation d'un serveur **MCP (Model Context Protocol)** pour exposer les outils des assistants.
    - Refactorisation du backend vers des modèles de données plus robustes (Pydantic) pour la gestion des questions et de la qualité.
- **Sécurité et Accès** :
    - Correction de plusieurs vulnérabilités critiques (certifi, pillow, nginx).
    - Renforcement du contrôle d'accès via des liens signés et une gestion des droits basée sur des groupes administrateurs configurables.
    - Mise à jour de la gestion du SSO et de la configuration frontend.
- **Fiabilité et Infrastructure** :
    - Optimisation de l'indexation : reprise automatique après redémarrage et prévention des doublons.
    - Modernisation de la gestion des dépendances backend avec `uv`.
    - Mise en place de nouveaux workflows de déploiement (ArgoCD, Helm charts) et renforcement de la CI/CD.
    - Extension de la couverture de tests (E2E, unitaires frontend et backend).

### Autres changements
- **Documentation** : Mise à jour majeure de la documentation technique (ADR, AGENTS.md, README) et des guides d'utilisation.
- **Qualité du code** : Intégration de contrôles de qualité automatisés (linting, type-checking) pour le frontend et le backend.
