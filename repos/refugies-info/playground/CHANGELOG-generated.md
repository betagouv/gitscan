## Changelog : playground (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des fiches, notamment en ajoutant l'auto-sauvegarde, en corrigeant des bugs liés à la sauvegarde des coordonnées GPS et à l'affichage des titres, et en améliorant l'attribution des tâches aux utilisateurs. Des améliorations ont également été apportées à la gestion des métadonnées et à l'archivage des fiches. Enfin, des travaux de maintenance et d'optimisation ont été réalisés, notamment sur les crons et la sécurité.

### Évolutions fonctionnelles
- Ajout de l'auto-sauvegarde des fiches Bomo [#247](https://github.com/refugies-info/playground/pull/247).
- Correction d'un bug empêchant la sauvegarde correcte des coordonnées GPS [#253](https://github.com/refugies-info/playground/pull/253).
- Correction d'un bug d'affichage des titres des fiches RCO en langage clair [#252](https://github.com/refugies-info/playground/pull/252).
- Possibilité d'assigner une fiche à un utilisateur spécifique, avec une gestion des permissions améliorée [#245](https://github.com/refugies-info/playground/pull/245), [#251](https://github.com/refugies-info/playground/pull/251).
- Ajout de la date de fin dans les tableaux d'ingestion [#232](https://github.com/refugies-info/playground/pull/232).
- Ajout du nombre de mots dans le tableau d'ingestion [#230](https://github.com/refugies-info/playground/pull/230).
- Possibilité d'afficher le bouton "enregistrer" même pour les fiches archivées [#237](https://github.com/refugies-info/playground/pull/237).
- Amélioration de l'affichage de l'état de publication [#237](https://github.com/refugies-info/playground/pull/237).

### Évolutions techniques
- Refactorisation de la gestion des métadonnées pour optimiser l'utilisation de l'IA et ne générer des métadonnées que pour les fiches conformes [#230](https://github.com/refugies-info/playground/pull/230).
- Mise à jour de la base de données avec une commande de migration dédiée [#251](https://github.com/refugies-info/playground/pull/251).
- Amélioration de la sécurité en limitant les rôles autorisés pour l'assignation d'utilisateurs [#204](https://github.com/refugies-info/playground/pull/204).
- Correction de bugs et refactorisation du code liés à l'archivage des fiches [#240](https://github.com/refugies-info/playground/pull/240).
- Mise à jour des dépendances du workflow [#236](https://github.com/refugies-info/playground/pull/236).
- Ajout d'un scan de vulnérabilités des dépendances en pré-push [#244](https://github.com/refugies-info/playground/pull/244).

### Autres changements
- Suppression de code mort lié à l'ancien workflow de traduction [#236](https://github.com/refugies-info/playground/pull/236).
- Correction de tests Storybook bloquant la CI [#239](https://github.com/refugies-info/playground/pull/239).
- Mise à jour de la configuration des crons pour l'ingestion de données [#228](https://github.com/refugies-info/playground/pull/228), [#231](https://github.com/refugies-info/playground/pull/231).
- Modification du nom de la variable `author_id` en `assignee_id` pour refléter la nouvelle fonctionnalité d'assignation [#238](https://github.com/refugies-info/playground/pull/238).
- Amélioration de la gestion des erreurs lors de la mise à jour du statut de conformité [#248](https://github.com/refugies-info/playground/pull/248).
