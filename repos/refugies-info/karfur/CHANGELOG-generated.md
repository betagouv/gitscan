## Changelog : karfur (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration des performances et de la stabilité de l'application, notamment au niveau de la recherche et du chargement des données. Des corrections de bugs ont été apportées pour améliorer l'expérience utilisateur, en particulier concernant l'affichage des fiches et des sessions. De nouvelles fonctionnalités ont été implémentées, comme l'intégration de Speedgoose pour la mise en cache et l'amélioration de la gestion des webhooks.

### Évolutions fonctionnelles
- Correction de l'affichage des logos des structures, désormais modifiables depuis l'administration. [#3546](https://github.com/refugies-info/karfur/pull/3546)
- Amélioration de l'affichage des sessions pour les dispositifs RCO, avec une nouvelle interface et une meilleure gestion des cas multiples. [#3482](https://github.com/refugies-info/karfur/pull/3482)
- Correction d'un bug empêchant l'affichage correct des fiches traduites. [#3494](https://github.com/refugies-info/karfur/pull/3494)
- Ajout de la possibilité de filtrer les contributions des utilisateurs par origine (RI). [#3482](https://github.com/refugies-info/karfur/pull/3482)
- Correction d'un bug empêchant l'affichage correct des fiches RCO publiées en brouillon. [#3489](https://github.com/refugies-info/karfur/pull/3489)
- Suppression temporaire de la section "équipe" sur la page mission et impact. [#3487](https://github.com/refugies-info/karfur/pull/3487)

### Évolutions techniques
- Implémentation de Speedgoose pour la mise en cache des requêtes fréquentes, améliorant ainsi les performances. [#3556](https://github.com/refugies-info/karfur/pull/3556), [#3558](https://github.com/refugies-info/karfur/pull/3558)
- Refactorisation de l'architecture de recherche pour utiliser une pagination côté serveur, améliorant la réactivité et la scalabilité.
- Migration des schémas MongoDB vers des modèles partagés pour une meilleure cohérence et maintenabilité. [#3555](https://github.com/refugies-info/karfur/pull/3555)
- Mise à jour de la bibliothèque Brevo vers la version 5. [#3550](https://github.com/refugies-info/karfur/pull/3550)
- Mise à jour de Storybook vers la version 10.2 avec migration vers Vite. [#3553](https://github.com/refugies-info/karfur/pull/3553)
- Unification des branches de production et de staging. [#3502](https://github.com/refugies-info/karfur/pull/3502), [#3503](https://github.com/refugies-info/karfur/pull/3503)
- Amélioration de la gestion des erreurs Zod dans les routes API webhook. [#3541](https://github.com/refugies-info/karfur/pull/3541)
- Mise à jour des dépendances et suppression des scripts PR obsolètes. [#3548](https://github.com/refugies-info/karfur/pull/3548)

### Autres changements
- Documentation de l'utilisation de REDIS_URI dans les environnements client et serveur. [#3558](https://github.com/refugies-info/karfur/pull/3558)
- Ajout de tests pour la modification du mot de passe. [#3557](https://github.com/refugies-info/karfur/pull/3557)
- Correction de divers problèmes de typage et de validation.
- Amélioration de la robustesse de l'application face à des données incorrectes ou manquantes.
- Suppression du fichier `.envrc` et ajout de `.letta` à `.gitignore`.
- Correction de problèmes de build et de déploiement.
- Ajout d'une configuration worktrunk pour la gestion des branches de travail.
