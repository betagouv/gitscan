# Synthèse d'activité : cloud-gouv (du 16 avril 2026 au 29 avril 2026)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la sécurité, de la robustesse et de la flexibilité de ses outils et infrastructures. Des efforts significatifs ont été déployés pour corriger des vulnérabilités et améliorer la gestion des secrets, notamment avec [openbao](/repos/cloud-gouv/openbao). Les charts Helm ([common-helm-charts](/repos/cloud-gouv/common-helm-charts) et [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts)) ont été mis à jour pour offrir plus de contrôle sur la configuration et améliorer l'intégration avec des outils externes.  Des améliorations de l'expérience utilisateur ont également été apportées à [securix](/repos/cloud-gouv/securix), notamment pour la gestion des clés YubiKey.

## Sécurité
Plusieurs correctifs de sécurité ont été déployés :
- Correction de vulnérabilités dans la bibliothèque `go.opentelemetry.io/otel/sdk` dans [openbao](/repos/cloud-gouv/openbao).
- Mise à jour vers Go 1.25.7 pour corriger une vulnérabilité (CVE-2025-68121 / GO-2026-4337) dans [openbao](/repos/cloud-gouv/openbao).
- Amélioration de la sécurité des nœuds worker via l'injection de règles de sécurité (Security Groups) dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).

## Autres changements notables
- [portail](/repos/cloud-gouv/portail) a bénéficié d'améliorations du serveur RPC et de l'ajout de tests d'intégration.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a vu des améliorations significatives dans la gestion des CIDR, des volumes snapshot et des secrets externes.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) a été mis à jour pour inclure l'outil `kustomize` dans l'image `k8s-tools`.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Amélioration de l'expérience utilisateur et de la gestion des clés YubiKey.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et améliorations de la sécurité liées à la gestion des baux et des secrets.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la configuration et de la flexibilité des clusters Kubernetes.
- [portail](/repos/cloud-gouv/portail) : Amélioration de la robustesse et des fonctionnalités du serveur RPC.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de fonctionnalités et corrections de bugs pour faciliter le déploiement d'applications.
