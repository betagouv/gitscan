## Changelog : agreste (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, le projet agreste a connu des avancées significatives dans la gestion et l'affichage des publications, des thèmes et des collections. Des améliorations ont été apportées à la migration des données, à l'interface utilisateur (notamment les filtres et les résultats de recherche), et à l'infrastructure de déploiement. Des corrections de bugs et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la gestion des Publications, des Thèmes et des Collections.
- Amélioration du filtre des publications : les thèmes sont maintenant affichés au-dessus des collections dans la barre de recherche [#24](https://github.com/betagouv/agreste/pull/24).
- Possibilité de personnaliser le libellé du bouton "Voir toutes les publications".
- Le bouton "Voir toutes les publications" filtre désormais correctement les résultats.
- Correction d'une erreur 500 lors du changement de type d'en-tête avec une image d'arrière-plan [#512](https://github.com/betagouv/agreste/pull/512).
- Correction d'une erreur 500 liée à l'absence d'image [#90da814](https://github.com/betagouv/agreste/commit/90da814).
- Suppression des thèmes des cartes de résultats dans la page d'index des publications et dans le bloc "Publications récentes".
- Ajout d'un nouveau bloc "Publications récentes" et enregistrement de ce bloc à différents endroits de l'arborescence des blocs.

### Évolutions techniques
- Mise en place d'un workflow de publication via GitHub Actions et publication sur PyPi [#515](https://github.com/betagouv/agreste/pull/515).
- Amélioration de la recette de mise à jour pour gérer le projet de démonstration [#527](https://github.com/betagouv/agreste/pull/527).
- Mise en place du déploiement en un clic sur Scalingo [#487](https://github.com/betagouv/agreste/pull/487).
- Correction d'erreurs de validation dans le fichier `publiccode.yml` [#496](https://github.com/betagouv/agreste/pull/496).
- Correction du setup Docker [#519](https://github.com/betagouv/agreste/pull/519).
- Refactorisation du code pour utiliser un code commun pour les taxonomies.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Migration des données de publications : plusieurs phases de migration ont été implémentées et testées.
- Amélioration de la gestion des URL pour les filtres.
- Suppression de la gestion des thèmes dans le menu (simplification).

### Autres changements
- Mise à jour de la documentation et du fichier README.
- Correction de plusieurs erreurs de linting.
- Mise à jour des dépendances (requests, sqlparse, urllib3, python-dotenv, idna, cryptography, pillow) dans le projet de démonstration.
- Ajout de commentaires pour faciliter la maintenance et la compréhension du code.
- Suppression d'un script de gestion des traductions devenu inutile.
- Bump de version : 2.4.0-4.0.1, 3.1.1-4.0.1, 4.0.0-rc1-2.3.0, 4.0.0-rc1-2.2.0, 4.0.0-rc1-2.1.0.
