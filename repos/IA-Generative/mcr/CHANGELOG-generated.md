## Changelog : mcr (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la performance du traitement des transcriptions, ainsi que sur l'expérience utilisateur avec de nouvelles fonctionnalités comme le téléchargement de fichiers et la gestion des erreurs. Des refactorings importants ont également été effectués pour simplifier l'architecture et préparer le projet pour de futures évolutions.

### Évolutions fonctionnelles
- Ajout de la possibilité de générer des livrables directement depuis une carte de livrable [#978](https://github.com/IA-Generative/mcr/pull/978).
- Implémentation d'un verrouillage des réunions pour gérer les requêtes concurrentes [#977](https://github.com/IA-Generative/mcr/pull/977).
- Amélioration de la gestion des erreurs et ajout d'un endpoint d'administration pour relancer les transcriptions en cas d'échec [#969](https://github.com/IA-Generative/mcr/pull/969).
- Possibilité de télécharger les artefacts (fichiers) d'une réunion [#935](https://github.com/IA-Generative/mcr/pull/935) et [#903](https://github.com/IA-Generative/mcr/pull/903).
- Ajout d'une fonctionnalité d'import de fichiers en un clic [#908](https://github.com/IA-Generative/mcr/pull/908).
- Amélioration du suivi de l'importation de fichiers avec affichage des erreurs et de la progression [#976](https://github.com/IA-Generative/mcr/pull/976) et [#894](https://github.com/IA-Generative/mcr/pull/894).
- Ajout d'un glossaire avec un en-tête amélioré [#938](https://github.com/IA-Generative/mcr/pull/938).

### Évolutions techniques
- Refactorisation majeure de l'architecture pour dissoudre la machine d'état de la réunion et simplifier le code [#861](https://github.com/IA-Generative/mcr/pull/861) et [#912](https://github.com/IA-Generative/mcr/pull/912).
- Passage de la transcription en mode asynchrone pour améliorer la performance et la scalabilité [#898](https://github.com/IA-Generative/mcr/pull/898).
- Amélioration de la gestion des erreurs S3 avec des mécanismes de retry [#943](https://github.com/IA-Generative/mcr/pull/943).
- Utilisation de lazy loading pour les modèles de speech-to-text afin de réduire le temps de démarrage [#923](https://github.com/IA-Generative/mcr/pull/923).
- Amélioration de la gestion des dépendances et des environnements de développement [#917](https://github.com/IA-Generative/mcr/pull/917) et [#907](https://github.com/IA-Generative/mcr/pull/907).
- Ajout de tests unitaires et d'intégration pour améliorer la qualité du code.
- Mise en place de hooks Git pour améliorer la qualité du code et automatiser les tests [#920](https://github.com/IA-Generative/mcr/pull/920).

### Autres changements
- Amélioration de la documentation et des templates de rapport d'erreurs [#939](https://github.com/IA-Generative/mcr/pull/939) et [#913](https://github.com/IA-Generative/mcr/pull/913).
- Suppression de code obsolète et nettoyage du codebase.
- Correction de bugs mineurs et améliorations de la stabilité.
- Ajout d'une skill de test pour standardiser les tests [#925](https://github.com/IA-Generative/mcr/pull/925).
- Mise à jour des dépendances.
