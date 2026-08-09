## Changelog : bhasile (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois-ci, l'application a franchi une étape importante dans la richesse de son tableau de bord et de ses outils de pilotage. Les utilisateurs bénéficient de nouveaux indicateurs statistiques (RMU, activités), d'une meilleure gestion des documents (CPOM) et d'une interface de recherche de ressources enrichie. La fiabilité globale a été renforcée par l'ajout de tests automatisés et l'optimisation des processus de données.

### Évolutions fonctionnelles
- **Tableau de bord et statistiques** : 
    - Ajout de nouveaux blocs de suivi : transformations en cours [#1479], statistiques RMU [#1491], activités [#1484] et rappels [#1486].
    - Amélioration de la cartographie avec une navigation fluide entre régions et départements [#1526] et ajout d'une carte statique sur la page des statistiques [#1516].
    - Mise en place de notifications directement sur le tableau de bord [#1487].
- **Gestion des structures et ressources** : 
    - Création d'un moteur de recherche et de nouvelles pages dédiées aux ressources [#1538](https://github.com/betagouv/bhasile/issues/1538), [#1535](https://github.com/betagouv/bhasile/issues/1535) et [#1533](https://github.com/betagouv/bhasile/issues/1533).
    - Déploiement d'un nouveau formulaire d'actualisation des données [#1451](https://github.com/betagouv/bhasile/issues/1451), [#1449](https://github.com/betagouv/bhasile/issues/1449) et [#1450](https://github.com/betagouv/bhasile/issues/1450).
    - Amélioration de la gestion des documents et actes liés aux CPOM [#1552](https://github.com/betagouv/bhasile/issues/1552), [#1547](https://github.com/betagouv/bhasile/issues/1547), [#1498](https://github.com/betagouv/bhasile/issues/1498), [#1543](https://github.com/betagouv/bhasile/issues/1543) et [#1495](https://github.com/betagouv/bhasile/issues/1495).
- **Suivi des transformations** : 
    - Ajout de la pagination pour le bloc des transformations [#1565](https://github.com/betagouv/bhasile/issues/1565).
    - Masquage automatique des transformations dont la structure n'est pas encore finalisée [#1567](https://github.com/betagouv/bhasile/issues/1567).
- **Corrections** : 
    - Résolution de divers problèmes liés à l'affichage des statistiques, à la récupération des données de transformation et à la gestion des filtres de départements [#1553](https://github.com/betagouv/bhasile/issues/1553), [#1557](https://github.com/betagouv/bhasile/issues/1557), [#1564](https://github.com/betagouv/bhasile/issues/1564), [#1550](https://github.com/betagouv/bhasile/issues/1550), [#1500](https://github.com/betagouv/bhasile/issues/1500) et [#1480](https://github.com/betagouv/bhasile/issues/1480).

### Évolutions techniques
- **Qualité et CI/CD** : 
    - Intégration des tests dans le pipeline de CI [#1398](https://github.com/betagouv/bhasile/issues/1398) et stabilisation importante des tests de bout en bout (E2E) [#1542](https://github.com/betagouv/bhasile/issues/1542), [#1529](https://github.com/betagouv/bhasile/issues/1529), [#1525](https://github.com/betagouv/bhasile/issues/1525) et [#1512](https://github.com/betagouv/bhasile/issues/1512).
- **Architecture et Backend** : 
    - Optimisation de la gestion des connexions à la base de données pour éviter les erreurs de saturation [#1548](https://github.com/betagouv/bhasile/issues/1548).
    - Modularisation de la récupération des données pour les démarches numériques [#1499](https://github.com/betagouv/bhasile/issues/1499).
    - Automatisation de certaines tâches via des processus planifiés (crons) [#1515](https://github.com/betagouv/bhasile/issues/1515) et [#1573](https://github.com/betagouv/bhasile/issues/1573).
    - Refactorisation et factorisation des contextes applicatifs [#1569](https://github.com/betagouv/bhasile/issues/1569).
- **Sécurité** : 
    - Renforcement de la protection des fichiers téléchargés pour empêcher toute consultation ou suppression non autorisée [#1460](https://github.com/betagouv/bhasile/issues/1460).

### Autres changements
- Mise à jour de la documentation concernant les typologies de structures [#1531](https://github.com/betagouv/bhasile/issues/1531).
- Nettoyage du code et ajustements mineurs de l'interface utilisateur (espacements, bannières) [#1534](https://github.com/betagouv/bhasile/issues/1534), [#1560](https://github.com/betagouv/bhasile/issues/1560) et [#1493](https://github.com/betagouv/bhasile/issues/1493).
