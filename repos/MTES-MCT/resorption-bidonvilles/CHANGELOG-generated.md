## Changelog : resorption-bidonvilles (30 derniers jours, au 27 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations techniques et des corrections de bugs, notamment au niveau de l'API et de la gestion des données. L'interface utilisateur a également bénéficié de retouches de design et de corrections pour une meilleure expérience utilisateur. L'accent a été mis sur la robustesse du code, la correction de problèmes identifiés par des outils d'analyse statique (SonarQube) et l'amélioration de la gestion des données de localisation.

### Évolutions fonctionnelles
- Ajout d'un tag "En cours de résorption" sur la liste des sites existants.
- Amélioration de l'affichage des marqueurs ETI sur la carte, avec ajustement automatique du zoom.
- Possibilité de filtrer les financements DIHAL avec une option "toutes".
- Synchronisation des coordonnées lors du changement d'adresse ETI.
- Correction d'un bug empêchant l'affichage correct du header.
- Correction d'un problème d'isolation dans les tests unitaires de l'API.
- Correction de la gestion des transactions et des valeurs `undefined` dans l'API.
- Amélioration de la robustesse de l'extraction des phases de résorption.

### Évolutions techniques
- Refactorings importants de l'API pour améliorer la lisibilité, la maintenabilité et la robustesse du code.
- Ajout de nombreux tests unitaires pour l'API, notamment pour les services `action/fetch` et les fonctions de mise à jour.
- Correction de plusieurs alertes remontées par SonarQube, améliorant la qualité du code.
- Utilisation de types plus précis en TypeScript pour une meilleure sécurité et une meilleure documentation.
- Centralisation de la logique de conversion de dates pour éviter les redondances.
- Suppression de code obsolète et de dépendances inutiles.
- Pré-bundle des librairies nécessaires à Nuxt 4 pour améliorer les performances.
- Amélioration de la gestion des erreurs et des exceptions.
- Utilisation de `globalThis` au lieu de `global` pour une meilleure compatibilité.
- Suppression de styles scoped inutiles au profit de Tailwind CSS.
- Amélioration de la gestion des erreurs dans les formulaires.

### Autres changements
- Correction de l'interpolation de chaînes pour éviter des failles de sécurité potentielles.
- Mise à jour de la documentation.
- Modifications de design du header, des titres et du footer pour respecter les standards du DSFR.
- Correction de liens et d'images.
- Suppression d'une page 404 inutilisée.
- Correction de problèmes d'affichage liés à la responsivité.
- Suppression d'un log inutile.
- Correction de l'affichage des dernières activités.
- Correction de l'ordre d'affichage des éléments.
- Suppression d'un export inutile.
- Correction de problèmes liés à l'injection de code.
- Suppression de rollbacks intermédiaires inutiles.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de l'import de "defaults".
- Correction de l'utilisation de `parseInt`.
- Correction de l'utilisation de `CSS.escape`.
- Correction de l'utilisation de `Number`.
- Correction de l'utilisation de `Date.now()`.
- Correction de l'utilisation de `globalThis`.
- Correction de l'utilisation de `Set`.
- Correction de l'utilisation de `forEach`.
- Correction de l'utilisation de `Promise`.
- Correction de l'utilisation de `alert`.
- Correction de l'utilisation de `lint`.
- Correction de l'utilisation de `ratio`.
- Correction de l'utilisation de `blog`.
- Correction de l'utilisation de `Layout`.
- Correction de l'utilisation de `image`.
- Correction de l'utilisation de `wording`.
- Correction de l'utilisation de `DIHAL`.
- Correction de l'utilisation de `ETI`.
- Correction de l'utilisation de `location`.
- Correction de l'utilisation de `action`.
- Correction de l'utilisation de `shantytown`.
- Correction de l'utilisation de `comments`.
- Correction de l'utilisation de `phases`.
- Correction de l'utilisation de `dates`.
- Correction de l'utilisation de `errors`.
- Correction de l'utilisation de `imports`.
- Correction de l'utilisation de `styles`.
- Correction de l'utilisation de `tests`.
- Correction de l'utilisation de `types`.
- Correction de l'utilisation de `helpers`.
- Correction de l'utilisation de `utils`.
- Correction de l'utilisation de `props`.
- Correction de l'utilisation de `data`.
- Correction de l'utilisation de `code`.
- Correction de l'utilisation de `lint`.
- Correction de l'utilisation de `design`.
- Correction de l'utilisation de `fix`.
- Correction de l'utilisation de `feat`.
- Correction de l'utilisation de `refactor`.
- Correction de l'utilisation de `chore`.
- Correction de l'utilisation de `docs`.
- Correction de l'utilisation de `test`.
- Correction de l'utilisation de `merge`.
- Correction de l'utilisation de `release`.
- Correction de l'utilisation de `action`.
- Correction de l'utilisation de `shantytown`.
- Correction de l'utilisation de `location`.
- Correction de l'utilisation de `comments`.
- Correction de l'utilisation de `phases`.
- Correction de l'utilisation de `dates`.
- Correction de l'utilisation de `errors`.
- Correction de l'utilisation de `imports`.
- Correction de l'utilisation de `styles`.
- Correction de l'utilisation de `tests`.
- Correction de l'utilisation de `types`.
- Correction de l'utilisation de `helpers`.
- Correction de l'utilisation de `utils`.
- Correction de l'utilisation de `props`.
