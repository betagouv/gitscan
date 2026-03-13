# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une semaine productive, marquée par le lancement d'un nouveau dépôt pour les charts Helm ([common-helm-charts](/repos/cloud-gouv/common-helm-charts)) et des améliorations significatives dans plusieurs projets existants. Les efforts se sont concentrés sur la sécurité, notamment avec des corrections de vulnérabilités dans [openbao](/repos/cloud-gouv/openbao) et l'ajout de mTLS dans [portail](/repos/cloud-gouv/portail).  Des améliorations fonctionnelles ont également été apportées à la gestion de clusters Kubernetes via [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) et à la gestion des secrets avec [openbao](/repos/cloud-gouv/openbao).

## Sécurité
Plusieurs changements ont été apportés pour améliorer la sécurité :

- Correction de vulnérabilités dans `go.opentelemetry.io/otel/sdk` dans [openbao](/repos/cloud-gouv/openbao).
- Mise à jour vers Go 1.25.7 pour corriger une vulnérabilité (CVE-2025-68121 / GO-2026-4337) dans [openbao](/repos/cloud-gouv/openbao).
- Ajout du support mTLS (mutual TLS) côté serveur dans [portail](/repos/cloud-gouv/portail) pour une authentification renforcée.

## Autres changements notables
- Initialisation du dépôt [common-helm-charts](/repos/cloud-gouv/common-helm-charts) pour faciliter le déploiement d'applications sur Kubernetes.
- Amélioration de l'outil `k8s-tools` dans [dockerfiles](/repos/cloud-gouv/dockerfiles) avec l'ajout de `kustomize` et la mise à niveau des outils existants.
- Suppression du mode développeur dans [securix](/repos/cloud-gouv/securix) pour une configuration plus sécurisée.

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et améliorations de la sécurité liées à la gestion des secrets et des clés.
- [portail](/repos/cloud-gouv/portail) : Ajout du support mTLS et HTTP pour une connectivité plus flexible et sécurisée.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des clusters Kubernetes sur Openstack et Outscale, incluant une correction pour CoreDNS et la prise en charge du multi-tenant sur Outscale.
- [securix](/repos/cloud-gouv/securix) : Corrections de bugs, améliorations de la configuration et ajout de la prise en charge de qrencode.
