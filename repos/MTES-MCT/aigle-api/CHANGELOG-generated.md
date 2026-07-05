## Changelog : aigle-api (30 derniers jours, au 03 juillet 2026)

### Résumé
Les dernières mises à jour de l'API Aigle se concentrent sur l'amélioration des commandes d'administration, l'optimisation des performances, et l'ajout de nouvelles fonctionnalités liées à la gestion des données et des utilisateurs. Plusieurs améliorations ont été apportées aux commandes d'importation de données (Sitadel, parcelles, détections, zones personnalisées) pour une meilleure gestion et une plus grande fiabilité.

### Évolutions fonctionnelles
- Ajout de nouveaux statuts pour les détections : "illégal" et "à contrôler".
- Ajout du champ `is_staff` aux utilisateurs.
- Amélioration du mécanisme de prescription.
- Ajout d'un paramètre "department" pour la commande `update_detection_parcels`.
- Ajout de la valeur "JUGEMENT" au statut de contrôle des détections.
- Contrainte : un super-admin ne peut pas créer/mettre à jour des jeux de tuiles sans collectivité associée.
- Amélioration de la gestion de l'impersonnation de super-admin.
- Interdiction des appels DELETE.

### Évolutions techniques
- Amélioration de la gestion des groupes d'utilisateurs lors du déploiement.
- Optimisation des performances de l'endpoint `deployed-data`.
- Amélioration de la stratégie de déploiement de Celery.
- Amélioration de la commande `sitadel`.
- Amélioration des commandes d'importation de données (Sitadel, parcelles, détections).
- Amélioration de la gestion des arguments des commandes d'administration.
- Nettoyage de code et suppression de commentaires inutiles.
- Amélioration de la gestion des commandes d'administration via l'interface utilisateur.
- Amélioration de la commande `run_command`.

### Autres changements
- Ajout d'une interface d'administration pour les données déployées (en cours de développement).
- Suppression des routes liées aux statistiques.
- Suppression des tests de sécurité (reportés à plus tard).
- Amélioration de la gestion des erreurs et des logs.
