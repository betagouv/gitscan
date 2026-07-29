## Changelog : transport-site (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la consolidation et la validation des données IRVE (Infrastructure de Recharge pour Véhicules Électriques), l'ajout de nouveaux opérateurs de vélos en libre-service, et l'amélioration de la robustesse du système. Des efforts ont également été faits pour améliorer la qualité du code et la surveillance des erreurs.

### Évolutions fonctionnelles
- Ajout de l'opérateur Yelo VLS de La Rochelle à la liste des opérateurs de vélos en libre-service reconnus. [#5555](https://github.com/etalab/transport-site/issues/5555)
- Amélioration de l'affichage des instructions relatives aux formats de données. [#5549](https://github.com/etalab/transport-site/issues/5549)
- Ajout de textes pour les lignes de covoiturage. [#5548](https://github.com/etalab/transport-site/issues/5548)

### Évolutions techniques
- Refactorisation de la consolidation IRVE pour simplifier le traitement des fichiers et améliorer la validation des données. [#5559](https://github.com/etalab/transport-site/issues/5559)
- Mise à jour de la définition protobuf GTFS-RT. [#5569](https://github.com/etalab/transport-site/issues/5569)
- Amélioration de la gestion des erreurs lors de l'upload S3 multipart pour la consolidation IRVE, avec envoi des erreurs à Sentry et ajustement des timeouts et de la concurrence. [#5551](https://github.com/etalab/transport-site/issues/5551)
- Suppression de la librairie `exvcr`. [#5564](https://github.com/etalab/transport-site/issues/5564)
- Suppression de `proxy_request` suite à la décommissionnement de TimescaleDB. [#5546](https://github.com/etalab/transport-site/issues/5546)
- Mise en place d'un scanner de vulnérabilités et upgrades de librairies. [#5566](https://github.com/etalab/transport-site/issues/5566)
- Mise à jour des règles pour MobilityData v8.0.1. [#5574](https://github.com/etalab/transport-site/issues/5574)

### Autres changements
- Amélioration du rapport IRVE avec l'utilisation de messages explicites au lieu d'exceptions pour les erreurs connues. [#5544](https://github.com/etalab/transport-site/issues/5544)
- Ajout d'avertissements concernant les inversions de coordonnées dans le validateur IRVE. [#5541](https://github.com/etalab/transport-site/issues/5541)
- Suppression de warnings Credo pour la lecture de la configuration. [#5550](https://github.com/etalab/transport-site/issues/5550)
