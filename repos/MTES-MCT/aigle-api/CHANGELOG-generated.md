## Changelog : aigle-api (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'API Aigle a bénéficié d'améliorations significatives en termes de performance, de sécurité et d'administration. Des optimisations ont été apportées à la gestion des données déployées, à l'importation de données (SITADEL, parcelles, zones personnalisées) et à l'interface d'administration. De nouvelles fonctionnalités ont été ajoutées pour la gestion des statuts de détection et des utilisateurs.

### Évolutions fonctionnelles
- Ajout de deux nouveaux statuts pour les détections : "illégal" et "à contrôler". [#69](https://github.com/MTES-MCT/aigle-api/pull/69)
- Ajout d'un champ "JUGEMENT" au statut de contrôle des détections. [#68](https://github.com/MTES-MCT/aigle-api/pull/68)
- Ajout d'un champ "is_staff" à l'utilisateur pour une gestion des droits améliorée. [#66](https://github.com/MTES-MCT/aigle-api/pull/66)
- Amélioration du mécanisme de prescription. [#70](https://github.com/MTES-MCT/aigle-api/pull/70)
- Restriction pour les super-admins : ils ne peuvent plus créer ou mettre à jour des jeux de tuiles sans collectivité associée. [#66](https://github.com/MTES-MCT/aigle-api/pull/66)

### Évolutions techniques
- Amélioration des performances de l'endpoint `deployed-data` grâce à une meilleure gestion du cache et de l'invalidation du cache. [#70](https://github.com/MTES-MCT/aigle-api/pull/70)
- Optimisation de la stratégie de déploiement de Celery. [#72](https://github.com/MTES-MCT/aigle-api/pull/72)
- Amélioration des commandes d'importation de données : `import_sitadel`, `import_parcelles`, `import_detections`, `import_custom_zones`. [#73](https://github.com/MTES-MCT/aigle-api/pull/73), [#74](https://github.com/MTES-MCT/aigle-api/pull/74), [#75](https://github.com/MTES-MCT/aigle-api/pull/75), [#76](https://github.com/MTES-MCT/aigle-api/pull/76)
- Ajout d'un paramètre `department` pour la commande `update_detection_parcels`. [#71](https://github.com/MTES-MCT/aigle-api/pull/71)
- Amélioration de la gestion des arguments des commandes d'administration. [#68](https://github.com/MTES-MCT/aigle-api/pull/68)
- Ajout d'une commande `clean_detections`. [#72](https://github.com/MTES-MCT/aigle-api/pull/72)
- Mise en place d'une stratégie améliorée pour le déploiement en un clic. [#76](https://github.com/MTES-MCT/aigle-api/pull/76)

### Autres changements
- Interdiction des appels DELETE. [#70](https://github.com/MTES-MCT/aigle-api/pull/70)
- Suppression des commentaires inutiles. [#72](https://github.com/MTES-MCT/aigle-api/pull/72)
- Suppression des routes liées aux statistiques. [#75](https://github.com/MTES-MCT/aigle-api/pull/75)
- Suppression du mot de passe des logs d'actions utilisateur. [#67](https://github.com/MTES-MCT/aigle-api/pull/67)
- Amélioration de la gestion de l'impersonnation d'administrateur super. [#66](https://github.com/MTES-MCT/aigle-api/pull/66)
- Travaux en cours sur l'interface d'administration pour les données déployées. [#66](https://github.com/MTES-MCT/aigle-api/pull/66)
