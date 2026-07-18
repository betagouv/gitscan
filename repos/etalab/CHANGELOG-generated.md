# Synthèse d'activité : etalab (du 27 avril 2026 au 03 juillet 2026)

## Résumé de l'activité
L'activité de l'organisation etalab durant les dernières semaines s'est concentrée sur l'amélioration et l'extension de ses services liés aux données de transport, aux dispositifs d'aide, et aux API gouvernementales. Plusieurs dépôts ont bénéficié de mises à jour pour améliorer la performance, la stabilité et la sécurité. L'ajout de nouveaux opérateurs de vélos en libre-service sur [transport-site](/repos/etalab/transport-site) et l'introduction de l'architecture "data packages" pour le schéma des dispositifs d'aide ([schema-dispositif-aide](/repos/etalab/schema-dispositif-aide)) sont des évolutions notables. Les API [data_pass](/repos/etalab/data_pass) et [admin_api_entreprise](/repos/etalab/admin_api_entreprise) ont connu des évolutions importantes en termes de sécurité et de fonctionnalités.

## Sécurité
- Durcissement de la sécurité des sessions sur [data_pass](/repos/etalab/data_pass) avec une durée fixe de 12 heures.
- Rotation annuelle du token webhook sur [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour renforcer la sécurité.
- Suppression des endpoints dépréciés de l'API Particulier sur [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Passage à l'allocateur mémoire `jemalloc` par défaut dans [transport-validator](/repos/etalab/transport-validator) pour optimiser la consommation mémoire.
- Suppression de `proxy_request` dans [transport-site](/repos/etalab/transport-site) suite à la décommission de TimescaleDB.
- Publication de la v2.4.0 du profil France NeTEx sur [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) avec des clarifications et des améliorations.
- Migration des scopes des tokens vers les demandes d'autorisation sur [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Amélioration de l'import et de la validation des données IRVE, ajout de nouveaux opérateurs de vélos en libre-service et corrections de bugs.
- [data_pass](/repos/etalab/data_pass) : Ajout de la gestion des éditeurs, de nouveaux scopes et amélioration de la sécurité des sessions.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs (CNOUS, MSA), mise à jour d'APIs existantes et amélioration de la gestion des tokens.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version majeure du profil France NeTEx.
- [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) : Introduction de l'architecture "data packages" pour une plus grande flexibilité du schéma.
