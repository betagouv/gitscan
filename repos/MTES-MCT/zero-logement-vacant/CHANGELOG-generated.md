## Changelog : zero-logement-vacant (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'importation des données LOVAC 2026, l'intégration de nouveaux types de graphiques DSFR (Diagrammes en barres, tableaux, diagrammes circulaires) et l'optimisation des performances, notamment au niveau du cache et du chargement des données. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- **Import LOVAC 2026 :** Amélioration significative du processus d'importation des données LOVAC 2026, incluant la gestion des propriétaires, des logements et des événements associés. Ajout de nouvelles étapes de transformation et de validation des données.
- **Graphiques DSFR :** Intégration de nouveaux types de graphiques basés sur la bibliothèque DSFR (Diagrammes en barres, tableaux, diagrammes circulaires) pour une meilleure visualisation des données dans l'interface d'analyse.
- **Campagnes :**
    - Possibilité de lier les logements aux campagnes directement depuis la carte.
    - Ajout d'une colonne "Statut de suivi" dans le tableau des destinataires de campagne.
    - Correction d'un bug empêchant l'application du filtre de campagne lors de la navigation vers la liste des logements.
- **Interface utilisateur :**
    - Ajout d'un état de chargement au bouton de connexion.
    - Amélioration de l'affichage des noms de propriétaires (utilisation du nom d'utilisateur si disponible).
    - Redirection vers la vue tableau lors du clic sur le bouton de regroupement sur la carte.

### Évolutions techniques
- **Cache :** Implémentation d'un cache pour les réponses de l'API Metabase afin d'améliorer les performances de la page d'analyse.
- **Architecture :** Refactorisation du code pour une meilleure organisation et maintenabilité.
- **Tests :** Ajout et amélioration des tests unitaires et d'intégration.
- **Déploiement :** Amélioration de la configuration et du processus de déploiement.
- **Base de données :** Optimisation des requêtes et des index pour améliorer les performances.
- **Dépendances :** Mise à jour de certaines dépendances.
- **Performance:** Optimisation du chargement des données et de l'exécution des requêtes, notamment lors de l'importation des données LOVAC.
- **Pipeline ETL :** Refonte du pipeline ETL pour l'importation des données LOVAC, avec l'utilisation de DuckDB et de fichiers Parquet.
- **React Router V7:** Mise à jour vers la version 7 de React Router.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements de configuration.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Ajout de règles de linting et de formatage pour assurer la cohérence du code.
- Ajout de documentation sur l'implémentation des nouveaux graphiques et du pipeline d'importation LOVAC.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration des messages d'erreur et des logs pour faciliter le débogage.
- Ajout de variables d'environnement pour configurer l'application.
- Correction de problèmes de typographie (utilisation des apostrophes françaises).
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout d'un système de suivi des performances pour identifier les goulots d'étranglement.
