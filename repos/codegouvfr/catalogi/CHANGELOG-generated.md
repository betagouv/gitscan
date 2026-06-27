## Changelog : catalogi (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions de catalogi se concentrent sur l'amélioration de l'importation et de la gestion des sources de données externes, ainsi que sur l'expérience utilisateur avec l'ajout de protections logicielles et la configuration de la page d'accueil. Des corrections et optimisations ont également été apportées pour stabiliser les tests et améliorer la performance.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer les cartes de sélection de logiciels sur la page d'accueil via l'interface utilisateur [#38c7e06](https://github.com/codegouvfr/catalogi/commit/38c7e06).
- Implémentation de l'affichage des protections logicielles dans une modale avec un message d'administration [#5911dfc](https://github.com/codegouvfr/catalogi/commit/5911dfc).
- Amélioration de la recherche et de la récupération des organisations sur Wikidata [#505](https://github.com/codegouvfr/catalogi/issues/505).
- Ajout de la récupération de tous les identifiants sur HAL [#515](https://github.com/codegouvfr/catalogi/issues/515).
- Possibilité de bloquer l'API de création de logiciel lorsque l'utilisation de l'interface "ajouter un logiciel ou service" est désactivée [#0863b05](https://github.com/codegouvfr/catalogi/commit/0863b05).
- Réintégration de la métadonnée de dépôt sur GitHub pour les références de données externes [#547](https://github.com/codegouvfr/catalogi/issues/547).

### Évolutions techniques
- Optimisation de la requête SQL pour l'importation de données par source, effectuant le filtrage directement en base de données [#538df80](https://github.com/codegouvfr/catalogi/commit/538df80).
- Amélioration de la stabilité des tests Playwright, notamment en stabilisant les assertions sur les logiciels similaires [#b400140](https://github.com/codegouvfr/catalogi/commit/b400140) et en fixant l'installation et l'exécution des navigateurs en CI [#ec39f26](https://github.com/codegouvfr/catalogi/commit/ec39f26).
- Refactorisation du code pour utiliser des objets en entrée et renommer les variables [#89152dd](https://github.com/codegouvfr/catalogi/commit/89152dd).
- Mise en cache des navigateurs Playwright pour accélérer l'exécution des tests en CI [#29ee9e4](https://github.com/codegouvfr/catalogi/commit/29ee9e4).
- Correction de l'ordre des tests pour éviter les problèmes de concurrence [#4f47f1e](https://github.com/codegouvfr/catalogi/commit/4f47f1e).

### Autres changements
- Documentation clarifiée concernant le routage de l'API Helm [#5717d54](https://github.com/codegouvfr/catalogi/commit/5717d54).
- Ajout d'un script pour initialiser la base de données racine [#8bf9747](https://github.com/codegouvfr/catalogi/commit/8bf9747).
- Correction de l'espacement entre le héros de la page d'accueil et la sélection des logiciels [#9e0e76f](https://github.com/codegouvfr/catalogi/commit/9e0e76f).
- Correction d'un bug empêchant le nom du logiciel de se baser sur les sources [#909e86e](https://github.com/codegouvfr/catalogi/commit/909e86e).
- Correction de l'ordre des tests [#d5df4ea](https://github.com/codegouvfr/catalogi/commit/d5df4ea).
- Amélioration suite à revue de code [#8d99f34](https://github.com/codegouvfr/catalogi/commit/8d99f34).
- Ajout d'un test et correction de la fermeture de la pull request pour github [#9182681](https://github.com/codegouvfr/catalogi/commit/9182681).
- Correction de l'ordre des migrations [#f7b1ca9](https://github.com/codegouvfr/catalogi/commit/f7b1ca9).
