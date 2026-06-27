## Changelog : a-just (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'un système de feedback intégré, des améliorations sur la page "Panorama" et la gestion des dates. Des corrections et des optimisations techniques ont également été apportées pour stabiliser l'application et améliorer les tests.

### Évolutions fonctionnelles
- Ajout d'un système de feedback utilisateur permettant aux utilisateurs de noter et commenter l'application A-JUST [#89024c55](https://github.com/betagouv/a-just/commit/89024c55).
- Amélioration de la gestion des dates sur la page "Situation à prendre en compte" pour une meilleure précision et une plus grande flexibilité [#aa0879f8](https://github.com/betagouv/a-just/commit/aa0879f8).
- Possibilité de saisir manuellement les dates dans les composants `aj-date-select` et `aj-date-select-blue` [#761752ed](https://github.com/betagouv/a-just/commit/761752ed).
- Ajout d'une page d'administration pour consulter les avis utilisateurs (historique, notes moyennes, commentaires) [#f3001459](https://github.com/betagouv/a-just/commit/f3001459).
- Amélioration de l'affichage des informations sur la page "Panorama" pour les utilisateurs sans droits de modification des ressources humaines [#7141b0fe](https://github.com/betagouv/a-just/commit/7141b0fe).
- Mise à jour des textes d'aide pour la démo "Panorama" [#41f42fc2](https://github.com/betagouv/a-just/commit/41f42fc2).
- Possibilité de dupliquer les agents [#dd034c15](https://github.com/betagouv/a-just/commit/dd034c15).
- Synchronisation des origines [#c7a3d05a](https://github.com/betagouv/a-just/commit/c7a3d05a).

### Évolutions techniques
- Refactorisation du workflow GitHub Actions pour simplifier les déploiements [#2ce96a06](https://github.com/betagouv/a-just/commit/2ce96a06).
- Mise à jour de la configuration de Cypress [#e67c7077](https://github.com/betagouv/a-just/commit/e67c7077).
- Amélioration des tests E2E pour la page "Panorama" [#66f76958](https://github.com/betagouv/a-just/commit/66f76958).
- Correction de bugs et optimisation des requêtes Sequelize [#06e52cb2](https://github.com/betagouv/a-just/commit/06e52cb2).
- Correction de problèmes liés à la gestion des dates et des types dans les requêtes API [#ec31cd51](https://github.com/betagouv/a-just/commit/ec31cd51).
- Suppression de code commenté et de fichiers inutiles pour améliorer la lisibilité et la maintenabilité du code.
- Mise à jour des fichiers de nomenclature [#09f0d356](https://github.com/betagouv/a-just/commit/09f0d356).

### Autres changements
- Mise à jour des fichiers Excel pour l'extracteur d'effectifs [#3f3e31de](https://github.com/betagouv/a-just/commit/3f3e31de) et l'extracteur-collecte-2026 [#216bf323](https://github.com/betagouv/a-just/commit/216bf323).
- Ajout de CSP security [#88bcc8ef](https://github.com/betagouv/a-just/commit/88bcc8ef) et [#4cc7bcff](https://github.com/betagouv/a-just/commit/4cc7bcff).
- Correction de la catégorisation ASA [#9e73db5c](https://github.com/betagouv/a-just/commit/9e73db5c).
- Ajout du nom de l'agent à l'utilisation [#cc8242bc](https://github.com/betagouv/a-just/commit/cc8242bc).
- Correction de l'affichage du "se projecter" en "greffe" [#76cde8dc](https://github.com/betagouv/a-just/commit/76cde8dc).
- Ajout de logs pour faciliter le débogage [#c9d8277e](https://github.com/betagouv/a-just/commit/c9d8277e) et [#66dc8923](https://github.com/betagouv/a-just/commit/66dc8923).
- Correction de la gestion de l'état de chargement dans le composant `PopinEditActivitiesComponent` [#8bb98145](https://github.com/betagouv/a-just/commit/8bb98145).
- Correction de l'appel de script JS [#5a8c4c9d](https://github.com/betagouv/a-just/commit/5a8c4c9d).
- Mise à jour du numéro de version pour la release [#6131eabc](https://github.com/betagouv/a-just/commit/6131eabc).
