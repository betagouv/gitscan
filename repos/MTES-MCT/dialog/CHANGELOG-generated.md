## Changelog : dialog (30 derniers jours)

### Résumé
Les dernières mises à jour de dialog se concentrent sur l'amélioration de l'intégration des données de circulation, notamment via Literalis et la BDTOPO. Des corrections de bugs et des améliorations de l'API ont également été apportées, ainsi que des optimisations pour la gestion des données et l'expérience utilisateur.

### Évolutions fonctionnelles
- Amélioration de l'autocomplétion via la BDTOPO [#1688](https://github.com/MTES-MCT/dialog/issues/1688).
- Tri des tronçons affichés sur la carte par ordre d'importance [#1672](https://github.com/MTES-MCT/dialog/issues/1672).
- Correction de l'affichage du bandeau "notice" [#1678](https://github.com/MTES-MCT/dialog/issues/1678).
- Intégration des données Literalis pour les Côtes d'Armor [#1681](https://github.com/MTES-MCT/dialog/issues/1681).
- Amélioration du contrôle des variables pour les templates [#1652](https://github.com/MTES-MCT/dialog/issues/1652).

### Évolutions techniques
- Mise en place d'une transaction pour l'import Literalis afin d'assurer la cohérence des données [#1686](https://github.com/MTES-MCT/dialog/issues/1686).
- Amélioration du rollback Literalis [#1693](https://github.com/MTES-MCT/dialog/issues/1693).
- Gestion des erreurs applicatives lors de l'import Literalis : l'import continue même en cas d'erreur [#1697](https://github.com/MTES-MCT/dialog/issues/1697).
- Configuration du client Literalis pour augmenter le timeout et les tentatives de reconnexion [#1682](https://github.com/MTES-MCT/dialog/issues/1682).
- Suppression de la notion de rôles utilisateurs [#1698](https://github.com/MTES-MCT/dialog/issues/1698).
- Suppression de la mise à jour BDTOPO de la CI [#1685](https://github.com/MTES-MCT/dialog/issues/1685).
- Ajout d'une documentation plus complète pour l'API concernant les règles permanentes [#1683](https://github.com/MTES-MCT/dialog/issues/1683).
- Augmentation de la durée de vie des tokens à 1 mois [#1671](https://github.com/MTES-MCT/dialog/issues/1671).
- Exclure les polygones lors de l'import Literalis [#1699](https://github.com/MTES-MCT/dialog/issues/1699).

### Autres changements
- Ajout d'une crontask pour mettre à jour les statuts de l'IGN [#1694](https://github.com/MTES-MCT/dialog/issues/1694).
- Transfert de propriété de l'organisation [#1701](https://github.com/MTES-MCT/dialog/issues/1701).
- Migration des contacts du site web vers Zammad [#1680](https://github.com/MTES-MCT/dialog/issues/1680).
- Correction d'une faute de frappe [#1675](https://github.com/MTES-MCT/dialog/issues/1675).
