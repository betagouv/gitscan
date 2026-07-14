## Changelog : playground (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de gestion des logs d'activité, de suivi des tokens consommés par l'IA, et de l'expérience utilisateur sur les pages de traduction et d'archivage. Des corrections et des optimisations ont également été apportées à l'infrastructure et aux workflows.

### Évolutions fonctionnelles

*   Ajout d'un journal d'activités pour suivre les actions réalisées sur les fiches (publication, archivage, etc.) [#294](https://github.com/refugies-info/playground/pull/294).
*   Possibilité de mettre à jour le statut de travail directement depuis l'en-tête de la fiche et la liste des documents [#293](https://github.com/refugies-info/playground/pull/293).
*   Ajout de dates de publication et d'archivage aux fiches [#296](https://github.com/refugies-info/playground/pull/296).
*   Intégration d'un système de notes [#292](https://github.com/refugies-info/playground/pull/292).
*   Ajout de filtres à l'onglet "Importer" [#291](https://github.com/refugies-info/playground/pull/291).
*   Amélioration de l'UX/UI des pages de traduction et de la liste des traductions [#282](https://github.com/refugies-info/playground/pull/282), [#286](https://github.com/refugies-info/playground/pull/286), [#283](https://github.com/refugies-info/playground/pull/283).
*   Possibilité de trier les versions d'ingestion par numéro de version [#278](https://github.com/refugies-info/playground/pull/278).
*   Affichage amélioré des versions d'ingestion [#272](https://github.com/refugies-info/playground/pull/272).
*   Ajout d'une action d'archivage sur les fiches [#287](https://github.com/refugies-info/playground/pull/287).
*   Ajout de la possibilité de verrouiller/déverrouiller l'édition d'une fiche par un utilisateur, avec gestion de la libération du verrouillage lors de la fermeture de l'onglet [#256](https://github.com/refugies-info/playground/pull/256).

### Évolutions techniques

*   Enregistrement de l'utilisation des tokens et du modèle lors des interactions avec Letta [#295](https://github.com/refugies-info/playground/pull/295).
*   Refactoring et optimisation du code, notamment suppression de fichiers inutiles et mise à jour des stories [#294](https://github.com/refugies-info/playground/pull/294).
*   Migration de `assignee_id` de la table `editorial_records` vers la table `workflows` [#257](https://github.com/refugies-info/playground/pull/257).
*   Ajout d'un environnement local pour Letta afin d'éviter la consommation de tokens en production [#274](https://github.com/refugies-info/playground/pull/274).
*   Amélioration de la gestion des logs et ajout d'énums pour les types d'événements [#273](https://github.com/refugies-info/playground/pull/273).
*   Mise en place d'un cron pour mettre à jour les fiches (bouton de débogage) [#290](https://github.com/refugies-info/playground/pull/290).
*   Correction de problèmes liés à la migration de la base de données et à la relecture des workflows [#271](https://github.com/refugies-info/playground/pull/271), [#272](https://github.com/refugies-info/playground/pull/272).
*   Mise à jour des dépendances pour corriger des vulnérabilités de sécurité [#262](https://github.com/refugies-info/playground/pull/262).

### Autres changements

*   Ajout de données de seed pour le débogage et les tests sur l'environnement de staging [#276](https://github.com/refugies-info/playground/pull/276).
*   Documentation de l'inventaire de Letta Cloud [#259](https://github.com/refugies-info/playground/pull/259).
*   Archivage des anciens assets RCO [#260](https://github.com/refugies-info/playground/pull/260).
*   Amélioration des scripts CI/CD et des workflows GitHub Actions [#268](https://github.com/refugies-info/playground/pull/268).
*   Nettoyage du code et suppression de configurations inutiles.
*   Mise à jour des types Supabase.
