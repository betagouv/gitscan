## Changelog : benefriches (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'architecture du projet, notamment au niveau de l'API et du formulaire de création de projet. Des refactorings importants ont été effectués pour une meilleure maintenabilité et extensibilité. Des corrections et améliorations ont également été apportées à l'expérience utilisateur, notamment dans le processus de création de projets photovoltaïques et urbains, ainsi qu'à la gestion des impacts.

### Évolutions fonctionnelles
- Ajout d'une étape "implique-t-il une remise en culture" au formulaire de création de projet urbain. [#40c312a](https://github.com/incubateur-ademe/benefriches/commit/40c312a)
- Amélioration de l'accessibilité du formulaire d'édition de projet photovoltaïque. [#8adcbca](https://github.com/incubateur-ademe/benefriches/commit/8adcbca)
- Affichage de la surface contaminée et de la surface du site dans les exports CSV des projets de reconversion. [#e2fb0a6](https://github.com/incubateur-ademe/benefriches/commit/e2fb0a6)
- Amélioration des messages d'erreur lors de l'authentification avec un token. [#8d7bd5c](https://github.com/incubateur-ademe/benefriches/commit/8d7bd5c)
- Suppression de la vue graphique des impacts et réorganisation des sélecteurs. [#1e50680](https://github.com/incubateur-ademe/benefriches/commit/1e50680)
- Calcul des impacts avec un niveau de seuil de rentabilité et utilisation dans l'onglet "évaluation des impacts". [#4374377](https://github.com/incubateur-ademe/benefriches/commit/4374377)

### Évolutions techniques
- Migration de l'API vers ESM natif avec SWC pour la construction et un chargeur de tests ESM. [#3bbffae](https://github.com/incubateur-ademe/benefriches/commit/3bbffae)
- Remplacement des tests Vitest par node:test pour l'API et les intégrations. [#b60acd5](https://github.com/incubateur-ademe/benefriches/commit/b60acd5)
- Refactorings importants du code web pour une meilleure architecture et une plus grande modularité, notamment autour du formulaire de création de projet (wizard-form). [#ba05d43](https://github.com/incubateur-ademe/benefriches/commit/ba05d43), [#8cd5b96](https://github.com/incubateur-ademe/benefriches/commit/8cd5b96), [#57d0001](https://github.com/incubateur-ademe/benefriches/commit/57d0001)
- Ajout de règles oxlint pour renforcer la qualité du code et l'application de l'architecture propre. [#0964159](https://github.com/incubateur-ademe/benefriches/commit/0964159)
- Déplacement des interfaces `DateProvider` et `UidGenerator` hors des adaptateurs. [#7571e70](https://github.com/incubateur-ademe/benefriches/commit/7571e70)
- Amélioration de la configuration de l'environnement de développement avec un Makefile et une mise à jour des noms de fichiers docker-compose. [#f0a0514](https://github.com/incubateur-ademe/benefriches/commit/f0a0514)
- Refactor des tests E2E pour améliorer la robustesse et la clarté. [#dcf15f7](https://github.com/incubateur-ademe/benefriches/commit/dcf15f7)

### Autres changements
- Ajout d'un outil `fix-ci` pour diagnostiquer et corriger les échecs de CI. [#c676548](https://github.com/incubateur-ademe/benefriches/commit/c676548)
- Mise à jour des dépendances. [#ea8412e](https://github.com/incubateur-ademe/benefriches/commit/ea8412e), [#0b77993](https://github.com/incubateur-ademe/benefriches/commit/0b77993)
- Ajout de documentation et de tests unitaires.
- Amélioration de la documentation et des commentaires.
- Correction de divers bugs et améliorations de la performance.
