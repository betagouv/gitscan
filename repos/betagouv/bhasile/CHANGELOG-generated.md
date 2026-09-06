## Changelog : bhasile (30 derniers jours, au 03/09/2026)

### Résumé
Ce mois-ci, l'application a considérablement renforcé ses capacités d'extraction de données avec l'ajout de nouveaux exports (Excel, PDF) et a amélioré la visibilité des anomalies grâce à un nouveau bloc dédié dans le tableau de bord. Une refonte technique majeure a été réalisée pour accélérer le chargement des pages et améliorer la fiabilité globale du système.

### Évolutions fonctionnelles
- **Exports de données** : Ajout de l'export Excel pour les statistiques [#1640], d'une interface d'export PDF [#1632], et de nouveaux téléchargements de feuilles de calcul pour les types de lieux [#1625, #1614].
- **Interface et Expérience Utilisateur** : 
    - Amélioration de la navigation avec la mémorisation des paramètres de recherche dans la liste des opérateurs [#1613].
    - Corrections visuelles sur les accordéons [#1636], le style des fiches fermées [#1591] et l'interactivité des contrôles de la carte [#1596].
    - Correction de l'affichage des en-têtes lors des transformations [#1623].
- **Nouveautés et Corrections métier** :
    - Ajout d'un bloc de tableau de bord pour le suivi des anomalies [#1578].
    - Correction de l'authentification pour les transformations [#1571].
    - Résolution de divers bugs d'affichage et de calcul (graphiques d'évaluation [#1598], évaluations à zéro [#1594], récupération des codes DNA [#1628] et règles d'état des structures [#1600]).
    - Amélioration du filtrage des opérateurs sans structure associée [#1593].

### Évolutions techniques
- **Architecture** : Migration massive vers le chargement de données via les *React Server Components* (RSC) pour optimiser les performances de l'application (listes de structures, fiches opérateurs, transformations, CPOM, etc. [#1633, #1629, #1626, #1608, #1576, #1611]).
- **Qualité et Tests** : 
    - Intégration de tests de bout en bout (E2E) dans la chaîne de déploiement (CI) [#1587, #1570].
    - Correction et stabilisation des tests unitaires [#1621, #1604].
- **Infrastructure et Performance** : 
    - Mise à jour de l'environnement vers Node 26 [#1605].
    - Optimisation de la base de données via l'ajout d'index [#1577].
    - Ajustement des tâches planifiées (crons) [#1573].
- **Maintenance et Refactoring** : 
    - Refonte complète du système de génération de données de test (*seeders*) pour garantir des données cohérentes [#1585, #1620, #1619, #1606, #1617, #1616].
    - Refactorisation de la gestion des paramètres de recherche [#1615] et renommage de classes internes [#1627].
    - Mise en place du suivi (tracking) des exports et des statistiques simples [#1630, #1603].

### Autres changements
- Mise à jour de la documentation (README) [#1638].
- Nettoyage de la configuration (linting) [#1584] et corrections de coquilles [#1572].
