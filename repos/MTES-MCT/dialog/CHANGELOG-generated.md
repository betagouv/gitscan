## Changelog : dialog (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au projet dialog au cours du dernier mois. Les efforts se sont concentrés sur l'amélioration de l'intégration et de la gestion des données, notamment via Literalis et la BDTOPO, ainsi que sur des corrections de bugs et des optimisations de l'interface utilisateur. Des améliorations ont également été apportées à l'export de données et à la configuration de l'infrastructure.

### Évolutions fonctionnelles
- Amélioration de l'intégration de données via Literalis, avec gestion des erreurs et rollback (#1697, #1693, #1682, #1681, #1658).
- Ajout de l'import de la circulation alternée via Literalis (#1658, #1641).
- Autocomplétion des adresses via la BDTOPO (#1688).
- Tri des tronçons affichés sur la carte par ordre d'importance (#1672).
- Amélioration de l'export CIFS (#1661).
- Ajout de la gestion des liens Sogelink en tant que ressource (#1642).
- Correction de l'affichage du bandeau "notice" (#1678).
- Augmentation de la durée de vie des tokens à 1 mois (#1671).

### Évolutions techniques
- Intégration de Literalis dans une transaction pour garantir la cohérence des données (#1686).
- Suppression de la mise à jour BDTOPO de la CI pour optimiser le pipeline (#1685).
- Amélioration de la configuration de Monolog en production (#1640).
- Correction de l'installation des dépendances sur la CI pour la BDTOPO (#1655).
- Amélioration de la récupération des dernières versions de la BDTOPO (#1643).
- Script d'import automatique de la BDTOPO (#1639).
- Ajout de variables pour les templates afin d'améliorer la flexibilité (#1652).
- Mise à jour de la clé CIFS (#1664).
- Complétion de la documentation de l'API pour les règles permanentes (#1683).
- Export du nombre d'arrêtés créés par utilisateur vers Grist (#1636).
- Complétion de l'export vers Metabase (#1650).

### Autres changements
- Migration des contacts du site web vers Zammad (#1680).
- Suppression des références à l'ancienne BDTOPO (2023) (#1635).
- Correction d'une faute de frappe (#1675).
