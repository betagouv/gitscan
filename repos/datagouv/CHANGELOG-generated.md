# Synthèse d'activité : datagouv (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de cette période est marquée par une mise à jour majeure des données de référence, notamment le découpage administratif (COG 2026), les données cadastrales et l'intégration des données de l'Observatoire des Données Métropolitaines ([datagouvfr-pages](/repos/datagouv/datagouvfr-pages), [cadastre](/repos/datagouv/cadastre), [contours-administratifs](/repos/datagouv/contours-administratifs)). Parallèlement, l'organisation a réalisé des avancées significatives sur l'expérience utilisateur avec le déploiement de nouvelles interfaces de gestion et de consultation plus modernes et modulaires ([cdata](/repos/datagouv/cdata), [simplifions](/repos/datagouv/simplifions), [regles.data.gouv.fr](/repos/datagouv/regles.data.gouv.fr)).

L'effort de modernisation technique se poursuit à travers la refonte de l'outil en ligne de commande ([datagouv-cli](/repos/datagouv/datagouv-cli)), l'optimisation des pipelines de collecte de données pour plus de fiabilité ([hydra](/repos/datagouv/hydra), [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines)) et la montée en version de plusieurs infrastructures critiques ([relais](/repos/datagouv/relais), [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr)).

## Sécurité
- **Renforcement de la protection des données et des accès** : mise en place du MFA pour l'authentification ProConnect, sécurisation des exports CSV contre les injections de formules, et restriction par IP des jetons éditeur ([apistration](/repos/datagouv/apistration)).
- **Correction de vulnérabilités** : résolution de plusieurs failles de sécurité (CVE) et amélioration de la confidentialité via le masquage des données sensibles (adresses, noms, nonces) dans les journaux d'activité et d'erreurs ([hubee](/repos/datagouv/hubee), [roles.data](/repos/datagouv/roles.data)).

## Autres changements notables
- **Modernisation des infrastructures et des outils de build** : migration vers PNPM et Vite ([ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr), [grist-plugin-opendata](/repos/datagouv/grist-plugin-opendata)), mise à jour vers Rails 8.1 ([relais](/repos/datagouv/relais)), et adoption de la bibliothèque `niquests` pour optimiser la gestion des requêtes HTTP ([datagouv_client](/repos/datagouv/datagouv_client), [datagouv-mcp](/repos/datagouv/datagouv-mcp), [datagouv-client](/repos/datagouv/datagouv-client)).
- **Évolutions architecturales majeures** : introduction d'une couche sémantique pour l'évaluation des modèles d'IA ([datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation)), refonte complète de l'interface CLI pour une distribution autonome ([datagouv-cli](/repos/datagouv/datagouv-cli)), et passage à un système de mise en page modulaire par blocs ([cdata](/repos/datagouv/cdata)).
- **Optimisation des flux de données** : amélioration de la robustesse des crawlers et optimisation du traitement des fichiers compressés pour les pipelines de données ([hydra](/repos/datagouv/hydra), [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines)).

## Dépôts les plus actifs
- [simplifions](/repos/datagouv/simplifions) : Amélioration de l'interface d'administration et introduction d'un système de brouillons.
- [relais](/repos/datagouv/relais) : Refonte majeure de l'architecture et intégration de nouveaux services (CNOUS).
- [hubee](/repos/datagouv/hubee) : Évolutions fonctionnelles sur la gestion des agents et renforcement de la sécurité.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration et refonte complète de l'outil en ligne de commande.
- [regles.data.gouv.fr](/repos/datagouv/regles.data.gouv.fr) : Mise en place d'un catalogue de règles structuré et conforme au DSFR.
- [passemarche](/repos/datagouv/passemarche) : Amélioration de la gestion collaborative des groupements et du suivi des candidatures.
- [cdata](/repos/datagouv/cdata) : Refonte de l'interface utilisateur et de la navigation.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle pour l'évaluation sémantique des modèles d'IA.
