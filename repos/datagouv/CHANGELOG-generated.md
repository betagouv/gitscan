# Synthèse d'activité : datagouv (du 13 mai 2026 au 27 juillet 2026)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des améliorations significatives de l'infrastructure, de la sécurité et des fonctionnalités de ses différents services. Plusieurs projets ont bénéficié de mises à jour majeures, comme le passage à Rails 8.1 pour [relais](/repos/datagouv/relais) et la migration vers PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr). L'accent a également été mis sur l'amélioration de l'accessibilité et de la robustesse des API, notamment [apistration](/repos/datagouv/apistration) et [api-tabular](/repos/datagouv/api-tabular). De nouveaux services et fonctionnalités ont été introduits, comme l'intégration CNOUS dans [relais](/repos/datagouv/relais) et l'ajout de l'IdRNB au format de validation dans [fr-format](/repos/datagouv/fr-format). Enfin, plusieurs projets ont bénéficié de mises à jour de données, comme [cadastre.data.gouv.fr](/repos/datagouv/cadastre.data.gouv.fr) et [contours-administratifs](/repos/datagouv/contours-administratifs).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de vulnérabilités dans [hubee](/repos/datagouv/hubee) (CVEs) et [apistration](/repos/datagouv/apistration) (tabnapping, XSS).
- Anonymisation des adresses email dans les logs d'erreur de [roles.data](/repos/datagouv/roles.data).
- Ajout d'une Content Security Policy (CSP) minimale dans [hubee](/repos/datagouv/hubee).

## Autres changements notables
- Migration vers Airflow 3 dans [data-engineering-stack](/repos/datagouv/data-engineering-stack).
- Refonte de l'architecture de [relais](/repos/datagouv/relais) pour s'aligner avec apistration.
- Introduction d'une nouvelle couche sémantique dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) pour faciliter l'évaluation des modèles d'IA.
- Nouvelle version de l'API géographique (v2) dans [api-decoupage-administratif](/repos/datagouv/api-decoupage-administratif).
- Migration de l'interface en ligne de commande vers `datagouv-cli` dans [datagouv_client](/repos/datagouv/datagouv_client).

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de nouvelles fonctionnalités (intégration CNOUS, demandes proactives).
- [hubee](/repos/datagouv/hubee) : Améliorations de la sécurité, modernisation de l'infrastructure et préparation du portail V2.
- [roles.data](/repos/datagouv/roles.data) : Amélioration de la robustesse et du débogage de l'application.
- [apistration](/repos/datagouv/apistration) : Ajout de nouvelles fonctionnalités (gestion des tokens éditeur, webhook) et amélioration de l'accessibilité.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Corrections et améliorations des pipelines de données, migration vers OVH.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration du code CLI et amélioration de la distribution.
