## Changelog : mycollections (30 derniers jours, au 15 novembre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'expérience utilisateur, notamment avec l'introduction complète des "Assistants de recherche" (désormais "Chat MirAI") et une intégration profondément renforcée avec la source de données Résana. Le projet est passé d'une gestion de collections à un véritable écosystème où l'on peut créer, tester et publier des assistants intelligents, tout en bénéficiant d'un processus d'importation de documents beaucoup plus robuste et transparent.

### Évolutions fonctionnelles
- **Assistants de recherche (Chat MirAI) :** 
    - Mise en place d'un assistant de création complet en 5 étapes avec un nouveau gabarit de formulaire [#83](https://github.com/IA-Generative/mycollections/pull/83).
    - Introduction d'un "bac à sable" (sandbox) pour tester les réponses des assistants et visualiser le raisonnement de recherche.
    - Possibilité d'exporter et d'importer la configuration des assistants via des fichiers YAML [#194](https://github.com/IA-Generative/mycollections/pull/194).
    - Rebranding de l'interface "Mon assistant" vers "Chat MirAI".
- **Intégration Résana :**
    - Nouveau parcours de connexion permettant de reprendre automatiquement un import interrompu.
    - Gestion optimisée des grands volumes (jusqu'à 20 000 documents par dossier) et création d'espaces de travail dédiés.
    - Meilleure visibilité sur la qualité des documents : signalement des scans (OCR), des tableurs tronqués ou des formats non pris en charge.
- **Gestion des collections et catalogue :**
    - Nouveau catalogue permettant de trier les collections, de consulter les avis des utilisateurs et de voir la fraîcheur des données.
    - Identification automatique des sites d'origine des documents pour plus de traçabilité.
- **Partage et collaboration :**
    - Amélioration du partage de collections via une barre de recherche pour sélectionner les groupes cibles.
    - Introduction d'un réseau d'entraide pour recommander des appels ou des ressources existantes.

### Évolutions techniques
- **Protocole MCP (Model Context Protocol) :** Implémentation de nouveaux outils MCP permettant aux modèles d'IA de trouver des collections et de lister des sources de manière autonome et intelligente.
- **Optimisation de l'indexation :** 
    - Refonte de l'architecture de l'indexeur pour une meilleure modularité.
    - Amélioration des performances via le chargement des vecteurs par lots (batching) et une meilleure gestion de la mémoire.
- **Sécurité et Authentification :**
    - Correction de vulnérabilités critiques sur les dépendances (brotli, certifi, pillow).
    - Amélioration de la gestion des sessions SSO (Keycloak) pour éviter les déconnexions intempestives lors du renouvellement des jetons.
- **Fiabilité des données :** Généralisation de l'utilisation de modèles Pydantic pour stabiliser les échanges de données entre l'API, l'indexeur et les outils de test.

### Autres changements
- **Documentation :** Mise à jour massive de la documentation technique, incluant l'API documentaire de Résana, le mode d'emploi des assistants et les procédures de test du "harnais".
- **Qualité logicielle :** Intégration de `commitlint` dans la chaîne CI/CD pour garantir la conformité des messages de commit.
