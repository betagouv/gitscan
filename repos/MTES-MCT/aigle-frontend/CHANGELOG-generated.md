## Changelog : aigle-frontend (30 derniers jours, au 26 juin 2026)

### Résumé
Les dernières mises à jour d'aigle-frontend se concentrent sur l'amélioration de l'interface d'administration, notamment pour la gestion des commandes et des données déployées. Des améliorations ont également été apportées à la gestion des utilisateurs et des statuts des éléments, ainsi que des corrections de bugs pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de nouveaux statuts : "illégal" et "à contrôler" [#51](https://github.com/MTES-MCT/aigle-frontend/pull/51).
- Ajout d'un bouton pour copier l'UUID dans les vues de tableau, facilitant la manipulation des identifiants uniques [#52](https://github.com/MTES-MCT/aigle-frontend/pull/52).
- Possibilité de télécharger des fichiers CSV/XLSX dans les vues de tableau, même lorsque la catégorie "autres" est sélectionnée [#46](https://github.com/MTES-MCT/aigle-frontend/pull/46).
- Ajout de la valeur "JUGEMENT" au statut de contrôle de détection [#48](https://github.com/MTES-MCT/aigle-frontend/pull/48).
- Ajout de données Sitadel à l'aperçu du déploiement [#48](https://github.com/MTES-MCT/aigle-frontend/pull/48).
- Ajout de filtres prédéfinis [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47).
- Ajout d'un champ "is_staff" pour les utilisateurs, permettant de définir des rôles d'administration [#45](https://github.com/MTES-MCT/aigle-frontend/pull/45).

### Évolutions techniques
- Refonte de la gestion des arguments de commande dans l'interface d'administration [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47).
- Amélioration de la gestion des commandes d'administration, avec un bouton de relance en cas d'erreur [#47](https://github.com/MTES-MCT/aigle-frontend/pull/47).
- Nettoyage du code et suppression de commentaires inutiles [#50](https://github.com/MTES-MCT/aigle-frontend/pull/50).
- Refactorisation de la logique de `run_command` pour corriger un bug [#46](https://github.com/MTES-MCT/aigle-frontend/pull/46).
- Implémentation d'un déploiement en un clic [#53](https://github.com/MTES-MCT/aigle-frontend/pull/53).
- Prévention de la rotation accidentelle de la carte [#51](https://github.com/MTES-MCT/aigle-frontend/pull/51).
- Suppression des routes liées aux statistiques [#53](https://github.com/MTES-MCT/aigle-frontend/pull/53).
- Amélioration de l'interface pour les données déployées [#49](https://github.com/MTES-MCT/aigle-frontend/pull/49).
- Amélioration de la gestion des paramètres d'URL dans l'administration [#48](https://github.com/MTES-MCT/aigle-frontend/pull/48).

### Autres changements
- Correction d'un bug empêchant l'application de l'impersonation pour les routes d'administration.
- Modification de l'ordre des statuts pour placer "JUGEMENT" avant "OBSERVATION_REPORT_REDACTED".
- Amélioration de la gestion des permissions pour empêcher l'attribution de départements et de communes à un groupe d'utilisateurs [#52](https://github.com/MTES-MCT/aigle-frontend/pull/52).
- Ajustement de la formulation du champ "is_staff" pour plus de clarté.
