## Changelog : aigle-frontend (30 derniers jours, au 03 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de l'interface d'administration, notamment pour le déploiement et la gestion des données. Des correctifs et des améliorations ont également été apportés à la gestion des utilisateurs et à la cartographie.

### Évolutions fonctionnelles
- Ajout de boutons pour copier l'UUID dans les tableaux de l'interface d'administration. [#52](https://github.com/MTES-MCT/aigle-frontend/pull/52)
- Ajout de filtres prédéfinis pour faciliter la recherche et la visualisation des données. [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47)
- Ajout des statuts "illégal" et "à contrôler" pour une meilleure gestion des éléments détectés. [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47)
- Ajout de la valeur "JUGEMENT" au statut de contrôle de détection. [#48](https://github.com/MTES-MCT/aigle-frontend/pull/48)
- Amélioration de l'interface pour afficher les données déployées, incluant les données Sitadel. [#48](https://github.com/MTES-MCT/aigle-frontend/pull/48)
- Possibilité de télécharger des fichiers CSV/XLSX dans les vues de tableaux, même lorsque la catégorie "autres" est sélectionnée. [#46](https://github.com/MTES-MCT/aigle-frontend/pull/46)
- Ajout d'un champ "is_staff" pour les utilisateurs, permettant de définir des rôles d'administration. [#45](https://github.com/MTES-MCT/aigle-frontend/pull/45)
- L'impersonation n'est plus appliquée aux routes commençant par `/admin/`. [#45](https://github.com/MTES-MCT/aigle-frontend/pull/45)

### Évolutions techniques
- Refonte de la gestion des commandes d'administration, avec ajout d'un bouton de relance en cas d'erreur. [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47)
- Amélioration de la gestion des arguments des commandes d'administration. [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47)
- Suppression des routes liées aux statistiques. [#53](https://github.com/MTES-MCT/aigle-frontend/pull/53)
- Correction d'un problème empêchant la rotation de la carte. [#51](https://github.com/MTES-MCT/aigle-frontend/pull/51)
- Nettoyage du code et suppression de commentaires inutiles. [#50](https://github.com/MTES-MCT/aigle-frontend/pull/50)
- Optimisation du déploiement pour ne déployer qu'un seul batch ou une seule ZAE à la fois. [#54](https://github.com/MTES-MCT/aigle-frontend/pull/54)
- Prévention de l'assignation de départements et de communes à un groupe d'utilisateurs dans l'administration. [#52](https://github.com/MTES-MCT/aigle-frontend/pull/52)

### Autres changements
- Amélioration de l'interface pour la gestion des données déployées. [#49](https://github.com/MTES-MCT/aigle-frontend/pull/49)
- Modification de l'ordre des statuts pour placer "JUGEMENT" avant "OBSERVATION_REPORT_REDACTED". [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47)
- Amélioration de la gestion des commandes d'administration (progress). [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47)
- Correction d'un problème avec la commande `run_command`. [#46](https://github.com/MTES-MCT/aigle-frontend/pull/46)
- Ajustement de la formulation du champ `is_staff`. [#45](https://github.com/MTES-MCT/aigle-frontend/pull/45)
