# Synthèse d'activité : cloud-gouv (du 16 avril 2026 au 26 mai 2026)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue au cours des dernières semaines, avec des améliorations significatives apportées à plusieurs de ses projets. Les efforts se sont concentrés sur l'amélioration de la sécurité, la stabilisation des tests et l'ajout de nouvelles fonctionnalités pour faciliter le déploiement et la gestion d'applications, notamment dans un contexte Kubernetes. L'ajout d'un chart Helm pour les benchmarks PostgreSQL via [common-helm-charts](/repos/cloud-gouv/common-helm-charts) permet aux utilisateurs de mieux évaluer les performances de leurs bases de données. Des corrections de bugs et des améliorations de la documentation ont également été apportées à [securix](/repos/cloud-gouv/securix) et [securix-infra-reference-implementation](/repos/cloud-gouv/securix-infra-reference-implementation).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Mise à jour de Go dans [openbao](/repos/cloud-gouv/openbao) pour corriger des vulnérabilités (CVE-2025-68121 / GO-2026-4337, CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- Amélioration de la sécurité des nœuds worker dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) avec la possibilité d'injecter des règles de sécurité supplémentaires.

## Autres changements notables
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a vu des améliorations dans la gestion des CIDR, des volumes snapshot, des secrets externes et des règles de sécurité.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) a été mis à jour avec l'ajout de `kustomize` et la mise à niveau des outils Kubernetes.
- [portail](/repos/cloud-gouv/portail) a bénéficié d'une correction pour stabiliser les tests du multiplexage H2.
- [openbao](/repos/cloud-gouv/openbao) a corrigé des bugs liés à l'auto-déverrouillage, la révocation de baux et les erreurs 500.

## Dépôts les plus actifs
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations significatives de la gestion des clusters Kubernetes via Helm charts.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité pour la gestion des secrets.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout d'un nouveau chart pour les benchmarks PostgreSQL.
- [securix](/repos/cloud-gouv/securix) : Corrections de bugs et améliorations de la validation des commandes.
