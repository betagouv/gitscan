## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 09 avril 2026)

### Résumé
Ce mois-ci, le projet a connu des avancées significatives dans l'automatisation de l'évaluation et de l'amélioration des données, notamment avec l'introduction d'un système de "jeopardy" pour identifier les points faibles des documents et un travail important sur la reformulation des questions. Des améliorations ont également été apportées à l'infrastructure et à la sécurité du projet.

### Évolutions fonctionnelles
- Implémentation d'un système de "jeopardy" pour rechercher des documents par leur nom et générer des questions associées. [#1]
- Ajout de la possibilité de lancer la génération de questions sur une collection de documents via une nouvelle route API.
- Amélioration du prompt utilisé pour le "jeopardy" afin d'optimiser la qualité des questions générées.
- Ajout de la possibilité d'ajouter des chunks (fragments) à un document existant.
- Intégration de nouveaux documents de sources importantes comme le CERT-FR et la CNIL.
- Mise en place d'un système d'évaluation de la reformulation des questions, avec publication des résultats via un bus d'événements.
- Exposition d'une API pour exécuter des évaluations de reformulation.

### Évolutions techniques
- Refactorisation du code pour séparer les responsabilités et améliorer la maintenabilité, notamment concernant l'évaluation et l'indexation.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (requests, svelte, flatted, pyasn1).
- Amélioration de l'intégration avec l'API Albert, notamment pour l'ajout de chunks et la recherche de documents.
- Utilisation de Uvicorn pour la gestion des logs.
- Configuration de la CI/CD pour automatiser le déploiement du serveur MQC Data.
- Ajout de tests unitaires pour valider l'ajout de questions comme chunks.
- Introduction de nouvelles métriques pour évaluer la qualité de la reformulation (MetriqueSuppressionParasites et autres).

### Autres changements
- Ajout de documentation sur la solution de génération de questions.
- Mise à jour de la documentation HyDE.
- Ajout de logs pour faciliter le suivi du processus de "jeopardy".
- Correction de bugs mineurs et améliorations de la performance.
- Suppression de dépendances inutiles (openai du client d’indexation).
- Amélioration de la gestion des erreurs lors de l'ajout de documents et de chunks.

[#1]:  Référence aux commits concernant le jeopardy (dc3158b, 0b536f9, 5cc06b9, 2a45eb5, 0cb89f4, a466988, 4b0bcd5, 7512a38, 533e03d, 04643c7)
