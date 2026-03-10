## Changelog : anssi-recommandations-cyber (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur en introduisant la notion de conversation avec Albert, le modèle d'IA.  Il est désormais possible de poser des questions dans un contexte conversationnel, avec la possibilité de reformuler les questions pour de meilleurs résultats. Des améliorations de la robustesse et de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Possibilité d'interroger Albert en mode conversationnel, permettant de poser des questions dans un contexte et d'obtenir des réponses plus pertinentes.
- Ajout d'un reformulateur de question pour améliorer la qualité des requêtes envoyées à Albert.
- En cas d'erreur, le message d'erreur du backend est maintenant affiché sur le frontend pour faciliter le diagnostic.
- Ajout de tags pour annoter les conversations.
- Amélioration du prompt de reformulation pour de meilleurs résultats.
- Ajout d'un filtre pour ne conserver que les N derniers messages d'une conversation.
- Possibilité de spécifier le modèle à utiliser pour la reformulation.
- Ajout d'une violation "question non comprise" au reformulateur.

### Évolutions techniques
- Refactorisation de l'architecture API avec séparation des routes dans des routeurs distincts.
- Implémentation de la persistance des conversations dans la base de données PostgreSQL.
- Création de scripts SQL pour la création de la table `conversations` et la migration des interactions.
- Implémentation d'un outil de migration BDD personnalisé.
- Encapsulation de l'appel à l'API dans le store Svelte pour une meilleure gestion de l'état.
- Séparation de la création d'une conversation et de l'ajout d'une interaction en deux étapes distinctes.
- Journalisation de la question et des sources retournées par Albert lorsque la variable d'environnement `ALPHA_TEST` est activée.
- Amélioration de la robustesse des prompts utilisés par Albert.
- Suppression de dépendances inutilisées suite aux alertes de sécurité Dependabot.
- Mise à jour de plusieurs dépendances (cryptography, rollup, svelte) pour corriger des vulnérabilités de sécurité et améliorer la stabilité.
- Ajout d'un type utilisateur `EVALUATION`.

### Autres changements
- Suppression d'un print oublié dans le code.
- Correction de l'ordre inverse des messages dans le reformulateur de question.
- Suppression de la notion de prompt depuis l'interface utilisateur.
- Renommage de la route `pose_question` en `conversation`.
- Ajout de tests pour les interactions et la création de conversations.
- Uniformisation du nom des variables `*_id` en `id_*`.
- Ajout d'un check pour les fichiers Svelte dans le CI.
- Ajout d'un événement `INTERACTION_AJOUTEE` et `CONVERSATION_CREEE`.
- Correction de l'injection du DSFR.
- Fixe prettier.
- Ajout d'un constructeur de `ReponseQuestion` pour les tests.
- Ajout d'une date de création pour les interactions.
- Suppression de méthodes obsolètes pour la gestion des retours utilisateurs.
