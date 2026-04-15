## Changelog : transport-site (30 derniers jours, au 14 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'administration des jeux de données, la validation des données IRVE et NeTEx, ainsi que sur l'amélioration de l'expérience utilisateur dans le backoffice. Des corrections et des ajouts ont été apportés pour faciliter l'export de données, la gestion des ressources associées et l'affichage d'informations système.

### Évolutions fonctionnelles
- Amélioration de la pagination dans l'interface utilisateur [#5459](https://github.com/etalab/transport-site/issues/5459).
- Possibilité d'exporter les jeux de données en format CSV depuis l'administration PAN [#5454](https://github.com/etalab/transport-site/issues/5454) et [#5462](https://github.com/etalab/transport-site/issues/5462).
- Gestion manuelle des ressources associées aux jeux de données dans le backoffice [#5439](https://github.com/etalab/transport-site/issues/5439).
- Ajout de colonnes "ressources associées" et "nom entreprise" lors de l'export des ressources [#5438](https://github.com/etalab/transport-site/issues/5438).
- Amélioration du wrapping des textes sur la landing page VLS [#5445](https://github.com/etalab/transport-site/issues/5445).
- Amélioration du badge de notification [#5433](https://github.com/etalab/transport-site/issues/5433).
- Ajout de la possibilité d'overrider les headers de réponse pour le service Unlock S3 [#5432](https://github.com/etalab/transport-site/issues/5432).

### Évolutions techniques
- Gestion des valeurs `nil` pour `critical_errors?` dans `Transport.Validators.GTFSRT` [#5465](https://github.com/etalab/transport-site/issues/5465).
- Création d'une validation fatale et notification en cas d'erreur FATAL pour GTFS-RT [#5457](https://github.com/etalab/transport-site/issues/5457).
- Correction de l'agrégation des régions lors de l'export des ressources pour éviter les doublons [#5456](https://github.com/etalab/transport-site/issues/5456).
- Ajout du flux dynamique dans le calcul des statistiques d'unicité des points de contact IRVE [#5458](https://github.com/etalab/transport-site/issues/5458).
- Amélioration du script de détection des ressources IRVE dynamiques valables [#5453](https://github.com/etalab/transport-site/issues/5453).
- Ajout d'un nouveau rapport de validation NeTEx [#5393](https://github.com/etalab/transport-site/issues/5393).
- Révision des règles du profil France NeTEx [#5447](https://github.com/etalab/transport-site/issues/5447).
- Documentation en ligne des règles France NeTEx [#5461](https://github.com/etalab/transport-site/issues/5461).
- Documentation de la mise à jour des règles NeTEx [#5460](https://github.com/etalab/transport-site/issues/5460).
- Ajout de métadonnées statistiques NeTEx [#5354](https://github.com/etalab/transport-site/issues/5354).
- Affichage des tailles totales RAM et disque dans `ProxyConfigLive` [#5441](https://github.com/etalab/transport-site/issues/5441).
- Ajustements de l'IHM dans `Backoffice.DatasetControllerTest` et utilisation du mode `shared` pour Ecto [#5437](https://github.com/etalab/transport-site/issues/5437).
- Exclure les ressources communautaires des selects dans le backoffice dataset [#5449](https://github.com/etalab/transport-site/issues/5449).

### Autres changements
- Résumé de validation IRVE [#5429](https://github.com/etalab/transport-site/issues/5429).
- Conversion NeTEx vers GeoJSON [#5312](https://github.com/etalab/transport-site/issues/5312).
