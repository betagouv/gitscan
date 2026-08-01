## Changelog : mcr (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la flexibilité de la plateforme, notamment en matière de gestion des erreurs, de gestion des fichiers et de pipeline de transcription. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'import de fichiers audio et le téléchargement des artefacts de réunion. L'architecture interne a été refactorisée pour une meilleure maintenabilité et performance.

### Évolutions fonctionnelles
- Ajout de la possibilité de générer des rapports de type "Minutes structurées" [#986](https://github.com/IA-Generative/mcr/issues/986).
- Implémentation d'une interface pour relancer manuellement les transcriptions en cas d'échec [#969](https://github.com/IA-Generative/mcr/issues/969).
- Amélioration du suivi de l'import de fichiers avec affichage des erreurs par fichier et estimation du temps restant [#976](https://github.com/IA-Generative/mcr/issues/976).
- Ajout d'une fonctionnalité d'import simplifié en un clic [#908](https://github.com/IA-Generative/mcr/issues/908).
- Possibilité de télécharger les fichiers d'une réunion depuis S3 via un script dédié [#903](https://github.com/IA-Generative/mcr/issues/903).
- Ajout de comptes utilisateurs `@fake.com` pour les connexions MCR [#1001](https://github.com/IA-Generative/mcr/issues/1001).
- Amélioration de la gestion des erreurs lors de l'import de fichiers, avec affichage des erreurs en ligne et abandon de l'utilisation de toasts [#939](https://github.com/IA-Generative/mcr/issues/939).

### Évolutions techniques
- Refactorisation majeure de l'architecture interne, notamment la séparation des responsabilités et l'utilisation de microservices [#959](https://github.com/IA-Generative/mcr/issues/959).
- Suppression des modèles de speech-to-text locaux et passage à une utilisation exclusive des API distantes [#987](https://github.com/IA-Generative/mcr/issues/987).
- Amélioration de la gestion des erreurs S3 avec implémentation de mécanismes de retry [#943](https://github.com/IA-Generative/mcr/issues/943).
- Optimisation du pipeline de transcription en le divisant en quatre tâches distinctes [#912](https://github.com/IA-Generative/mcr/issues/912).
- Amélioration de la gestion des états de la transcription avec l'ajout d'un état "En cours" [#944](https://github.com/IA-Generative/mcr/issues/944).
- Utilisation de lazy loading pour les modèles de speech-to-text afin de réduire le temps de démarrage [#923](https://github.com/IA-Generative/mcr/issues/923).
- Mise en place d'un système de gestion des erreurs plus robuste avec l'utilisation de Sentry et la gestion des exceptions [#952](https://github.com/IA-Generative/mcr/issues/952).
- Amélioration des tests unitaires et d'intégration.
- Configuration du CI pour exécuter les tests sur les pull requests et sur les changements des fichiers d'environnement partagés [#976](https://github.com/IA-Generative/mcr/issues/976).
- Uniformisation de l'utilisation de Keycloak pour l'authentification.

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés à la plateforme.
- Amélioration des messages de log pour faciliter le débogage.
- Correction de bugs mineurs et améliorations de la performance.
- Ajout d'un modèle de rapport de bug et de feedback plus complet.
- Mise à jour des dépendances.
- Ajout d'un bot Slack "Amalaric".
- Suppression des anciens comptes utilisateurs `@theodo.com`.
- Ajout d'une règle d'infrastructure pour Claude.
- Amélioration de la documentation sur l'utilisation de Kaniko pour la construction des images Docker.
- Ajout d'un script pour télécharger les artefacts d'une réunion.
- Ajout d'une nouvelle skill pour les tests.
