## Changelog : aigle-frontend (30 derniers jours, au 28 mai 2026)

### Résumé
Les dernières mises à jour d'aigle-frontend se concentrent sur l'amélioration de l'administration et de l'expérience utilisateur, notamment en facilitant la gestion des groupes d'utilisateurs, l'import/export en masse, et en optimisant les performances de l'application. Des améliorations ont également été apportées à la cartographie et à la recherche géolocalisée.

### Évolutions fonctionnelles
- **Administration :**
    - Possibilité de changer de groupe d'utilisateurs plus facilement pour les administrateurs SUPER_ADMIN [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42).
    - Réinitialisation des filtres après un changement de groupe d'utilisateurs dans l'interface d'administration [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42).
- **Cartographie :**
    - Ajout de la bounding box (bbox) dans l'URL pour faciliter le partage et la reprise de vues spécifiques [#44](https://github.com/MTES-MCT/aigle-frontend/pull/44).
    - Restriction de la recherche du géolocalisateur pour améliorer la précision et la pertinence des résultats [#44](https://github.com/MTES-MCT/aigle-frontend/pull/44).
    - Correction d'un problème de zoom/dézoom sur les appareils Android et iOS [#44](https://github.com/MTES-MCT/aigle-frontend/pull/44).
- **Import/Export :** Amélioration de la fonctionnalité d'import/export en masse [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42).
- **Téléchargement :** Correction d'un problème lié au téléchargement de fichiers [#43](https://github.com/MTES-MCT/aigle-frontend/pull/43).
- **Requêtes Admin :** Ajout de paramètres de requête pour l'administration [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42).

### Évolutions techniques
- **Performance :** Diverses optimisations de performance ont été implémentées pour améliorer la réactivité de l'application [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42).
- **Types de données :** Le type de données de la date des tilesets a été modifié de datetime à date [#42](https://github.com/MTES-MCT/aigle-frontend/pull/42).

### Autres changements
- Aucun changement significatif à signaler.
