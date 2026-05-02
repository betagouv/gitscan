## Changelog : nosgestesclimat-app (30 derniers jours, au 2026-04-30)

### Résumé
Ce mois-ci, l'application a bénéficié d'une refonte technique importante avec la migration vers une architecture monorepo, améliorant la structure du projet et facilitant le développement. De nombreuses corrections de bugs ont été apportées, notamment concernant le fonctionnement des tests, le déploiement et l'affichage des informations utilisateur. Des améliorations ont également été apportées au suivi des événements (tracking) et à l'accessibilité.

### Évolutions fonctionnelles
- Ajout d'un bouton "Je ne sais pas" pour certaines questions, dans le cadre d'un test A/B. [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737)
- Ajout d'une bannière JVA (Justice Verte et Accès). [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748)
- Possibilité de supprimer une simulation depuis l'espace personnel. [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747)
- Nouvelle option pour la question sur la consommation d'électricité. [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701)
- Suppression des balises meta hreflang si la page est uniquement en français. [#1719](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1719)
- Amélioration du partage de données via iframe. [#1732](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1732)
- Ajout de la documentation sur l'installation du projet. [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733)
- Améliorations d'accessibilité. [#1703](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1703)

### Évolutions techniques
- Migration vers une architecture monorepo. [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745)
- Refonte de la configuration CI/CD et des workflows. [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765)
- Mise à jour de Prisma vers la version 7.0.
- Amélioration du suivi des événements (tracking) et de la gestion des cookies. [#1669](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1669)
- Refactorisation de la configuration Sentry pour une meilleure gestion des releases et des stacktraces.
- Mise en place de devcontainers pour faciliter le développement local. [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751)
- Correction de problèmes de déploiement sur Scalingo et en préproduction.
- Amélioration de la gestion des erreurs et des logs.
- Correction de problèmes liés aux tests (E2E, unitaires).
- Mise à jour des dépendances.

### Autres changements
- Ajout de "feature flags" pour activer/désactiver certaines fonctionnalités (actions). [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775)
- Amélioration de la documentation README.
- Correction de divers problèmes mineurs et améliorations de la qualité du code.
- Ajout de la possibilité de récupérer uniquement les données Matomo avec un token sécurisé. [#1770](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1770)
- Correction de l'affichage du nom des participants et des administrateurs. [#1773](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773)
- Correction d'un bug empêchant le bouton "Terminer" de fonctionner après avoir atteint la dernière question. [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776)
- Correction de l'opérateur `!=` dans les conditions des "funfacts". [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755)
- Ajout de traductions. [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769)
