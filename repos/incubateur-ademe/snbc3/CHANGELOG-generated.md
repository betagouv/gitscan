## Changelog : snbc3 (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois-ci, le projet a progressé sur la précision des calculs de trajectoires de gaz à effet de serre (GES) à l'échelle locale (EPCI) et sur la fiabilisation des données climatiques utilisées via l'API.

### Évolutions fonctionnelles
- Amélioration du calcul des trajectoires GES de la SNBC pour une application territorialisée à l'échelle des EPCI (v2).
- Encadrement des paramètres de l'API pour la variante DJU, désormais limitée aux options autorisées (COSTIC ou METEO) pour éviter les erreurs de saisie. [#1](https://github.com/incubateur-ademe/snbc3/pull/1)

### Évolutions techniques
- **Fiabilisation du pipeline de données** : Centralisation et validation systématique des variantes DJU pour rejeter toute valeur inconnue lors du traitement.
- **Optimisation du cache** : Amélioration de la logique de gestion du cache OREC pour garantir la cohérence des données en privilégiant les données brutes par rapport au cache annuel.
- **Correction API** : Résolution de problèmes liés à la gestion des variantes DJU. [#1](https://github.com/incubateur-ademe/snbc3/pull/1)
