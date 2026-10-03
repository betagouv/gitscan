# Synthèse d'activité : datagouv (du 25/05 au 01/06)

## Résumé de l'activité
L'activité de cette période est marquée par une double dynamique : une amélioration significative de l'expérience utilisateur sur les outils de candidature et de consultation, et une modernisation profonde des infrastructures techniques. Les utilisateurs bénéficieront de parcours plus fluides sur [passemarche](/repos/datagouv/passemarche) et d'un nouveau catalogue plus performant sur [simplifions](/repos/datagouv/simplifions). 

Parallèlement, l'organisation assure la fraîcheur des données avec la mise à jour des découpages administratifs pour 2026 sur plusieurs dépôts comme [cadastre](/repos/datagouv/cadastre) et [contours-administratifs](/repos/datagouv/contours-administratifs). Ces évolutions visent à renforcer la fiabilité des services tout en préparant les bases techniques des futurs développements.

## Sécurité
- Renforcement de l'authentification et de la gestion des accès avec l'intégration d'OpenID Connect (OIDC), du MFA et d'OAuth2 sur [hubee](/repos/datagouv/hubee) et [apistration](/repos/datagouv/apistration).
- Amélioration de la protection des données via l'anonymisation des informations sensibles dans les logs sur [roles.data](/repos/datagouv/roles.data) et la sécurisation du rendu Markdown sur [simplifions](/repos/datagouv/simplifions).
- Mise en place de contrôles d'accès par adresse IP et d'une nouvelle introspection de jetons sur [apistration](/repos/datagouv/apistration).

## Autres changements notables
- **Migrations technologiques majeures** : passage à Rails 8.1 pour [relais](/repos/datagouv/relais), à Airflow 3 pour [data-engineering-stack](/repos/datagouv/data-engineering-stack), et adoption de PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr).
- **Refonte de l'outil en ligne de commande** : migration du code CLI vers un dépôt dédié [datagouv-cli](/repos/datagouv/datagouv-cli) pour permettre une distribution autonome sur Windows et macOS.
- **Optimisation des pipelines et de la collecte** : amélioration des processus de traitement des données immobilières (DVF) sur [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) et renforcement de la robustesse du crawler sur [hydra](/repos/datagouv/hydra).
- **Modernisation des bibliothèques clientes** : remplacement de la librairie `httpx` par `niquests` pour améliorer les performances et la stabilité sur [datagouv_client](/repos/datagouv/datagouv_client), [datagouv-client](/repos/datagouv/datagouv-client) et [datagouv-mcp](/repos/datagouv/datagouv-mcp).
- **Évolution structurelle de l'IA** : introduction d'une couche sémantique majeure pour faciliter l'évaluation des modèles sur [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).

## Dépôts les plus actifs
- [simplifions](/repos/datagouv/simplifions) : Mise en service d'un nouveau catalogue avec recherche et filtrage.
- [passemarche](/repos/datagouv/passemarche) : Refonte du parcours de candidature et de la navigation assistée.
- [apistration](/repos/datagouv/apistration) : Intégration de DataPass et renforcement de la sécurité des jetons.
- [relais](/repos/datagouv/relais) : Refonte majeure de l'architecture et intégration du CNOUS.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle et amélioration de la qualité du code.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration et amélioration de la distribution de l'outil en ligne de commande.
