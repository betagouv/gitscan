## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, le projet a connu des avancées significatives dans l'intégration de l'IA pour l'analyse et la génération de questions à partir de documents. L'ajout de la fonctionnalité "Jeopardy" permet de créer des questions/réponses à partir de documents, améliorant ainsi l'évaluation et l'indexation des recommandations de l'ANSSI. Des améliorations ont également été apportées à l'infrastructure de déploiement et à la gestion des logs.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité "Jeopardy" permettant de générer des questions à partir de documents, avec une interface d'exposition via une route POST dédiée. [#1234 (lien fictif)]
- Possibilité de "jeopardyser" une liste de documents en les recherchant par leur nom.
- Intégration du modèle C4 pour le Jeopardy, améliorant la qualité des questions générées.
- Amélioration du prompt utilisé pour la génération de questions (Jeopardy).
- Ajout de la possibilité de lire un document à partir de son identifiant.
- Ajout de la possibilité d'ajouter des questions comme chunks.
- Intégration d'un appel à un VLM (Vision Language Model) via Docling pour effectuer de l'OCR.

### Évolutions techniques
- Refactorisation du code pour extraire un service dédié à la "jeopardisation" des documents, améliorant la modularité et la maintenabilité.
- Séparation des environnements de développement et de production.
- Amélioration de la gestion des erreurs lors de l'ajout de chunks et de la génération de questions, assurant une meilleure robustesse.
- Mise à jour des dépendances `aiohttp` et `requests` pour corriger des vulnérabilités de sécurité (via Dependabot).
- Mise à jour de la dépendance `svelte` pour corriger des vulnérabilités de sécurité (via Dependabot).
- Amélioration de la gestion des logs, notamment pour le suivi de la fonctionnalité Jeopardy.
- Refactorisation de l'appel à l'API Albert pour éviter la duplication de code.
- Typage plus précis de certaines méthodes pour améliorer la qualité du code.
- Configuration de la CI/CD pour automatiser le déploiement depuis GitHub.

### Autres changements
- Ajout de logs pour le suivi de la fonctionnalité Jeopardy.
- Mise à jour de la documentation HyDE.
- Correction du déploiement qui échouait en raison d'une dépendance manquante (pilote Postgres).
- Correction de bugs mineurs et améliorations de la sortie de `deepeval`.
- Mise à jour des droits d'exécution du script clever.
- Ajout d'un script `pre-run` pour builder le front-end.
- Publication d'événements lors de la génération de questions.
- Ajout de tests unitaires pour l'ajout de questions comme chunks.
