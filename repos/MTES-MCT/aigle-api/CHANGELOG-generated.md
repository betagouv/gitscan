## Changelog : aigle-api (30 derniers jours, au 9 juillet 2026)

### Résumé
Les dernières mises à jour de l'API Aigle se concentrent sur l'amélioration des outils d'administration, l'optimisation des performances et la correction de bugs liés à l'importation et au traitement des données. Des nouvelles fonctionnalités ont été ajoutées pour faciliter le déploiement et la gestion des données, notamment pour les zones d'activités économiques (ZAE).

### Évolutions fonctionnelles
- Amélioration du tableau de bord DDT (Direction Départementale des Territoires et de la Mer).
- Ajout de nouveaux statuts pour les détections : "illégal" et "à contrôler".
- Possibilité de rechercher des commandes d'exécution dans l'interface d'administration.
- Amélioration de la gestion des collectivité territoriales dans l'interface d'administration.
- Correction du flux de prescription [#80](https://github.com/MTES-MCT/aigle-api/pull/80).
- Correction de l'attribution des détections aux bons ensembles de tuiles [#80](https://github.com/MTES-MCT/aigle-api/pull/80).

### Évolutions techniques
- Amélioration de la gestion des utilisateurs et des groupes lors du déploiement.
- Optimisation du déploiement pour ne déployer qu'une seule batch ou une seule ZAE à la fois.
- Amélioration de la stratégie de déploiement de Celery.
- Amélioration des performances de l'endpoint `deployed-data`.
- Refonte et nettoyage des commandes d'importation de données (Sitadel, parcelles, détections).
- Amélioration de la commande `create_tile` et `import_sitadel`.
- Ajout d'un paramètre département pour la commande `update_detection_parcels`.
- Ajout d'une commande `clean_detections`.
- Amélioration de la gestion des commandes d'administration (ajout d'une barre de progression).
- Amélioration de la sécurité (corrections et report de tests de sécurité).

### Autres changements
- Suppression des routes liées aux statistiques.
- Nettoyage de code et suppression de commentaires inutiles.
- Mise à jour de la documentation et de la configuration pour faciliter le déploiement.
