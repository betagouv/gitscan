# Synthèse d'activité : datagouv (du 29 avril au 16 mai 2026)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des mises à jour importantes de plusieurs de ses projets clés. On observe une forte concentration sur l'amélioration de l'infrastructure et de la qualité des données, avec des refontes techniques majeures pour des projets comme `relais` et `ouverture.data.gouv.fr`.  Des améliorations significatives ont également été apportées aux APIs, notamment `apistration` et `api-tabular`, pour une meilleure performance et une plus grande robustesse. Plusieurs projets ont bénéficié de mises à jour de données, comme `cadastre` et `contours-administratifs`, assurant ainsi la pertinence et l'actualité des informations fournies aux utilisateurs. Enfin, des efforts ont été déployés pour améliorer l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités sur `cdata` et `hubee`.

## Sécurité
Aucun changement lié à la sécurité n'a été spécifiquement mentionné dans les changelogs fournis.

## Autres changements notables
Plusieurs projets ont subi des refontes techniques importantes :
- **`relais`**: Migration vers Rails 8.1 aligné sur `apistration`, intégrant des outils de test et de linting.
- **`ouverture.data.gouv.fr`**: Migration vers PNPM pour une meilleure gestion des dépendances et des performances.
- **`api-tabular`**: Intégration continue et déploiement (CI/CD) avec la construction et la publication de l'image Docker directement depuis la chaîne CI d'Applicative.
- **`apistration`**: Refactorisation de l'authentification et de l'autorisation.
- **`csv-detective`**: Mise à jour de la version minimale de Python supportée.

## Dépôts les plus actifs
- **`roles.data`**: Améliorations de l'administration des groupes et des utilisateurs, refonte des emails.
- **`relais`**: Refonte de l'infrastructure et migration vers Rails 8.1.
- **`passemarche`**: Ajout de fonctionnalités pour la gestion des candidatures aux marchés publics et amélioration de l'interface d'administration.
- **`datagouvfr_data_pipelines`**: Amélioration de la robustesse et de la fiabilité des pipelines de données.
- **`cdata`**: Ajout de filtres personnalisés, nouvelle mise en page pour les pages d'organisation et nouvelle interface pour l'exploration tabulaire des données.
- **`cadastre`**: Mise à jour des données cadastrales et correction de problèmes de linting.
- **`api-meteo`**: Correction de bugs liés à la gestion des années dans les requêtes.
- **`fr-format`**: Ajout du format de validation IdRNB et documentation en français.
- **`hydra`**: Optimisation de l'extraction de données et ajout du support des WMS.
