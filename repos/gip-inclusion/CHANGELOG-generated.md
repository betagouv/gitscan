# Synthèse d'activité : gip-inclusion (du 01/09 au 08/10)

## Résumé de l'activité
L'activité de cette période est marquée par des transformations majeures d'identité et de fonctionnalités, notamment avec le rebranding de [les-emplois](/repos/gip-inclusion/les-emplois) en "La plateforme de l'inclusion" et de [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) vers "Match Europe". L'organisation a considérablement enrichi ses outils avec l'introduction d'un mode démo pour [inclusion-connect](/repos/gip-inclusion/inclusion-connect), de nouveaux modèles de rapports PDF via [export_merged_pull_requests](/repos/gip-inclusion/export_merged_pull_requests), et des capacités de matching et de gestion des candidatures accrues pour [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms). 

Parallèlement, un effort important a été déployé pour moderniser les infrastructures, notamment via le passage au serverless pour [fluo-proto](/repos/gip-inclusion/fluo-proto) et le déploiement complet de l'environnement pour le projet "emplois-cnav" dans [infrastructure](/repos/gip-inclusion/infrastructure). Ces évolutions visent à améliorer l'expérience utilisateur, la fiabilité des données et la scalabilité des services.

## Sécurité
- **Renforcement des politiques d'accès et de contrôle** : Mise en place de la gestion des secrets (SOPS, Secret Manager) dans [infrastructure](/repos/gip-inclusion/infrastructure) et sécurisation des authentifications (ProConnect, JWKS) pour [les-emplois](/repos/gip-inclusion/les-emplois) et [dora](/repos/gip-inclusion/dora).
- **Amélioration de la traçabilité** : Implémentation de journaux d'audit complets dans [les-emplois](/repos/gip-inclusion/les-emplois), [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav) et [autometa-jobs](/repos/gip-inclusion/autometa-jobs).
- **Protection des interfaces et des données** : Renforcement de la politique de sécurité (CSP) pour l'intégration iframe dans [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) et suppression des mots de passe codés en dur dans [fluo-proto](/repos/gip-inclusion/fluo-proto).

## Autres changements notables
- **Modernisation de l'infrastructure** : Transition vers un déploiement de conteneurs serverless pour [fluo-proto](/repos/gip-inclusion/fluo-proto) et mise en place de l'architecture Kubernetes/réseau pour le projet "emplois-cnav" dans [infrastructure](/repos/gip-inclusion/infrastructure).
- **Migrations de stockage** : Migration des données de MinIO vers SeaweedFS et RustFS pour [dora](/repos/gip-inclusion/dora) et [autometa](/repos/gip-inclusion/autometa).
- **Internationalisation** : Mise en place de la gestion des traductions (i18n) pour le [site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025).

## Dépôts les plus actifs
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding complet, gestion des candidatures spontanées et nouveaux outils d'analytics.
- [infrastructure](/repos/gip-inclusion/infrastructure) : Déploiement massif de l'architecture dédiée à "emplois-cnav" et sécurisation des accès.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Enrichissement des modèles de reporting et optimisation des pipelines de données.
- [les-emplois](/repos/gip-inclusion/les-emplois) : Refonte de l'identité, nouveau système d'orientation et renforcement de la traçabilité.
- [autometa](/repos/gip-inclusion/autometa) : Intégration de nouvelles sources de données et capacités d'analyse statistique avancées.
