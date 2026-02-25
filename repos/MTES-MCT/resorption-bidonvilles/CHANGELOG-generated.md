## Changelog : resorption-bidonvilles (30 derniers jours)

### Résumé
Cette période a été marquée par d'importantes améliorations de la plateforme, notamment l'ajout de la gestion des logs de connexion, l'amélioration de la recherche et de la gestion des structures, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations de l'interface utilisateur ont également été apportées, notamment pour la gestion des erreurs et l'affichage des informations.

### Évolutions fonctionnelles
- Ajout de la gestion des logs de connexion : visualisation, filtrage et purge des logs. (#2606)
- Amélioration de la recherche : possibilité de rechercher par ID d'action, localisation géographique et structures "opérateurs". (#2584, #2606)
- Ajout d'un bouton pour mettre à jour le champ "Objectif résorption" sur les fiches de site. (#2603)
- Amélioration de l'affichage du taux de MAJ des actions. (#2602)
- Possibilité de filtrer les actions par structure "opératrice". (#2584)
- Ajout d'un onglet affichant le taux de MAJ des actions par département. (#2591)

### Évolutions techniques
- Mise à jour de la bibliothèque Dockerfile pour réduire les vulnérabilités.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Optimisation des requêtes SQL pour améliorer les performances.
- Migration de `isPlural` vers un utilitaire.
- Utilisation de composants DSFR pour une meilleure cohérence visuelle et accessibilité.
- Ajout de tests unitaires pour les nouvelles fonctionnalités.
- Sécurisation du traitement des données et validation des entrées.
- Amélioration du typage du code.

### Autres changements
- Correction de bugs mineurs liés à l'affichage et à la gestion des erreurs.
- Mise à jour de la documentation.
- Suppression de commentaires inutiles.
- Modifications de wording pour une meilleure clarté.
- Correction de l'isolation des tests unitaires.
- Suppression de "/" en fin d'URL.
- Mise à jour des dépendances.
