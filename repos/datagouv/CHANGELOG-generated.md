# Synthèse d'activité : datagouv (du 01/09 au 07/09)

## Résumé de l'activité
L'activité de la semaine est marquée par des avancées majeures sur les interfaces utilisateurs et les outils de gestion de données. Les plateformes [hubee](/repos/datagouv/hubee), [passemarche](/repos/datagouv/passemarche) et [simplifions](/repos/datagouv/simplifions) ont bénéficié d'améliorations significatives, facilitant la recherche, le filtrage et le parcours de candidature pour les utilisateurs finaux. Parallèlement, l'écosystème d'outils de ligne de commande a été profondément restructuré avec la création de [datagouv-cli](/repos/datagouv/datagouv-cli), offrant une meilleure expérience de développement et de distribution.

L'organisation renforce également la fiabilité de ses pipelines de données et de ses infrastructures, notamment via la mise à jour des données administratives 2026 ([cadastre](/repos/datagouv/cadastre), [decoupage-administratif](/repos/datagouv/decoupage-administratif)) et la modernisation des outils de traitement ([datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines), [hydra](/repos/datagouv/hydra)).

## Sécurité
- Renforcement de l'authentification sur [hubee](/repos/datagouv/hubee) avec l'intégration du multi-facteur (MFA) et du socle OAuth2.
- Correction d'une vulnérabilité (CVE) liée à la gestion des fichiers dans [apistration](/repos/datagouv/apistration).
- Amélioration de la protection de la vie privée dans [roles.data](/repos/datagouv/roles.data) via l'anonymisation des adresses email dans les logs d'erreur.
- Sécurisation du rendu du contenu Markdown dans [simplifions](/repos/datagouv/simplifions).

## Autres changements notables
- Refonte majeure de l'infrastructure et de l'architecture de [relais](/repos/datagouv/relais) (passage à Rails 8.1 et intégration de GoodJob).
- Migration de l'interface en ligne de commande vers un dépôt dédié, [datagouv-cli](/repos/datagouv/datagouv-cli), permettant une distribution autonome sur Windows et macOS.
- Modernisation technique de plusieurs composants, incluant la migration vers PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) et le passage à Airflow 3 pour [data-engineering-stack](/repos/datagouv/data-engineering-stack).
- Évolution de la stack HTTP pour [datagouv-client](/repos/datagouv/datagouv-client) et [datagouv-mcp](/repos/datagouv/datagouv-mcp) avec l'adoption de la librairie `niquests`.
- Introduction d'une couche sémantique majeure dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) pour l'évaluation des modèles d'IA.

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Améliorations importantes du portail (recherche, téléchargement) et renforcement de la sécurité.
- [passemarche](/repos/datagouv/passemarche) : Refonte du parcours de candidature et de la navigation (mode wizard).
- [simplifions](/repos/datagouv/simplifions) : Mise en service d'un nouveau catalogue avec recherche et filtrage.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Refonte majeure pour une distribution indépendante et multi-plateforme.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle axée sur l'évaluation sémantique et la qualité du code.
- [cdata](/repos/datagouv/cdata) : Optimisations de performance (mise en cache) et améliorations de l'interface de recherche.
- [datagouv-client](/repos/datagouv/datagouv-client) : Migration vers une nouvelle structure CLI et optimisation des appels API.
