# Synthèse d'activité : datagouv (du 01/05 au 31/08)

## Résumé de l'activité
L'activité de cette période est marquée par une mise à jour majeure des données de référence, notamment avec l'intégration des nouvelles données de découpage administratif et cadastral pour 2026 dans des dépôts comme [cadastre](/repos/datagouv/cadastre) et [decoupage-administratif](/repos/datagouv/decoupage-administratif). L'organisation a également franchi des étapes importantes dans l'amélioration de l'expérience utilisateur, avec l'ajout de fonctionnalités d'exploration de données dans [cdata](/repos/datagouv/cdata) et l'intégration de nouveaux services (CNOUS) dans [relais](/repos/datagouv/relais).

Parallèlement, un effort conséquent a été porté sur la modernisation des socles techniques. Cela se traduit par des refontes architecturales profondes pour améliorer la performance et la sécurité, ainsi que par l'enrichissement des capacités d'évaluation des modèles d'intelligence artificielle dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).

## Sécurité
- **Renforcement de l'authentification** : Refonte majeure du système d'identité dans [hubee](/repos/datagouv/hubee) avec l'intégration native du protocole OIDC, la mise en place de la double authentification (MFA) et un chiffrement des jetons au repos.
- **Protection de la vie privée** : Anonymisation des adresses email dans les logs d'exception pour [roles.data](/repos/datagouv/roles.data) et filtrage des données sensibles dans les logs de [hubee](/repos/datagouv/hubee).
- **Corrections de vulnérabilités** : Mise à jour de Rails pour corriger une vulnérabilité dans [passemarche](/repos/datagouv/passemarche) et gestion sécurisée des secrets dans [apistration](/repos/datagouv/apistration).
- **Résilience et contrôle** : Implémentation de systèmes de limitation de débit (throttling) dans [apistration](/repos/datagouv/apistration) et amélioration de la gestion des sessions dans [hubee](/repos/datagouv/hubee).

## Autres changements notables
- **Migrations d'infrastructure et de frameworks** : Passage à Rails 8.1 et intégration de GoodJob pour [relais](/repos/datagouv/relais), migration vers Airflow 3 pour [data-engineering-stack](/repos/datagouv/data-engineering-stack), et adoption de PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr).
- **Évolution de l'écosystème CLI** : Migration de l'interface en ligne de commande vers un nouveau dépôt dédié [datagouv-cli](/repos/datagouv/datagouv-cli) pour permettre une distribution autonome sur Windows et macOS.
- **Modernisation des dépendances réseau** : Remplacement de la librairie `httpx` par `niquests` pour améliorer la stabilité et les performances dans [datagouv_client](/repos/datagouv/datagouv_client), [datagouv-mcp](/repos/datagouv/datagouv-mcp) et [datagouv-client](/repos/datagouv/datagouv-client).
- **Avancées sur l'IA** : Introduction d'une couche sémantique majeure dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) pour structurer l'évaluation des modèles.

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Refonte complète du système d'authentification et de la gestion des profils agents.
- [cdata](/repos/datagouv/cdata) : Évolutions importantes de l'interface d'exploration, de visualisation et de suivi des publications.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle pour l'évaluation sémantique et la gestion des tâches d'IA.
- [relais](/repos/datagouv/relais) : Mise à jour majeure de l'architecture et intégration de nouveaux flux de données.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration et déploiement de la nouvelle interface de ligne de commande.
