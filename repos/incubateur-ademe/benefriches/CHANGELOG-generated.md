## Changelog : benefriches (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de l'application, notamment au niveau des tests et de l'infrastructure, ainsi que sur l'ajout de nouvelles fonctionnalités d'analyse et de documentation des impacts des reconversions de friches. L'interface utilisateur a également été améliorée pour une meilleure expérience utilisateur, notamment dans l'interprétation des données et la création de projets.

### Évolutions fonctionnelles
- Ajout de la documentation sur les impacts évités, le seuil de rentabilité et le score de développement dans l'interface web [#fae3183](https://github.com/incubateur-ademe/benefriches/commit/fae3183).
- Amélioration de l'affichage des conditions dans l'onglet "score de développement" et correction des formulations dans la documentation des impacts [#9aefc49](https://github.com/incubateur-ademe/benefriches/commit/9aefc49).
- Ajout de la valeur d'augmentation de la propriété locale dans la section qualité de vie de l'onglet "score de développement" [#866976d](https://github.com/incubateur-ademe/benefriches/commit/866976d).
- Refonte de l'onglet de comparaison des impacts pour afficher les coûts d'inaction et les coûts de l'étalement urbain [#0d497fd](https://github.com/incubateur-ademe/benefriches/commit/0d497fd).
- Ajout d'un endpoint API pour calculer les impacts du statu quo d'un site [#0506228](https://github.com/incubateur-ademe/benefriches/commit/0506228).
- Amélioration du texte d'information du formulaire pour le lien de l'évaluation immobilière DVF [#5c00498](https://github.com/incubateur-ademe/benefriches/commit/5c00498).
- Correction du comportement de l'étape d'introduction des bâtiments lors de la création d'un site, en l'ignorant si le site a des bâtiments mais le projet n'en a pas [#9825fbf](https://github.com/incubateur-ademe/benefriches/commit/9825fbf).
- Utilisation du type de zone urbaine pour générer le nom par défaut du site dans le formulaire de création [#52544b3](https://github.com/incubateur-ademe/benefriches/commit/52544b3).
- Réduction de la hauteur du graphique du seuil de rentabilité [#1fe81aa](https://github.com/incubateur-ademe/benefriches/commit/1fe81aa).
- Mise à jour de l'affichage du badge pour l'année de rentabilité et modification du texte si l'indice de l'année de rentabilité est 0 [#b09f78a](https://github.com/incubateur-ademe/benefriches/commit/b09f78a).

### Évolutions techniques
- Correction de l'instabilité des tests E2E en utilisant des mocks pour les APIs externes PVGIS et CRM [#0589282](https://github.com/incubateur-ademe/benefriches/commit/0589282).
- Ajout d'un healthcheck API pour s'assurer que NestJS est démarré avant l'exécution des tests E2E [#83de2d4](https://github.com/incubateur-ademe/benefriches/commit/83de2d4).
- Mise en place d'un timeout de 10 secondes pour les requêtes HTTP vers PVGIS afin d'éviter les blocages [#3303f6a](https://github.com/incubateur-ademe/benefriches/commit/3303f6a).
- Mise en cache des builds d'images Docker pour les tests E2E afin d'accélérer les CI [#7c0b34b](https://github.com/incubateur-ademe/benefriches/commit/7c0b34b).
- Mise à jour de Playwright à la version 1.60.0 pour corriger un problème de blocage de l'installation du navigateur [#4374188](https://github.com/incubateur-ademe/benefriches/commit/4374188).
- Ajout d'un scan de secrets avec Talisman au hook pre-commit [#4963c04](https://github.com/incubateur-ademe/benefriches/commit/4963c04).
- Mise à jour de pnpm de la version 10.31.0 à la version 11.5.2 [#058e9d9](https://github.com/incubateur-ademe/benefriches/commit/058e9d9).
- Restructuration du module `ademe-csv-import` de l'API pour une meilleure organisation [#819a4d1](https://github.com/incubateur-ademe/benefriches/commit/819a4d1).
- Structuration, documentation et orchestration du pipeline d'analyse des projets de reconversion ADEME [#e821bba](https://github.com/incubateur-ademe/benefriches/commit/e821bba).
- Ajout d'un script pour exporter les impacts au format CSV pour tous les projets de reconversion personnalisés [#3a7a9c8](https://github.com/incubateur-ademe/benefriches/commit/3a7a9c8).
- Création d'un script pour créer des projets de reconversion à partir d'un fichier CSV [#c63da3c](https://github.com/incubateur-ademe/benefriches/commit/c63da3c).
- Ajout d'un throttleur pour la sécurité de l'API [#61785ed](https://github.com/incubateur-ademe/benefriches/commit/61785ed).
- Amélioration de la journalisation des erreurs dans l'API [#f34e292](https://github.com/incubateur-ademe/benefriches/commit/f34e292).

### Autres changements
- Correction d'un bug dans le calcul de la somme des revenus fiscaux sur le site impact [#15b0311](https://github.com/incubateur-ademe/benefriches/commit/15b0311).
- Correction d'un bug dans l'endpoint stats, avec des arguments incorrects utilisés dans l'appel au usecase et au service SQL [#4b623c2](https://github.com/incubateur-ademe/benefriches/commit/4b623c2).
- Refactorisation de la structure des dossiers du module stats [#b46acf0](https://github.com/incubateur-ademe/benefriches/commit/b46acf0).
- Spécification de la version attendue de PostgreSQL dans le fichier Readme [#3634aaf](https://github.com/incubateur-ademe/benefriches/commit/3634aaf).
- Correction d'un problème de blocage de CI dû à l'absence de TTY dans pnpm 11 [#dcd49d8](https://github.com/incubateur-ademe/benefriches/commit/dcd49d8).
- Correction d'un bug lié à la gestion des erreurs dans le gestionnaire d'événements CRM [#f2e17a0](https://github.com/incubateur-ademe/benefriches/commit/f2e17a0).
- Correction de l'affichage des noms de zones urbaines dans les tests E2E [#a06c0bc](https://github.com/incubateur-ademe/benefriches/commit/a06c0bc).
