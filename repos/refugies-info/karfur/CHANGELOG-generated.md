## Changelog : karfur (30 derniers jours)

### Résumé
Les dernières mises à jour de karfur se concentrent sur l'amélioration de la gestion des dispositifs, notamment l'ajout de la gestion des sessions de formation pour les RCO, l'amélioration des webhooks pour la création et la mise à jour des dispositifs, et la correction de plusieurs bugs d'affichage et de fonctionnement. Des optimisations techniques ont également été apportées, notamment au niveau des tests et de la configuration du projet.

### Évolutions fonctionnelles

- Ajout de l'affichage des sessions de formation pour les dispositifs RCO, incluant une nouvelle interface utilisateur et des mises à jour de schéma. [#3481](https://github.com/refugies-info/karfur/pull/3481)
- Amélioration de la gestion des webhooks pour la création et la mise à jour des dispositifs, avec une validation plus stricte des données et une meilleure gestion des traductions. [#3478](https://github.com/refugies-info/karfur/pull/3478)
- Correction d'un bug empêchant le chargement de la liste des fiches en environnement de staging. [#3478](https://github.com/refugies-info/karfur/pull/3478)
- Correction d'un problème d'affichage des listes numérotées qui cassait la mise en page. [#3476](https://github.com/refugies-info/karfur/pull/3476)
- Correction d'une erreur empêchant la visualisation des fiches RCO publiées en mode brouillon. [#3489](https://github.com/refugies-info/karfur/pull/3489)
- Suppression temporaire de la section "équipe" de la page mission et impact. [#3487](https://github.com/refugies-info/karfur/pull/3487)
- Correction d'un bug lié à l'affichage des caractères spéciaux dans les fiches traduites. [#3481](https://github.com/refugies-info/karfur/pull/3481)
- Restriction de l'envoi d'emails pour le réseau MENS. [#3535](https://github.com/refugies-info/karfur/pull/3535)

### Évolutions techniques

- Refactor de la gestion des webhooks, avec la création d'endpoints dédiés pour la création, la mise à jour, la traduction et l'archivage des dispositifs. [#3481](https://github.com/refugies-info/karfur/pull/3481)
- Amélioration de la sécurité et de la validation des données dans les webhooks.
- Mise à jour de la version de Next.js vers la 15.5.10. [#3521](https://github.com/refugies-info/karfur/pull/3521)
- Standardisation et synchronisation des blocs de mémoire des agents. [#3480](https://github.com/refugies-info/karfur/pull/3480)
- Amélioration de la lisibilité du code et ajout de commentaires.
- Amélioration de la gestion des erreurs Zod dans les routes API webhook. [#3541](https://github.com/refugies-info/karfur/pull/3541)
- Refactor de la gestion des sessions de dispositif pour une meilleure organisation des données. [#3539](https://github.com/refugies-info/karfur/pull/3539)

### Autres changements

- Mise à jour des dépendances : tj-actions/changed-files, google-github-actions/auth, google-github-actions/setup-gcloud. [#3525](https://github.com/refugies-info/karfur/pull/3525), [#3524](https://github.com/refugies-info/karfur/pull/3524), [#3523](https://github.com/refugies-info/karfur/pull/3523)
- Suppression du fichier `.envrc` et ajout de `.letta` à `.gitignore`. [#3529](https://github.com/refugies-info/karfur/pull/3529), [#3493](https://github.com/refugies-info/karfur/pull/3493)
- Configuration des pipelines de déploiement CI/CD. [#3520](https://github.com/refugies-info/karfur/pull/3520), [#3504](https://github.com/refugies-info/karfur/pull/3504)
- Unification des branches de production et de staging. [#3503](https://github.com/refugies-info/karfur/pull/3503), [#3502](https://github.com/refugies-info/karfur/pull/3502)
- Amélioration de la documentation.
- Correction de problèmes de style et de formatage du code.
- Ajout de tests unitaires.
