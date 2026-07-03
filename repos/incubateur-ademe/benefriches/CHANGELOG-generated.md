## Changelog : benefriches (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la fiabilité de l'application, notamment au niveau des tests et de l'infrastructure. Des corrections et des refactorisations ont été apportées pour optimiser les performances et la maintenance du code. Des fonctionnalités ont également été ajoutées pour affiner le calcul des impacts et améliorer l'expérience utilisateur, notamment concernant les projets urbains et les friches.

### Évolutions fonctionnelles
- Ajout de la prise en compte de la réhabilitation dans le processus de création de projet urbain [#912fb85](https://github.com/incubateur-ademe/benefriches/commit/912fb85).
- Amélioration de la gestion des étapes de décontamination et de réhabilitation dans les projets urbains [#59ee001](https://github.com/incubateur-ademe/benefriches/commit/59ee001).
- Ajout d'une section "Avancement" et de la gestion des corps de métier dans le résumé des projets urbains [#a2b7673](https://github.com/incubateur-ademe/benefriches/commit/a2b7673), [#f9632d0](https://github.com/incubateur-ademe/benefriches/commit/f9632d0), [#42462f1](https://github.com/incubateur-ademe/benefriches/commit/42462f1).
- Affichage des coûts d'inaction et de l'étalement urbain dans l'onglet de comparaison des impacts [#0506228](https://github.com/incubateur-ademe/benefriches/commit/0506228).
- Documentation des impacts dans les onglets "analyse des coûts évités", "niveau de seuil" et "développement du score" [#fae3183](https://github.com/incubateur-ademe/benefriches/commit/fae3183).
- Amélioration de l'affichage des informations sur les bâtiments dans le résumé des projets urbains [#5e70ebe](https://github.com/incubateur-ademe/benefriches/commit/5e70ebe).
- Ajout d'un lien vers la base de données DVF pour l'évaluation immobilière [#5c00498](https://github.com/incubateur-ademe/benefriches/commit/5c00498).
- Amélioration de l'affichage des messages d'erreur liés à l'authentification [#8d7bd5c](https://github.com/incubateur-ademe/benefriches/commit/8d7bd5c).

### Évolutions techniques
- Migration des tests unitaires et d'intégration de Vitest vers node:test pour une meilleure performance et une maintenance simplifiée [#d8716d7](https://github.com/incubateur-ademe/benefriches/commit/d8716d7), [#7c0eccc](https://github.com/incubateur-ademe/benefriches/commit/7c0eccc), [#b60acd5](https://github.com/incubateur-ademe/benefriches/commit/b60acd5).
- Migration de l'API vers ESM (EcmaScript Modules) avec SWC pour une meilleure performance et compatibilité avec les navigateurs modernes [#3bbffae](https://github.com/incubateur-ademe/benefriches/commit/3bbffae).
- Refactorisation du code pour améliorer la structure et la maintenabilité, notamment au niveau du calcul des impacts [#c91528a](https://github.com/incubateur-ademe/benefriches/commit/c91528a), [#40066b7](https://github.com/incubateur-ademe/benefriches/commit/40066b7), [#5e970c9](https://github.com/incubateur-ademe/benefriches/commit/5e970c9), [#4374377](https://github.com/incubateur-ademe/benefriches/commit/4374377).
- Amélioration de la gestion des variables d'environnement en production [#11ea341](https://github.com/incubateur-ademe/benefriches/commit/11ea341).
- Ajout d'un système de limitation de débit (throttler) pour renforcer la sécurité de l'API [#61785ed](https://github.com/incubateur-ademe/benefriches/commit/61785ed).
- Mise à jour des dépendances et correction de problèmes liés à la compatibilité des versions [#cd28792](https://github.com/incubateur-ademe/benefriches/commit/cd28792), [#ea8412e](https://github.com/incubateur-ademe/benefriches/commit/ea8412e), [#0b77993](https://github.com/incubateur-ademe/benefriches/commit/0b77993).
- Amélioration du caching des images Docker pour accélérer les tests e2e [#7c0b34b](https://github.com/incubateur-ademe/benefriches/commit/7c0b34b).

### Autres changements
- Ajout de tests e2e pour le scénario de friche [#622fea9](https://github.com/incubateur-ademe/benefriches/commit/622fea9).
- Amélioration de la documentation et ajout de références aux jeux de données utilisés [#15b0311](https://github.com/incubateur-ademe/benefriches/commit/15b0311), [#23f401f](https://github.com/incubateur-ademe/benefriches/commit/23f401f).
- Ajout d'un outil de scan de secrets (talisman) aux hooks pre-commit [#4963c04](https://github.com/incubateur-ademe/benefriches/commit/4963c04).
- Refactorisation des tests d'interface utilisateur pour améliorer leur organisation et leur lisibilité [#be50cbd](https://github.com/incubateur-ademe/benefriches/commit/be50cbd), [#4521751](https://github.com/incubateur-ademe/benefriches/commit/4521751), [#12310b5](https://github.com/incubateur-ademe/benefriches/commit/12310b5).
- Amélioration de la gestion des erreurs et ajout de logs plus informatifs [#657919b](https://github.com/incubateur-ademe/benefriches/commit/657919b), [#dcd49d8](https://github.com/incubateur-ademe/benefriches/commit/dcd49d8).
- Ajout de tests pour la gestion des données de ruralité des communes [#3a7a9c8](https://github.com/incubateur-ademe/benefriches/commit/3a7a9c8).
