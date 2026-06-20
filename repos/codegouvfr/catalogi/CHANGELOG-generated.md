## Changelog : catalogi (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions de catalogi se concentrent sur l'amélioration de l'administration et de la gestion des logiciels, notamment avec l'ajout de protections logicielles et de configurations plus fines via l'interface utilisateur. Des améliorations ont également été apportées à l'importation de données depuis différentes sources et à la stabilité des tests.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer l'affichage des logiciels sur la page d'accueil via l'interface utilisateur. [#38c7e06](https://github.com/codegouvfr/catalogi/commit/38c7e06)
- Implémentation de protections logicielles, visualisables dans une modale avec un message d'administration. [#5911dfc](https://github.com/codegouvfr/catalogi/commit/5911dfc)
- Ajout de la gestion des organisations sur Wikidata, permettant de récupérer et rechercher des informations. [#505](https://github.com/codegouvfr/catalogi/issues/505) et [#0459d87](https://github.com/codegouvfr/catalogi/commit/0459d87)
- Possibilité de récupérer tous les identifiants sur HAL (Hyper Article en Ligne). [#515](https://github.com/codegouvfr/catalogi/issues/515) et [#dd3a12a](https://github.com/codegouvfr/catalogi/commit/dd3a12a)
- Amélioration de l'interface d'administration avec des contraintes de largeur et troncature des étiquettes d'attributs longs. [#b9f8d89](https://github.com/codegouvfr/catalogi/commit/b9f8d89)
- Restriction de l'accès aux attributs personnalisés en mode administration. [#52bdc24](https://github.com/codegouvfr/catalogi/commit/52bdc24)
- Ajout d'un rôle administrateur et d'une page d'administration pour gérer les attributs personnalisés. [#46170aa](https://github.com/codegouvfr/catalogi/commit/46170aa)

### Évolutions techniques
- Refactorisation du filtre SQL pour améliorer les performances lors de la récupération des sources. [#538df80](https://github.com/codegouvfr/catalogi/commit/538df80) et [#9467c74](https://github.com/codegouvfr/catalogi/commit/9467c74)
- Amélioration de la configuration de l'importation automatique pour éviter la création d'entrées utilisateur inutiles. [#89152dd](https://github.com/codegouvfr/catalogi/commit/89152dd)
- Correction de l'ordre des tests pour garantir une exécution déterministe. [#4f47f1e](https://github.com/codegouvfr/catalogi/commit/4f47f1e)
- Mise en cache des navigateurs Playwright pour accélérer l'exécution des tests en CI. [#29ee9e4](https://github.com/codegouvfr/catalogi/commit/29ee9e4)
- Correction des problèmes d'installation et d'exécution des tests Playwright en CI. [#ec39f26](https://github.com/codegouvfr/catalogi/commit/ec39f26) et [#2f6c8f2](https://github.com/codegouvfr/catalogi/commit/2f6c8f2)
- Amélioration de la résolution des identifiants de dépôt à partir de la configuration de la source. [#457d81e](https://github.com/codegouvfr/catalogi/commit/457d81e)
- Correction d'un bug empêchant le nom du logiciel de se baser sur les sources. [#909e86e](https://github.com/codegouvfr/catalogi/commit/909e86e)

### Autres changements
- Documentation clarifiée concernant le routage de l'API Helm. [#5717d54](https://github.com/codegouvfr/catalogi/commit/5717d54)
- Ajout d'un script de démarrage de la base de données racine. [#8bf9747](https://github.com/codegouvfr/catalogi/commit/8bf9747)
- Correction d'un bug lié à la fermeture des requêtes de fusion GitHub. [#9182681](https://github.com/codegouvfr/catalogi/commit/9182681)
- Réorganisation des migrations. [#f7b1ca9](https://github.com/codegouvfr/catalogi/commit/f7b1ca9)
- Améliorations suite aux revues de code. [#8d99f34](https://github.com/codegouvfr/catalogi/commit/8d99f34)
