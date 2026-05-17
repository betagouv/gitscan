## Changelog : mon-entreprise (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la modernisation de l'infrastructure du projet, notamment avec la migration vers Next.js 16 et une refonte complète des workflows GitHub Actions. Des corrections de bugs ont également été apportées, notamment concernant le calcul de l'IR pour les auto-entrepreneurs et la gestion des erreurs Algolia.

### Évolutions fonctionnelles

- Mise en place de la traduction de la page d'accueil avec Next.js 16 et i18n SSR. [#4215](https://github.com/betagouv/mon-entreprise/issues/4215)
- Correction du calcul de l'IR pour les auto-entrepreneurs. [#4105](https://github.com/betagouv/mon-entreprise/issues/4105)

### Évolutions techniques

- Migration vers Next.js 16 avec support SSR et i18n. [#4215](https://github.com/betagouv/mon-entreprise/issues/4215)
- Refonte complète des workflows GitHub Actions pour améliorer la clarté, la robustesse et l'intégration avec OIDC.
- Séparation des tests E2E de production dans un workflow dédié.
- Amélioration de la gestion des erreurs Algolia avec la capture et la journalisation des erreurs du script de cleanup.
- Isolation du téléchargement d'artefacts pour calmer CodeQL.
- Découpage du script `update-data` Algolia en `export-data` et `push-data` pour plus de modularité.
- Correction d'un problème de FOUC (Flash of Unstyled Content) en corrigeant l'utilisation de `navigator` en environnement Node 24.

### Autres changements

- Correction de l'envoi d'échecs de chargement Piano Analytics à Sentry.
- Ajout d'un fichier `.gitignore` pour `next-env.d.ts` généré par Next.js.
- Correction du fichier `flake.nix`.
- Renommage de plusieurs workflows GitHub Actions pour une meilleure lisibilité.
- Traitement des warnings CodeQL sur le checkout de ref non vérifié.
- Ajout de l'environnement `master` au job `npm-publish` pour OIDC.
- Correction de la syntaxe invalide `secrets: inherit` dans `workflow_call`.
- Renommage du fichier `publish.yaml` en `npm-publish.yaml`.
