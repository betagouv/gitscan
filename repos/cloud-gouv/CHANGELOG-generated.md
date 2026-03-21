# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une semaine riche en développement, avec des contributions notables à la sécurité, à l'amélioration des outils de gestion de clusters Kubernetes et à la simplification du déploiement d'applications. L'initialisation du dépôt [common-helm-charts](/repos/cloud-gouv/common-helm-charts) marque le début d'une initiative pour faciliter le déploiement d'applications sur Kubernetes. Des améliorations significatives ont également été apportées à [openbao](/repos/cloud-gouv/openbao) et [portail](/repos/cloud-gouv/portail) en matière de sécurité et de fonctionnalités réseau.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 et a corrigé des vulnérabilités dans `go.opentelemetry.io/otel/sdk` (CVE-2026-24051, CVE-2026-4394, GHSA-9h8m-3fm2-qjrq).
- [portail](/repos/cloud-gouv/portail) a activé le support mTLS (mutual TLS) côté serveur pour une communication plus sécurisée.
- [securix](/repos/cloud-gouv/securix) a corrigé un bug empêchant l'acceptation de mots de passe hachés vides et supprimé le mode développeur pour une meilleure sécurité.

## Autres changements notables
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a apporté des corrections et des améliorations à la gestion des clusters Kubernetes sur Openstack et Outscale, notamment pour CoreDNS et les addons CAPI.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) a ajouté l'outil `kustomize` à l'image `k8s-tools` et mis à niveau les versions des outils inclus.
- [securix](/repos/cloud-gouv/securix) a ajouté la prise en charge de qrencode pour faciliter l'authentification.

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Correction de bugs et améliorations de sécurité, notamment la mise à jour de Go et des dépendances.
- [portail](/repos/cloud-gouv/portail) : Ajout du support mTLS et de la redirection HTTP CONNECT pour une communication plus sécurisée et flexible.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des clusters Kubernetes sur différentes plateformes.
- [securix](/repos/cloud-gouv/securix) : Corrections de bugs, améliorations de la configuration et ajout de nouvelles fonctionnalités comme la prise en charge de qrencode.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Ajout de nouveaux outils et mise à niveau des versions existantes pour faciliter le déploiement d'applications.
