## Changelog : transport-site (30 derniers jours, au 3 juillet 2026)

### Résumé
Les dernières mises à jour de transport-site se concentrent sur l'amélioration de l'import et de la consolidation des données IRVE (Infrastructure de Recharge pour Véhicules Électriques), ainsi que sur l'ajout de nouveaux opérateurs de vélos en libre-service. Des améliorations de l'interface utilisateur et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'opérateur Yelo VLS de La Rochelle à la liste des opérateurs de vélos en libre-service reconnus. [#5555](https://github.com/etalab/transport-site/issues/5555)
- Amélioration de l'affichage des instructions relatives aux formats de données. [#5549](https://github.com/etalab/transport-site/issues/5549)
- Ajout de textes pour les lignes de covoiturage. [#5548](https://github.com/etalab/transport-site/issues/5548)

### Évolutions techniques
- Amélioration du traitement de l'export de la base de données IRVE, avec gestion des erreurs et optimisation des performances (timeout et concurrence). [#5553](https://github.com/etalab/transport-site/issues/5553) et [#5551](https://github.com/etalab/transport-site/issues/5551)
- Correction des coordonnées inversées lors de la consolidation IRVE. [#5535](https://github.com/etalab/transport-site/issues/5535)
- Utilisation de floats en base de données pour le champ `puissance_nominale` dans les données IRVE. [#5531](https://github.com/etalab/transport-site/issues/5531)
- Suppression du code lié à `proxy_request` suite à la décommission de TimescaleDB. [#5546](https://github.com/etalab/transport-site/issues/5546)
- Mise à jour de la bibliothèque Protobuf. [#5533](https://github.com/etalab/transport-site/issues/5533)
- Amélioration du rapport IRVE avec des messages explicites pour les erreurs connues. [#5544](https://github.com/etalab/transport-site/issues/5544)

### Autres changements
- Suppression des warnings Credo pour la lecture de la configuration. [#5550](https://github.com/etalab/transport-site/issues/5550)
- Stabilisation des tests. [#5538](https://github.com/etalab/transport-site/issues/5538)
- Affichage d'avertissements concernant les inversions de coordonnées dans le validateur IRVE à la demande. [#5541](https://github.com/etalab/transport-site/issues/5541)
