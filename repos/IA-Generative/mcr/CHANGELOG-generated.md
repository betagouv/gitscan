## Changelog : mcr (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors de l'import de fichiers audio, avec une meilleure gestion des erreurs et un suivi de progression plus clair. Des efforts importants ont également été déployés pour améliorer la robustesse et la performance du pipeline de transcription, notamment en rendant la diarisation asynchrone et en gérant les erreurs S3. Enfin, une refactorisation architecturale est en cours pour moderniser le code et faciliter sa maintenance.

### Évolutions fonctionnelles
- Amélioration du suivi de l'import de fichiers : affichage de la progression par fichier, estimation du temps restant, et gestion des erreurs d'import directement dans l'interface utilisateur [#976](https://github.com/IA-Generative/mcr/issues/976).
- Possibilité de lancer l'import d'un fichier audio en un seul clic, simplifiant ainsi le processus pour l'utilisateur [#896](https://github.com/IA-Generative/mcr/issues/896).
- Ajout d'un script permettant de télécharger les fichiers d'une réunion depuis S3 [#903](https://github.com/IA-Generative/mcr/issues/903).
- Amélioration de la gestion des erreurs lors de l'import : détection des uploads bloqués par un proxy et signalement à Sentry [#899](https://github.com/IA-Generative/mcr/issues/899).
- Ajout d'une fonctionnalité permettant de marquer un deliverable comme étant "en cours" pour indiquer une génération en cours [#944](https://github.com/IA-Generative/mcr/issues/944).
- Amélioration de la navigation avec des boutons d'action plus clairs et cohérents [#885](https://github.com/IA-Generative/mcr/issues/885).

### Évolutions techniques
- Refactorisation de l'architecture du projet, notamment pour la gestion des livrables et la transcription, afin de la rendre plus modulaire et maintenable [#959](https://github.com/IA-Generative/mcr/issues/959), [#943](https://github.com/IA-Generative/mcr/issues/943), [#937](https://github.com/IA-Generative/mcr/issues/937), [#919](https://github.com/IA-Generative/mcr/issues/919), [#901](https://github.com/IA-Generative/mcr/issues/901).
- Implémentation de la diarisation asynchrone pour améliorer la performance et la réactivité de l'application [#866](https://github.com/IA-Generative/mcr/issues/866).
- Ajout de mécanismes de retry pour les opérations S3 afin d'améliorer la robustesse du pipeline [#943](https://github.com/IA-Generative/mcr/issues/943).
- Amélioration de la gestion des erreurs et des timeouts dans le worker de transcription [#937](https://github.com/IA-Generative/mcr/issues/937).
- Utilisation de `tenacity` pour gérer les retries de manière centralisée et configurable [#937](https://github.com/IA-Generative/mcr/issues/937).
- Ajout de tests unitaires et d'intégration pour valider les nouvelles fonctionnalités et les refactorisations.
- Amélioration de la configuration de l'environnement de développement avec l'utilisation de variables d'environnement gérées par 1Password [#907](https://github.com/IA-Generative/mcr/issues/907).

### Autres changements
- Documentation de la configuration de Sentry avec 1Password dans le README [#909](https://github.com/IA-Generative/mcr/issues/909).
- Ajout de hooks Git pour effectuer des vérifications de code (mypy, vue-tsc) avant chaque commit [#911](https://github.com/IA-Generative/mcr/issues/911).
- Ajout d'une skill pour les tests standard [#925](https://github.com/IA-Generative/mcr/issues/925).
- Nettoyage du code et suppression de code mort.
- Mise à jour des dépendances.
