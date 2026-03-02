## Changelog : dialog (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au projet dialog au cours des 30 derniers jours. Les principales évolutions concernent l'import de données Literalis, l'intégration de la BDTOPO, l'amélioration de l'export CIFS et des corrections d'affichage. Des modifications techniques ont également été apportées pour améliorer la robustesse et la configuration du système.

### Évolutions fonctionnelles

- Amélioration de l'import de données Literalis :
    - Gestion des erreurs lors de l'import, permettant de continuer même en cas d'échec partiel [#1697](https://github.com/MTES-MCT/dialog/issues/1697).
    - Exclusion des polygones lors de l'import Literalis [#1699](https://github.com/MTES-MCT/dialog/issues/1699).
    - Ajout de la gestion de la circulation alternée dans l'import Literalis [#1658](https://github.com/MTES-MCT/dialog/issues/1658) et [#1641](https://github.com/MTES-MCT/dialog/issues/1641).
    - Rapport d'intégration Literalis [#1695](https://github.com/MTES-MCT/dialog/issues/1695).
    - Amélioration du rollback Literalis [#1693](https://github.com/MTES-MCT/dialog/issues/1693).
- Intégration de la BDTOPO :
    - Autocomplétion via la BDTOPO [#1688](https://github.com/MTES-MCT/dialog/issues/1688).
    - Correction de l'installation des dépendances sur la CI de la BDTOPO [#1655](https://github.com/MTES-MCT/dialog/issues/1655).
- Amélioration de l'export CIFS [#1661](https://github.com/MTES-MCT/dialog/issues/1661).
- Correction de l'affichage du bandeau "notice" [#1678](https://github.com/MTES-MCT/dialog/issues/1678).
- Tri de l'affichage des tronçons sur la carte par ordre d'importance [#1672](https://github.com/MTES-MCT/dialog/issues/1672).
- Augmentation de la durée de vie des tokens à 1 mois [#1671](https://github.com/MTES-MCT/dialog/issues/1671).
- Ajout de variables pour les templates [#1652](https://github.com/MTES-MCT/dialog/issues/1652).

### Évolutions techniques

- Mise en place d'une transaction pour l'import Literalis afin d'assurer la cohérence des données [#1686](https://github.com/MTES-MCT/dialog/issues/1686).
- Configuration du client Literalis pour augmenter son délai d'inactivité et le nombre de tentatives [#1682](https://github.com/MTES-MCT/dialog/issues/1682).
- Suppression de la mise à jour BDTOPO de la CI [#1685](https://github.com/MTES-MCT/dialog/issues/1685).
- Ajout d'une tâche cron pour mettre à jour les statuts de l'IGN [#1694](https://github.com/MTES-MCT/dialog/issues/1694).
- Suppression de la notion de rôles utilisateurs [#1698](https://github.com/MTES-MCT/dialog/issues/1698).

### Autres changements

- Transfert de propriété de l'organisation [#1701](https://github.com/MTES-MCT/dialog/issues/1701).
- Migration des contacts du site web vers Zammad [#1680](https://github.com/MTES-MCT/dialog/issues/1680).
- Documentation complète de l'API pour les règles permanentes [#1683](https://github.com/MTES-MCT/dialog/issues/1683).
- Mise à jour de la clé CIFS [#1664](https://github.com/MTES-MCT/dialog/issues/1664).
- Correction d'une faute de frappe [#1675](https://github.com/MTES-MCT/dialog/issues/1675).
- Complétion de l'export Metabase [#1650](https://github.com/MTES-MCT/dialog/issues/1650).
