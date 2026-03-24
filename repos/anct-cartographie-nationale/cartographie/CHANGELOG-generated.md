## Changelog : cartographie (30 derniers jours, au 23 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances, la refactorisation du code pour une meilleure maintenabilité et l'ajout de capacités d'analyse via l'intégration de Matomo. Des améliorations ont également été apportées au composant web, notamment en termes de configuration de la carte et de gestion des filtres territoriaux.

### Évolutions fonctionnelles
- Ajout de la configuration de la carte basée sur l'URL pour l'application Next.js.
- Amélioration du filtrage territorial et de la navigation dans le composant web.
- Le composant web affiche désormais un indicateur de chargement pendant la récupération des données.
- Possibilité de définir une position et un zoom personnalisés pour la carte dans le composant web.
- Ajout d'un suivi d'événements avec Matomo pour analyser l'utilisation des composants.
- Amélioration de la recherche d'adresse.

### Évolutions techniques
- Refactorisation des requêtes `lieux` pour unifier le paramètre `collectivite`.
- Remplacement de l'API basée sur des pipes par un modèle de constructeur fluent.
- Extraction du schéma de pagination et utilisation de `withRegion` dans les routes API.
- Simplification des routes et amélioration de l'organisation du code.
- Migration des gestionnaires de routes vers une API basée sur des pipes.
- Migration des pages vers une API basée sur des pipes avec des middlewares.
- Refactorisation vers une architecture basée sur les "abilities" avec des bibliothèques partagées.
- Optimisation des appels API avec mise en cache et parallélisation.
- Suppression du code Next.js qui se retrouvait dans le bundle du composant web.
- Amélioration de la gestion des changements de configuration du composant web.
- Mutualisation des middlewares requis pour les routes et les pages.

### Autres changements
- Mise à jour de la documentation pour refléter la version 6.3.
- Ajout d'un docker-compose pour les tests locaux de Matomo.
- Suppression de commentaires redondants dans le code d'analyse.
- Suppression d'attributs de configuration inutilisés du composant web.
- Correction de problèmes de fragilité des tuiles et du survol des éléments du menu déroulant dans le composant web.
- Correction d'une faute de frappe (`curentPage` corrigé en `currentPage`).
- Plusieurs releases de correctifs et d'améliorations (6.1.0 à 6.6.0).
