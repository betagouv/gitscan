## Changelog : aigle-api (30 derniers jours, au 09 juillet 2026)

### Résumé
Les dernières mises à jour de l'API Aigle se concentrent sur l'amélioration des processus de déploiement, l'optimisation des commandes d'importation de données et la correction de bugs liés au flux de prescription et à l'attribution des détections. Des améliorations ont également été apportées à l'interface de gestion des données DDT (Dispositif de Détection des Traitements).

### Évolutions fonctionnelles
- Amélioration de l'interface DDT pour une meilleure gestion des données. [#76](https://github.com/MTES-MCT/aigle-api/pull/76)
- Correction du flux de prescription pour assurer son bon fonctionnement. [#80](https://github.com/MTES-MCT/aigle-api/pull/80)
- Correction de l'attribution des détections aux bons ensembles de tuiles (tilesets). [#72](https://github.com/MTES-MCT/aigle-api/pull/72)
- Ajout d'une interface de statistiques pour les données DDT (en interne uniquement pour le moment). [#78](https://github.com/MTES-MCT/aigle-api/pull/78)

### Évolutions techniques
- Amélioration de la gestion des utilisateurs et des groupes lors du déploiement. [#78](https://github.com/MTES-MCT/aigle-api/pull/78)
- Optimisation du déploiement pour ne déployer qu'une seule batch ou une seule ZAE (Zone d'Activités Économiques) à la fois. [#78](https://github.com/MTES-MCT/aigle-api/pull/78)
- Amélioration de la stratégie de déploiement de Celery pour une meilleure performance. [#75](https://github.com/MTES-MCT/aigle-api/pull/75)
- Amélioration des commandes `import_sitadel`, `import_parcelles` et `import_detections` pour une meilleure fiabilité et performance. [#74](https://github.com/MTES-MCT/aigle-api/pull/74)
- Amélioration de la création des tuiles (tiles). [#74](https://github.com/MTES-MCT/aigle-api/pull/74)
- Mise en place d'améliorations de sécurité. [#75](https://github.com/MTES-MCT/aigle-api/pull/75)

### Autres changements
- Nettoyage du code lié aux statistiques (routes supprimées). [#75](https://github.com/MTES-MCT/aigle-api/pull/75)
- Suppression de code obsolète dans la commande `import_detections`. [#75](https://github.com/MTES-MCT/aigle-api/pull/75)
- Mise à jour de la gestion du cache après les commandes d'importation. [#75](https://github.com/MTES-MCT/aigle-api/pull/75)
