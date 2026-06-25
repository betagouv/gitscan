## Changelog : a-just (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout d'un système de feedback, des améliorations sur la page "Panorama" (aide à l'utilisation, tests automatisés), et des corrections concernant la gestion des dates et des situations des agents. Des améliorations techniques ont également été apportées pour faciliter le développement et le déploiement.

### Évolutions fonctionnelles
- Ajout d'un système de feedback utilisateur permettant aux utilisateurs de noter et commenter l'application a-just [#89024c55](https://github.com/betagouv/a-just/commit/89024c55).
- Amélioration de la page "Panorama" avec un guide pas à pas (IntroJS) pour faciliter la prise en main et une meilleure compréhension des fonctionnalités [#3b7e92a8](https://github.com/betagouv/a-just/commit/3b7e92a8).
- Possibilité de saisir manuellement les dates dans le composant `aj-date-select` et `aj-date-select-blue` [#761752ed](https://github.com/betagouv/a-just/commit/761752ed).
- Amélioration de la gestion de la date de début d'un statut lors de la création d'un enregistrement d'agent [#b27b19f7](https://github.com/betagouv/a-just/commit/b27b19f7).
- Ajout d'une page d'administration pour consulter les avis utilisateurs (historique, notes moyennes, commentaires) [#f3001459](https://github.com/betagouv/a-just/commit/f3001459).
- Affichage conditionnel d'un bouton "Qu'est-ce que c'est ?" pour les utilisateurs sans permission d'édition des ressources humaines [#7141b0fe](https://github.com/betagouv/a-just/commit/7141b0fe).

### Évolutions techniques
- Refactorisation des workflows GitHub Actions pour simplifier le déploiement [#2ce96a06](https://github.com/betagouv/a-just/commit/2ce96a06).
- Mise à jour de la configuration Cypress [#e67c7077](https://github.com/betagouv/a-just/commit/e67c7077).
- Amélioration des tests E2E pour la page "Panorama" et la saisie de données de contentieux [#66f76958](https://github.com/betagouv/a-just/commit/66f76958).
- Correction de problèmes liés à l'utilisation de `koa-smart` et gestion des erreurs HTTP [#ec31cd51](https://github.com/betagouv/a-just/commit/ec31cd51).
- Mise à jour de l'extracteur de données pour utiliser les nouveaux fichiers [#12fdf48f](https://github.com/betagouv/a-just/commit/12fdf48f).
- Correction de la gestion de l'état de chargement dans le composant `PopinEditActivitiesComponent` [#8bb98145](https://github.com/betagouv/a-just/commit/8bb98145).
- Ajout de mesures de sécurité CSP (Content Security Policy) [#88bcc8ef](https://github.com/betagouv/a-just/commit/88bcc8ef) et [#4cc7bcff](https://github.com/betagouv/a-just/commit/4cc7bcff).

### Autres changements
- Mise à jour des fichiers de nomenclature [#09f0d356](https://github.com/betagouv/a-just/commit/09f0d356).
- Corrections de typos et améliorations de la documentation [#76cde8dc](https://github.com/betagouv/a-just/commit/76cde8dc) et [#1fde3081](https://github.com/betagouv/a-just/commit/1fde3081).
- Suppression de code commenté et de fichiers inutiles [#8223a9b1](https://github.com/betagouv/a-just/commit/8223a9b1), [#32a0f972](https://github.com/betagouv/a-just/commit/32a0f972), [#7f9788c3](https://github.com/betagouv/a-just/commit/7f9788c3) et [#b1db5b53](https://github.com/betagouv/a-just/commit/b1db5b53).
- Ajout du nom de l'agent à l'usage [#cc8242bc](https://github.com/betagouv/a-just/commit/cc8242bc).
- Correction de la catégorisation ASA [#9e73db5c](https://github.com/betagouv/a-just/commit/9e73db5c).
- Correction de l'affichage des dates dans le cockpit [#fdad6960](https://github.com/betagouv/a-just/commit/fdad6960).
- Correction de l'accès aux juridictions CLE [#54a8ae17](https://github.com/betagouv/a-just/commit/54a8ae17).
