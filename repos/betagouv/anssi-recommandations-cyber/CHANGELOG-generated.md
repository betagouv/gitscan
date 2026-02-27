## Changelog : anssi-recommandations-cyber (30 derniers jours)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives concernant la gestion des conversations, la reformulation des questions et la persistance des données. Des corrections de bugs et des optimisations ont également été apportées pour améliorer l'expérience utilisateur et la robustesse de l'application. L'équipe a également travaillé sur la sécurité en mettant à jour certaines dépendances.

### Évolutions fonctionnelles
- Permet d'interroger Albert en mode conversationnel, avec la création et la gestion de conversations.
- Ajout d'un reformulateur de question pour améliorer la compréhension des requêtes par le modèle Albert.
- Possibilité de taguer les conversations pour une meilleure organisation.
- Amélioration de l'affichage des messages d'erreur provenant du backend.
- Ajout d'un indicateur visuel pendant le traitement des questions.
- Possibilité d'ajouter des interactions à une conversation existante.
- Ajout du type d'utilisateur `EVALUATION`.
- Ajout de la violation `MECONNAISSANCE`.

### Évolutions techniques
- Refactorisation de l'architecture backend pour séparer les routes d'API dans des routeurs distincts.
- Implémentation d'un système de persistance des conversations en base de données.
- Utilisation d'une implémentation mémoire pour certains services (Albert, Sentry) pour faciliter les tests et le développement.
- Mise en place d'un outil de migration de base de données.
- Amélioration de la robustesse des prompts envoyés à Albert.
- Suppression de dépendances inutilisées et mise à jour de certaines librairies (pip, urllib3, eslint, cryptography).
- Uniformisation de la nomenclature des identifiants en base de données.

### Autres changements
- Ajout de scripts SQL pour la création et la migration de la table `conversations`.
- Ajout d'un favicon.
- Suppression de code mort et de prints inutiles.
- Amélioration des tests et ajout de checks pour les fichiers Svelte.
- Journalisation de la question et des sources retournées en mode `ALPHA_TEST`.
- Ajout d'un constructeur de `ReponseQuestion` pour les tests.
- Suppression de méthodes obsolètes pour la gestion des retours utilisateurs.
- Correction de bugs mineurs liés à l'affichage et au comportement de l'interface utilisateur.
