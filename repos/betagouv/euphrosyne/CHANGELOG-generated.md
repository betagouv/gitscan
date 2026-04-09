## Changelog : euphrosyne (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la correction de bugs, l'amélioration de la stabilité et la mise à jour des dépendances du projet. Une nouvelle fonctionnalité permettant d'exempter un plan de prévention a été ajoutée dans l'interface d'administration. Des améliorations ont également été apportées à la gestion de l'authentification ORCID.

### Évolutions fonctionnelles
- Ajout d'un commutateur pour exempter un plan de prévention dans l'interface d'administration. [#1807](https://github.com/betagouv/euphrosyne/pull/1807)
- Correction d'un bug empêchant la bonne configuration du statut "is_staff" lors de la vérification ORCID. [#1808](https://github.com/betagouv/euphrosyne/pull/1808)
- Correction d'un test instable lié à la factory de projets. [#1822](https://github.com/betagouv/euphrosyne/pull/1822)

### Évolutions techniques
- Mise à jour de Django en version 6.0.3 pour bénéficier des dernières corrections et améliorations. [#1795](https://github.com/betagouv/euphrosyne/pull/1795)
- Mises à jour de plusieurs dépendances npm (webpack, axios, typescript-eslint, vitest, etc.) pour améliorer la sécurité et les performances.
- Mises à jour de plusieurs dépendances Python (pytest, isort, python-dotenv, dj-database-url, etc.) pour bénéficier des dernières corrections et améliorations.

### Autres changements
- Exécution de `npm audit fix` pour corriger les vulnérabilités détectées dans les dépendances npm. [#1799](https://github.com/betagouv/euphrosyne/pull/1799)
- Amélioration de la position des objectools dans la liste des éléments. [#1820](https://github.com/betagouv/euphrosyne/pull/1820)
