## Changelog : aigle-frontend (30 derniers jours, au 9 juillet 2026)

### Résumé
Les dernières mises à jour d'aigle-frontend se concentrent sur l'amélioration des fonctionnalités d'administration et de gestion des données, notamment pour le tableau de bord DDT. Des améliorations ont été apportées au déploiement, à la recherche et à la gestion des statuts des données. L'interface utilisateur a également été optimisée pour une meilleure expérience.

### Évolutions fonctionnelles

*   **Tableau de bord DDT :** Amélioration de l'interface et des fonctionnalités. [#57](https://github.com/MTES-MCT/aigle-frontend/pull/57)
*   **Gestion des statuts :** Ajout de nouveaux statuts "illégal" et "à contrôler" pour une meilleure classification des données. [#51](https://github.com/MTES-MCT/aigle-frontend/pull/51)
*   **Copie d'UUID :** Ajout d'un bouton pour copier facilement l'UUID dans les vues de tableau. [#52](https://github.com/MTES-MCT/aigle-frontend/pull/52)
*   **Filtres prédéfinis :** Implémentation de filtres prédéfinis pour faciliter la recherche et l'analyse des données. [#49](https://github.com/MTES-MCT/aigle-frontend/pull/49)
*   **Déploiement simplifié :** Possibilité de déployer une seule batch ou une seule ZAE. [#54](https://github.com/MTES-MCT/aigle-frontend/pull/54)
*   **Limites d'édition multiples :** Augmentation de la limite d'édition multiple à 500. [#56](https://github.com/MTES-MCT/aigle-frontend/pull/56)

### Évolutions techniques

*   **Commandes d'administration :** Amélioration et ajout de nouvelles commandes d'administration (recherche, exécution, progression).
*   **Refactoring du déploiement :** Optimisation du processus de déploiement pour ne déployer que les parties spécifiées.
*   **Suppression de routes obsolètes :** Suppression des routes liées aux statistiques. [#53](https://github.com/MTES-MCT/aigle-frontend/pull/53)
*   **Ordre des statuts :** Modification de l'ordre des statuts, plaçant "JUGEMENT" avant "OBSERVATION_REPORT_REDACTED". [#50](https://github.com/MTES-MCT/aigle-frontend/pull/50)
*   **Prévention d'assignations incorrectes :** Empêche l'assignation simultanée de départements et de communes à un groupe d'utilisateurs. [#55](https://github.com/MTES-MCT/aigle-frontend/pull/55)

### Autres changements

*   Correction d'un bug empêchant la rotation accidentelle de la carte. [#48](https://github.com/MTES-MCT/aigle-frontend/pull/48)
*   Nettoyage de commentaires inutiles dans le code.
*   Améliorations de l'interface de gestion des données déployées.
*   Rollback d'un statut illégal. [#54](https://github.com/MTES-MCT/aigle-frontend/pull/54)
