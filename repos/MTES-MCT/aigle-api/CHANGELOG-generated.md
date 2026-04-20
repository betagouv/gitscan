## Changelog : aigle-api (30 derniers jours, au 17 mai 2026)

### Résumé
Les dernières mises à jour de l'API Aigle se concentrent sur l'amélioration des performances de certains endpoints, notamment ceux liés au téléchargement d'informations et à la récupération de géométries personnalisées. Des corrections ont également été apportées pour affiner le filtrage des données affichées aux utilisateurs, et des actions de l'administrateur sont maintenant loguées.

### Évolutions fonctionnelles
- Amélioration de l'affichage des géozones : Seules les géozones associées aux parcelles sont maintenant affichées. [#55](https://github.com/MTES-MCT/aigle-api/pull/55)
- Filtrage des détections : L'endpoint d'informations de téléchargement filtre désormais les détections non pertinentes. [#49](https://github.com/MTES-MCT/aigle-api/pull/49)
- Log des actions de l'administrateur : Les actions effectuées par l'administrateur (SUPER_ADMIN) sont maintenant enregistrées pour un meilleur suivi. [#57](https://github.com/MTES-MCT/aigle-api/pull/57)

### Évolutions techniques
- Optimisation des performances : Amélioration des performances de l'endpoint `get-custom-geometry`. [#56](https://github.com/MTES-MCT/aigle-api/pull/56)
- Optimisation des performances : Amélioration des performances de l'endpoint d'informations de téléchargement. [#56](https://github.com/MTES-MCT/aigle-api/pull/56)
- Correction : Filtrage des géozones personnalisées indésirables pour la liste des détections. [#54](https://github.com/MTES-MCT/aigle-api/pull/54)

### Autres changements
- Nettoyage du code : Quelques améliorations de la lisibilité et de la maintenance du code ont été effectuées. [#55](https://github.com/MTES-MCT/aigle-api/pull/55)
- Amélioration des commandes d'administration : Des améliorations ont été apportées aux commandes d'administration. [#57](https://github.com/MTES-MCT/aigle-api/pull/57)
