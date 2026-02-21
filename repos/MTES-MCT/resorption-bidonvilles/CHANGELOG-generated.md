## Changelog : resorption-bidonvilles (30 derniers jours)

### Résumé
Cette période a été marquée par d'importantes améliorations de la plateforme, notamment autour de la gestion des logs de connexion, de la recherche et de l'affichage des données cartographiques. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de l'application. Plusieurs mises à jour de sécurité ont été intégrées.

### Évolutions fonctionnelles
- Ajout de la gestion des logs de connexion : visualisation, filtrage et purge des logs. (#1412, #1410, #1409, #1402)
- Amélioration de la recherche : possibilité de rechercher des actions par ID, des localisations géographiques et des structures opérateurs. (#1406, #1405, #1404, #1403)
- Ajout d'un bouton pour définir un "Objectif résorption" pour les sites. (#1398)
- Amélioration de l'affichage des points d'intérêt sur la carte, avec des optimisations de performance. (#1397)
- Possibilité de filtrer les valeurs `undefined` et `null` pour éviter les erreurs SQL. (#1387)
- Ajout d'un indicateur du taux de mise à jour des actions. (#1396)

### Évolutions techniques
- Migration de `isPlural` vers des utilitaires. (#1401)
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité. (#1400)
- Optimisation des performances du chargement des points d'intérêt sur la carte. (#1395)
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Snyk et Dependabot). (#1391, #1390)
- Amélioration de la gestion des erreurs et des validations.
- Utilisation de formes géométriques pour les marqueurs sur la carte afin d'améliorer les performances.

### Autres changements
- Correction de la police utilisée dans les PDF exportés.
- Suppression de commentaires inutiles et de code mort.
- Amélioration de la documentation et des tests unitaires.
- Corrections de typographie et de wording.
- Suppression de fichiers inutilisés.
- Amélioration de l'isolation des tests unitaires.
- Correction de l'URL pour supprimer le "/" final.
