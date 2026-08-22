# Synthèse d'activité : datagouv (du 01/08 au 07/08)

## Résumé de l'activité
L'activité de cette période est marquée par trois axes majeurs : la modernisation profonde des infrastructures techniques, le renforcement de la sécurité des accès et la mise à jour des données de référence pour 2026. Les équipes ont réalisé des migrations technologiques importantes (Airflow, Rails, PNPM) pour garantir la pérennité et la performance des services.

Parallèlement, l'expérience utilisateur est enrichie par de nouvelles fonctionnalités d'exploration de données dans [cdata](/repos/datagouv/cdata) et une refonte de l'interface de ligne de commande pour les développeurs. Enfin, l'organisation assure la fraîcheur de ses services en intégrant les nouvelles données de découpage administratif et cadastral.

## Sécurité
- **Renforcement de l'authentification** : Mise en place de l'authentification multi-facteur (MFA) et migration vers le protocole OIDC pour sécuriser les accès dans [hubee](/repos/datagouv/hubee).
- **Protection des données personnelles** : Anonymisation des adresses email dans les logs d'erreurs pour protéger la vie privée dans [roles.data](/repos/datagouv/roles.data).
- **Corrections de vulnérabilités** : Résolution de failles de sécurité (CVE) liées à la gestion des fichiers dans [apistration](/repos/datagouv/apistration) et mise à jour de Rails dans [passemarche](/repos/datagouv/passemarche).
- **Sécurisation des données sensibles** : Chiffrement des jetons d'authentification au repos dans [hubee](/repos/datagouv/hubee) et gestion centralisée des secrets dans [apistration](/repos/datagouv/apistration).

## Autres changements notables
- **Migrations d'infrastructure majeures** : Passage à Airflow 3 pour [data-engineering-stack](/repos/datagouv/data-engineering-stack), à Rails 8.1 pour [relais](/repos/datagouv/relais), et adoption de PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr).
- **Refonte de l'écosystème CLI** : Séparation de l'interface en ligne de commande du client Python, permettant une distribution autonome et multiplateforme (Windows, macOS) via [datagouv-cli](/repos/datagouv/datagouv-cli) et [datagouv-client](/repos/datagouv/datagouv-client).
- **Mise à jour des données de référence** : Intégration des données de découpage administratif et cadastral 2026 dans [decoupage-administratif](/repos/datagouv/decoupage-administratif), [cadastre](/repos/datagouv/cadastre) et [contours-administratifs](/repos/datagouv/contours-administratifs).
- **Optimisation des pipelines de données** : Amélioration des performances et de la fiabilité des flux de données immobilières (DVF) dans [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines).
- **Évolution de l'IA** : Introduction d'une couche sémantique pour l'évaluation des modèles d'IA dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Refonte majeure du système d'authentification, de gestion des sessions et des profils agents.
- [cdata](/repos/datagouv/cdata) : Évolutions importantes de l'interface d'exploration, de visualisation et de suivi de publication.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle profonde pour l'évaluation sémantique des modèles.
- [datagouv-client](/repos/datagouv/datagouv-client) et [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration et séparation de l'interface de ligne de commande.
- [passemarche](/repos/datagouv/passemarche) : Améliorations fonctionnelles liées aux procédures de candidature et à la conformité juridique.
