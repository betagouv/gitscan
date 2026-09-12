# Synthèse d'activité : datagouv (du 09/03 au 11/09)

## Résumé de l'activité
L'activité récente est marquée par des avancées majeures sur l'expérience utilisateur et la robustesse des services. Des outils comme [simplifions](/repos/datagouv/simplifions) et [passemarche](/repos/datagouv/passemarche) ont vu leurs parcours utilisateurs fluidifiés et modernisés, facilitant notamment les démarches de candidature. Parallèlement, la plateforme [cdata](/repos/datagouv/cdata) et [hubee](/repos/datagouv/hubee) ont bénéficié d'optimisations de recherche et d'interfaces, améliorant l'accessibilité et la navigation. Enfin, une mise à jour massive des données de découpage administratif (COG 2026) a été déployée sur plusieurs dépôts pour garantir la fiabilité des informations géographiques.

## Sécurité
- Renforcement de la sécurité sur [hubee](/repos/datagouv/hubee) avec l'introduction de la double authentification (MFA), la migration vers OIDC et la mise en place de journaux d'audit.
- Amélioration de la protection des données personnelles dans [roles.data](/repos/datagouv/roles.data) et [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) via l'anonymisation des informations sensibles dans les logs et les requêtes.
- Correction de vulnérabilités et renforcement de la sécurité réseau sur [apistration](/repos/datagouv/apistration).

## Autres changements notables
- **Refontes architecturales et migrations** : passage à Rails 8.1 pour [relais](/repos/datagouv/relais), migration vers Airflow 3 pour [data-engineering-stack](/repos/datagouv/data-engineering-stack), introduction d'une couche sémantique pour [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) et migration vers PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr).
- **Évolution de l'écosystème CLI** : migration du code de l'interface en ligne de commande vers un dépôt dédié [datagouv-cli](/repos/datagouv/datagouv-cli) pour une meilleure distribution.
- **Optimisations techniques et maintenance** : remplacement de la librairie HTTPX par niquests pour [datagouv-client](/repos/datagouv/datagouv-client) et [datagouv-mcp](/repos/datagouv/datagouv-mcp), modernisation du support Python pour [fr-format](/repos/datagouv/fr-format) et amélioration de la configuration de l'agrégation pour [api-tabular](/repos/datagouv/api-tabular).
- **Fiabilisation des données et pipelines** : amélioration de la robustesse du crawler [hydra](/repos/datagouv/hydra), optimisation des pipelines [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) et mise à jour des données de découpage administratif (COG 2026) sur [decoupage-administratif](/repos/datagouv/decoupage-administratif), [cadastre](/repos/datagouv/cadastre) et [contours-administratifs](/repos/datagouv/contours-administratifs).
- **Infrastructure** : mise à niveau majeure d'Ansible dans [docker-ansible-git-crypt](/repos/datagouv/docker-ansible-git-crypt).

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Refonte majeure de l'authentification, de l'API et de l'interface.
- [passemarche](/repos/datagouv/passemarche) : Amélioration du parcours de candidature et de la navigation.
- [datagouv-client](/repos/datagouv/datagouv-client) et [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration et refonte de l'outil en ligne de commande.
- [cdata](/repos/datagouv/cdata) : Optimisations de recherche, de performance et de l'interface.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle pour l'évaluation des modèles d'IA.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Optimisation des pipelines de données et fiabilisation des connexions de stockage.
