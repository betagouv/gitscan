# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une semaine productive, marquée par le lancement du dépôt [common-helm-charts](/repos/cloud-gouv/common-helm-charts) qui vise à simplifier le déploiement d'applications sur Kubernetes. Des améliorations significatives ont été apportées à [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) pour la gestion de clusters Kubernetes sur Openstack et Outscale, notamment en matière de stabilité et de support multi-tenant. Le projet [openbao](/repos/cloud-gouv/openbao) a bénéficié d'une attention particulière en matière de sécurité et de correction de bugs, tandis que [portail](/repos/cloud-gouv/portail) a renforcé sa sécurité avec l'ajout du support mTLS et de la redirection HTTP CONNECT. Enfin, [securix](/repos/cloud-gouv/securix) a continué son amélioration avec des corrections de bugs, des améliorations de configuration et l'ajout de nouvelles fonctionnalités.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour axées sur la sécurité :

- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 et les dépendances `go.opentelemetry.io/otel/sdk` pour corriger des vulnérabilités (CVE-2025-68121 / GO-2026-4337, CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- [securix](/repos/cloud-gouv/securix) a supprimé le mode développeur et le flag associé pour renforcer la sécurité.
- [portail](/repos/cloud-gouv/portail) a activé le support mTLS côté serveur pour une communication plus sécurisée.

## Autres changements notables
- L'image `k8s-tools` dans [dockerfiles](/repos/cloud-gouv/dockerfiles) a été mise à jour avec l'ajout de `kustomize` et des versions plus récentes des outils Kubernetes.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a modernisé ses addons CAPI pour une meilleure maintenabilité.
- [openbao](/repos/cloud-gouv/openbao) a amélioré sa robustesse en corrigeant des erreurs non gérées et des problèmes d'initialisation de PostgreSQL.

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Nombreuses corrections de bugs et améliorations de la sécurité, notamment la mise à jour de Go et des dépendances.
- [portail](/repos/cloud-gouv/portail) : Ajout du support mTLS et de la redirection HTTP CONNECT pour une sécurité et une flexibilité accrues.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des clusters Kubernetes sur Openstack et Outscale, incluant des corrections de bugs et du support multi-tenant.
- [securix](/repos/cloud-gouv/securix) : Corrections de bugs, améliorations de la configuration et ajout de nouvelles fonctionnalités comme la prise en charge de qrencode.
