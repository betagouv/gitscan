## Changelog : catalogi (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de catalogi, axées sur une refonte majeure de la gestion des types de logiciels. Ces changements visent à unifier et simplifier la représentation des logiciels dans le catalogue, améliorant ainsi la cohérence des données et facilitant l'intégration avec d'autres systèmes. Des tests d'intégration de bout en bout ont également été ajoutés pour garantir la qualité du logiciel.

### Évolutions fonctionnelles
- Amélioration de la gestion des liens externes : correction d'un bug qui empêchait la mise à jour correcte des liens externes vers les logiciels. [#726ce20](https://github.com/codegouvfr/catalogi/commit/726ce20)
- Ajout d'un nouveau point de terminaison API `/v2/catalogi.json` qui renvoie la liste complète des logiciels. [#9980212](https://github.com/codegouvfr/catalogi/commit/9980212)

### Évolutions techniques
- Refactor majeur de la gestion des types de logiciels (issue #491) :
    - Définition de nouveaux types de logiciels canoniques avec des alias. [#7e3f7e7](https://github.com/codegouvfr/catalogi/commit/7e3f7e7)
    - Renommage des colonnes de la table `softwares` pour correspondre au nouveau schéma canonique. [#b25d1fa](https://github.com/codegouvfr/catalogi/commit/b25d1fa)
    - Suppression des anciennes données externes et migration vers le nouveau schéma. [#f556bd9](https://github.com/codegouvfr/catalogi/commit/f556bd9)
    - Remplacement du type `SoftwareType` par `operatingSystems` et `runtimePlatforms`. [#0100fa5](https://github.com/codegouvfr/catalogi/commit/0100fa5)
    - Mise à jour des types API et web pour correspondre au nouveau schéma canonique. [#2cc2ee4](https://github.com/codegouvfr/catalogi/commit/2cc2ee4)
    - Ajout d'une passerelle source canonique et migration de l'autocomplétion. [#4fe147a](https://github.com/codegouvfr/catalogi/commit/4fe147a)
    - Suppression de l'espace de noms Db hérité et correction des fixtures Zenodo. [#51ad6b9](https://github.com/codegouvfr/catalogi/commit/51ad6b9)
    - Renommage de `logoUrl` en `image`. [#f556bd9](https://github.com/codegouvfr/catalogi/commit/f556bd9)
- Ajout de tests d'intégration de bout en bout avec Playwright et Testcontainers, incluant l'authentification Keycloak. [#47e483e](https://github.com/codegouvfr/catalogi/commit/47e483e)
- Documentation : ajout d'une feuille de route pour l'unification des types de logiciels. [#fe94aa5](https://github.com/codegouvfr/catalogi/commit/fe94aa5) et mise à jour de la feuille de route existante [#80842d9](https://github.com/codegouvfr/catalogi/commit/80842d9) et [#78320a4](https://github.com/codegouvfr/catalogi/commit/78320a4)

### Autres changements
- Mise à jour de la version du projet. [#05ff366](https://github.com/codegouvfr/catalogi/commit/05ff366) et [#827f2a1](https://github.com/codegouvfr/catalogi/commit/827f2a1)
- Ajout d'un fichier de documentation ignoré par Git. [#6dc158a](https://github.com/codegouvfr/catalogi/commit/6dc158a)
