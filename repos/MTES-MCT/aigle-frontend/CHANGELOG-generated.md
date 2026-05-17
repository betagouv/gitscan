## Changelog : aigle-frontend (30 derniers jours, au 15 mai 2026)

### Résumé
Les dernières mises à jour d'aigle-frontend se concentrent sur l'amélioration de l'interface d'administration, notamment en ajoutant des fonctionnalités d'import/export de données utilisateurs et en facilitant la gestion des groupes d'utilisateurs. Des optimisations de performance ont également été apportées, ainsi que des corrections de types de données pour une meilleure cohérence.

### Évolutions fonctionnelles
- **Administration des utilisateurs :**
    - Possibilité de filtrer la liste des utilisateurs par groupe dans l'interface d'administration. [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42)
    - Simplification du changement de groupe pour les utilisateurs ayant le rôle `SUPER_ADMIN`. [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42)
    - Ajout de paramètres de requête pour l'interface d'administration. [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42)
    - Implémentation de l'import et de l'export de données utilisateurs dans l'interface d'administration. [#41](https://github.com/MTES-MCT/aigle-frontend/pull/41)
- **Gestion des données :**
    - Correction du type de données de la date des tilesets, passant de `datetime` à `date`. [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42)
    - Amélioration de la fonctionnalité d'import/export en masse. [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42)

### Évolutions techniques
- **Performance :** Diverses optimisations de performance ont été implémentées pour améliorer la réactivité de l'application. [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42)
- **Dépendances :** Suppression de la dépendance à la librairie `axios`. [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42)

### Autres changements
- Intégration des modifications du branch `develop` dans la branche principale. [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42) et [#40](https://github.com/MTES-MCT/aigle-frontend/pull/40)
