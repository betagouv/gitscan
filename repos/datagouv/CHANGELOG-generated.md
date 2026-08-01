# Synthèse d'activité : datagouv (du 01/05 au 31/07)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des mises à jour importantes de plusieurs de ses projets clés.  On observe une forte concentration sur l'amélioration de la robustesse, de la sécurité et de la performance des infrastructures existantes, notamment avec la migration vers de nouvelles versions de librairies et de frameworks (Rails 8.1, Airflow 3).  Plusieurs projets ont également bénéficié d'améliorations fonctionnelles, comme l'ajout de nouvelles intégrations (CNOUS pour relais, IdRNB pour fr-format) et l'amélioration des interfaces utilisateurs (cdata, api-geo).  L'accent est mis sur la préparation de nouvelles fonctionnalités et l'amélioration de l'expérience développeur, avec la création de nouveaux outils (datagouv-cli) et l'amélioration de la documentation.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction de vulnérabilités dans `passemarche` (Rails 8.1.3.1, CVE-2026-66066).
*   Correction de vulnérabilités dans `hubee` (Loofah, Rails HTML Sanitizer, Active Storage).
*   Renforcement de la sécurité dans `apistration` avec la validation des adresses IP autorisées pour les tokens d'éditeur.
*   Correction d'une vulnérabilité ActiveStorage dans `apistration`.

## Autres changements notables
Plusieurs projets ont connu des évolutions techniques majeures :

*   Migration vers Rails 8.1 et intégration de GoodJob dans `relais`, refonte de l'architecture.
*   Migration vers PNPM dans `ouverture.data.gouv.fr` pour améliorer la performance et la sécurité.
*   Mise à jour d'Airflow vers la version 3 dans `data-engineering-stack`.
*   Remplacement de `httpx` par `niquests` dans plusieurs projets (`datagouv_client`, `hubee`, `api-tabular`) pour une meilleure gestion des requêtes HTTP.
*   Refonte de l'API géographique (v2) dans `api-decoupage-administratif`.
*   Migration du code CLI de `datagouv_client` vers un nouveau dépôt `datagouv-cli` pour une meilleure distribution et support multi-plateforme.

## Dépôts les plus actifs
*   [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et intégration de nouvelles fonctionnalités pour l'intégration avec CNOUS et la gestion des demandes proactives.
*   [hubee](/repos/datagouv/hubee) : Améliorations significatives de la sécurité, modernisation de l'infrastructure et simplification de la configuration.
*   [cdata](/repos/datagouv/cdata) : Ajout de nouvelles fonctionnalités d'exploration et d'amélioration de la visualisation des données.
*   [apistration](/repos/datagouv/apistration) : Amélioration de la gestion des éditeurs d'API et ajout de la prise en charge de l'INE pour l'API CNOUS v5.
*   [datagouv-cli](/repos/datagouv/datagouv-cli) : Création d'un nouveau dépôt pour l'interface en ligne de commande, permettant une distribution plus autonome et un support multi-plateforme.
