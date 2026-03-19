## Changelog : hydra (30 derniers jours, au 18 mars 2026)

### Résumé
Cette version apporte des améliorations à la gestion des données, notamment dans l'analyse des WFS et la gestion des valeurs numériques dans les tables. Des corrections ont également été apportées pour améliorer la stabilité du processus de publication en CI et l'insertion de données dans la table `tables_index`. Enfin, une nouvelle information sur le temps de fonctionnement (uptime) a été ajoutée à l'API de santé.

### Évolutions fonctionnelles
- Ajout de la prise en charge de l'analyse des WFS (Web Feature Service) pour extraire les métadonnées et les informations sur les couches de données. [#385](https://github.com/datagouv/hydra/pull/385)
- L'API `/api/health/` inclut désormais un champ `uptime_since` indiquant la date et l'heure du dernier redémarrage du service. [#394](https://github.com/datagouv/hydra/pull/394)
- Correction de l'insertion de données dans la table `tables_index` pour gérer correctement les valeurs `nan` (Not a Number) et `inf` (Infinity). [#397](https://github.com/datagouv/hydra/pull/397)

### Évolutions techniques
- Mise à jour de la librairie `csv-detective` vers la version 0.11.0. [#396](https://github.com/datagouv/hydra)
- Correction de l'étape de publication dans le pipeline CI pour les versions (releases). [#398](https://github.com/datagouv/hydra/pull/398)
