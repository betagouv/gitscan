# Synthèse d'activité : datagouv (du 2026-04-23 au 2026-05-27)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs de ses projets clés.  Un effort important a été consacré à la modernisation des infrastructures (Rails 8.1, PNPM, Airflow 3) et à l'amélioration de la robustesse des pipelines de données.  De nouvelles fonctionnalités ont été introduites, notamment une API pour l'intégration avec CNOUS ([relais](/repos/datagouv/relais)), un système de notifications pour Hubee ([hubee](/repos/datagouv/hubee)), et un SDK Node.js pour apistration ([apistration](/repos/datagouv/apistration)).  Plusieurs projets ont également bénéficié de mises à jour de données (cadastre, ODM) et de corrections de bugs pour améliorer la qualité et la fiabilité des services.

## Sécurité
Une vulnérabilité de sécurité a été corrigée dans [datagouv-mcp](/repos/datagouv/datagouv-mcp) en contraignant la version de la librairie `urllib3`.

## Autres changements notables
Plusieurs projets ont subi des mises à jour techniques majeures :
*   Migration vers Rails 8.1 et intégration de GoodJob dans [relais](/repos/datagouv/relais) pour une meilleure performance et scalabilité.
*   Migration vers PNPM dans [schema.data.gouv.fr](/repos/datagouv/schema.data.gouv.fr) et [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) pour une meilleure gestion des dépendances.
*   Migration vers Airflow 3 dans [data-engineering-stack](/repos/datagouv/data-engineering-stack).
*   Refactorisation de l'architecture d'authentification dans [apistration](/repos/datagouv/apistration).
*   Migration de l'outil de rendu MJML vers mrml dans [apistration](/repos/datagouv/apistration).

## Dépôts les plus actifs
*   [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de l'intégration avec CNOUS.
*   [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Amélioration de la robustesse des pipelines de données et gestion des données sources changeantes.
*   [apistration](/repos/datagouv/apistration) : Ajout d'un SDK Node.js, refonte du tableau de bord des fournisseurs et amélioration de la sécurité.
*   [cdata](/repos/datagouv/cdata) : Amélioration de la recherche, de l'administration et de l'expérience utilisateur.
*   [datagouv-mcp](/repos/datagouv/datagouv-mcp) : Ajout de nouveaux outils et correction d'une vulnérabilité de sécurité.
