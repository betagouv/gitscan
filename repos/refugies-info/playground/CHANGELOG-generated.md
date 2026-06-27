## Changelog : playground (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des documents, notamment en ajoutant un journal d'activité pour suivre les modifications, en améliorant l'affichage des versions d'ingestion et en permettant l'archivage des fiches. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité et de l'infrastructure.

### Évolutions fonctionnelles
- Ajout d'un onglet "Journal d'activité" pour suivre les événements importants liés aux documents [#279](https://github.com/refugies-info/playground/pull/279).
- Possibilité d'assigner une fiche à un utilisateur pour le suivi des tâches [#242](https://github.com/refugies-info/playground/pull/242).
- Amélioration de l'affichage des versions d'ingestion des documents, avec un tri par ordre décroissant [#278](https://github.com/refugies-info/playground/pull/278) et un affichage fractionnaire [#277](https://github.com/refugies-info/playground/pull/277).
- Ajout de la possibilité d'archiver les fiches non publiées [#240](https://github.com/refugies-info/playground/pull/240).
- Le bouton "Enregistrer" est maintenant visible même pour les fiches archivées [#237](https://github.com/refugies-info/playground/pull/237).
- Correction d'un bug empêchant la sauvegarde des fiches Bomo [#243](https://github.com/refugies-info/playground/pull/243).
- Correction d'un bug lié à l'affichage des titres des fiches RCO en langage clair [#252](https://github.com/refugies-info/playground/pull/252).
- Correction d'un bug empêchant la sauvegarde des coordonnées GPS [#253](https://github.com/refugies-info/playground/pull/253).
- Ajout d'un message d'avertissement pour indiquer à l'utilisateur qu'il est en train de céder l'édition [#256](https://github.com/refugies-info/playground/pull/256).
- Suppression du blocage de l'édition lors du changement d'onglet ou de la fermeture de l'onglet [#281](https://github.com/refugies-info/playground/pull/281).

### Évolutions techniques
- Mise en place d'un environnement de développement local pour éviter la consommation de ressources de production [#274](https://github.com/refugies-info/playground/pull/274).
- Refactoring du nom de la variable `pendingUpdate` en `previousUpdate` [#270](https://github.com/refugies-info/playground/pull/270).
- Ajout de types pour les logs et gestion des différents événements pour l'enregistrement dans le journal d'activité [#280](https://github.com/refugies-info/playground/pull/280).
- Migration de `author_id` vers `assignee_id` dans les tables concernées [#238](https://github.com/refugies-info/playground/pull/238) et [#242](https://github.com/refugies-info/playground/pull/242).
- Ajout d'une commande pour migrer la base de données [#251](https://github.com/refugies-info/playground/pull/251).
- Amélioration de la gestion des erreurs lors de la mise à jour du statut de conformité [#241](https://github.com/refugies-info/playground/pull/241).
- Correction d'un test Storybook qui bloquait la CI [#239](https://github.com/refugies-info/playground/pull/239).
- Mise à jour des dépendances et correction de vulnérabilités de sécurité [#262](https://github.com/refugies-info/playground/pull/262), [#263](https://github.com/refugies-info/playground/pull/263), [#266](https://github.com/refugies-info/playground/pull/266), [#268](https://github.com/refugies-info/playground/pull/268).
- Ajout d'une action GitHub Actions pour la revue de code Letta [#268](https://github.com/refugies-info/playground/pull/268).

### Autres changements
- Ajout de données de seed pour les tests et le débogage [#269](https://github.com/refugies-info/playground/pull/269).
- Ajout de nouveaux agents traducteurs [#260](https://github.com/refugies-info/playground/pull/260).
- Archivage des anciens assets RCO [#260](https://github.com/refugies-info/playground/pull/260).
- Amélioration de la documentation et des commentaires dans le code.
- Corrections mineures et refactoring du code.
