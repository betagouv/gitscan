## Changelog : playground (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de gestion des utilisateurs, de journalisation des activités et de l'expérience utilisateur sur la plateforme. Des corrections de bugs ont été apportées, notamment concernant la sauvegarde des fiches, la gestion des coordonnées GPS et l'affichage des informations. Des fonctionnalités d'archivage et de filtrage ont été ajoutées, ainsi que des améliorations de la sécurité et de la conformité.

### Évolutions fonctionnelles
- Ajout de filtres dans l'onglet d'importation pour faciliter la recherche et la sélection des données [#291](https://github.com/refugies-info/playground/pull/291).
- Implémentation d'un système de notes pour les fiches, permettant aux utilisateurs d'ajouter des commentaires et des annotations [#292](https://github.com/refugies-info/playground/pull/292).
- Lorsqu'une fiche française est archivée et que toutes les traductions le sont également, l'archivage est maintenant correctement propagé [#293](https://github.com/refugies-info/playground/pull/293).
- Ajout d'un journal d'activités pour suivre les actions effectuées sur les fiches et les utilisateurs [#269](https://github.com/refugies-info/playground/pull/269), [#287](https://github.com/refugies-info/playground/pull/287).
- Amélioration de l'interface utilisateur pour la page de traduction et la liste des traductions, incluant l'auto-sauvegarde et la gestion des traducteurs [#257](https://github.com/refugies-info/playground/pull/257), [#282](https://github.com/refugies-info/playground/pull/282), [#283](https://github.com/refugies-info/playground/pull/283).
- Possibilité d'assigner une fiche à un auteur et de gérer les utilisateurs plus efficacement [#242](https://github.com/refugies-info/playground/pull/242), [#238](https://github.com/refugies-info/playground/pull/238).
- Ajout d'un message d'avertissement pour indiquer aux utilisateurs les fiches nécessitant une attention particulière [#256](https://github.com/refugies-info/playground/pull/256).
- Amélioration de l'affichage de la version d'ingestion des documents [#272](https://github.com/refugies-info/playground/pull/272), [#248](https://github.com/refugies-info/playground/pull/248).

### Évolutions techniques
- Mise en place d'un cron pour mettre à jour les fiches automatiquement [#290](https://github.com/refugies-info/playground/pull/290).
- Refactorisation de la gestion des logs et ajout de nouveaux événements pour le suivi des activités [#290](https://github.com/refugies-info/playground/pull/290).
- Centralisation des données utilisateurs dans le backend pour une meilleure cohérence [#289](https://github.com/refugies-info/playground/pull/289).
- Migration de `author_id` vers `assignee_id` dans la base de données pour une meilleure clarté [#238](https://github.com/refugies-info/playground/pull/238).
- Amélioration de la gestion des erreurs et des logs dans le processus d'ingestion des données [#275](https://github.com/refugies-info/playground/pull/275).
- Mise à jour des dépendances et correction de vulnérabilités de sécurité [#268](https://github.com/refugies-info/playground/pull/268), [#262](https://github.com/refugies-info/playground/pull/262), [#244](https://github.com/refugies-info/playground/pull/244).
- Ajout d'un environnement de développement local pour éviter la consommation excessive de ressources [#255](https://github.com/refugies-info/playground/pull/255).
- Mise en place d'un workflow CI/CD pour automatiser le processus de déploiement [#267](https://github.com/refugies-info/playground/pull/267).

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements d'architecture.
- Nettoyage du code et suppression de code obsolète.
- Amélioration des tests unitaires et d'intégration.
- Correction de bugs mineurs et amélioration de la stabilité de la plateforme.
- Ajout de données de test pour faciliter le débogage et le développement.
- Suppression des assets RCO legacy.
- Correction de problèmes de typage et de cohérence du code.
