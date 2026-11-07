# Synthèse d'activité : etalab (du 25/10 au 01/11)

## Résumé de l'activité
L'activité de la période est marquée par une modernisation profonde des outils de gestion des données de transport, notamment via la montée en version technologique de [transport-site](/repos/etalab/transport-site) et l'évolution des standards de données avec [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr). Ces évolutions visent à accroître la fiabilité du traitement des données et la robustesse des interfaces d'administration.

Parallèlement, un effort important a été porté sur la sécurisation des services publics numériques et la protection de la vie privée. Les travaux sur [formulaire-qf](/repos/etalab/formulaire-qf) et [data_pass](/repos/etalab/data_pass) illustrent cette volonté de renforcer la confidentialité des données personnelles et la fiabilité des échanges entre les services de l'État et les collectivités.

## Sécurité
- **Protection des données personnelles** : Réduction massive des fuites de données (PII) vers les outils de monitoring sur [formulaire-qf](/repos/etalab/formulaire-qf), en excluant systématiquement les identités et données de quotient familial des logs.
- **Gestion des accès et authentification** : Renforcement de la sécurité sur [data_pass](/repos/etalab/data_pass) avec l'obligation de la double authentification (2FA) et sur [admin_api_entreprise](/repos/etalab/admin_api_entreprise) via la rotation des tokens et la migration des scopes d'autorisation.
- **Correction de vulnérabilités** : Mise à jour de bibliothèques critiques pour corriger des failles de sécurité sur [formulaire-qf](/repos/etalab/formulaire-qf).

## Autres changements notables
- **Modernisation technologique** : Migration majeure de [transport-site](/repos/etalab/transport-site) vers Phoenix 1.8 et Elixir 1.20, accompagnée d'une refonte du backoffice.
- **Évolution d'architecture** : Introduction de l'architecture "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide), permettant d'étendre les schémas de données de manière flexible.
- **Optimisation des performances** : Amélioration de la gestion mémoire de [transport-validator](/repos/etalab/transport-validator) via l'adoption de l'allocateur `jemalloc`.
- **Élargissement des capacités API** : Intégration de nouveaux flux de données (CNOUS, MSA, MEN) dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Modernisation complète du framework et fiabilisation du traitement des données NeTEx.
- [formulaire-qf](/repos/etalab/formulaire-qf) : Travaux intensifs sur la confidentialité des données, la sécurité des dépendances et la stabilisation des parcours utilisateurs.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Évolution des capacités d'intégration API et gestion des accès sécurisés.
- [data_pass](/repos/etalab/data_pass) : Automatisation du cycle de vie des demandes et renforcement de la sécurité.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 et clarifications des règles de gestion des données.
