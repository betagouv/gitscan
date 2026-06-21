## Changelog : docs (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout du mode présentateur, l'amélioration de la recherche, l'accessibilité et la correction de bugs. Des améliorations techniques ont également été apportées, notamment des optimisations de performance et la gestion des événements pour le suivi analytique.

### Évolutions fonctionnelles
- Ajout de la possibilité de quitter un document [#2365](https://github.com/suitenumerique/docs/issues/2365).
- Implémentation du mode présentateur pour faciliter les présentations [#2321](https://github.com/suitenumerique/docs/issues/2321).
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches [#2407](https://github.com/suitenumerique/docs/issues/2407).
- Ajout d'une barre latérale dédiée aux commentaires pour une meilleure organisation [#2279](https://github.com/suitenumerique/docs/issues/2279).
- Amélioration de la recherche pour inclure les documents parents [#1952](https://github.com/suitenumerique/docs/issues/1952).
- Ajout d'une limite au nombre de réactions par commentaire [#1978](https://github.com/suitenumerique/docs/issues/1978).
- Possibilité de supprimer les relations d'un utilisateur lors de sa suppression (backend) [#2410](https://github.com/suitenumerique/docs/issues/2410).

### Évolutions techniques
- Optimisation des requêtes pour la récupération des commentaires d'un fil de discussion, réduisant ainsi les problèmes de performance (N+1 queries) [#2415](https://github.com/suitenumerique/docs/issues/2415).
- Amélioration de la gestion des connexions à la base de données pour éviter les erreurs lors des tests [#2385](https://github.com/suitenumerique/docs/issues/2385).
- Refactorisation de la pagination pour supprimer un paramètre inutilisé.
- Mise en place d'un système de capture d'événements avec PostHog pour le suivi de l'utilisation des documents (création, suppression, favoris, etc.).
- Amélioration de la gestion des conversions de documents avec un service dédié.
- Correction de problèmes de streaming de contenu sous ASGI.

### Autres changements
- Améliorations de l'accessibilité :
    - Utilisation d'éléments de titre appropriés pour la section des documents épinglés.
    - Ajout d'attributs ARIA pour améliorer la navigation au clavier et la compatibilité avec les lecteurs d'écran.
    - Amélioration de la gestion du focus dans les boîtes de dialogue.
- Mise à jour des traductions [#2377](https://github.com/suitenumerique/docs/issues/2377) et [#2306](https://github.com/suitenumerique/docs/issues/2306).
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression d'un job de test CI obsolète [#2404](https://github.com/suitenumerique/docs/issues/2404).
- Ajout de la configuration manquante `CONVERSION_UPLOAD_ENABLED` dans la documentation [#2358](https://github.com/suitenumerique/docs/issues/2358).
- Correction de problèmes de mise en page et d'affichage.
- Mise à jour de la dépendance Blocknote à la version 0.51.4.
