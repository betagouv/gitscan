## Changelog : aigle-frontend (30 derniers jours, au 12 juin 2026)

### Résumé
Les dernières mises à jour d'aigle-frontend se concentrent sur l'amélioration de l'interface d'administration, notamment pour la gestion des utilisateurs, des groupes d'utilisateurs et des commandes. Des améliorations ont également été apportées à la cartographie et à la gestion des données, avec l'ajout de nouvelles informations et la correction de bugs liés à l'export de données.

### Évolutions fonctionnelles
- Ajout du champ "is_staff" aux utilisateurs pour une gestion des permissions plus fine. [#45](https://github.com/MTES-MCT/aigle-frontend/pull/45)
- Amélioration de la gestion des groupes d'utilisateurs dans l'interface d'administration : ajout d'informations sur le formulaire, filtrage par type de groupe et réinitialisation des filtres après changement de groupe. [#44](https://github.com/MTES-MCT/aigle-frontend/pull/44)
- Correction d'un bug empêchant le téléchargement de fichiers CSV/XLSX dans la vue tableau lorsque d'autres catégories étaient sélectionnées. [#46](https://github.com/MTES-MCT/aigle-frontend/pull/46)
- Ajout de la valeur "JUGEMENT" au statut de contrôle de détection.
- Ajout de données Sitadel à l'aperçu du déploiement.
- Possibilité de restreindre la recherche du géocodeur.
- Amélioration de la fonctionnalité de changement de groupe dans l'interface d'administration.
- Ajout de la possibilité de spécifier une bounding box (bbox) dans l'URL.

### Évolutions techniques
- Amélioration de la gestion des arguments de commande dans l'interface d'administration. [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47)
- Ajout d'un bouton de relance pour les commandes qui échouent dans l'interface d'administration.
- Refonte de la gestion des paramètres d'URL dans l'interface d'administration.
- Implémentation d'une interface d'administration pour les données déployées (en cours de développement).
- Suppression du cache des fichiers sources pour éviter des comportements inattendus.
- Correction d'un problème de zoom/dézoom sur les appareils Android et iOS.
- L'impersonation n'est plus appliquée aux routes commençant par `/admin/`.

### Autres changements
- Amélioration de la formulation du champ "is_staff".
- Correction d'un bug lié au téléchargement de fichiers.
