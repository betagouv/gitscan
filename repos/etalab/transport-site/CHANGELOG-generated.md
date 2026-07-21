## Changelog : transport-site (30 derniers jours, au 20 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration du traitement des données IRVE (Infrastructure de Recharge pour Véhicules Électriques) avec des optimisations de la consolidation et de la validation des données. Des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant l'affichage des instructions relatives aux formats de données et des textes pour les lignes de covoiturage.

### Évolutions fonctionnelles
- Ajout de l'opérateur Yelo VLS (La Rochelle) à la liste des opérateurs de vélos en libre-service connus. [#5555](https://github.com/etalab/transport-site/issues/5555)
- Amélioration de l'affichage des instructions relatives aux formats de données. [#5549](https://github.com/etalab/transport-site/issues/5549)
- Ajout de textes pour les lignes de covoiturage. [#5548](https://github.com/etalab/transport-site/issues/5548)
- Amélioration du rapport IRVE avec des messages plus explicites pour les erreurs connues. [#5544](https://github.com/etalab/transport-site/issues/5544)
- Affichage d'avertissements concernant les inversions de coordonnées dans le validateur IRVE. [#5541](https://github.com/etalab/transport-site/issues/5541)

### Évolutions techniques
- Refactorisation de la consolidation IRVE pour un seul passage des fichiers vers un dataframe et une vérification de pré-validation. [#5559](https://github.com/etalab/transport-site/issues/5559)
- Mise à jour de protobuf GTFS-RT. [#5569](https://github.com/etalab/transport-site/issues/5569)
- Amélioration de l'upload S3 multipart avec envoi d'erreurs sur Sentry, ajustement du timeout et de la concurrence pour la consolidation IRVE. [#5551](https://github.com/etalab/transport-site/issues/5551)
- Suppression de `exvcr` et de `proxy_request` (décommissionnement TimescaleDB). [#5564](https://github.com/etalab/transport-site/issues/5564) et [#5546](https://github.com/etalab/transport-site/issues/5546)
- Chunk du traitement de l’export base de données IRVE. [#5553](https://github.com/etalab/transport-site/issues/5553)

### Autres changements
- Silence des warnings Credo pour la lecture de la configuration. [#5550](https://github.com/etalab/transport-site/issues/5550)
- Stabilisation de tests. [#5538](https://github.com/etalab/transport-site/issues/5538)
