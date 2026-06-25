## Changelog : aigle-api (30 derniers jours, au 23 juin 2026)

### Résumé
Les dernières mises à jour de l'API Aigle se concentrent sur l'amélioration des performances, l'ajout de nouvelles fonctionnalités pour l'administration des données et des traitements, et la correction de bugs. Des améliorations ont été apportées à la gestion des utilisateurs, des zones personnalisées et des données déployées, ainsi qu'à l'importation de données SITADEL.

### Évolutions fonctionnelles
- Ajout de deux nouveaux statuts pour les détections : "illégal" et "à contrôler".
- Possibilité d'ajouter un paramètre "département" lors de la mise à jour des parcelles de détection via la commande `update_detection_parcels`.
- Ajout d'un champ `JUGEMENT` au statut de contrôle des détections.
- Amélioration de la gestion des données déployées via une interface d'administration.
- Restriction de la recherche du géocodage aux types de groupes d'utilisateurs.
- Ajout d'un champ `is_staff` à l'utilisateur.
- Contrainte : un super-administrateur ne peut pas créer/mettre à jour des jeux de tuiles sans collectivité associée.
- Amélioration de la gestion de l'impersonnation de super-administrateur.
- Ajout d'une commande `import_custom_zones` pour importer des zones personnalisées.
- Interdiction des appels DELETE.

### Évolutions techniques
- Amélioration des performances de l'endpoint `deployed-data`.
- Optimisation du mécanisme de prescription.
- Amélioration de la configuration de Celery et ajout d'une commande `clean_detections`.
- Amélioration des performances de l'endpoint `deployed-data` (bis).
- Amélioration de la gestion des arguments des commandes d'administration.
- Amélioration de la commande `import_sitadel` et de l'endpoint `deployed_data` pour les performances.
- Amélioration de la commande `import_zae`.
- Amélioration de la commande `import_custom_zones`.
- Amélioration de la gestion du cache et de l'invalidation du cache.
- Ajout de cache sur les droits des utilisateurs pour optimiser les performances.
- Suppression des commentaires inutiles.
- Amélioration de la gestion des arguments des commandes d'administration.

### Autres changements
- Suppression du test de sécurité (reporté).
- Suppression du mot de passe des journaux d'action des utilisateurs.
- Amélioration de la gestion des commandes d'administration (recherche et exécution).
- Correction de la commande `run_command`.
- Correction de la commande `run_command` (bis).
- Correction de la commande `run_command` (ter).
- Amélioration de la gestion des jeux de tuiles.
