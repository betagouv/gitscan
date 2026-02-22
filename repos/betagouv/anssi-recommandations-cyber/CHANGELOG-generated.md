## Changelog : anssi-recommandations-cyber (30 derniers jours)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives en termes de gestion des conversations, de robustesse et de correction de bugs. L'ajout de la persistance des conversations permet de conserver l'historique des échanges avec Albert, l'IA. Des efforts ont également été faits pour améliorer la qualité des prompts envoyés à Albert et pour une meilleure gestion des erreurs. Enfin, des corrections de sécurité et des améliorations de code ont été apportées.

### Évolutions fonctionnelles
- Permet d'interroger Albert en mode conversationnel, conservant l'historique des échanges.
- Ajout de la possibilité d'ajouter des interactions à une conversation existante.
- Affichage du message d'attente lors de la soumission d'une question.
- Ajout des pages CGU et politique de confidentialité.
- Ajout du type utilisateur `EVALUATION`.
- Ajout de la violation MECONNAISSANCE.
- Amélioration de la robustesse des prompts envoyés à Albert.
- Instructions spécifiques ajoutées pour le DG de l'ANSSI.

### Évolutions techniques
- Implémentation de la persistance des conversations via une base de données.
- Refactoring de l'architecture pour séparer les routes API dans des routeurs distincts.
- Utilisation d'une implémentation mémoire pour certains services (adaptateur journal, sentry) afin de faciliter les tests et le développement.
- Amélioration de la gestion des erreurs et affichage des messages d'erreur dans l'interface utilisateur.
- Suppression de dépendances inutilisées (fastapi-armor) et mise à jour de certaines librairies (pip, urllib3, eslint, cryptography).
- Ajout d'un outil de migration de base de données.
- Ajout d'un reformulateur de question pour améliorer la qualité des requêtes envoyées à Albert.
- Utilisation de la question reformulée dans différentes étapes du processus de recherche et de réponse.

### Autres changements
- Ajout de tests pour les interactions et la création de conversations.
- Suppression de code mort et de fichiers inutiles.
- Amélioration de la configuration (ajout d'un paramètre pour la taille de la fenêtre historique).
- Ajout de githooks pour appliquer automatiquement les règles de formatage de code (prettier, eslint).
- Ajout du favicon.
- Correction du logo République Française.
- Uniformisation du nom des variables `*_id` en `id_*`.
- Suppression de la notion de prompt depuis l'interface utilisateur.
- Renommage de la route `pose_question` en `conversation`.
- Ajout d'un check pour les fichiers Svelte.
- Ajout de la date de création des interactions.
- Suppression de la duplication entre la création d’une conversation et l’ajout d’une interaction.
- Émission d'événements pour le suivi des interactions et des conversations.
