# Synthèse d'activité : cloud-gouv (du 24/04 au 02/05/2026)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue cette semaine, avec des améliorations significatives apportées à plusieurs de ses dépôts. Les efforts se sont concentrés sur la sécurité, notamment avec des mises à jour de dépendances dans [openbao](/repos/cloud-gouv/openbao) pour corriger des vulnérabilités, et l'ajout de fonctionnalités de sécurité pour les nœuds worker dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts). Des améliorations de l'expérience utilisateur ont également été apportées, comme l'outil de gestion des clés YubiKey dans [securix](/repos/cloud-gouv/securix) et l'ajout de la prise en charge des groupes supplémentaires pour le serveur RPC dans [portail](/repos/cloud-gouv/portail). Enfin, de nouveaux outils et charts ont été ajoutés pour faciliter le déploiement et la gestion des applications, notamment avec l'ajout du chart pgbench dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts) et l'outil kustomize dans [dockerfiles](/repos/cloud-gouv/dockerfiles).

## Sécurité
Plusieurs correctifs de sécurité ont été déployés :
- Mise à jour de Go dans [openbao](/repos/cloud-gouv/openbao) pour corriger une vulnérabilité (CVE-2025-68121 / GO-2026-4337).
- Mise à jour de dépendances dans [openbao](/repos/cloud-gouv/openbao) pour corriger des vulnérabilités (CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- Amélioration de la sécurité des nœuds worker avec la possibilité d'injecter des règles de sécurité supplémentaires dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).

## Autres changements notables
- Refactorisation du code dans [securix](/repos/cloud-gouv/securix) pour une meilleure cohérence et structure.
- Ajout d'un chart pgbench pour les benchmarks PostgreSQL dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts).
- Ajout de l'outil kustomize à l'image `k8s-tools` dans [dockerfiles](/repos/cloud-gouv/dockerfiles).
- Correction de bugs et améliorations de la gestion des CIDR et des volumes snapshot dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Amélioration de l'expérience utilisateur et de la gestion des clés YubiKey.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Amélioration de la sécurité et de la configuration des clusters Kubernetes.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de nouveaux charts et amélioration de la flexibilité de la configuration.
- [portail](/repos/cloud-gouv/portail) : Ajout de la prise en charge des groupes supplémentaires pour une gestion plus fine des autorisations.
