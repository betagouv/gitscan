## Changelog : bal (30 derniers jours, au 18 juin 2026)

### Résumé
Cette version apporte des améliorations à l'importation de données Akto, corrige des erreurs typographiques et des problèmes liés aux listes de diffusion. Des migrations de serveurs ont également été effectuées pour les environnements de production et de recette. Enfin, des sous-modules obsolètes ont été supprimés pour simplifier l'infrastructure.

### Évolutions fonctionnelles
- Importation des données Akto : Ajout de la fonctionnalité d'importation des données Akto. [#518](https://github.com/mission-apprentissage/bal/issues/518)
- Correction des listes de diffusion : Résolution d'un problème empêchant la mise à jour correcte des listes de diffusion LBA. [#520](https://github.com/mission-apprentissage/bal/issues/520)
- Mise à jour de la clé Akto : La clé Akto a été mise à jour. [#519](https://github.com/mission-apprentissage/bal/issues/519)

### Évolutions techniques
- Suppression des sous-modules : Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` pour simplifier l'infrastructure. [#522](https://github.com/mission-apprentissage/bal/issues/522)
- Migration des serveurs : Migration des serveurs `bal-production` et `bal-recette`. [#525](https://github.com/mission-apprentissage/bal/issues/525) et [#523](https://github.com/mission-apprentissage/bal/issues/523)
- Ajout de descripteurs de modèles manquants : Correction de l'absence de descripteurs de modèles. [#521](https://github.com/mission-apprentissage/bal/issues/521)

### Autres changements
- Correction de fautes de frappe : Correction de quelques erreurs typographiques dans le code. [#524](https://github.com/mission-apprentissage/bal/issues/524)
