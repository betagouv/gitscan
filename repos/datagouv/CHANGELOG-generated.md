# Synthèse d'activité : datagouv (du 01/08 au 04/09)

## Résumé de l'activité
L'activité de cette période est marquée par des évolutions majeures sur les plateformes de services, notamment avec le renforcement de la sécurité et de l'authentification sur [hubee](/repos/datagouv/hubee) et l'introduction de la gestion des candidatures en groupement sur [passemarche](/repos/datagouv/passemarche). Parallèlement, une mise à jour importante des données administratives et cadastrales (COG 2026) a été déployée sur plusieurs dépôts tels que [cadastre](/repos/datagouv/cadastre), [decoupage-administratif](/repos/datagouv/decoupage-administratif) et [contours-administratifs](/repos/datagouv/contours-administratifs).

L'écosystème technique progresse également avec une refonte de l'outil en ligne de commande vers [datagouv-cli](/repos/datagouv/datagouv-cli), une modernisation de la stack de données avec le passage à Airflow 3 dans [data-engineering-stack](/repos/datagouv/data-engineering-stack), et une restructuration profonde de l'évaluation de l'IA dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).

## Sécurité
- **Renforcement de l'authentification** : Mise en place de la double authentification (MFA), gestion des sessions et migration vers une implémentation native OIDC sur [hubee](/repos/datagouv/hubee).
- **Protection des données et de la vie privée** : Anonymisation des adresses email dans les logs d'erreurs sur [roles.data](/repos/datagouv/roles.data) et intégration de protections PII lors du parsing de fichiers sur [relais](/repos/datagouv/relais).
- **Corrections de vulnérabilités** : Mise à jour de Rails pour corriger une vulnérabilité sur [passemarche](/repos/datagouv/passemarche) et correction de CVE sur [apistration](/repos/datagouv/apistration).
- **Contrôle d'accès** : Restriction d'accès par IP et migration centralisée des identifiants sur [apistration](/repos/datagouv/apistration).

## Autres changements notables
- **Refontes architecturales et infrastructurelles** :
    - Migration vers Rails 8.1 et intégration de GoodJob pour la gestion des tâches asynchrones sur [relais](/repos/datagouv/relais).
    - Migration vers PNPM pour améliorer les performances et la maintenabilité sur [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr).
    - Passage à Airflow 3 pour la stack d'ingénierie de données sur [data-engineering-stack](/repos/datagouv/data-engineering-stack).
    - Migration du code de l'interface en ligne de commande vers un dépôt autonome [datagouv-cli](/repos/datagouv/datagouv-cli).
- **Optimisations de performance et de stabilité** :
    - Mise en place de stratégies de mise en cache et réduction des appels API sur [cdata](/repos/datagouv/cdata).
    - Remplacement de la librairie `httpx` par `niquests` pour une meilleure stabilité sur [datagouv_client](/repos/datagouv/datagouv_client), [datagouv-mcp](/repos/datagouv/datagouv-mcp) et [datagouv-client](/repos/datagouv/datagouv-client).
    - Optimisation des pipelines de données immobilières (DVF) via le format compressé `.gz` sur [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines).
- **Évolutions sémantiques et outils** :
    - Introduction d'une nouvelle couche sémantique pour l'évaluation des modèles d'IA sur [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).
    - Amélioration de la détection des types de données (SIREN/SIRET) sur [csv-detective](/repos/datagouv/csv-detective).

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Refonte majeure du système d'authentification et lancement de l'API V2.
- [passemarche](/repos/datagouv/passemarche) : Introduction de la gestion des groupements et optimisation du parcours utilisateur.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle profonde et ajout de nouvelles capacités d'évaluation.
- [cdata](/repos/datagouv/cdata) : Améliorations significatives de l'interface, de la recherche et des performances.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration complète et autonomisation de l'outil en ligne de commande.
- [relais](/repos/datagouv/relais) : Mise à jour majeure de l'infrastructure et intégration de nouveaux services (CNOUS).
