# Synthèse d'activité : datagouv (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de la période est marquée par une amélioration significative de l'expérience utilisateur sur plusieurs services clés. Les plateformes de gestion de candidatures et de dossiers, notamment [simplifions](/repos/datagouv/simplifions), [passemarche](/repos/datagouv/passemarche) et [hubee](/repos/datagouv/hubee), ont bénéficié de nouvelles interfaces (nouveaux catalogues, assistants de saisie, gestion documentaire facilitée) visant à fluidifier le parcours des agents et des usagers.

Parallèlement, l'organisation a engagé des transitions techniques majeures pour moderniser ses infrastructures. Cela inclut une refonte de l'outillage en ligne de commande, la migration vers de nouveaux standards de gestion de dépendances et de pipelines de données, ainsi qu'une mise à jour massive des données de découpage administratif pour l'année 2026.

## Sécurité
- **Renforcement de l'authentification et des accès** : Mise en place de l'authentification multi-facteur (MFA) pour les comptes à privilèges et support des protocoles OAuth2/OIDC dans [hubee](/repos/datagouv/hubee), ainsi qu'une nouvelle version de l'introspection de jetons dans [apistration](/repos/datagouv/apistration).
- **Protection de la vie privée** : Amélioration de l'anonymisation des données sensibles (adresses email, requêtes de support) dans les logs et les processus d'évaluation pour [roles.data](/repos/datagouv/roles.data) et [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).
- **Corrections de vulnérabilités** : Résolution de failles de sécurité auditées dans [cdata](/repos/datagouv/cdata).

## Autres changements notables
- **Refonte de l'outillage CLI** : Migration et séparation du code de l'interface en ligne de commande entre [datagouv-client](/repos/datagouv/datagouv-client) et [datagouv-cli](/repos/datagouv/datagouv-cli) pour une meilleure autonomie de distribution.
- **Modernisation des infrastructures et frameworks** : Migrations majeures vers Airflow 3 pour [data-engineering-stack](/repos/datagouv/data-engineering-stack), vers Rails 8.1 pour [relais](/repos/datagouv/relais), et adoption de PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr).
- **Optimisation des communications HTTP** : Remplacement de la librairie `httpx` par `niquests` pour améliorer la stabilité et les performances dans [datagouv-mcp](/repos/datagouv/datagouv-mcp), [datagouv-client](/repos/datagouv/datagouv-client) et [datagouv_client](/repos/datagouv/datagouv_client).
- **Mise à jour des données de référence** : Intégration des nouvelles données de découpage administratif (COG/DGCL 2026) dans [decoupage-administratif](/repos/datagouv/decoupage-administratif), [cadastre](/repos/datagouv/cadastre) et [contours-administratifs](/repos/datagouv/contours-administratifs).
- **Optimisation des pipelines de données** : Amélioration de la gestion des fichiers compressés et de la fiabilité des connexions de stockage (S3/SFTP) dans [hydra](/repos/datagouv/hydra) et [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines).

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Évolutions majeures sur l'expérience agent, la recherche et la sécurité.
- [simplifions](/repos/datagouv/simplifions) : Mise en service d'un nouveau catalogue et refonte de l'architecture de données.
- [passemarche](/repos/datagouv/passemarche) : Refonte du parcours de candidature avec un système de navigation assistée (wizard).
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Refonte complète et migration de l'interface en ligne de commande.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle profonde pour l'évaluation des modèles d'IA.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Optimisation des pipelines de données immobilières et fiabilisation des connexions.
