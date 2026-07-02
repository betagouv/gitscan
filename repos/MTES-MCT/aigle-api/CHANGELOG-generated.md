## Changelog : aigle-api (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, l'API Aigle a bénéficié d'améliorations significatives en termes d'administration, d'import de données et de performance. De nouvelles fonctionnalités ont été ajoutées pour la gestion des statuts de détection et des zones personnalisées, tandis que des optimisations ont été apportées à l'importation de données Sitadel et Parcelle. L'interface d'administration a également été enrichie avec de nouvelles commandes et une meilleure gestion des données déployées.

### Évolutions fonctionnelles
- Ajout de nouveaux statuts pour les détections : "illégal" et "à contrôler".
- Possibilité d'ajouter un champ "JUGEMENT" au statut de contrôle des détections.
- Amélioration du mécanisme de prescription.
- Ajout d'un champ `is_staff` aux utilisateurs.
- Contrainte pour les super-admins : impossible de créer/mettre à jour des jeux de tuiles sans collectivités associées.
- Nouvelle commande d'import pour les zones personnalisées : `import_custom_zones` [#66](https://github.com/MTES-MCT/aigle-api/pull/66).
- Amélioration de la gestion des données déployées via une nouvelle interface d'administration (en cours de développement).
- Possibilité de spécifier le département lors de la mise à jour des parcelles de détection.

### Évolutions techniques
- Amélioration de la stratégie de déploiement de Celery pour une meilleure performance.
- Optimisation de la performance de l'endpoint `deployed-data`.
- Amélioration de la gestion des commandes d'administration (recherche, arguments, progression).
- Refactorisation et nettoyage du code, notamment suppression de commentaires inutiles.
- Amélioration des commandes d'importation : `import_sitadel`, `import_parcelles`, `import_detections`.
- Correction de bugs et améliorations de la sécurité.
- Amélioration de la gestion de l'impersonnation des super-admins.
- Correction de problèmes liés à l'exécution des commandes depuis l'interface d'administration.
- Ajout de la possibilité de vider le cache après les commandes d'import.

### Autres changements
- Interdiction des requêtes DELETE.
- Suppression des routes liées aux statistiques.
- Amélioration de la gestion des arguments des commandes d'administration.
- Ajout d'une commande pour nettoyer les détections : `clean_detections`.
- Amélioration de la gestion des erreurs et des logs.
