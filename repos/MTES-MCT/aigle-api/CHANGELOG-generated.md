## Changelog : aigle-api (30 derniers jours, au 12 juin 2026)

### Résumé
Les dernières mises à jour de l'API Aigle se concentrent sur l'amélioration des performances, l'enrichissement des fonctionnalités d'administration et la correction de bugs. Des améliorations ont été apportées à la gestion des données déployées, à l'importation de données personnalisées et à la gestion des droits d'accès des utilisateurs, notamment pour les super-administrateurs.

### Évolutions fonctionnelles
- Ajout du champ `JUGEMENT` au statut de contrôle de détection.
- Possibilité d'ajouter un champ `is_staff` aux utilisateurs.
- Restriction de la recherche du géocodeur.
- Amélioration de l'interface d'administration pour la gestion des données déployées [#70](https://github.com/MTES-MCT/aigle-api/pull/70).
- Ajout d'une commande `import_custom_zones` pour importer des zones personnalisées [#65](https://github.com/MTES-MCT/aigle-api/pull/65).
- Possibilité de filtrer les groupes d'utilisateurs par types de groupes (`userGroupTypes`).
- Amélioration de la gestion des droits des super-administrateurs, notamment pour la création et la mise à jour des jeux de tuiles (tilesets) [#62](https://github.com/MTES-MCT/aigle-api/pull/62).
- Amélioration de la gestion de l'impersonnation des super-administrateurs.
- Amélioration de la gestion des zones personnalisées dans l'interface d'administration [#63](https://github.com/MTES-MCT/aigle-api/pull/63).

### Évolutions techniques
- Optimisation des performances de l'endpoint des données déployées et amélioration du mécanisme de prescription [#70](https://github.com/MTES-MCT/aigle-api/pull/70).
- Amélioration de la gestion des arguments des commandes d'administration.
- Amélioration de la gestion des commandes `run_command` [#66](https://github.com/MTES-MCT/aigle-api/pull/66), [#67](https://github.com/MTES-MCT/aigle-api/pull/67).
- Mise en cache des droits des utilisateurs pour optimiser les performances.
- Amélioration de la stratégie de cache et d'invalidation de cache.
- Suppression du mot de passe des logs d'actions des utilisateurs.
- Conversion du champ de date des jeux de tuiles (tilesets) [#61](https://github.com/MTES-MCT/aigle-api/pull/61).
- Amélioration du CI/CD : déploiement uniquement si les tests réussissent [#64](https://github.com/MTES-MCT/aigle-api/pull/64).

### Autres changements
- Ajout de contraintes pour empêcher les super-administrateurs de créer/mettre à jour des jeux de tuiles sans collectivité associée.
- Travaux en cours (WIP) sur l'interface d'administration des données déployées.
- Amélioration de l'importation des ZAE (Zones d'Activités Économiques).
