## Changelog : karfur (30 derniers jours, au 2026-04-21)

### Résumé
Cette période a été marquée par des corrections de bugs et des améliorations de la stabilité, notamment concernant la gestion des données, la sécurité et les performances. Des mises à jour ont été apportées pour corriger des erreurs 500, améliorer la gestion des traductions et renforcer la sécurité en corrigeant des vulnérabilités identifiées par Dependabot. Des optimisations ont également été réalisées pour améliorer les performances du serveur et de l'application mobile.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct des validations et publications dans l'interface. [#3671](https://github.com/refugies-info/karfur/pull/3671)
- Correction d'un problème où les fiches traduites à traduire étaient envoyées sur l'interface. [#3712](https://github.com/refugies-info/karfur/pull/3712)
- Correction de l'affichage des titres dans les popups. [#3718](https://github.com/refugies-info/karfur/pull/3718)
- Correction d'un bug empêchant la prise en compte des favoris sur l'application mobile après validation. [#3649](https://github.com/refugies-info/karfur/pull/3649)
- Mise à jour des informations de contact des opérateurs AGIR. [#3728](https://github.com/refugies-info/karfur/pull/3728)

### Évolutions techniques
- Mise à jour de Next.js en version 15.5.14 dans Storybook pour corriger des vulnérabilités de sécurité. [#3582](https://github.com/refugies-info/karfur/pull/3582)
- Correction de plusieurs vulnérabilités de sécurité identifiées par Dependabot dans diverses dépendances (handlebars, node-forge, brace-expansion, picomatch, etc.). [#3647](https://github.com/refugies-info/karfur/pull/3647), [#3652](https://github.com/refugies-info/karfur/pull/3652), [#3634](https://github.com/refugies-info/karfur/pull/3634)
- Amélioration des performances du serveur en optimisant la récupération des statistiques de traduction et en ajoutant des index MongoDB. [#3691](https://github.com/refugies-info/karfur/pull/3691), [#3610](https://github.com/refugies-info/karfur/pull/3610)
- Mise à jour de Expo SDK à la version 54 pour l'application mobile. [#3650](https://github.com/refugies-info/karfur/pull/3650)
- Ajout d'un outil de débogage pour les erreurs 5xx sur le serveur. [#3670](https://github.com/refugies-info/karfur/pull/3670)
- Mise en place d'un hook GitLeaks pour la détection de secrets dans le code. [#3699](https://github.com/refugies-info/karfur/pull/3699)
- Amélioration de la gestion des erreurs et des validations pour éviter les erreurs 500. [#3721](https://github.com/refugies-info/karfur/pull/3721), [#3714](https://github.com/refugies-info/karfur/pull/3714)
- Refactorings divers pour améliorer la qualité du code et la maintenabilité.

### Autres changements
- Ajout d'une déclaration d'accessibilité partiellement conforme. [#3686](https://github.com/refugies-info/karfur/pull/3686)
- Mise à jour de la documentation et des commentaires.
- Amélioration des tests et de la couverture de code.
- Configuration de release-please pour l'automatisation des versions. [#3630](https://github.com/refugies-info/karfur/pull/3630)
- Suppression de configurations obsolètes.
