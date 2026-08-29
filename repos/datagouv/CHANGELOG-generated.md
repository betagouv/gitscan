# Synthèse d'activité : datagouv (du 01/03 au 31/08)

## Résumé de l'activité
L'activité récente est marquée par des avancées fonctionnelles majeures, notamment l'introduction de la gestion des candidatures en groupement d'entreprises dans [passemarche](/repos/datagouv/passemarche) et de nouvelles capacités d'exploration de données dans [cdata](/repos/datagouv/cdata). L'organisation a également assuré la mise à jour de ses référentiels de découpage administratif pour l'année 2026 via [cadastre](/repos/datagouv/cadastre) et [decoupage-administratif](/repos/datagouv/decoupage-administratif).

Parallèlement, plusieurs projets ont entamé des phases de refonte structurelle pour améliorer leur performance et leur maintenabilité, comme le lancement de l'application autonome [simplifions](/repos/datagouv/simplifions) ou l'autonomisation de l'outil en ligne de commande [datagouv-cli](/repos/datagouv/datagouv-cli).

## Sécurité
- Renforcement de l'authentification via l'introduction du multi-facteur (MFA), le chiffrement des jetons au repos et la gestion des sessions dans [hubee](/repos/datagouv/hubee).
- Amélioration de la protection de la vie privée par l'anonymisation des données sensibles dans les logs d'erreurs dans [roles.data](/repos/datagouv/roles.data).
- Durcissement de la sécurité par la restriction d'IP, la correction de CVE et la mise à jour de Rails dans [apistration](/repos/datagouv/apistration) et [passemarche](/repos/datagouv/passemarche).

## Autres changements notables
- Migrations d'infrastructure majeures : passage à Airflow 3 pour [data-engineering-stack](/repos/datagouv/data-engineering-stack), adoption de PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) et montée de version vers Rails 8.1 pour [relais](/repos/datagouv/relais).
- Refonte de l'outil en ligne de commande, désormais autonome et multiplateforme (Windows, macOS, Linux), via [datagouv-cli](/repos/datagouv/datagouv-cli).
- Évolution de l'architecture d'évaluation de l'IA avec l'introduction d'une couche sémantique dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).
- Modernisation de la gestion des requêtes HTTP par la migration vers la librairie `niquests` dans plusieurs dépôts ([datagouv_client](/repos/datagouv/datagouv_client), [datagouv-mcp](/repos/datagouv/datagouv-mcp) et [datagouv-client](/repos/datagouv/datagouv-client)).

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Refonte majeure du système d'authentification et de la gestion des profils agents.
- [passemarche](/repos/datagouv/passemarche) : Introduction de la gestion des groupements et optimisation du parcours utilisateur.
- [cdata](/repos/datagouv/cdata) : Amélioration de l'exploration, de la visualisation et du suivi de publication.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle pour l'évaluation sémantique des modèles d'IA.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration et autonomisation de l'interface en ligne de commande.
- [relais](/repos/datagouv/relais) : Refonte de l'infrastructure et intégration de nouveaux services (CNOUS).
- [simplifions](/repos/datagouv/simplifions) : Lancement de l'application Rails autonome et mise en conformité avec le Design System de l'État.
