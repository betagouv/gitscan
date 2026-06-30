## Changelog : benefriches (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la fiabilité de la plateforme, notamment au niveau des tests et de l'infrastructure. Des corrections ont été apportées pour améliorer l'expérience utilisateur dans la création de projets, et des fonctionnalités ont été ajoutées pour mieux prendre en compte la réhabilitation et l'état initial des friches. Des efforts ont également été faits pour améliorer la sécurité et l'observabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'une étape "Implication de la réhabilitation" au wizard de création de projet de friche [#912fb85](https://github.com/incubateur-ademe/benefriches/commit/912fb85).
- Amélioration de la gestion des étapes de décontamination des projets urbains, en fonction de la nature du site [#59ee001](https://github.com/incubateur-ademe/benefriches/commit/59ee001).
- Ajout de la prise en compte de la ruralité des communes pour le calcul des dépenses de sécurité par défaut des friches [#48a6392](https://github.com/incubateur-ademe/benefriches/commit/48a6392).
- Ajout de la section "Avancement" et des informations sur les bâtiments (contractant, existants/nouveaux) au résumé du projet urbain [#15d56f8](https://github.com/incubateur-ademe/benefriches/commit/15d56f8), [#42462f1](https://github.com/incubateur-ademe/benefriches/commit/42462f1), [#f9632d0](https://github.com/incubateur-ademe/benefriches/commit/f9632d0).
- Amélioration de l'affichage des informations sur la qualité de vie dans l'onglet "Score de développement" [#866976d](https://github.com/incubateur-ademe/benefriches/commit/866976d).
- Ajout de la documentation sur les coûts d'inaction et la comparaison avec l'étalement urbain dans l'onglet "Score de développement" [#fae3183](https://github.com/incubateur-ademe/benefriches/commit/fae3183).
- Suppression de la vue graphique dans l'onglet "Impacts" et regroupement des sélecteurs dans un sous-dossier [#1e50680](https://github.com/incubateur-ademe/benefriches/commit/1e50680).
- Mise à jour du texte d'information pour le lien vers l'évaluation immobilière DVF [#5c00498](https://github.com/incubateur-ademe/benefriches/commit/5c00498).

### Évolutions techniques
- Migration des tests unitaires et d'intégration de Vitest vers node:test pour améliorer les performances et la compatibilité [#d8716d7](https://github.com/incubateur-ademe/benefriches/commit/d8716d7), [#7c0eccc](https://github.com/incubateur-ademe/benefriches/commit/7c0eccc), [#b60acd5](https://github.com/incubateur-ademe/benefriches/commit/b60acd5).
- Migration de l'API vers native ESM avec SWC pour améliorer la performance et la compatibilité avec les navigateurs modernes [#3bbffae](https://github.com/incubateur-ademe/benefriches/commit/3bbffae).
- Amélioration de la configuration du CI/CD pour le caching des images Docker et l'optimisation des tests E2E [#1e12026](https://github.com/incubateur-ademe/benefriches/commit/1e12026).
- Refactor de l'architecture de l'API pour une meilleure organisation et maintenabilité [#a93c040](https://github.com/incubateur-ademe/benefriches/commit/a93c040), [#c63da3c](https://github.com/incubateur-ademe/benefriches/commit/c63da3c).
- Ajout d'un Makefile et renommage des fichiers docker-compose pour une meilleure gestion de l'environnement de développement [#f0a0514](https://github.com/incubateur-ademe/benefriches/commit/f0a0514).
- Amélioration de la gestion des erreurs et ajout de logs structurés dans l'API [#34c6d70](https://github.com/incubateur-ademe/benefriches/commit/34c6d70).
- Ajout d'un throttle pour la sécurité de l'API [#61785ed](https://github.com/incubateur-ademe/benefriches/commit/61785ed).
- Mise à jour des dépendances du projet (API, web, shared) [#ea8412e](https://github.com/incubateur-ademe/benefriches/commit/ea8412e), [#0b77993](https://github.com/incubateur-ademe/benefriches/commit/0b77993).

### Autres changements
- Ajout de scans de secrets avec talisman au pre-commit hook [#4963c04](https://github.com/incubateur-ademe/benefriches/commit/4963c04).
- Mise à jour de la documentation (README, CLAUDE.md) pour refléter les changements et ajouter des références aux jeux de données utilisés [#15b0311](https://github.com/incubateur-ademe/benefriches/commit/15b0311), [#23f401f](https://github.com/incubateur-ademe/benefriches/commit/23f401f).
- Correction de problèmes de flakiness dans les tests E2E en utilisant des mocks et des timeouts [#3303f6a](https://github.com/incubateur-ademe/benefriches/commit/3303f6a), [#79b1fcb](https://github.com/incubateur-ademe/benefriches/commit/79b1fcb), [#f2e17a0](https://github.com/incubateur-ademe/benefriches/commit/f2e17a0).
- Amélioration de la robustesse des scripts de génération d'environnement [#11ea341](https://github.com/incubateur-ademe/benefriches/commit/11ea341).
