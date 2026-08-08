# Synthèse d'activité : datagouv (du 01/08 au 07/08)

## Résumé de l'activité
L'activité récente est marquée par une mise à jour majeure des référentiels de découpage administratif pour l'année 2026 ([decoupage-administratif](/repos/datagouv/decoupage-administratif), [cadastre](/repos/datagouv/cadastre)) et une modernisation profonde des outils d'accès et de gestion des identités ([hubee](/repos/datagouv/hubee), [relais](/repos/datagouv/relais)). 

Parallèlement, l'organisation renforce ses capacités d'exploration de données et d'évaluation de l'intelligence artificielle ([cdata](/repos/datagouv/cdata), [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation)), tout en optimisant la robustesse de ses pipelines de données pour garantir la fiabilité des informations publiées.

## Sécurité
- Correction de vulnérabilités critiques via la mise à jour de Rails ([passemarche](/repos/datagouv/passemarche)) et d'ActiveStorage ([apistration](/repos/datagouv/apistration)).
- Sécurisation de la construction des URLs ([passemarche](/repos/datagouv/passemarche)).
- Renforcement de l'authentification avec l'intégration de la double authentification (MFA), la gestion sécurisée des sessions et le chiffrement des jetons ([hubee](/repos/datagouv/hubee)).
- Protection de la vie privée par l'anonymisation des adresses email dans les logs d'erreur ([roles.data](/repos/datagouv/roles.data)).

## Autres changements notables
- **Refontes d'infrastructure et d'authentification** : Migration vers le protocole OIDC natif ([hubee](/repos/datagouv/hubee)), déploiement de la version 2 de l'API géographique ([api-decoupage-administratif](/repos/datagouv/api-decoupage-administratif)) et migration de l'interface en ligne de commande vers un dépôt autonome ([datagouv-cli](/repos/datagouv/datagouv-cli)).
- **Modernisation des stacks techniques** : Passage à Rails 8.1 ([relais](/repos/datagouv/relais)), migration vers Airflow 3 ([data-engineering-stack](/repos/datagouv/data-engineering-stack)) et adoption de PNPM pour la gestion des dépendances ([ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr)).
- **Optimisation des communications** : Transition de la librairie HTTPX vers `niquests` pour améliorer la stabilité et les performances des clients API ([datagouv_client](/repos/datagouv/datagouv_client), [datagouv-mcp](/repos/datagouv/datagouv-mcp), [datagouv-client](/repos/datagouv/datagouv-client)).

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Refonte majeure du système d'authentification et de la gestion des agents.
- [cdata](/repos/datagouv/cdata) : Évolutions significatives de l'interface d'exploration et de visualisation des données.
- [datagouv-client](/repos/datagouv/datagouv-client) : Migration de l'interface de commande et optimisation des appels API.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle pour l'évaluation sémantique des modèles d'IA.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Maintenance intensive et renforcement de la robustesse des flux de données.
