## Changelog : aigle-frontend (30 derniers jours, au 21 juillet 2026)

### Résumé
Les dernières mises à jour d'aigle-frontend se concentrent sur l'amélioration des fonctionnalités d'administration, notamment la gestion des utilisateurs et des groupes, ainsi que sur l'optimisation des processus de déploiement et de gestion des données. Des améliorations ont également été apportées à l'interface DDT (Droit de Préemption Urbain) et à la gestion des signalements.

### Évolutions fonctionnelles
- Amélioration du tableau de bord DDT avec de nouvelles fonctionnalités. [#57](https://github.com/MTES-MCT/aigle-frontend/pull/57)
- Possibilité de bloquer des zones urbaines. [#58](https://github.com/MTES-MCT/aigle-frontend/pull/58)
- Ajout d'une interface statistique pour le DDTM (Droit de Préemption Urbain Métropolitain), accessible en interne pour le moment. [#56](https://github.com/MTES-MCT/aigle-frontend/pull/56)
- Correction d'un bug empêchant le téléchargement du PDF de signalement en l'absence de parcelle. [#58](https://github.com/MTES-MCT/aigle-frontend/pull/58)
- Ajout d'un bouton pour copier l'UUID dans les vues de tableau de l'administration. [#52](https://github.com/MTES-MCT/aigle-frontend/pull/52)
- Amélioration de la gestion des collectivités dans l'administration. [#56](https://github.com/MTES-MCT/aigle-frontend/pull/56)
- Vérification du statut "interne" des utilisateurs lors de la création/modification dans l'administration. [#58](https://github.com/MTES-MCT/aigle-frontend/pull/58)
- Limitation du nombre d'éditions multiples augmentée à 500. [#57](https://github.com/MTES-MCT/aigle-frontend/pull/57)

### Évolutions techniques
- Mise en place de la configuration de Brevo pour remplacer Crisp Chat. [#50](https://github.com/MTES-MCT/aigle-frontend/pull/50)
- Amélioration des processus de déploiement : possibilité de déployer une seule batch ou une seule ZAE. [#55](https://github.com/MTES-MCT/aigle-frontend/pull/55)
- Possibilité de déployer uniquement des parties spécifiques de l'application. [#56](https://github.com/MTES-MCT/aigle-frontend/pull/56)
- Suppression des routes liées aux statistiques (nettoyage). [#53](https://github.com/MTES-MCT/aigle-frontend/pull/53)
- Prévention de l'assignation simultanée de départements et de communes à un groupe d'utilisateurs dans l'administration. [#54](https://github.com/MTES-MCT/aigle-frontend/pull/54)

### Autres changements
- Suppression d'un statut illégal (rollback). [#54](https://github.com/MTES-MCT/aigle-frontend/pull/54)
