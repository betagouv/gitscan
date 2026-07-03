## Changelog : transport-site (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent principalement sur le traitement et la consolidation des données IRVE (Infrastructure de Recharge pour Véhicules Électriques), avec des corrections pour la gestion des coordonnées, l'affichage d'avertissements et l'optimisation du processus d'export. Des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant l'affichage des instructions de format et des textes relatifs au covoiturage. Enfin, des travaux de maintenance ont été réalisés, notamment la suppression de code lié à TimescaleDB qui a été décommissionné.

### Évolutions fonctionnelles
- Amélioration de l'affichage des instructions relatives aux formats de données [#5549](https://github.com/etalab/transport-site/issues/5549).
- Ajout de textes plus clairs pour les lignes de covoiturage [#5548](https://github.com/etalab/transport-site/issues/5548).
- Affichage d'avertissements concernant les inversions de coordonnées lors de la validation des données IRVE [#5541](https://github.com/etalab/transport-site/issues/5541).
- Amélioration du rapport de consolidation IRVE avec des messages plus explicites en cas d'erreurs connues [#5544](https://github.com/etalab/transport-site/issues/5544).

### Évolutions techniques
- Optimisation du processus d'upload vers S3 pour la consolidation IRVE, avec gestion des erreurs via Sentry, ajustement du timeout et de la concurrence [#5551](https://github.com/etalab/transport-site/issues/5551).
- Correction des coordonnées dans la consolidation IRVE [#5535](https://github.com/etalab/transport-site/issues/5535).
- Utilisation de floats en base de données pour le champ `puissance_nominale` dans le contexte de l'IRVE [#5531](https://github.com/etalab/transport-site/issues/5531).
- Suppression du code lié à `proxy_request` suite à la décommission de TimescaleDB [#5546](https://github.com/etalab/transport-site/issues/5546).
- Mise à jour de protobuf [#5533](https://github.com/etalab/transport-site/issues/5533).
- Avancement du chunk de traitement de l'export de la base de données IRVE [#5553](https://github.com/etalab/transport-site/issues/5553).

### Autres changements
- Suppression des warnings Credo pour la lecture de la configuration [#5550](https://github.com/etalab/transport-site/issues/5550).
- Stabilisation des tests [#5538](https://github.com/etalab/transport-site/issues/5538).
