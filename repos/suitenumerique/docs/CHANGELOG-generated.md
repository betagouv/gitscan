## Changelog : docs (30 derniers jours, au 15 juin 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à la recherche, à l'accessibilité et à la collaboration. L'ajout du mode présentateur et la possibilité de quitter un document sont des fonctionnalités notables. Des corrections de bugs et des optimisations de performance ont également été implémentées pour améliorer l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Ajout de la possibilité de quitter un document [#2410](https://github.com/suitenumerique/docs/issues/2410).
- Implémentation du mode présentateur pour faciliter les présentations [#2321](https://github.com/suitenumerique/docs/issues/2321).
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches [#2407](https://github.com/suitenumerique/docs/issues/2407).
- Ajout d'une fonctionnalité permettant de rechercher des documents parents lors de la recherche de sous-documents [#1952](https://github.com/suitenumerique/docs/issues/1952).
- Ajout d'un breadcrumb dans les résultats de recherche pour une meilleure navigation [#2310](https://github.com/suitenumerique/docs/issues/2310).
- Ajout d'une action pour "résoudre" les threads de commentaires [#2395](https://github.com/suitenumerique/docs/issues/2395).

### Évolutions techniques
- Optimisation des requêtes pour la récupération des commentaires d'un thread, corrigeant un problème de performance (N+1 queries) [#2415](https://github.com/suitenumerique/docs/issues/2415).
- Refonte de l'architecture de recherche pour permettre la recherche globale dans les sous-documents [#2310](https://github.com/suitenumerique/docs/issues/2310).
- Amélioration de la gestion des connexions à la base de données pour éviter les erreurs lors des tests [#2385](https://github.com/suitenumerique/docs/issues/2385).
- Mise en place d'un service dédié pour la conversion de documents avec Yjs [#2358](https://github.com/suitenumerique/docs/issues/2358).
- Refactorisation de la configuration PostHog pour une meilleure organisation [#2378](https://github.com/suitenumerique/docs/issues/2378).
- Suppression d'un job de test E2E obsolète [#2404](https://github.com/suitenumerique/docs/issues/2404).
- Mise à jour de Blocknote vers la version 0.51.4 [#2373](https://github.com/suitenumerique/docs/issues/2373).

### Autres changements
- Améliorations de l'accessibilité :
    - Utilisation d'éléments de titre appropriés pour la section des documents épinglés [#2380](https://github.com/suitenumerique/docs/issues/2380).
    - Ajout de liens d'ancrage pour les entrées de la table des matières [#2390](https://github.com/suitenumerique/docs/issues/2390).
    - Amélioration du support de lecteur d'écran et du clavier en mode présentateur [#2383](https://github.com/suitenumerique/docs/issues/2383).
    - Amélioration de l'accessibilité du modal d'export [#2422](https://github.com/suitenumerique/docs/issues/2422).
    - Amélioration de l'accessibilité des composants de recherche [#2396](https://github.com/suitenumerique/docs/issues/2396).
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests unitaires pour les hooks du mode présentateur.
- Mise à jour des chaînes de traduction.
- Ajout de la configuration manquante `CONVERSION_UPLOAD_ENABLED` dans la documentation.
- Ajout d'événements de suivi avec PostHog pour diverses actions (création/suppression de documents, création de commentaires, etc.).
- Correction d'un problème de streaming de contenu de document sous ASGI.
- Correction de l'ordre de la réponse de la corbeille.
- Correction d'un problème de sécurité lié à une alerte de dépendance.
