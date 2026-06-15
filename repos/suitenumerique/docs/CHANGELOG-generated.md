## Changelog : docs (30 derniers jours, au 2026-06-12)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment avec l'ajout du mode présentateur, l'amélioration de la recherche, et l'accessibilité. Des corrections de bugs et des optimisations de performance ont également été apportées, en particulier au niveau de la gestion des commentaires et du streaming de contenu. L'ajout d'événements de suivi avec PostHog permet une meilleure analyse de l'utilisation de la plateforme.

### Évolutions fonctionnelles
- Ajout du mode présentateur pour faciliter les présentations de documents [#2321](https://github.com/suitenumerique/docs/issues/2321).
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches [#2407](https://github.com/suitenumerique/docs/issues/2407).
- Possibilité de quitter un document [#2410](https://github.com/suitenumerique/docs/issues/2410).
- Ajout d'une barre latérale droite contenant la table des matières et les commentaires.
- Ajout d'une fonctionnalité permettant de retrouver le document parent lors de la recherche dans les sous-documents [#1952](https://github.com/suitenumerique/docs/issues/1952).
- Ajout d'un breadcrumb dans les résultats de recherche.
- Possibilité de marquer un document comme résolu dans la vue des threads.

### Évolutions techniques
- Optimisation des requêtes pour la sérialisation des commentaires afin de corriger un problème de performance (N+1 queries) [#2415](https://github.com/suitenumerique/docs/issues/2415).
- Amélioration du streaming de contenu sous ASGI pour une meilleure réactivité.
- Refactorisation de la configuration PostHog pour une meilleure organisation.
- Suppression du code de masquage des documents.
- Mise à jour de Blocknote vers la version 0.51.4.
- Suppression d'un job de test E2E obsolète.
- Suppression de code inutilisé dans la classe Paginator.
- Ajout de support pour le déploiement sur des plateformes PaaS comme Scalingo.
- Amélioration de la gestion des connexions à la base de données pour éviter les erreurs lors des tests.
- Mise à jour des dépendances JavaScript.

### Autres changements
- Améliorations de l'accessibilité :
    - Ajout d'attributs ARIA pour les éléments décoratifs.
    - Amélioration de la navigation au clavier et de la prise en charge des lecteurs d'écran en mode présentateur [#2383](https://github.com/suitenumerique/docs/issues/2383).
    - Amélioration du focus sur les champs de saisie.
- Corrections de bugs mineurs liés à l'interface utilisateur et à l'affichage.
- Ajout d'événements de suivi avec PostHog pour diverses actions (création, suppression, duplication de documents, etc.).
- Mise à jour de la documentation pour inclure les nouveaux paramètres de configuration.
- Corrections de problèmes liés à l'affichage des titres longs dans la table des matières.
- Amélioration de la gestion des erreurs et des cas limites.
- Mise à jour des traductions.
- Correction d'un problème de crash lors de l'utilisation de GTranslate et du zoom.
- Correction d'un problème d'affichage des emojis dans les PDF.
- Correction de l'ordre des éléments dans la corbeille.
- Ajout de tests E2E pour le mode présentateur.
