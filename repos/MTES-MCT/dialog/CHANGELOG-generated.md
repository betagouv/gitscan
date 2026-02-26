## Changelog : dialog (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à l'application dialog au cours du dernier mois. Les efforts se sont concentrés sur l'amélioration de l'importation et de la gestion des données de circulation, notamment via l'intégration de Literalis et de la BDTOPO. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été réalisées.

### Évolutions fonctionnelles
- Amélioration de l'importation des données Literalis :
    - Les polygones sont exclus de l'import Literalis (#1699).
    - L'import continue même en cas d'erreurs applicatives (#1697).
    - Un rapport d'intégration Literalis est maintenant disponible (#1695).
    - Amélioration du rollback Literalis (#1693).
    - Intégration Literalis pour la région des Côtes d'Armor (#1681).
    - Ajout de la gestion de la circulation alternée dans l'import Literalis (#1658).
    - Ajout du type de restriction "circulation alternée" (#1641).
- Amélioration de la gestion de la BDTOPO :
    - Autocomplétion via la BDTOPO (#1688).
    - Amélioration de la récupération des dernières versions de la BDTOPO (#1643).
    - Script d'import automatique de la BDTOPO (#1639).
    - Suppression des références à l'ancienne BDTOPO (2023) (#1635).
    - Correction de l'installation des dépendances sur la CI de la BDTOPO (#1655).
- Amélioration de l'export CIFS (#1661).
- Intégration des liens Sogelink en tant que ressource (#1642).
- Tri de l'affichage des tronçons sur la carte par ordre d'importance (#1672).
- Correction de l'affichage du bandeau "notice" (#1678).
- Augmentation de la durée de vie des tokens à 1 mois (#1671).
- Amélioration des variables disponibles pour les templates (#1652).

### Évolutions techniques
- Documentation de l'API complétée pour expliciter les règles permanentes (#1683).
- Configuration du client Literalis pour augmenter son délai d'inactivité et les tentatives de reconnexion (#1682).
- Englobement de l'import Literalis dans une transaction pour garantir la cohérence des données (#1686).
- Suppression de la mise à jour BDTOPO de la CI (#1685).
- Mise à jour de la clé CIFS (#1664).
- Complétion de l'export Metabase (#1650).

### Autres changements
- Migration des contacts du site web vers Zammad (#1680).
- Correction d'une faute de frappe (#1675).
