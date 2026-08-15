# Synthèse d'activité : etalab (du 01/08 au 10/08)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par un renforcement de la fiabilité des données de transport et une extension significative des outils de gestion administrative. Les mises à jour du profil France NeTEx dans [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) et l'amélioration de la gestion des données de mobilité dans [transport-site](/repos/etalab/transport-site) garantissent des standards de données plus précis et une meilleure stabilité pour les services de transport.

Parallèlement, l'écosystème de gestion des données administratives s'enrichit avec l'ajout de nouveaux éditeurs et formulaires dans [data_pass](/repos/etalab/data_pass), ainsi que de nouvelles intégrations API dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise). Ces évolutions visent à fluidifier les processus numériques et à offrir une meilleure expérience utilisateur tout en consolidant la sécurité et l'observabilité des plateformes.

## Sécurité
- [data_pass](/repos/etalab/data_pass) : Correction d'une vulnérabilité Rails (CVE-2026-66066) et restriction des privilèges OAuth pour HubEE afin de limiter les risques.
- [transport-site](/repos/etalab/transport-site) : Mise en place d'un scanner de vulnérabilités pour renforcer la surveillance des dépendances.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Rotation annuelle du token webhook et migration des scopes des tokens vers les demandes d'autorisation.
- [formulaire-qf](/repos/etalab/formulaire-qf) : Correction de la logique de suppression des notifications pour éviter les suppressions accidentelles.

## Autres changements notables
- **Architecture et Performance** :
    - Introduction de l'architecture "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) pour permettre l'extension flexible des schémas de données.
    - Optimisation de la consommation mémoire via l'utilisation de l'allocateur `jemalloc` dans [transport-validator](/repos/etalab/transport-validator).
    - Refactorisation du processus de consolidation des données de recharge pour véhicules électriques dans [transport-site](/repos/etalab/transport-site).
- **Infrastructure et Observabilité** :
    - Migration vers le format de journalisation JSON dans [data_pass](/repos/etalab/data_pass) et [formulaire-qf](/repos/etalab/formulaire-qf) pour faciliter l'analyse des logs.
    - Centralisation de la gestion des environnements via Ansible dans [data_pass](/repos/etalab/data_pass).

## Dépôts les plus actifs
- [data_pass](/repos/etalab/data_pass) : Évolutions majeures incluant de nouveaux éditeurs, des améliorations d'interface et des mises à jour de sécurité.
- [transport-site](/repos/etalab/transport-site) : Amélioration de la fiabilité des données de mobilité et renforcement de la surveillance de sécurité.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Nouvelles intégrations API, gestion optimisée des tokens et évolutions de sécurité.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 apportant des clarifications structurelles et fonctionnelles.
