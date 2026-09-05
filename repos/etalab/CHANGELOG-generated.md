# Synthèse d'activité : etalab (du 01/08 au 31/08)

## Résumé de l'activité
L'activité récente est marquée par une montée en maturité des outils de gestion de données de transport et de services publics. Les efforts se sont concentrés sur l'enrichissement des données de mobilité, notamment via la mise à jour majeure du profil France NeTEx [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) et l'extension des bases de données de covoiturage [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) et des lieux de covoiturage [lieux-covoiturage](/repos/etalab/lieux-covoiturage).

Parallèlement, l'organisation renforce la flexibilité de ses standards grâce à l'introduction de nouvelles architectures d'extension de schémas [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) et à l'intégration de nouveaux services et formulaires dans [data_pass](/repos/etalab/data_pass). Ces évolutions visent à offrir des outils plus robustes, précis et adaptables aux besoins des services de l'État.

## Sécurité
- Renforcement de la protection contre les injections SQL et correction des scopes OAuth dans [data_pass](/repos/etalab/data_pass).
- Mise en place d'un scanner de vulnérabilités et sécurisation des processus dans [transport-site](/repos/etalab/transport-site).
- Amélioration de la gestion des accès via la rotation annuelle des tokens et la migration des scopes dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).
- Sécurisation de la logique de suppression des notifications dans [formulaire-qf](/repos/etalab/formulaire-qf).

## Autres changements notables
- Évolution architecturale majeure introduisant les "data packages" pour permettre l'extension dynamique des schémas dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).
- Optimisation des performances et de la consommation mémoire via l'adoption de l'allocateur `jemalloc` dans [transport-validator](/repos/etalab/transport-validator).
- Amélioration de l'observabilité avec l'implémentation de la journalisation au format JSON dans [formulaire-qf](/repos/etalab/formulaire-qf).
- Corrections critiques du backend S3 concernant la suppression de fichiers et la détection des types de contenu dans [flask-storage](/repos/etalab/flask-storage).
- Simplification des dépendances du projet par le remplacement de librairies de génération d'UUID dans [schema-irve](/repos/etalab/schema-irve).

## Dépôts les plus actifs
- [data_pass](/repos/etalab/data_pass) : Enrichissement important du catalogue de formulaires, intégration de nouveaux services et harmonisation des interfaces.
- [transport-site](/repos/etalab/transport-site) : Travaux divers mêlant sécurité, mise à jour des règles de validation et stabilisation des tests.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Nouvelles intégrations API, gestion renforcée des accès et améliorations de l'interface.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 apportant des clarifications structurelles importantes.
