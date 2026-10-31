# Synthèse d'activité : datagouv (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de la période est marquée par une modernisation profonde des outils et une mise à jour majeure des données de référence pour 2026. Les utilisateurs bénéficieront d'interfaces plus intuitives et collaboratives, notamment sur [simplifions](/repos/datagouv/simplifions), [passemarche](/repos/datagouv/passemarche) et [hubee](/repos/datagouv/hubee). L'écosystème de ligne de commande est également transformé avec la migration vers un outil dédié, [datagouv-cli](/repos/datagouv/datagouv-cli), offrant une meilleure portabilité sur différents systèmes d'exploitation.

Parallèlement, la fiabilité des données est renforcée par l'intégration des nouvelles nomenclatures administratives (COG 2026) dans [decoupage-administratif](/repos/datagouv/decoupage-administratif) et [cadastre](/repos/datagouv/cadastre), ainsi que par l'optimisation des pipelines de données avec [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines).

## Sécurité
- Renforcement de la sécurité sur [apistration](/repos/datagouv/apistration) via l'imposition du MFA pour ProConnect, la protection contre les injections de formules dans les exports CSV, la restriction d'IP pour les jetons éditeur et la protection contre le "tabnabbing".
- Amélioration de la protection de la vie privée dans [roles.data](/repos/datagouv/roles.data) par l'anonymisation des adresses email dans les logs d'erreurs envoyés à Sentry.
- Sécurisation des conteneurs dans [hubee](/repos/datagouv/hubee) par l'utilisation d'images Docker "distroless" et filtrage des données sensibles vers Sentry.

## Autres changements notables
- Refonte majeure de l'infrastructure et de l'architecture de [relais](/repos/datagouv/relais), passant à Rails 8.1 et intégrant GoodJob pour la gestion des tâches asynchrones.
- Migration de l'interface en ligne de commande vers un nouveau dépôt autonome, [datagouv-cli](/repos/datagouv/datagouv-cli), pour faciliter sa distribution (macOS, Windows).
- Modernisation technique de [grist-plugin-opendata](/repos/datagouv/grist-plugin-opendata) (Vite, pnpm, Docker) et de [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) (migration vers PNPM).
- Évolution structurelle de [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) avec l'introduction d'une couche sémantique et le passage à Opik 2 pour l'évaluation des modèles d'IA.
- Amélioration de la robustesse du crawler et de la gestion des formats de données dans [hydra](/repos/datagouv/hydra).

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Enrichissement des capacités d'échange documentaire et refonte de l'expérience utilisateur.
- [regles.data.gouv.fr](/repos/datagouv/regles.data.gouv.fr) : Mise en place d'un catalogue de règles structuré et mise en conformité avec le Design System de l'État.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte profonde axée sur la qualité du code et l'évaluation sémantique.
- [simplifions](/repos/datagouv/simplifions) : Modernisation de l'interface d'administration et des outils de gestion de contenu.
- [passemarche](/repos/datagouv/passemarche) : Optimisation des workflows collaboratifs pour la gestion des groupements et des candidatures.
