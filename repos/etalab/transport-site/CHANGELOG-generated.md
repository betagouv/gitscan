## Changelog : transport-site (30 derniers jours, au 22 juillet 2026)

### Résumé
Les dernières mises à jour de transport-site se concentrent sur l'amélioration du traitement des données IRVE (Infrastructure de Recharge pour Véhicules Électriques), l'ajout de nouveaux opérateurs de vélos en libre-service et des corrections pour une meilleure stabilité et clarté de l'application. Des efforts ont également été faits pour simplifier la configuration et supprimer des composants obsolètes.

### Évolutions fonctionnelles
- Ajout de l'opérateur Yelo VLS (La Rochelle) à la liste des opérateurs de vélos en libre-service reconnus. [#5555](https://github.com/etalab/transport-site/issues/5555)
- Amélioration de l'affichage des instructions relatives aux formats de données. [#5549](https://github.com/etalab/transport-site/issues/5549)
- Ajout de textes pour les lignes de covoiturage. [#5548](https://github.com/etalab/transport-site/issues/5548)

### Évolutions techniques
- Refactorisation du processus de consolidation IRVE pour optimiser le passage des fichiers vers un dataframe et ajouter une pré-validation. [#5559](https://github.com/etalab/transport-site/issues/5559)
- Mise à jour des règles pour MobilityData v8.0.1. [#5574](https://github.com/etalab/transport-site/issues/5574)
- Mise à jour de protobuf GTFS-RT. [#5569](https://github.com/etalab/transport-site/issues/5569)
- Amélioration de la gestion des erreurs lors de l'upload S3 multipart pour la consolidation IRVE, avec envoi d'erreurs à Sentry et ajustement des timeouts et de la concurrence. [#5551](https://github.com/etalab/transport-site/issues/5551)
- Amélioration du rapport IRVE avec l'utilisation de messages explicites au lieu d'exceptions pour les erreurs connues. [#5544](https://github.com/etalab/transport-site/issues/5544)
- Suppression de la librairie `exvcr` et du code associé. [#5564](https://github.com/etalab/transport-site/issues/5564)
- Suppression du code lié à `proxy_request` suite à la décommissionnement de TimescaleDB. [#5546](https://github.com/etalab/transport-site/issues/5546)

### Autres changements
- Silence des warnings Credo pour la lecture de la configuration. [#5550](https://github.com/etalab/transport-site/issues/5550)
- Ajout d'avertissements dans le validateur IRVE concernant les inversions de coordonnées. [#5541](https://github.com/etalab/transport-site/issues/5541)
- Stabilisation des tests. [#5538](https://github.com/etalab/transport-site/issues/5538)
