# Synthèse d'activité : datagouv (du 01/01 au 07/01)

## Résumé de l'activité
L'activité récente est marquée par une amélioration notable des outils de gestion pour les agents et les utilisateurs, notamment avec de nouvelles fonctionnalités de gestion documentaire dans [hubee](/repos/datagouv/hubee) et une interface d'administration plus complète pour [simplifions](/repos/datagouv/simplifions). L'organisation prépare également l'avenir en intégrant les nouvelles données administratives et cadastrales de 2026 ([cadastre](/repos/datagouv/cadastre), [decoupage-administratif](/repos/datagouv/decoupage-administratif)) et en modernisant ses outils de ligne de commande ([datagouv-cli](/repos/datagouv/datagouv-cli)).

Par ailleurs, des efforts importants ont été consacrés à la modernisation des infrastructures techniques et à la robustesse des pipelines de données pour garantir la fiabilité des services à long terme.

## Sécurité
- **Renforcement de l'authentification et de la protection des données** :
    - Imposition du MFA pour l'authentification ProConnect et protection contre les injections de données dans les exports CSV et le "tabnabbing" dans [apistration](/repos/datagouv/apistration).
    - Amélioration de la traçabilité via la journalisation des adresses IP et masquage des informations sensibles (nonces, adresses) dans [hubee](/repos/datagouv/hubee).
    - Anonymisation des adresses email dans les logs d'erreur pour protéger la vie privée dans [roles.data](/repos/datagouv/roles.data).
    - Renforcement global de la sécurité dans [cdata](/repos/datagouv/cdata).

## Autres changements notables
- **Modernisation des infrastructures et des architectures** :
    - Refonte majeure de l'architecture de [relais](/repos/datagouv/relais) (passage à Rails 8.1 et GoodJob).
    - Migration vers de nouveaux gestionnaires de paquets pour améliorer les performances : PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) et Vite pour [grist-plugin-opendata](/repos/datagouv/grist-plugin-opendata).
    - Introduction d'une nouvelle couche sémantique pour l'évaluation des modèles d'IA dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).
- **Évolutions des outils de développement et de distribution** :
    - Refonte et autonomisation de l'interface en ligne de commande via le nouveau dépôt [datagouv-cli](/repos/datagouv/datagouv-cli).
    - Migration vers la bibliothèque `niquests` pour une meilleure gestion des requêtes HTTP dans [datagouv-client](/repos/datagouv/datagouv-client), [datagouv_client](/repos/datagouv/datagouv_client) et [datagouv-mcp](/repos/datagouv/datagouv-mcp).
- **Fiabilisation des flux de données** :
    - Optimisation des pipelines de données immobilières (DVF) dans [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines).
    - Amélioration de la robustesse du crawler dans [hydra](/repos/datagouv/hydra).

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Amélioration significative de la gestion documentaire et de l'expérience utilisateur.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte structurelle majeure pour l'évaluation des modèles d'IA.
- [passemarche](/repos/datagouv/passemarche) : Évolutions fonctionnelles importantes et optimisation du parcours utilisateur.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration et refonte complète de l'outil en ligne de commande.
- [apistration](/repos/datagouv/apistration) : Introduction de nouveaux flux de données et renforcement de la sécurité.
