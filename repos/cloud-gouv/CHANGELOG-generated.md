# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue cette semaine, avec des améliorations significatives en matière de sécurité, de gestion de clusters Kubernetes et de simplification du déploiement d'applications. L'ajout de support mTLS et HTTP au [portail](/repos/cloud-gouv/portail) renforce la sécurité et la flexibilité d'accès. Des corrections importantes ont été apportées à [openbao](/repos/cloud-gouv/openbao) pour résoudre des problèmes de déverrouillage et d'invalidation de cache, tout en améliorant la sécurité via des mises à jour de dépendances. L'écosystème Kubernetes est également renforcé avec des corrections et des améliorations apportées aux charts pour Cluster API via [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts). Enfin, les fondations pour un catalogue de charts Helm préconfigurés sont posées avec l'initialisation du dépôt [common-helm-charts](/repos/cloud-gouv/common-helm-charts).

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :

- Mise à jour de dépendances dans [openbao](/repos/cloud-gouv/openbao) pour corriger des vulnérabilités (CVE-2025-68121, GO-2026-4337, CVE-2026-24051, GO-2026-4394, GHSA-9h8m-3fm2-qjrq).
- Activation du support mTLS (mutual TLS) côté serveur dans [portail](/repos/cloud-gouv/portail) pour une authentification plus robuste.
- Suppression du mode développeur dans [securix](/repos/cloud-gouv/securix) pour une configuration plus sécurisée.

## Autres changements notables
- Ajout de l'outil `kustomize` à l'image `k8s-tools` dans [dockerfiles](/repos/cloud-gouv/dockerfiles) pour faciliter la personnalisation des configurations Kubernetes.
- Initialisation du dépôt [common-helm-charts](/repos/cloud-gouv/common-helm-charts) pour centraliser les charts Helm préconfigurés.
- Suppression de l'overlay g3proxy dans [securix](/repos/cloud-gouv/securix) et simplification de la documentation.

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et améliorations de la sécurité liées au déverrouillage, à la révocation de baux et à l'invalidation de cache.
- [portail](/repos/cloud-gouv/portail) : Ajout du support mTLS et HTTP pour une connectivité et une sécurité améliorées.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Corrections et améliorations pour la gestion des clusters Kubernetes sur Openstack et Outscale.
- [securix](/repos/cloud-gouv/securix) : Corrections de bugs, ajout de la prise en charge de qrencode et améliorations de la configuration.
