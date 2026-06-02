## Changelog : aigle-api (30 derniers jours, au 28 mai 2026)

### Résumé
Les dernières mises à jour de l'API Aigle se concentrent sur l'amélioration de l'administration des utilisateurs et des zones personnalisées, ainsi que sur l'optimisation des performances et la correction de bugs liés au téléchargement de données et au filtrage. Des améliorations ont également été apportées à la gestion des tilesets et à l'import/export de données.

### Évolutions fonctionnelles
- Amélioration de l'interface d'administration pour la gestion des groupes d'utilisateurs, permettant de modifier facilement les groupes des utilisateurs ayant le statut SUPER_ADMIN.
- Ajout d'un filtre sur le groupe d'utilisateurs dans la liste des utilisateurs de l'interface d'administration [#64](https://github.com/MTES-MCT/aigle-api/pull/64).
- Correction d'un bug empêchant l'application des filtres de zones personnalisées lors du téléchargement de parcelles [#58](https://github.com/MTES-MCT/aigle-api/pull/58).
- Correction d'un problème d'affichage d'un nombre excessif de détections lors du téléchargement de parcelles [#58](https://github.com/MTES-MCT/aigle-api/pull/58).
- Restriction de la recherche du géocodeur [#65](https://github.com/MTES-MCT/aigle-api/pull/65).
- Correction des droits SUPER_ADMIN [#62](https://github.com/MTES-MCT/aigle-api/pull/62).
- Correction de la gestion des zones personnalisées dans l'administration [#63](https://github.com/MTES-MCT/aigle-api/pull/63).
- Amélioration de l'import/export de données en masse [#66](https://github.com/MTES-MCT/aigle-api/pull/66).
- Ajout de la possibilité d'importer/exporter des données directement depuis l'interface d'administration [#59](https://github.com/MTES-MCT/aigle-api/pull/59).

### Évolutions techniques
- Le type de données de la date des tilesets a été modifié de `datetime` à `date` [#61](https://github.com/MTES-MCT/aigle-api/pull/61).
- Optimisations de performance diverses [#60](https://github.com/MTES-MCT/aigle-api/pull/60).
- Amélioration de la configuration locale pour faciliter le développement [#57](https://github.com/MTES-MCT/aigle-api/pull/57).
- Ajout de logs pour les routes super_admin afin de faciliter le débogage [#62](https://github.com/MTES-MCT/aigle-api/pull/62).
- Mise à jour de la configuration CI/CD pour ne déployer que si les tests réussissent [#61](https://github.com/MTES-MCT/aigle-api/pull/61).
- Correction de la suite de tests [#56](https://github.com/MTES-MCT/aigle-api/pull/56).

### Autres changements
- Correction d'un bug où le filtre par défaut pour le téléchargement de parcelles était incorrect (défini à 0.3) [#59](https://github.com/MTES-MCT/aigle-api/pull/59).
