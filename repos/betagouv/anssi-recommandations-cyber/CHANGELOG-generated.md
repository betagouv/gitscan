## Changelog : anssi-recommandations-cyber (30 derniers jours)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives concernant la gestion des conversations et des interactions avec le modèle d'IA Albert. L'ajout de la persistance des conversations permet de conserver l'historique des échanges, améliorant ainsi l'expérience utilisateur. Des corrections de bugs et des optimisations ont également été apportées pour une meilleure stabilité et performance.

### Évolutions fonctionnelles
- Possibilité d'interroger Albert en mode conversationnel, permettant un échange plus naturel et contextuel.
- Ajout de la persistance des conversations : l'historique des questions et réponses est maintenant conservé.
- Amélioration de la gestion des erreurs : affichage du message d'erreur du backend au frontend.
- Ajout de la possibilité d'annoter une conversation avec des tags.
- Ajout de la violation `MECONNAISSANCE`.
- Retour de l'ID de la conversation après une question posée.
- Amélioration du prompt de reformulation pour une meilleure compréhension des questions.

### Évolutions techniques
- Refactorisation de l'architecture backend : séparation des routes d'API dans des routeurs distincts.
- Implémentation d'un outil de migration de base de données personnalisé.
- Extraction de la logique métier des adaptateurs de base de données pour une meilleure organisation du code.
- Utilisation d'un constructeur de `ReponseQuestion` pour les tests.
- Remplacement du service Albert par une implémentation en mémoire pour certains tests et développements.
- Ajout d'un type utilisateur `EVALUATION`.
- Mise à jour des dépendances `cryptography`, `eslint` et `pip` pour corriger des vulnérabilités et bénéficier des dernières améliorations.
- Suppression de code mort et de dépendances inutilisées.

### Autres changements
- Journalisation de la question et des sources retournées en mode `ALPHA_TEST`.
- Ajout d'un check pour les fichiers Svelte lors des tests.
- Suppression de méthodes obsolètes liées aux retours utilisateurs.
- Correction de la persistance des violations.
- Uniformisation du nom des variables d'ID (`*_id` en `id_*`).
- Suppression du prompt depuis l'interface utilisateur.
- Renommage de la route `pose_question` en `conversation`.
- Ajout d'une date de création pour les interactions.
- Correction de l'ordre inverse des messages dans le reformulateur de question.
- Ajout d'un reformulateur de question pour améliorer la compréhension des requêtes.
- Ajout d'un filtre pour ne conserver que les N derniers messages d'une conversation.
- Émission d'événements pour les interactions et les conversations.
- Suppression de la duplication de code lors de la création d'une conversation et de l'ajout d'une interaction.
- Correction d'un bug lié à l'encodage des URL.
