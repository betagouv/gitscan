## Changelog : benefriches (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles fonctionnalités pour le calcul des impacts économiques liés à la reconversion de friches, notamment pour l'installation de panneaux photovoltaïques et la réhabilitation de sites. Des efforts importants ont également été réalisés pour améliorer la qualité du code, la robustesse des tests et l'architecture du projet, avec une migration vers des outils de test natifs Node.js et une refactorisation de l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité de définir des bilans économiques pour la réhabilitation de sites ([#44d4f46](https://github.com/incubateur-ademe/benefriches/commit/44d4f46)).
- Ajout de la possibilité de définir des bilans économiques pour l'installation de panneaux photovoltaïques ([#d52af12](https://github.com/incubateur-ademe/benefriches/commit/d52af12)).
- Ajout de la possibilité de définir des bilans économiques pour des projets urbains ([#95f462e](https://github.com/incubateur-ademe/benefriches/commit/95f462e)).
- Ajout de la possibilité de définir des bilans économiques pour la revente de sites ([#0e048f0](https://github.com/incubateur-ademe/benefriches/commit/0e048f0)).
- Ajout de descriptions contextuelles (tooltips) pour le champ de déconstruction dans le formulaire de réhabilitation ([#707a40f](https://github.com/incubateur-ademe/benefriches/commit/707a40f)).
- Amélioration de l'affichage de la répartition des sols dans les modales de bilan économique ([#a27a91a](https://github.com/incubateur-ademe/benefriches/commit/a27a91a)).
- Suppression d'un placeholder inutile dans la modale de contenu pour la réhabilitation de sites ([#345c72c](https://github.com/incubateur-ademe/benefriches/commit/345c72c)).
- Ajout d'une indication sur la surface contaminée et la surface du site dans les exports CSV ([#e2fb0a6](https://github.com/incubateur-ademe/benefriches/commit/e2fb0a6)).
- Ajout d'un champ "implique une réhabilitation" dans le wizard de création de projets urbains ([#b6cdb26](https://github.com/incubateur-ademe/benefriches/commit/b6cdb26)).

### Évolutions techniques
- Refactorisation majeure de l'architecture de l'application web, notamment du wizard de création de projets, pour une meilleure maintenabilité et extensibilité.
- Migration des tests unitaires et d'intégration de Vitest vers le framework natif Node.js `node:test` pour une meilleure performance et intégration avec l'environnement d'exécution.
- Amélioration de la qualité du code avec l'intégration de règles de linting plus strictes via `oxlint`.
- Mise à jour de la configuration de build de l'API pour utiliser SWC et ESM.
- Refactorisation de la gestion des impacts pour une meilleure cohérence et réutilisation.
- Amélioration de la documentation et ajout de nouvelles règles de test.
- Normalisation des tests E2E pour une meilleure fiabilité.

### Autres changements
- Documentation de l'assertion des titres d'étape dans les tests E2E.
- Ajout d'un Makefile pour simplifier les tâches de développement.
- Clarification des règles de test dans la documentation.
- Mise à jour des dépendances et correction de bugs mineurs.
- Ajout de liens d'édition par section dans le résumé des projets photovoltaïques.
- Amélioration de la navigation et de l'accessibilité dans l'interface utilisateur.
- Correction de problèmes d'affichage et de calcul dans les graphiques de bilan économique.
- Ajout de tests unitaires pour couvrir les cas limites de la fonction de calcul du seuil de rentabilité.
- Amélioration de la gestion des catégories d'impacts.
- Correction de bugs liés à l'affichage des données dans les tableaux de bord.
- Ajout de tests E2E pour couvrir les scénarios de création de projets photovoltaïques sur des friches.
- Amélioration de la gestion des erreurs et des messages d'information.
