## Changelog : hyyypertool (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'expérience de modération via une meilleure pagination et la stabilisation de l'outil. Un travail majeur a été réalisé sur l'infrastructure de test pour accélérer les cycles de développement et garantir une plus grande fiabilité des fonctionnalités.

### Évolutions fonctionnelles
- Amélioration de la navigation dans les listes avec l'affichage de 20 modérations par page ([#1908](https://github.com/proconnect-gouv/hyyypertool/issues/1908)).
- Correction d'un lien vers la liste des dirigeants sur l'annuaire des entreprises ([#1847](https://github.com/proconnect-gouv/hyyypertool/issues/1847)).
- Ajout de l'adresse email Crisp lors des actions de support ([#1846](https://github.com/proconnect-gouv/hyyypertool/issues/1846)).
- Suppression d'une signature en double dans les emails de support ([#1891](https://github.com/proconnect-gouv/hyyypertool/issues/1891)).

### Évolutions techniques
- **Tests et Qualité** : Migration massive des tests de fonctionnalités vers Buncept pour une meilleure robustesse et portabilité, remplaçant l'ancien système Bunwright ([#1827](https://github.com/proconnect-gouv/hyyypertool/issues/1827)).
- **CI/CD et Performance** : Optimisation des pipelines de tests par le partitionnement (sharding) sur plusieurs runners et mise en cache des dépendances WebKit pour réduire les temps d'exécution ([#1881](https://github.com/proconnect-gouv/hyyypertool/issues/1881), [#1894](https://github.com/proconnect-gouv/hyyypertool/issues/1894)).
- **Infrastructure et Environnement** : 
    - Mise à jour de Node.js vers la version 24.22.1 ([#1919](https://github.com/proconnect-gouv/hyyypertool/issues/1919)).
    - Montée de version de PostgreSQL vers 18.6 ([#1922](https://github.com/proconnect-gouv/hyyypertool/issues/1922)).
    - Mise à jour des dépendances internes du projet `@proconnect-gouv/*` ([#1906](https://github.com/proconnect-gouv/hyyypertool/issues/1906)).
- **Refactoring** : Suppression de l'ancien client API `identite admin` devenu obsolète ([#1895](https://github.com/proconnect-gouv/hyyypertool/issues/1895)).

### Autres changements
- Nettoyage de la gestion des releases et suppression des commentaires de merge non révisés ([#1861](https://github.com/proconnect-gouv/hyyypertool/issues/1861), [#1892](https://github.com/proconnect-gouv/hyyypertool/issues/1892)).
