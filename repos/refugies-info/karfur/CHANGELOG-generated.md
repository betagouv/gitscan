## Changelog : karfur (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à karfur au cours des 30 derniers jours. Les modifications incluent des améliorations de l'interface utilisateur, notamment la gestion des logos des structures et l'affichage des sessions de formation, ainsi que des corrections de bugs et des optimisations techniques pour améliorer la stabilité et la performance de la plateforme. De nouvelles fonctionnalités ont été ajoutées pour faciliter la publication de fiches traduites et la gestion des webhooks.

### Évolutions fonctionnelles

- Possibilité pour les administrateurs de modifier le logo d'une structure directement depuis l'interface d'administration. [#3546](https://github.com/refugies-info/karfur/pull/3546)
- Amélioration de l'affichage des sessions de formation pour les dispositifs RCO, avec une nouvelle interface utilisateur. [#3481](https://github.com/refugies-info/karfur/pull/3481)
- Correction d'un bug empêchant la visualisation correcte des fiches RCO publiées en plusieurs langues. [#3489](https://github.com/refugies-info/karfur/pull/3489)
- Correction d'une erreur lors de la publication de fiches traduites. [#3481](https://github.com/refugies-info/karfur/pull/3481)
- Amélioration de l'affichage des sessions avec une meilleure gestion des cas où il y a plusieurs sessions pour un même dispositif. [#3482](https://github.com/refugies-info/karfur/pull/3482)
- Pagination des résultats de recherche au lieu du défilement infini. [#3527](https://github.com/refugies-info/karfur/pull/3527)
- Suppression temporaire de la section "équipe" sur la page mission et impact. [#3487](https://github.com/refugies-info/karfur/pull/3487)

### Évolutions techniques

- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans la gestion des webhooks et des schémas de données.
- Amélioration de la gestion des erreurs Zod dans les routes API des webhooks. [#3541](https://github.com/refugies-info/karfur/pull/3541)
- Mise à jour des schémas de publication pour inclure les données des cartes (POI). [#3543](https://github.com/refugies-info/karfur/pull/3543)
- Amélioration de la sécurité en validant le format des ObjectId dans les webhooks.
- Refactorisation de la gestion des thèmes et des webhooks pour une meilleure cohérence.
- Standardisation de la configuration des agents mémoire. [#3480](https://github.com/refugies-info/karfur/pull/3480)
- Mise à jour de Next.js vers la version 15.5.10. [#3521](https://github.com/refugies-info/karfur/pull/3521)
- Amélioration de la gestion des erreurs et de la robustesse du code.
- Utilisation de `tj-actions/changed-files` au lieu de `dorny/paths-filter` dans les workflows CI/CD. [#3520](https://github.com/refugies-info/karfur/pull/3520)

### Autres changements

- Ajout de documentation pour le nouveau point de terminaison webhook des thèmes.
- Ajout d'une configuration worktree pour faciliter le développement. [#3530](https://github.com/refugies-info/karfur/pull/3530)
- Suppression du fichier `.envrc` et ajout à `.gitignore`. [#3529](https://github.com/refugies-info/karfur/pull/3529)
- Correction de la configuration des scripts de déploiement.
- Suppression des builds mobiles standalone.
- Correction de faux positifs dans l'analyse statique du code avec Knip.
- Mise à jour des dépendances (tj-actions/changed-files, google-github-actions/auth, google-github-actions/setup-gcloud).
