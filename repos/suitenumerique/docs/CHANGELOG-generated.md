## Changelog : docs (30 derniers jours, au 2026-04-15)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de l'accessibilité, la correction de bugs et l'optimisation des performances. Des améliorations significatives ont été apportées à l'accessibilité au clavier et aux lecteurs d'écran, notamment dans la recherche, les menus et les tableaux. Des corrections ont également été apportées pour résoudre des problèmes liés à la gestion des documents, aux tests et à la stabilité générale de l'application.

### Évolutions fonctionnelles
- Ajout d'un indicateur visuel pour les résultats de recherche afin de les rendre plus facilement identifiables.
- Amélioration de la gestion des documents : les documents épinglés sont maintenant triés par date de dernière mise à jour.
- Possibilité d'ouvrir les liens internes avec le bouton central de la souris ou la touche Ctrl/Cmd.
- Ajout d'un "easter egg" lors de la création d'émojis dans les documents.
- Ajout d'un indicateur visuel pour les documents en cours de conversion.
- Amélioration de la gestion des documents lors de la duplication.
- Ajout d'une fonctionnalité de recherche.

### Évolutions techniques
- Refactorisation des tests E2E pour une meilleure organisation et compatibilité.
- Amélioration de la gestion des erreurs 5xx avec une redirection vers une page dédiée.
- Optimisation de la gestion des requêtes de réconciliation pour éviter les conditions de concurrence.
- Mise à jour des dépendances : Axios, Next.js, PyJWT, Lodash et requests.
- Ajout d'un workflow CI pour exécuter les tests E2E séparément.
- Amélioration de la gestion de la mémoire pour le fournisseur Yjs.
- Ajout d'un mécanisme de debounce pour la reconnexion WebSocket.
- Suppression des paramètres UTM des URLs.
- Ajout d'un système de gestion des ressources.
- Ajout d'un pool de connexions PostgreSQL configurable.

### Autres changements
- Mise à jour de la documentation et des modèles de pull request.
- Amélioration de la gestion des traductions.
- Corrections de style et de linting.
- Ajout de commentaires et de logs pour faciliter le débogage.
- Ajout d'un favicon par défaut.
- Mise à jour des tests pour couvrir les améliorations d'accessibilité.
- Ajout d'une politique concernant l'utilisation de l'IA.
- Correction de la structure des alertes d'erreur 5xx.
- Amélioration de l'affichage des icônes dans l'arborescence des documents.
- Suppression de la pagination pour la liste des threads.
- Correction de bugs mineurs liés à l'interface utilisateur et au comportement de l'application.
