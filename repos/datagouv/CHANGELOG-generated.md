# Synthèse d'activité : datagouv (du 06/11 au 13/11)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une amélioration significative de l'expérience utilisateur et une modernisation profonde des infrastructures. Les évolutions sur [simplifions](/repos/datagouv/simplifions) et [hubee](/repos/datagouv/hubee) facilitent la gestion administrative et la navigation sur les portails, tandis que la mise à jour des données de découpage administratif et cadastral (COG 2026) garantit la fiabilité des informations géographiques pour les utilisateurs ([cadastre](/repos/datagouv/cadastre), [decoupage-administratif](/repos/datagouv/decoupage-administratif)).

L'organisation renforce également ses capacités liées à l'intelligence artificielle avec des avancées structurelles sur [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) et [datagouv-mcp](/repos/datagouv/datagouv-mcp), tout en simplifiant l'usage de ses outils techniques via la refonte de l'interface en ligne de commande ([datagouv-cli](/repos/datagouv/datagouv-cli)).

## Sécurité
- Correction de vulnérabilités critiques (Rails, Rack, Addressable) et durcissement des conteneurs Docker sur [simplifions](/repos/datagouv/simplifions) et [hubee](/repos/datagouv/hubee).
- Renforcement de la protection de la vie privée par l'anonymisation des données sensibles dans les logs d'erreurs sur [roles.data](/repos/datagouv/roles.data).
- Amélioration de la traçabilité des événements de sécurité et de la gestion des accès sur [hubee](/repos/datagouv/hubee) et [apistration](/repos/datagouv/apistration).

## Autres changements notables
- **Modernisation des frameworks et infrastructures** : Migrations majeures vers Rails 8.1 et Ruby 4.0.9 sur [relais](/repos/datagouv/relais), [hubee](/repos/datagouv/hubee) et [apistration](/repos/datagouv/apistration). Adoption de nouveaux gestionnaires de paquets (PNPM, Vite) pour améliorer les performances de build sur [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) et [grist-plugin-opendata](/repos/datagouv/grist-plugin-opendata).
- **Refonte des outils de développement** : Migration complète du code de l'interface en ligne de commande vers un dépôt dédié [datagouv-cli](/repos/datagouv/datagouv-cli), permettant désormais une installation simplifiée sur Windows et macOS.
- **Avancées en Intelligence Artificielle** : Introduction d'une couche sémantique majeure pour l'évaluation des modèles d'IA sur [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).
- **Optimisation des flux de données** : Amélioration de la robustesse du processus de collecte sur [hydra](/repos/datagouv/hydra) et optimisation des pipelines de données immobilières sur [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines).

## Dépôts les plus actifs
- [simplifions](/repos/datagouv/simplifions) : Amélioration de l'expérience utilisateur, de l'accessibilité et de la gestion administrative.
- [hubee](/repos/datagouv/hubee) : Montée en puissance de l'API, refonte de l'interface portail et renforcement de la sécurité.
- [regles.data.gouv.fr](/repos/datagouv/regles.data.gouv.fr) : Personnalisation visuelle (multi-thèmes) et automatisation de la génération du catalogue de règles.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle pour permettre une évaluation plus fine et sémantique des modèles d'IA.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration et amélioration de l'outil de ligne de commande pour une meilleure portabilité.
