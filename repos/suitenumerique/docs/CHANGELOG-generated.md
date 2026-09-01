## Changelog : docs (30 derniers jours, au 28 août 2026)

### Résumé
Cette période a été marquée par l'enrichissement de l'expérience d'édition avec l'ajout d'outils de recherche, de comptage de mots et de liens directs vers les blocs. Le projet a également franchi une étape importante en matière d'accessibilité et de performance, tout en modernisant son infrastructure avec le passage à Python 3.14.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités d'édition** : ajout de la recherche et du remplacement dans l'éditeur [#2570](https://github.com/suitenumerique/docs/issues/2570), d'un compteur de mots dans l'en-tête [#2549](https://github.com/suitenumerique/docs/issues/2549), de la possibilité de copier un lien vers un bloc [#2547](https://github.com/suitenumerique/docs/issues/2547), et de la fonction de présentation à partir d'un bloc.
- **Gestion documentaire** : ajout de l'option de déplacement de document [#2555](https://github.com/suitenumerique/docs/issues/2555), de la possibilité d'imprimer depuis le menu des options, et du tri par nom dans la liste des documents.
- **Améliorations de l'interface** : passage du système de "favoris" aux "étoiles" [#2539](https://github.com/suitenumerique/docs/issues/2539), réinitialisation de l'état du panneau latéral entre les documents [#2583](https://github.com/suitenumerique/docs/issues/2583), et mise à jour de la barre d'outils documentaire.
- **Accessibilité** : amélioration de la navigation au clavier pour les liens inter-documents [#2391](https://github.com/suitenumerique/docs/issues/2391), annonce de l'état de chargement de la recherche pour les lecteurs d'écran [#2526](https://github.com/suitenumerique/docs/issues/2526), et application d'un style de focus global.
- **Corrections** : résolution du problème de barre d'outils tronquée dans les commentaires [#2585](https://github.com/suitenumerique/docs/issues/2585), correction de l'affichage des documents importés, rafraîchissement des épingles après suppression/restauration [#2581](https://github.com/suitenumerique/docs/issues/2581), et correction de l'export d'images avec des URLs relatives [#2573](https://github.com/suitenumerique/docs/issues/2573).

### Évolutions techniques
- **Optimisation des performances** : réduction de la consommation CPU et optimisation des requêtes SQL pour l'authentification des médias [#2594](https://github.com/suitenumerique/docs/issues/2594) et profilage de l'API via `django-silk`.
- **Refactoring et architecture** : transition de `ui-kit` vers `ui-components`, refonte de la grille de documents, et passage du *debouncing* au *throttling* pour améliorer la réactivité de l'interface.
- **Infrastructure et Backend** : montée de version vers Python 3.14, mise à jour des outils de linting (Ruff, Pylint), et correction des variables d'environnement Keycloak pour les déploiements en auto-hébergement.
- **Sécurité et stabilité** : correction de l'initialisation de Sentry, résolution de vulnérabilités de sécurité et correction des erreurs de base de données dans les jobs Helm.

### Autres changements
- **Internationalisation** : ajout de la langue polonaise et mise à jour des chaînes de traduction.
- **Design et Assets** : mise à jour du logo et passage des assets d'onboarding au format WebM/WebP pour optimiser le chargement.
