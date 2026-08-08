# Synthèse d'activité : etalab (du 01/08 au 07/08)

## Résumé de l'activité
L'activité de la période est marquée par une évolution significative des outils de gestion de données et des services de formulaires publics. Les standards de transport progressent avec la publication de la version 2.4.0 du profil France NeTEx [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) et l'amélioration de la validation des données de mobilité dans [transport-site](/repos/etalab/transport-site). 

Parallèlement, l'offre de services numériques s'enrichit avec l'intégration de nouveaux formulaires (cantines, aides sociales) dans [data_pass](/repos/etalab/data_pass) et une évolution majeure de l'architecture de [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) permettant une plus grande flexibilité des schémas de données. Ces évolutions visent à offrir une meilleure fiabilité des données de transport et une expérience utilisateur plus fluide et sécurisée sur les plateformes de services publics.

## Sécurité
- Renforcement de la sécurité de l'application [data_pass](/repos/etalab/data_pass) via la correction d'une vulnérabilité Rails (CVE-2026-66066) et une restriction des périmètres d'accès OAuth.
- Amélioration de la gestion des accès et de la sécurité des tokens dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise), incluant la rotation annuelle des tokens webhook et la migration des scopes vers les demandes d'autorisation.
- Mise en place d'un scanner de vulnérabilités pour renforcer la sécurité de [transport-site](/repos/etalab/transport-site).
- Correction de la logique de suppression des notifications dans [formulaire-qf](/repos/etalab/formulaire-qf) pour éviter les suppressions accidentelles.

## Autres changements notables
- Évolution majeure de l'architecture de [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) pour supporter l'extension des schémas via l'architecture "data packages".
- Optimisation des performances et de la gestion mémoire pour [transport-validator](/repos/etalab/transport-validator) grâce à l'adoption de l'allocateur `jemalloc`.
- Modernisation de l'infrastructure et de l'observabilité via le passage au format de journalisation JSON (logstasher) dans [data_pass](/repos/etalab/data_pass) et [formulaire-qf](/repos/etalab/formulaire-qf).
- Refonte du processus de consolidation des données IRVE pour une meilleure efficacité dans [transport-site](/repos/etalab/transport-site).
- Corrections techniques sur le stockage S3 pour [flask-storage](/repos/etalab/flask-storage), améliorant la précision de la suppression et la détection des types de fichiers.

## Dépôts les plus actifs
- [data_pass](/repos/etalab/data_pass) : Extension de l'offre de formulaires, améliorations de l'interface utilisateur et renforcement de la sécurité.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Évolutions importantes des API, de la gestion des accès et de l'interface de monitoring.
- [transport-site](/repos/etalab/transport-site) : Mise à jour des règles de validation, de la sécurité et optimisation des processus de données.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 et clarifications structurelles du profil France.
