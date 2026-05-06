## Changelog : nosgestesclimat-app (30 derniers jours, au 04 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de suivi des données, de correction de bugs et de refonte de l'architecture interne pour faciliter le développement futur. Des améliorations d'accessibilité et de documentation ont également été apportées. Une migration vers une structure de monorepo a été initiée, ouvrant la voie à une meilleure organisation du code et une collaboration plus efficace.

### Évolutions fonctionnelles
- Correction de l'ordre d'affichage des points sur les graphiques. [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780)
- Suppression de la bannière JVA. [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779)
- Correction de l'affichage des noms des participants et administrateurs. [NGC-3313](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773)
- Déblocage du bouton "Terminer" après avoir répondu à toutes les questions. [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776)
- Ajout d'un bouton "Je ne sais pas" en test A/B pour certaines questions. [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737)
- Ajout d'une route pour la suppression logicielle des simulations. [#462](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/462)
- Ajout d'une nouvelle question sur la consommation d'électricité avec un switch. [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701)
- Suppression des balises hreflang si la page n'est disponible qu'en français. [#1719](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1719)
- Amélioration du suivi des données sur le site et dans les iframes. [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782)
- Ajout de suivi pour la page "/fin".
- Correction de l'affichage de la bannière. [NGC-3240](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749)

### Évolutions techniques
- Migration vers une architecture monorepo pour une meilleure organisation du code.
- Refonte du CI/CD pour s'adapter à la structure monorepo.
- Mise en place de devcontainers pour un environnement de développement cohérent.
- Amélioration de la gestion des dépendances et du build.
- Refactorisation du code de suivi et de gestion des cookies. [#1669](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1669)
- Optimisation du schéma anonyme. [#465](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/465)
- Mise à jour des configurations ESLint et TypeScript.
- Correction de plusieurs erreurs liées au déploiement sur Scalingo et GitHub Actions.
- Ajout d'un fichier `.pnpm-store` à ignorer par Git.
- Suppression de fichiers inutilisés.
- Mise à jour des dépendances et des scripts de build.

### Autres changements
- Ajout de documentation sur l'installation du projet. [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733)
- Corrections d'accessibilité. [#1703](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1703)
- Ajout de traductions. [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769)
- Correction de l'opérateur `!=` dans les conditions des funfacts. [NGC-3226](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755)
- Amélioration des logs d'erreurs de session.
- Ajout d'un feature flag pour les actions. [NGC-3294](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775)
- Publication de la version 2.56.0 et 2.55.7.
