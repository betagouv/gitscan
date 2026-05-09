# Synthèse d'activité : cloud-gouv (du 24 avril 2026 au 02 mai 2026)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue cette semaine, avec des améliorations significatives apportées à plusieurs de ses projets. Les efforts se sont concentrés sur le renforcement de la sécurité (notamment dans [openbao](/repos/cloud-gouv/openbao) avec des corrections de vulnérabilités), l'amélioration de l'expérience utilisateur (dans [securix](/repos/cloud-gouv/securix) avec un nouvel outil pour la gestion des clés YubiKey) et l'ajout de nouvelles fonctionnalités (comme le chart pgbench-job dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts) pour les benchmarks PostgreSQL). Les charts Kubernetes ([k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) et [common-helm-charts](/repos/cloud-gouv/common-helm-charts)) ont bénéficié de nombreuses améliorations en termes de configuration et de sécurité.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour axées sur la sécurité :

- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 pour corriger une vulnérabilité (CVE-2025-68121 / GO-2026-4337) et a également mis à jour des dépendances pour corriger d'autres vulnérabilités (CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) permet désormais d'injecter des règles de sécurité supplémentaires pour les nœuds worker.

## Autres changements notables
- [securix](/repos/cloud-gouv/securix) a vu une refactorisation de son code et l'abandon d'une dépendance Python au profit de Nix.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) a implémenté un workflow de publication des charts au format OCI.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) a ajouté l'outil `kustomize` à l'image `k8s-tools` et mis à niveau les versions des outils inclus.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Amélioration de l'expérience utilisateur et de la gestion des clés YubiKey.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout d'un nouveau chart pour les benchmarks PostgreSQL et amélioration de la publication des charts.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des CIDR, des volumes snapshot et de la sécurité des nœuds worker.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité.
