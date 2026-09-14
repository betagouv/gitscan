## Changelog : docs (30 derniers jours, au 11 septembre 2026)

### Résumé
Cette période a été marquée par un enrichissement significatif des capacités d'édition, notamment avec l'introduction de blocs mathématiques, de diagrammes et d'une fonction de recherche et remplacement. L'expérience utilisateur a été renforcée par de nouvelles options d'exportation (PDF, images) et une attention accrue portée à l'accessibilité. En parallèle, des optimisations techniques importantes ont été réalisées pour améliorer les performances des requêtes SQL et la stabilité de l'infrastructure.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités d'édition** : Ajout de blocs pour les mathématiques et les diagrammes, intégration de la fonction "Rechercher et remplacer", et ajout d'un compteur de mots.
- **Exportation et partage** : Possibilité d'exporter les présentations en PDF (avec option de filigrane), export de n'importe quelle image raster vers PDF, et ajout de la fonctionnalité "Copier le lien vers un bloc".
- **Améliorations de l'interface (UI/UX)** : Refonte de la page de confirmation d'email, unification de la barre d'outils, passage du système de "favoris" à des "étoiles", et amélioration de l'affichage de la liste des documents (tri par nom, grille améliorée).
- **Accessibilité** : Amélioration de la navigation au clavier pour les liens inter-documents, annonces pour lecteurs d'écran lors du chargement de la recherche, et gestion des éléments décoratifs (emojis) pour les outils d'assistance.
- **Corrections** : Résolution de bugs concernant la duplication de documents vides, la préservation des titres lors de l'ajout d'emojis, et les erreurs de rendu dans les blocs de code.

### Évolutions techniques
- **Optimisation des performances** : Amélioration des requêtes SQL (suppression de fonctions coûteuses), optimisation de l'utilisation CPU pour l'authentification des médias, et ajustement des options de cache Redis.
- **Architecture et Refactoring** : Mise à jour majeure vers Blocknote 0.54.0, extraction de composants UI partagés (header et footer), et transition du kit d'interface vers un système de composants unifié.
- **Infrastructure et DevOps** : Optimisation des sondes de disponibilité Docker (liveness/readiness), changement de l'image docspec vers GHCR, et configuration de la gestion de la mémoire pour les uploads de données.
- **Stabilité et Tests** : Renforcement de la couverture de tests E2E (notamment pour les exports PNG, WebP et PDF) et correction de tests instables.

### Autres changements
- **Internationalisation** : Ajout de la langue polonaise et mise à jour des chaînes de caractères traduites.
- **Documentation** : Ajout de docstrings pour améliorer la clarté du code frontend.
