## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives concernant l'évaluation et l'indexation de documents, notamment avec l'ajout de la gestion de questions/réponses maîtrisées et l'intégration d'OCR via Docling. Des optimisations ont également été apportées à l'API et à l'évaluation des documents, avec un focus sur la robustesse et la sécurité.

### Évolutions fonctionnelles
- Ajout de la possibilité de passer les fichiers d'évaluation et de mapping en argument à la commande `evaluateur_mqc` [#33efb0d](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/33efb0d).
- Implémentation de l'ajout de documents maîtrisés à une collection [#ff400c9](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/ff400c9).
- Possibilité de créer un identifiant unique à partir de la question maîtrisée [#2def475](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/2def475).
- Ajout d'un dataset contenant tous les documents [#471295a](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/471295a).
- Exposition d'une route HTTP POST `/evaluation` pour lancer des évaluations en arrière-plan [#53b8f3a](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/53b8f3a).
- Ajout d'une route pour "jeopardyser" une liste de documents (génération de questions) [#f3cc453](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f3cc453).
- Amélioration du prompt utilisé pour la génération de questions (Jeopardy) [#a757000](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/a757000).

### Évolutions techniques
- Refactorisation du code pour introduire des documents contenant des questions/réponses maîtrisées [#afdd7c6](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/afdd7c6).
- Intégration d'un VLM (Vision Language Model) via Docling pour effectuer de l'OCR (reconnaissance optique de caractères) [#e93409e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/e93409e).
- Correction du déploiement qui échouait en raison d'une dépendance manquante (pilote Postgres) [#6350851](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/6350851).
- Séparation des environnements de développement et de production [#feefdae](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/feefdae).
- Extraction d'une classe abstraite pour encapsuler la logique de "jeopardy" et faciliter l'ajout de services similaires [#f084a46](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f084a46).
- Amélioration de la gestion des erreurs lors de l'ajout de chunks à l'API Albert [#435fabb](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/435fabb).
- Correction du mapping de la réponse Albert lors de la récupération de documents [#85af687](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/85af687).
- Mise à jour de la dépendance `aiohttp` suite à une alerte de sécurité dependabot [#36ec6c4](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/36ec6c4).

### Autres changements
- Slugification de la question de la réponse maîtrisée pour améliorer la cohérence des identifiants [#da04f69](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/da04f69).
- Déplacement et externalisation de l'écriture du fichier de correspondance pour une meilleure organisation [#1268ad3](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/1268ad3).
- Ajout du modèle C4 pour le Jeopardy [#b9f8421](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/b9f8421).
- Correction et complétion de la sortie de Deepeval [#b5871b0](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/b5871b0), [#4ea2a2b](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/4ea2a2b), [#46b4596](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/46b4596).
- Vérification que le contenu généré par le LLM n'est pas vide [#6774fc1](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/6774fc1).
- Ajout d'une liste de documents distants pour la collection MQC [#defc4ca](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/defc4ca).
- Ajout d'une question au jeopardy seulement si Albert a pu générer une question [#490dcff](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/490dcff).
- Demande à l’entrepôt de questions générées les questions pour un document donné [#5cc06b9](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/5cc06b9).
