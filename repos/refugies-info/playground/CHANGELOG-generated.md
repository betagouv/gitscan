## Changelog : playground (30 derniers jours, au 8 juin 2026)

### Résumé
Le projet a connu une période d'amélioration continue, axée sur la gestion des fiches, l'affectation des tâches, la gestion des erreurs et l'optimisation des processus d'ingestion de données. Des corrections de bugs et des améliorations de la sécurité ont également été apportées. L'interface utilisateur a été affinée pour une meilleure expérience utilisateur, notamment en ce qui concerne l'affichage des statuts et des dates.

### Évolutions fonctionnelles
- Possibilité d'assigner une fiche à un utilisateur spécifique [#238](https://github.com/refugies-info/playground/pull/238) et [#242](https://github.com/refugies-info/playground/pull/242).
- Amélioration de la sécurité en limitant l'accès à l'assignation d'utilisateurs en fonction des rôles [#20fba359](https://github.com/refugies-info/playground/commit/0fba359).
- Affichage du bouton "Enregistrer" même pour les fiches archivées [#237](https://github.com/refugies-info/playground/pull/237).
- Affichage de la date de fin dans les tableaux [#232](https://github.com/refugies-info/playground/pull/232).
- Ajout du nombre de mots dans le tableau d'ingestion [#230](https://github.com/refugies-info/playground/pull/230).
- Correction d'un bug empêchant la sauvegarde des fiches Bomo [#243](https://github.com/refugies-info/playground/pull/243).
- Correction de l'affichage du statut de publication lorsque qu'il n'y a pas de tag de statut de travail [#f366a51](https://github.com/refugies-info/playground/commit/f366a51).
- Utilisation de la date d'arbitrage au lieu de la date de création pour le suivi et le tri des documents [#233](https://github.com/refugies-info/playground/pull/233).

### Évolutions techniques
- Refactorisation de la logique d'archivage des fiches pour plus de simplicité et de clarté [#240](https://github.com/refugies-info/playground/pull/240).
- Mise à jour de la dépendance `workflow` en version 4.2.5 [#236](https://github.com/refugies-info/playground/pull/236).
- Amélioration de la gestion des erreurs et des autorisations pour les profils utilisateurs [#225](https://github.com/refugies-info/playground/pull/225).
- Optimisation du processus de versioning de l'ingestion en utilisant `di_services_latest` pour éviter les doublons [#571334e](https://github.com/refugies-info/playground/commit/571334e).
- Ajout d'un scan de vulnérabilités des dépendances en pré-push [#244](https://github.com/refugies-info/playground/pull/244).
- Correction de problèmes liés à l'ingestion de données et à la gestion des services DI [#223](https://github.com/refugies-info/playground/pull/223).
- Amélioration de la gestion des variables d'environnement DI et ajout d'un endpoint de débogage [#222](https://github.com/refugies-info/playground/pull/222).
- Correction d'un test Storybook qui bloquait la CI [#239](https://github.com/refugies-info/playground/pull/239).

### Autres changements
- Documentation ajoutée pour l'export et l'import de bases de données Supabase locales [#895e718](https://github.com/refugies-info/playground/commit/895e718).
- Renommage de `author_id` en `assignee_id` pour refléter la nouvelle fonctionnalité d'assignation [#238](https://github.com/refugies-info/playground/pull/238) et [#242](https://github.com/refugies-info/playground/pull/242).
- Suppression des jobs cron temporaires [#226](https://github.com/refugies-info/playground/pull/226) et [#228](https://github.com/refugies-info/playground/pull/228).
- Correction de la gestion des chemins d'analyseur LHEO optionnels [#7b1d4a0](https://github.com/refugies-info/playground/commit/7b1d4a0).
