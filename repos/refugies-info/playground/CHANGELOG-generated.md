## Changelog : playground (30 derniers jours, au 2026-06-18)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la gestion des workflows éditoriaux, notamment le suivi des versions d'ingestion, l'archivage des fiches, et l'assignation des tâches. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la documentation et de la sécurité.

### Évolutions fonctionnelles
- Ajout de l'affichage de la version d'ingestion dans l'interface utilisateur, permettant un meilleur suivi de l'évolution des documents [#267](https://github.com/refugies-info/playground/pull/267).
- Amélioration de l'affichage de la date de fin des sessions de DI (Données et Intelligence) dans les tableaux [#232](https://github.com/refugies-info/playground/pull/232).
- Ajout du nombre de mots dans le tableau d'ingestion pour une meilleure analyse des documents [#230](https://github.com/refugies-info/playground/pull/230).
- Possibilité d'assigner une fiche à un utilisateur spécifique pour le suivi et la collaboration [#251](https://github.com/refugies-info/playground/pull/251).
- Ajout d'un bouton "Enregistrer" même pour les fiches archivées, facilitant la gestion des documents [#237](https://github.com/refugies-info/playground/pull/237).
- Correction d'un bug empêchant la sauvegarde des fiches Bomo [#243](https://github.com/refugies-info/playground/pull/243).
- Correction d'un bug lié aux métadonnées et aux coordonnées GPS [#253](https://github.com/refugies-info/playground/pull/253).
- Correction d'un bug empêchant l'affichage correct des titres des fiches RCO en langage clair [#252](https://github.com/refugies-info/playground/pull/252).
- Mise en place d'un auto-save des fiches Bomo [#247](https://github.com/refugies-info/playground/pull/247).
- Amélioration de l'affichage du statut de publication [#239](https://github.com/refugies-info/playground/pull/239).

### Évolutions techniques
- Ajout d'une action Letta Cloud pour la revue de code, améliorant la qualité du code [#268](https://github.com/refugies-info/playground/pull/268).
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité [#262](https://github.com/refugies-info/playground/pull/262) et [#271](https://github.com/refugies-info/playground/pull/271).
- Refactorisation de la gestion des versions d'ingestion et de la logique d'archivage [#272](https://github.com/refugies-info/playground/pull/272), [#241](https://github.com/refugies-info/playground/pull/241) et [#238](https://github.com/refugies-info/playground/pull/238).
- Amélioration de la gestion des erreurs et de la conformité des métadonnées générées automatiquement [#248](https://github.com/refugies-info/playground/pull/248).
- Migration de `author_id` vers `assignee_id` dans la table `editorial_records` pour une meilleure cohérence [#257](https://github.com/refugies-info/playground/pull/257) et [#238](https://github.com/refugies-info/playground/pull/238).
- Suppression des paramètres Claude inutilisés [#256](https://github.com/refugies-info/playground/pull/256).
- Archivage des anciens assets RCO XML [#260](https://github.com/refugies-info/playground/pull/260).
- Suppression d'un workflow de migration Supabase redondant [#258](https://github.com/refugies-info/playground/pull/258).
- Ajout d'une commande pour migrer la base de données [#251](https://github.com/refugies-info/playground/pull/251).

### Autres changements
- Mise à jour de la documentation concernant l'inventaire Letta Cloud [#259](https://github.com/refugies-info/playground/pull/259).
- Ajout de nouveaux agents traducteurs [#2836f58](https://github.com/refugies-info/playground/commit/2836f58).
- Ajout de Camille et Jérémy au seed des utilisateurs pour le débogage [#248](https://github.com/refugies-info/playground/pull/248).
- Correction de références obsolètes dans la documentation [#260](https://github.com/refugies-info/playground/pull/260).
- Ajustement du cron pour l'ingestion de données [#231](https://github.com/refugies-info/playground/pull/231) et [#228](https://github.com/refugies-info/playground/pull/228).
- Génération des types Supabase [#250](https://github.com/refugies-info/playground/pull/250).
