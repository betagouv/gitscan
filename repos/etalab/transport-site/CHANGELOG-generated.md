## Changelog : transport-site (30 derniers jours, au 03 juillet 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'import et de la validation des données IRVE (Infrastructure de Recharge pour Véhicules Électriques), ainsi que sur l'ajout de nouveaux opérateurs de vélos en libre-service. Des améliorations de l'interface utilisateur et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'opérateur Yelo VLS de La Rochelle à la liste des opérateurs de vélos en libre-service reconnus. [#5555](https://github.com/etalab/transport-site/issues/5555)
- Amélioration de l'affichage des instructions relatives aux formats de données. [#5549](https://github.com/etalab/transport-site/issues/5549)
- Amélioration du rapport IRVE avec des messages plus explicites pour les erreurs connues. [#5544](https://github.com/etalab/transport-site/issues/5544)
- Ajout de textes pour les lignes de covoiturage. [#5548](https://github.com/etalab/transport-site/issues/5548)

### Évolutions techniques
- Amélioration du traitement de l'export de la base de données IRVE, avec découpage en *chunks*. [#5553](https://github.com/etalab/transport-site/issues/5553)
- Optimisation de l'upload S3 multipart pour la consolidation IRVE : gestion des erreurs via Sentry, ajustement du timeout et de la concurrence. [#5551](https://github.com/etalab/transport-site/issues/5551)
- Suppression de `proxy_request` suite à la décommission de TimescaleDB. [#5546](https://github.com/etalab/transport-site/issues/5546)
- Correction des coordonnées dans la consolidation IRVE. [#5535](https://github.com/etalab/transport-site/issues/5535)
- Affichage d'avertissements concernant les inversions de coordonnées dans le validateur IRVE. [#5541](https://github.com/etalab/transport-site/issues/5541)

### Autres changements
- Suppression des warnings Credo pour la lecture de la configuration. [#5550](https://github.com/etalab/transport-site/issues/5550)
- Stabilisation des tests. [#5538](https://github.com/etalab/transport-site/issues/5538)
