## Changelog : fondation (30 derniers jours, au 17 mars 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant l'ingestion et la gestion des données LoLfi, ainsi que par de nombreuses corrections et améliorations de l'interface utilisateur et des fonctionnalités existantes. L'affectation des ressources a également été optimisée, et des améliorations ont été apportées à la gestion des rapports et des observations.

### Évolutions fonctionnelles
- Ajout de la gestion des données LoLfi : ingestion des archives, page d'administration dédiée et cryptographie associée. ([#248](https://github.com/betagouv/fondation/issues/248), [#229](https://github.com/betagouv/fondation/issues/229), [#237](https://github.com/betagouv/fondation/issues/237))
- Amélioration de l'affectation des ressources : prise en compte de plusieurs priorités, gestion des arrondis, distribution arithmétique et affectation unique par grade et par membre.
- Ajout d'un indicateur de commentaire pour les descriptions d'observations et fichiers. ([#257](https://github.com/betagouv/fondation/issues/257), [#263](https://github.com/betagouv/fondation/issues/263))
- Possibilité de trier les résultats dans la liste des fichiers et des affectations. ([#258](https://github.com/betagouv/fondation/issues/258), [#260](https://github.com/betagouv/fondation/issues/260))
- Ajout d'un manuel utilisateur. ([#261](https://github.com/betagouv/fondation/issues/261))
- Ajout de la possibilité de spécifier un grade ciblé dans l'export Excel. ([#224](https://github.com/betagouv/fondation/issues/224))
- Amélioration de l'affichage des priorités multiples dans la liste des rapports des membres. ([#274](https://github.com/betagouv/fondation/issues/274))
- Ajout de deux nouveaux états de fichiers. ([#255](https://github.com/betagouv/fondation/issues/255))
- Ajout de la possibilité de joindre plusieurs fichiers en une seule session. ([#254](https://github.com/betagouv/fondation/issues/254))
- Correction de l'affectation de version pour la publication des rapports. ([#272](https://github.com/betagouv/fondation/issues/272))
- Correction de l'affichage des captures d'écran des observations. ([#271](https://github.com/betagouv/fondation/issues/271))
- Correction de l'utilisation de l'identifiant externe pour la recherche. ([#220](https://github.com/betagouv/fondation/issues/220))
- Correction de la sensibilité à la casse de la connexion. ([#253](https://github.com/betagouv/fondation/issues/253))
- Correction d'un problème empêchant la sauvegarde de la description des observations. ([#219](https://github.com/betagouv/fondation/issues/219))
- Correction d'un problème empêchant la récupération de la charge de travail sur une version non publiée. ([#222](https://github.com/betagouv/fondation/issues/222))

### Évolutions techniques
- Suppression des colonnes et tables dépréciées. ([#262](https://github.com/betagouv/fondation/issues/262))
- Ajout de métriques HTTP à Sentry pour une meilleure surveillance. ([#249](https://github.com/betagouv/fondation/issues/249))
- Mise en place de tests E2E pour l'affectation. ([#270](https://github.com/betagouv/fondation/issues/270))
- Utilisation de requêtes SQL brutes pour optimiser la récupération des détails de session des membres. ([#251](https://github.com/betagouv/fondation/issues/251))
- Refactorisation du code pour déplacer l'affectation automatique dans plusieurs fichiers. ([#236](https://github.com/betagouv/fondation/issues/236))
- Ajout de source maps pour faciliter le débogage dans Sentry. ([#267](https://github.com/betagouv/fondation/issues/267))
- Mise en place d'une release Sentry. ([#269](https://github.com/betagouv/fondation/issues/269))
- Mise en cache des fichiers et traçage des requêtes HTTP. ([#273](https://github.com/betagouv/fondation/issues/273))

### Autres changements
- Ajout de tags utilisateurs sur la notification de changelog. ([#227](https://github.com/betagouv/fondation/issues/227))
- Correction d'un problème de duplication d'importation. ([#233](https://github.com/betagouv/fondation/issues/233))
- Correction d'un problème d'affectation automatique excluant une juridiction. ([#235](https://github.com/betagouv/fondation/issues/235))
- Correction d'un problème d'arrondi dans l'affectation. ([#226](https://github.com/betagouv/fondation/issues/226))
- Correction d'un problème d'affectation unique par membre et par groupe de grade. ([#223](https://github.com/betagouv/fondation/issues/223))
- Suppression de Dependabot.
- Mise à jour des dépendances API et client.
- Actualisation des instructions Copilot.
