# Synthèse d'activité : datagouv (du 01/10 au 20/10)

## Résumé de l'activité
L'activité de cette période est marquée par des avancées majeures sur les outils de gestion, d'échange et de conformité des données. Les utilisateurs bénéficieront de nouvelles capacités de collaboration en groupement dans [passemarche](/repos/datagouv/passemarche) et d'une gestion documentaire nettement enrichie dans [hubee](/repos/datagouv/hubee). L'écosystème s'affine également avec la mise à disposition d'un nouvel outil en ligne de commande autonome [datagouv-cli](/repos/datagouv/datagouv-cli) et des évolutions significatives dans l'évaluation des modèles d'IA via [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation).

Par ailleurs, la plateforme de règles [regles.data.gouv.fr](/repos/datagouv/regles.data.gouv.fr) franchit une étape clé en proposant désormais un catalogue structuré et conforme aux standards de l'État, facilitant ainsi la consultation et la fiabilité des informations publiées.

## Sécurité
- Renforcement de la sécurité des accès avec l'imposition du MFA pour ProConnect et la restriction d'IP pour les jetons éditeur dans [apistration](/repos/datagouv/apistration).
- Protection contre les injections de formules dans les exports CSV et contre les attaques de type "tabnabbing" dans [apistration](/repos/datagouv/apistration).
- Amélioration de la confidentialité des données par l'anonymisation des adresses email dans les logs d'erreurs de [roles.data](/repos/datagouv/roles.data).
- Sécurisation des infrastructures de conteneurs via l'utilisation d'images "distroless" dans [hubee](/repos/datagouv/hubee).

## Autres changements notables
- **Refonte de l'interface CLI** : Migration de l'interface en ligne de commande vers un dépôt dédié [datagouv-cli](/repos/datagouv/datagouv-cli), permettant une distribution autonome et multiplateforme (Windows, macOS, Linux).
- **Modernisation des bibliothèques HTTP** : Migration massive de plusieurs composants ([datagouv_client](/repos/datagouv/datagouv_client), [datagouv-client](/repos/datagouv/datagouv-client), [datagouv-mcp](/repos/datagouv/datagouv-mcp)) vers `niquests` pour une meilleure stabilité et performance.
- **Évolution de l'IA** : Refonte profonde de [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) avec l'introduction d'une couche sémantique et l'adoption d'Opik 2 pour l'évaluation des modèles.
- **Optimisation des infrastructures de build** : Adoption de nouveaux outils de gestion de paquets et de build (`pnpm`, `Vite`) dans [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr), [grist-plugin-opendata](/repos/datagouv/grist-plugin-opendata) et [explore.data.gouv.fr](/repos/datagouv/explore.data.gouv.fr).
- **Mise à jour technologique** : Passage de [relais](/repos/datagouv/relais) à Rails 8.1.

## Dépôts les plus actifs
- [hubee](/repos/datagouv/hubee) : Enrichissement des fonctionnalités d'échange documentaire et amélioration de l'expérience utilisateur.
- [regles.data.gouv.fr](/repos/datagouv/regles.data.gouv.fr) : Mise en place d'un catalogue de règles structuré et mise en conformité visuelle (DSFR).
- [passemarche](/repos/datagouv/passemarche) : Introduction de la collaboration en groupement et amélioration du suivi des candidatures.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Refonte complète pour une distribution autonome et multiplateforme.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte de l'architecture pour l'évaluation sémantique des modèles d'IA.
- [apistration](/repos/datagouv/apistration) : Introduction des flux DataPass et renforcement de la sécurité des données.
