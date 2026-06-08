## Changelog : meet (30 derniers jours, au 4 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des fichiers, notamment un accès sécurisé et une administration dédiée. L'expérience utilisateur est également améliorée avec l'introduction du picture-in-picture, des réactions et des corrections de bugs pour une meilleure stabilité et fluidité. Des mises à jour de sécurité et des optimisations techniques ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une administration dédiée pour la gestion des fichiers [#1387](https://github.com/suitenumerique/meet/issues/1387).
- Support étendu des formats vidéo et audio pour les résumés de réunion [#1358](https://github.com/suitenumerique/meet/issues/1358).
- Introduction du mode Picture-in-Picture pour les réunions.
- Ajout de réactions pendant les réunions.
- Possibilité de muter les autres participants en fonction de la configuration de la salle.
- Support de la configuration et du niveau d'accès des salles via l'API externe [#1260](https://github.com/suitenumerique/meet/issues/1260).
- Amélioration de l'assignation des intervenants.

### Évolutions techniques
- Refactorisation de l'API pour une meilleure gestion de la configuration des salles.
- Utilisation de `uv` pour la gestion des dépendances dans les agents.
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (aiohttp, urllib3, core-js, webpack-dev-server, django).
- Amélioration de la robustesse du processus de suppression de fichiers.
- Optimisation du chargement des ressources frontend (code splitting, lazy loading).
- Amélioration de la gestion des erreurs et de la concurrence lors de la création d'utilisateurs.
- Mise à jour de la documentation de l'API.
- Utilisation de Rollup pour la visualisation des bundles frontend.
- Amélioration de la configuration des logs.

### Autres changements
- Correction de liens dans les emails de notification de l'enregistrement.
- Correction de bugs mineurs dans l'interface utilisateur (espacement, positionnement).
- Correction de problèmes de compatibilité avec certains navigateurs.
- Amélioration de la gestion des variables d'environnement pour le développement.
- Ajout d'une commande de gestion pour fusionner les utilisateurs en double.
- Mise à jour de la version du chart Helm.
- Correction de la configuration des jobs Kubernetes.
- Suppression de dépendances inutiles.
