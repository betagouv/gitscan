## Changelog : csplab (30 derniers jours, au 12 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans la gestion des organisations et des équipes de recrutement. Les administrateurs disposent désormais d'outils complets pour gérer les membres de leurs organismes (ajout, modification et révocation de rôles) et consulter des détails précis sur chaque structure. En parallèle, la fiabilité des données a été renforcée par l'intégration de nouveaux référentiels et une gestion plus sécurisée des secrets, tandis que l'architecture technique a été simplifiée pour gagner en efficacité.

### Évolutions fonctionnelles
- **Gestion des équipes et des organismes :**
    - Possibilité d'ajouter, modifier ou révoquer le rôle d'un agent au sein d'une équipe de recrutement [#1416](https://github.com/betagouv/csplab/issues/1416), [#1412](https://github.com/betagouv/csplab/issues/1412), [#1409](https://github.com/betagouv/csplab/issues/1409).
    - Gestion complète des membres d'un organisme : recherche par email, ajout de membres et mise à jour des rôles [#1391](https://github.com/betagouv/csplab/issues/1391), [#1318](https://github.com/betagouv/csplab/issues/1318), [#1264](https://github.com/betagouv/csplab/issues/1264).
    - Nouvelle interface permettant de consulter les détails d'un organisme et la liste de ses membres [#1255](https://github.com/betagouv/csplab/issues/1255), [#1254](https://github.com/betagouv/csplab/issues/1254).
    - Création et édition d'organismes directement depuis une nouvelle liste d'administration [#1228](https://github.com/betagouv/csplab/issues/1228), [#1229](https://github.com/betagouv/csplab/issues/1229).
- **Expérience utilisateur :**
    - Désactivation du parcours candidat [#1404](https://github.com/betagouv/csplab/issues/1404).
    - Amélioration de l'affichage des membres et de la navigation dans les processus de recrutement [#1383](https://github.com/betagouv/csplab/issues/1383).
    - Modernisation de l'interface (gestion des onglets, icônes et styles des tableaux) [#1331](https://github.com/betagouv/csplab/issues/1331), [#1292](https://github.com/betagouv/csplab/issues/1292).

### Évolutions techniques
- **Ingestion et gestion des données :**
    - Enrichissement des référentiels de données avec l'intégration des données ARS, GIPCDG et un nettoyage approfondi des établissements FINESS [#1399](https://github.com/betagouv/csplab/issues/1399), [#1224](https://github.com/betagouv/csplab/issues/1224), [#1190](https://github.com/betagouv/csplab/issues/1190).
    - Optimisation de la consommation mémoire du pipeline d'ingestion des organismes [#1369](https://github.com/betagouv/csplab/issues/1369).
    - Sécurisation de l'accès aux secrets via l'intégration de Scaleway Secret Manager pour les composants Web, Ingestion et OCR [#1302](https://github.com/betagouv/csplab/issues/1302), [#1301](https://github.com/betagouv/csplab/issues/1301), [#1280](https://github.com/betagouv/csplab/issues/1280).
- **Architecture et outils de développement :**
    - Évolution de l'architecture vers un modèle Django plus idiomatique (ADR-009) pour simplifier la maintenance [#1305](https://github.com/betagouv/csplab/issues/1305).
    - Refonte de la structure du frontend et intégration au sein du package web principal [#1346](https://github.com/betagouv/csplab/issues/1346), [#1344](https://github.com/betagouv/csplab/issues/1344).
    - Automatisation de la génération des schémas OpenAPI et des types TypeScript [#1388](https://github.com/betagouv/csplab/issues/1388), [#1398](https://github.com/betagouv/csplab/issues/1398).
    - Migration de la gestion des tâches de développement vers l'outil `mise` [#1276](https://github.com/betagouv/csplab/issues/1276), [#1242](https://github.com/betagouv/csplab/issues/1242).
- **Tests et CI/CD :**
    - Amélioration de la fiabilité des tests grâce à l'intégration de `factory-boy` [#1417](https://github.com/betagouv/csplab/issues/1417), [#1362](https://github.com/betagouv/csplab/issues/1362).
    - Optimisation des workflows de CI, notamment via la mise en cache des navigateurs Playwright [#1202](https://github.com/betagouv/csplab/issues/1202).

### Autres changements
- Documentation de la gestion des variables d'environnement et des secrets Scaleway [#1410](https://github.com/betagouv/csplab/issues/1410).
- Mise à jour de la documentation de l'API concernant les limites de requêtes (rate limiting) [#1345](https://github.com/betagouv/csplab/issues/1345).
