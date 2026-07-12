## Changelog : OpenGateLLM (30 derniers jours, au 11 juillet 2026)

### Résumé
Les dernières mises à jour d'OpenGateLLM se concentrent sur l'amélioration de la sécurité, la refactorisation de l'architecture pour une meilleure maintenabilité et la correction de bugs. Des améliorations ont été apportées à la gestion des documents, à l'authentification et à l'intégration des modèles, ainsi qu'à la robustesse globale du système. La fonctionnalité RAG (Retrieval-Augmented Generation) a été supprimée.

### Évolutions fonctionnelles
- **Documents :** Le calcul de la limite de documents a été amélioré en utilisant un tokenizer pour compter les tokens, offrant une gestion plus précise des limites de contexte. [#950]
- **Authentification :** Amélioration de la validation des clés API héritées après la refactorisation. [#941]
- **Playground :** Correction d'un bug empêchant la propagation du bouton de rôle dans l'interface Playground. [#943]
- **Chat Completion :** Fermeture de la session PostgreSQL avant l'appel aux LLMs pour améliorer la gestion des connexions et la performance. [#940]
- **Utilisateurs :** Ajout d'un suffixe "id" aux attributs utilisateur et organisation lors de la création d'un utilisateur. [#934]
- **Santé (Health) :** Ajout d'un endpoint de santé qui vérifie l'état des modèles en appelant l'endpoint `/metrics`. [#911]

### Évolutions techniques
- **Refactorisation :** Refactorisation importante des endpoints `/login`, `/v1/embeddings` et `/v1/admin/keys` vers une architecture plus propre et modulaire. [#937, #945, #933]
- **Sécurité :** Ignorisation de plusieurs CVE (Common Vulnerabilities and Exposures) pour des dépendances, avec justification. [#951, #944]
- **CI/CD :** Amélioration du workflow de release et de l'intégration avec Semgrep pour l'analyse de sécurité du code. [#957, #954]
- **Suppression RAG :** Suppression de la fonctionnalité RAG. [#956]
- **Nettoyage de code :** Suppression de champs inutiles dans l'objet `authenticated_user` et renommage de `user_with_role` en `authenticated_user`. [#932, #931]
- **Organisation du code :** Déplacement des schémas d'administration dans un dossier dédié. [#928]
- **Correction d'importations circulaires :** Résolution d'un problème d'importations circulaires. [#929]

### Autres changements
- Mise à jour de la documentation générée automatiquement. [#958, #916]
- Mise à jour des dépendances de développement (tmp). [#895]
- Ajout d'un âge minimum de release pour npm. [#907]
