## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la fonctionnalité "Jeopardy" permettant de générer des questions à partir de documents, ainsi que sur des corrections de sécurité et des améliorations de l'infrastructure de déploiement. L'ajout d'un nouveau dataset de documents est également notable.

### Évolutions fonctionnelles
- Ajout d'un nouveau dataset contenant tous les documents disponibles.
- Amélioration du prompt utilisé pour la génération de questions "Jeopardy", afin d'obtenir de meilleurs résultats.
- Possibilité de "jeopardyser" une liste de documents en les recherchant par leur nom.
- Implémentation d'une route API pour "jeopardyser" une liste de documents.
- Ajout de la possibilité d'indexer un document avec des questions/réponses maîtrisées.
- Permet d'ajouter à une collection un document maîtrisé.
- Slugification de la question de la réponse maîtrisée pour une meilleure gestion des identifiants.
- Appel d'un VLM (Vision Language Model) via Docling pour effectuer de l'OCR (reconnaissance optique de caractères).
- Ajout du modèle C4 au Jeopardy.
- Possibilité de demander à l'entrepôt de questions générées les questions pour un document donné.

### Évolutions techniques
- Correction du déploiement qui échouait en raison d'une dépendance manquante du pilote Postgres.
- Séparation des environnements de développement et de production.
- Refactorisation du code pour introduire une classe abstraite et un service dédié à la "jeopardy" de documents.
- Typage de la méthode "jeopardyse" pour une meilleure robustesse.
- Amélioration de la sortie de Deepeval pour une meilleure intégration.
- Correction du mapping de la réponse Albert lors de la récupération de documents.
- Extraction d'une classe abstraite pour faire émerger un service pour jeopardyser des documents ciblés.
- Mise à jour des droits d'exécution du script clever.
- Configuration de la CI pour lancer le déploiement depuis GitHub.
- Déploiement et démarrage du serveur MQC Data.
- Correction de l'erreur remontée par l'API Albert lors de l'ajout d'un chunk, en la transformant en chaîne de caractères.
- Vérification que le contenu généré par le LLM (Large Language Model) n'est pas vide.
- Ajout d'une liste de documents distants pour la collection MQC.
- Ajout d'une question au jeopardy seulement si Albert a pu générer une question.

### Autres changements
- Mise à jour des dépendances `aiohttp` et `requests` suite à des alertes de sécurité Dependabot.
- Mise à jour de la dépendance `svelte` suite à une alerte de sécurité Dependabot.
- Ajout de logs pour le suivi de la fonctionnalité "Jeopardy".
- Ajout de logs lors du traitement de "Jeopardy" et du traitement des documents.
- Publication d'événements lors de la génération de questions.
- Ajout du script `pre-run` pour builder le front-end.
- Correction pour s'assurer que le document Docling est bien ajouté lors de l'extraction.
- Amélioration de la gestion des logs, en laissant Uvicorn gérer l'initialisation.
- Ajout de logs pour le débogage de la non-prolifération des logs sur CC.
