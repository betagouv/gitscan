## Changelog : bhasile (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois a été marqué par une amélioration significative des capacités de pilotage et de reporting, notamment grâce à l'ajout d'un tableau de bord dédié aux anomalies et de nouvelles options d'exportation de données (PDF et tableurs). Parallèlement, une refonte technique majeure a été opérée pour optimiser la rapidité de l'application via l'adoption de nouvelles méthodes de récupération de données.

### Évolutions fonctionnelles
- **Reporting et exports** : 
    - Ajout d'une interface de modale pour l'exportation de documents en PDF [#1632](https://github.com/betagouv/bhasile/issues/1632).
    - Extension des possibilités de téléchargement de fichiers (tableurs et types de places) [#1625](https://github.com/betagouv/bhasile/issues/1625), [#1614](https://github.com/betagouv/bhasile/issues/1614).
- **Gestion des anomalies** : 
    - Création d'un nouveau bloc de statistiques dédié aux anomalies dans le tableau de bord [#1578](https://github.com/betagouv/bhasile/issues/1578).
    - Intégration de l'affichage des anomalies directement au sein des formulaires [#1599](https://github.com/betagouv/bhasile/issues/1599).
- **Navigation et recherche** : 
    - Mise en place d'un système de recherche et de pages dédiées aux ressources [#1538](https://github.com/betagouv/bhasile/issues/1538).
    - Amélioration de l'expérience utilisateur via la pagination des transformations [#1565](https://github.com/betagouv/bhasile/issues/1565) et la mémorisation des filtres de recherche sur la liste des opérateurs [#1613](https://github.com/betagouv/bhasile/issues/1613).
- **Corrections métier** : 
    - Ajustement des règles de gestion pour permettre la création de structures même sans certains documents financiers ou actes si ceux-ci sont présents au niveau du CPOM [#1552](https://github.com/betagouv/bhasile/issues/1552), [#1547](https://github.com/betagouv/bhasile/issues/1547).
    - Corrections diverses sur les graphiques d'évaluation [#1598](https://github.com/betagouv/bhasile/issues/1598) et l'affichage de la carte [#1596](https://github.com/betagouv/bhasile/issues/1596).

### Évolutions techniques
- **Optimisation des performances (RSC)** : Migration massive de la récupération de données vers les *React Server Components* pour les listes de structures, d'opérateurs, les fiches détaillées et les transformations, permettant un chargement plus rapide des pages [#1633](https://github.com/betagouv/bhasile/issues/1633), [#1629](https://github.com/betagouv/bhasile/issues/1629), [#1626](https://github.com/betagouv/bhasile/issues/1626), [#1608](https://github.com/betagouv/bhasile/issues/1608), [#1576](https://github.com/betagouv/bhasile/issues/1576), [#1611](https://github.com/betagouv/bhasile/issues/1611).
- **Qualité logicielle et CI/CD** : 
    - Renforcement de la fiabilité avec l'ajout de tests de bout en bout (E2E) dans la chaîne de déploiement automatique (CI) [#1587](https://github.com/betagouv/bhasile/issues/1587), [#1398](https://github.com/betagouv/bhasile/issues/1398).
    - Correction et stabilisation des tests unitaires [#1621](https://github.com/betagouv/bhasile/issues/1621), [#1604](https://github.com/betagouv/bhasile/issues/1604).
- **Infrastructure et Base de données** : 
    - Mise à jour de l'environnement d'exécution vers Node 26 [#1605](https://github.com/betagouv/bhasile/issues/1605).
    - Optimisation de la base de données via l'ajout d'index [#1577](https://github.com/betagouv/bhasile/issues/1577) et amélioration des scripts de peuplement de données (seeding) [#1620](https://github.com/betagouv/bhasile/issues/1620), [#1585](https://github.com/betagouv/bhasile/issues/1585).
- **Observabilité** : Remplacement de l'outil de suivi Matomo par un système de tracking interne pour les statistiques et les exports [#1618](https://github.com/betagouv/bhasile/issues/1618), [#1603](https://github.com/betagouv/bhasile/issues/1603), [#1630](https://github.com/betagouv/bhasile/issues/1630).

### Autres changements
- **Nettoyage et maintenance** : 
    - Refactorisation du code (renommage d'erreurs, suppression de variables obsolètes) [#1627](https://github.com/betagouv/bhasile/issues/1627), [#1602](https://github.com/betagouv/bhasile/issues/1602).
    - Corrections de diverses coquilles dans l'interface [#1572](https://github.com/betagouv/bhasile/issues/1572).
