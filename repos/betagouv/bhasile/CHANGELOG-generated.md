## Changelog : bhasile (30 derniers jours, au 07/09/2026)

### Résumé
Ce mois-ci, l'application a considérablement enrichi ses capacités d'extraction de données avec l'ajout de nouveaux exports (Excel, PDF) et a amélioré le pilotage via un nouveau bloc dédié aux anomalies dans le tableau de bord. Une refonte technique majeure a également été réalisée pour optimiser la vitesse de chargement des pages grâce à une nouvelle méthode de récupération des données.

### Évolutions fonctionnelles
- **Exportation de données** : Ajout de l'export Excel pour les statistiques [#1640], de nouveaux téléchargements de feuilles de calcul [#1625], d'un module d'export PDF [#1632] et de l'export des types de lieux [#1614].
- **Tableau de bord et interface** : Intégration d'un bloc dédié aux anomalies [#1578], affichage des anomalies directement dans les formulaires [#1599], amélioration de l'interactivité de la carte [#1596] et corrections visuelles sur les accordéons et les fiches [#1636, #1591].
- **Corrections et métier** : Résolution de bugs sur les graphiques d'évaluation [#1598], les cartes de dernière visite [#1597] et les évaluations à zéro [#1594] ; ajustement de la logique de tolérance pour la durée des actes [#1622] et correction de la récupération des codes DNA [#1628].
- **Expérience utilisateur** : Mémorisation des paramètres de recherche dans la liste des opérateurs [#1613] et filtrage des opérateurs sans structure associée [#1593].

### Évolutions techniques
- **Optimisation des performances** : Migration massive de la récupération de données vers les *React Server Components* (RSC) pour accélérer le chargement des listes et des fiches (structures, opérateurs, CPOM, transformations) [#1633, #1629, #1626, #1608, #1576, #1611].
- **Infrastructure et qualité** : Passage à Node 26 [#1605], intégration de tests de bout en bout (E2E) dans la chaîne de CI [#1587, #1570] et optimisation de la base de données par l'ajout d'index [#1577].
- **Maintenance et suivi** : Refonte complète des données de test (*seeders*) [#1585], amélioration du suivi analytique des exports et des statistiques [#1630, #1603] et refactorisation de la gestion des paramètres de recherche [#1615].

### Autres changements
- Mise à jour de la documentation (README) [#1638] et de la configuration du linting [#1584].
