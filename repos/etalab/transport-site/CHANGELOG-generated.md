## Changelog : transport-site (30 derniers jours, au 22 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration du traitement des données IRVE (Infrastructure de Recharge pour Véhicules Électriques), l'ajout de nouveaux opérateurs de vélos en libre-service et des améliorations de l'interface utilisateur pour la documentation des formats de données. La suppression de composants obsolètes comme `exvcr` et `proxy_request` contribue à la simplification du code.

### Évolutions fonctionnelles
- Ajout de l'opérateur Yelo VLS (La Rochelle) à la liste des opérateurs de vélos en libre-service reconnus. [#5555](https://github.com/etalab/transport-site/issues/5555)
- Amélioration de l'affichage des instructions relatives aux formats de données pour une meilleure clarté. [#5549](https://github.com/etalab/transport-site/issues/5549)
- Ajout de textes pour les lignes de covoiturage. [#5548](https://github.com/etalab/transport-site/issues/5548)
- Amélioration du rapport IRVE avec l'utilisation de messages explicites pour les erreurs connues. [#5544](https://github.com/etalab/transport-site/issues/5544)
- Affichage d'avertissements concernant les inversions de coordonnées dans le validateur IRVE. [#5541](https://github.com/etalab/transport-site/issues/5541)

### Évolutions techniques
- Refactorisation de la consolidation IRVE pour simplifier le traitement des fichiers et ajouter une pré-validation. [#5559](https://github.com/etalab/transport-site/issues/5559)
- Mise à jour des règles pour MobilityData v8.0.1. [#5574](https://github.com/etalab/transport-site/issues/5574)
- Mise à jour de protobuf GTFS-RT. [#5569](https://github.com/etalab/transport-site/issues/5569)
- Suppression de `exvcr` pour simplifier le code. [#5564](https://github.com/etalab/transport-site/issues/5564)
- Suppression de `proxy_request` suite à la décommission de TimescaleDB. [#5546](https://github.com/etalab/transport-site/issues/5546)
- Amélioration de la gestion des erreurs et du timeout pour l'upload S3 multipart dans le cadre de la consolidation IRVE. [#5551](https://github.com/etalab/transport-site/issues/5551)
- Chunk du traitement de l’export base de données IRVE. [#5553](https://github.com/etalab/transport-site/issues/5553)

### Autres changements
- Silence des warnings Credo pour la lecture de la configuration. [#5550](https://github.com/etalab/transport-site/issues/5550)
