## Changelog : transport-site (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration et l'affichage des données NeTEx (Norme de données pour l'échange de données relatives aux transports en Europe), l'amélioration de l'accessibilité du site, et l'optimisation des outils d'administration et de validation des données IRVE (Infrastructure de Recharge pour Véhicules Électriques). Des améliorations de la pagination et de la documentation ont également été apportées.

### Évolutions fonctionnelles
- **NeTEx :** Intégration de la conversion des données NeTEx au format GeoJSON et affichage sur une carte. [#5463](https://github.com/etalab/transport-site/issues/5463)
- **NeTEx :** Documentation en ligne des règles spécifiques au profil France pour les données NeTEx. [#5461](https://github.com/etalab/transport-site/issues/5461)
- **Accessibilité :** Amélioration de la navigation au clavier du menu principal. [#5466](https://github.com/etalab/transport-site/issues/5466)
- **Pagination :** Amélioration de la pagination pour une meilleure expérience utilisateur. [#5459](https://github.com/etalab/transport-site/issues/5459)
- **Export de données :** Possibilité d'exporter les jeux de données de l'administration PAN (Point d'Accès National) au format CSV. [#5454](https://github.com/etalab/transport-site/issues/5454) et [#5462](https://github.com/etalab/transport-site/issues/5462)

### Évolutions techniques
- **GTFS-RT :** Gestion des erreurs critiques dans le validateur GTFS-RT, avec création d'une validation fatale et notification en cas d'erreur FATAL. [#5457](https://github.com/etalab/transport-site/issues/5457)
- **GTFS-RT :** Prise en compte des valeurs `nil` pour `critical_errors?` dans le validateur GTFS-RT. [#5465](https://github.com/etalab/transport-site/issues/5465)
- **IRVE :** Amélioration du script de détection des ressources IRVE dynamiques valables. [#5453](https://github.com/etalab/transport-site/issues/5453)
- **IRVE :** Ajout du flux dynamique dans le calcul des statistiques d'unicité des points de contact IRVE. [#5458](https://github.com/etalab/transport-site/issues/5458)
- **Backoffice :** Ajustements de l'interface utilisateur (IHM) pour les ressources liées dans le backoffice. [#5450](https://github.com/etalab/transport-site/issues/5450)
- **Backoffice :** Exclusion des ressources communautaires des listes déroulantes dans le backoffice des jeux de données. [#5449](https://github.com/etalab/transport-site/issues/5449)
- **Export de ressources :** Correction de l'export des ressources pour éviter les doublons d'agrégation de régions. [#5456](https://github.com/etalab/transport-site/issues/5456)

### Autres changements
- **NeTEx :** Identification des grandes fonctionnalités du standard NeTEx. [#5467](https://github.com/etalab/transport-site/issues/5467)
- **IRVE :** Résumé de la validation IRVE. [#5429](https://github.com/etalab/transport-site/issues/5429)
- **Règles NeTEx :** Révision des règles du profil France pour NeTEx. [#5447](https://github.com/etalab/transport-site/issues/5447)
- **Documentation NeTEx :** Documentation de la mise à jour des règles NeTEx. [#5460](https://github.com/etalab/transport-site/issues/5460)
- **Police :** Correction de la police du menu principal. [#5468](https://github.com/etalab/transport-site/issues/5468)
