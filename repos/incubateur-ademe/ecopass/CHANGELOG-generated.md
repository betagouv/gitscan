## Changelog : ecopass (30 derniers jours, au 24 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface d'administration, notamment une vue plus complète et des options d'export de données. Des corrections ont été apportées pour gérer correctement les prix des produits en lots et les codes GTIN, ainsi que pour améliorer la gestion des organisations. La documentation du score a également été clarifiée.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données en lot et en masse (MC) [#138](https://github.com/incubateur-ademe/ecopass/issues/138).
- Amélioration de la vue d'administration avec une présentation plus claire et des informations plus complètes [#135](https://github.com/incubateur-ademe/ecopass/issues/135).
- Correction d'un bug empêchant la gestion correcte des prix inférieurs à 1 pour les produits en lot [#142](https://github.com/incubateur-ademe/ecopass/issues/142).
- Correction d'un problème de redirection après l'authentification en tant qu'administrateur.
- Clarification de la documentation concernant le calcul du score.

### Évolutions techniques
- Ajout de tests d'accessibilité privés [#140](https://github.com/incubateur-ademe/ecopass/issues/140).
- Correction d'un bug lié à la duplication des codes GTIN [#133](https://github.com/incubateur-ademe/ecopass/issues/133).
- Correction d'un problème lié à l'absence d'identifiant unique pour certaines organisations [#133](https://github.com/incubateur-ademe/ecopass/issues/133).
- Correction du problème d'encodage des codes GTIN [#134](https://github.com/incubateur-ademe/ecopass/issues/134).
- Ajustement de la largeur des statistiques d'administration [#139](https://github.com/incubateur-ademe/ecopass/issues/139).
